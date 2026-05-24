const express = require('express');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const path = require('path');
const db = require('./db');

const JWT_SECRET = process.env.JWT_SECRET || 'shichen_secret_change_in_production';
const PORT = process.env.PORT || 8080;

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(__dirname)); // 托管静态页面

// ========== JWT 中间件 ==========

function authMiddleware(req, res, next) {
    const auth = req.headers.authorization;
    if (!auth || !auth.startsWith('Bearer ')) {
        return res.status(401).json({ error: '未登录' });
    }
    try {
        const payload = jwt.verify(auth.slice(7), JWT_SECRET);
        req.userId = payload.userId;
        next();
    } catch (e) {
        return res.status(401).json({ error: '登录已过期' });
    }
}

function optionalAuth(req, res, next) {
    const auth = req.headers.authorization;
    if (auth && auth.startsWith('Bearer ')) {
        try {
            const payload = jwt.verify(auth.slice(7), JWT_SECRET);
            req.userId = payload.userId;
        } catch (e) { /* 忽略 */ }
    }
    next();
}

// ========== 微信快捷登录 ==========

// 注：生产环境需对接微信开放平台 OAuth2.0
// 当前接口接受 openid 直接登录（测试用），
// 真正上线时此处替换为 code → access_token → openid 的完整流程

app.post('/api/auth/wechat', (req, res) => {
    const { code, nickname, avatar } = req.body;

    if (!code) {
        return res.status(400).json({ error: '缺少授权码' });
    }

    // === 生产环境代码（替换下面这段）===
    // const wxRes = await fetch(
    //   `https://api.weixin.qq.com/sns/oauth2/access_token?appid=${APPID}&secret=${SECRET}&code=${code}&grant_type=authorization_code`
    // );
    // const wxData = await wxRes.json();
    // const { openid, unionid } = wxData;
    // === 测试环境：code 即 openid ===

    const openid = code;
    const unionid = req.body.unionid || '';

    const user = db.findOrCreateWechatUser(openid, unionid, nickname, avatar);

    const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: '30d' });

    res.json({
        token,
        user: {
            id: user.id,
            nickname: user.nickname,
            avatar: user.avatar,
            memberType: user.member_type,
            memberExpire: user.member_expire,
            trialQuota: user.trial_quota
        }
    });
});

// ========== 用户状态 ==========

app.get('/api/user/status', authMiddleware, (req, res) => {
    const user = db.getUserById(req.userId);
    if (!user) return res.status(404).json({ error: '用户不存在' });

    const isMember = user.member_type !== 'free' &&
        (!user.member_expire || new Date(user.member_expire) > new Date());

    res.json({
        id: user.id,
        nickname: user.nickname,
        avatar: user.avatar,
        memberType: isMember ? user.member_type : 'free',
        memberExpire: user.member_expire,
        trialQuota: user.trial_quota,
        shareCode: user.share_code,
        createdAt: user.created_at
    });
});

// ========== 赞助 ==========

app.post('/api/sponsor', authMiddleware, (req, res) => {
    const { amount, message } = req.body;
    if (!amount || amount <= 0) {
        return res.status(400).json({ error: '金额无效' });
    }
    db.addSponsor(req.userId, amount, message);
    res.json({ success: true, message: '感谢您的支持！' });
});

app.get('/api/sponsor/list', optionalAuth, (req, res) => {
    const list = db.getSponsors(20);
    res.json(list.map(s => ({
        nickname: s.nickname ? s.nickname.slice(0, 1) + '***' : '匿名',
        amount: s.amount,
        message: s.message,
        createdAt: s.created_at
    })));
});

// ========== 客服 ==========

app.post('/api/contact', authMiddleware, (req, res) => {
    const { message } = req.body;
    if (!message || !message.trim()) {
        return res.status(400).json({ error: '请输入内容' });
    }
    db.addContact(req.userId, message.trim());
    res.json({ success: true, message: '已收到您的留言，我们会尽快回复。' });
});

app.get('/api/contact/history', authMiddleware, (req, res) => {
    const list = db.getUserContacts(req.userId);
    res.json(list.map(c => ({
        id: c.id,
        message: c.message,
        reply: c.reply,
        replied: !!c.replied,
        createdAt: c.created_at
    })));
});

// ========== 访问统计 ==========

app.post('/api/visit/start', (req, res) => {
    const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress || '';
    const userAgent = req.headers['user-agent'] || '';
    const { country = '', city = '', pageUrl = '' } = req.body;
    const result = db.addVisit(ip, country, city, pageUrl, userAgent);
    res.json({ id: result.lastInsertRowid });
});

app.post('/api/visit/end', (req, res) => {
    const { id, durationSec } = req.body;
    if (!id || durationSec === undefined) {
        return res.status(400).json({ error: '缺少参数' });
    }
    db.updateVisitDuration(id, durationSec);
    res.json({ success: true });
});

app.get('/api/visit/stats', authMiddleware, (req, res) => {
    const { days = 7 } = req.query;
    const stats = db.getVisitStats(parseInt(days, 10));
    res.json(stats);
});

// 健康检查
app.get('/api/health', (req, res) => {
    res.json({ status: 'ok', time: new Date().toISOString() });
});

// 初始化数据库并启动
db.init();
app.listen(PORT, () => {
    console.log(`[Server] 运行在 http://localhost:${PORT}`);
    console.log(`[Server] 静态页面: http://localhost:${PORT}/index.html`);
});