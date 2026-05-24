const Database = require('better-sqlite3');
const path = require('path');

const DB_PATH = path.join(__dirname, 'data.db');

let db;

function init() {
    db = new Database(DB_PATH);
    db.pragma('journal_mode = WAL');
    db.pragma('foreign_keys = ON');

    db.exec(`
        CREATE TABLE IF NOT EXISTS users (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            openid          TEXT UNIQUE,
            unionid         TEXT,
            nickname        TEXT DEFAULT '',
            avatar          TEXT DEFAULT '',
            phone           TEXT DEFAULT '',
            email           TEXT DEFAULT '',
            member_type     TEXT DEFAULT 'free',
            member_expire   TEXT,
            trial_quota     INTEGER DEFAULT 0,
            share_code      TEXT UNIQUE,
            share_count     INTEGER DEFAULT 0,
            created_at      TEXT DEFAULT (datetime('now', 'localtime')),
            updated_at      TEXT DEFAULT (datetime('now', 'localtime'))
        );

        CREATE TABLE IF NOT EXISTS sponsors (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id         INTEGER,
            amount          REAL,
            message         TEXT DEFAULT '',
            created_at      TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS contacts (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id         INTEGER,
            message         TEXT,
            reply           TEXT DEFAULT '',
            replied         INTEGER DEFAULT 0,
            created_at      TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS visits (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            ip              TEXT DEFAULT '',
            country         TEXT DEFAULT '',
            city            TEXT DEFAULT '',
            duration_sec    INTEGER DEFAULT 0,
            page_url        TEXT DEFAULT '',
            user_agent      TEXT DEFAULT '',
            created_at      TEXT DEFAULT (datetime('now', 'localtime'))
        );
    `);

    console.log('[DB] 数据库初始化完成');
    return db;
}

function getDb() {
    if (!db) init();
    return db;
}

// ========== 用户操作 ==========

function findOrCreateWechatUser(openid, unionid, nickname, avatar) {
    const d = getDb();
    let user = d.prepare('SELECT * FROM users WHERE openid = ?').get(openid);
    if (!user) {
        const shareCode = require('uuid').v4().slice(0, 8);
        const result = d.prepare(
            'INSERT INTO users (openid, unionid, nickname, avatar, share_code) VALUES (?, ?, ?, ?, ?)'
        ).run(openid, unionid || '', nickname || '', avatar || '', shareCode);
        user = d.prepare('SELECT * FROM users WHERE id = ?').get(result.lastInsertRowid);
    } else {
        d.prepare(
            'UPDATE users SET nickname = ?, avatar = ?, updated_at = datetime(\'now\',\'localtime\') WHERE id = ?'
        ).run(nickname || user.nickname, avatar || user.avatar, user.id);
        user = d.prepare('SELECT * FROM users WHERE id = ?').get(user.id);
    }
    return user;
}

function getUserById(id) {
    return getDb().prepare('SELECT * FROM users WHERE id = ?').get(id);
}

function addTrialQuota(userId, count) {
    getDb().prepare('UPDATE users SET trial_quota = trial_quota + ? WHERE id = ?').run(count, userId);
}

function consumeTrialQuota(userId) {
    const user = getUserById(userId);
    if (user && user.trial_quota > 0) {
        getDb().prepare('UPDATE users SET trial_quota = trial_quota - 1 WHERE id = ?').run(userId);
        return true;
    }
    return false;
}

// ========== 赞助 ==========

function addSponsor(userId, amount, message) {
    return getDb().prepare(
        'INSERT INTO sponsors (user_id, amount, message) VALUES (?, ?, ?)'
    ).run(userId, amount, message || '');
}

function getSponsors(limit = 20) {
    return getDb().prepare(
        'SELECT s.*, u.nickname, u.avatar FROM sponsors s LEFT JOIN users u ON s.user_id = u.id ORDER BY s.created_at DESC LIMIT ?'
    ).all(limit);
}

// ========== 客服 ==========

function addContact(userId, message) {
    return getDb().prepare(
        'INSERT INTO contacts (user_id, message) VALUES (?, ?)'
    ).run(userId, message);
}

function getUserContacts(userId) {
    return getDb().prepare(
        'SELECT * FROM contacts WHERE user_id = ? ORDER BY created_at DESC'
    ).all(userId);
}

// ========== 访问统计 ==========

function addVisit(ip, country, city, pageUrl, userAgent) {
    return getDb().prepare(
        'INSERT INTO visits (ip, country, city, page_url, user_agent) VALUES (?, ?, ?, ?, ?)'
    ).run(ip, country, city, pageUrl, userAgent);
}

function updateVisitDuration(id, durationSec) {
    getDb().prepare('UPDATE visits SET duration_sec = ? WHERE id = ?').run(durationSec, id);
}

function getVisitStats(days = 7) {
    const d = getDb();
    const total = d.prepare('SELECT COUNT(*) as count FROM visits WHERE created_at >= datetime("now", "localtime", ?)').get('-' + days + ' days');
    const byCountry = d.prepare('SELECT country, COUNT(*) as count FROM visits WHERE created_at >= datetime("now", "localtime", ?) GROUP BY country ORDER BY count DESC').all('-' + days + ' days');
    const byCity = d.prepare('SELECT city, country, COUNT(*) as count FROM visits WHERE created_at >= datetime("now", "localtime", ?) AND city != "" GROUP BY city, country ORDER BY count DESC LIMIT 20').all('-' + days + ' days');
    const avgDuration = d.prepare('SELECT ROUND(AVG(duration_sec), 1) as avg FROM visits WHERE duration_sec > 0 AND created_at >= datetime("now", "localtime", ?)').get('-' + days + ' days');
    const recent = d.prepare('SELECT * FROM visits ORDER BY id DESC LIMIT 20').all();
    return { total: total.count, avgDuration: avgDuration.avg || 0, byCountry, byCity, recent };
}

module.exports = {
    init, getDb,
    findOrCreateWechatUser, getUserById, addTrialQuota, consumeTrialQuota,
    addSponsor, getSponsors,
    addContact, getUserContacts,
    addVisit, updateVisitDuration, getVisitStats
};