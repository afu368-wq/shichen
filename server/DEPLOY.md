# 时位小助手 - 部署指南

## 1. 服务器环境准备

```bash
# Ubuntu 20.04+ / Debian 11+
sudo apt update
sudo apt install nodejs npm nginx -y
```

## 2. 上传文件

```bash
# 假设项目目录为 /var/www/shichen
sudo mkdir -p /var/www/shichen
sudo chown -R $USER:$USER /var/www/shichen

# 上传所有文件到该目录（包括 index.html 和 server 文件夹）
```

## 3. 安装后端依赖

```bash
cd /var/www/shichen/server
npm install
```

## 4. 配置 systemd 服务

创建 `/etc/systemd/system/shichen.service`：

```ini
[Unit]
Description=Shichen Assistant Backend
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/shichen/server
Environment=NODE_ENV=production
Environment=PORT=3000
Environment=JWT_SECRET=your_super_secret_key_here
ExecStart=/usr/bin/node server.js
Restart=always

[Install]
WantedBy=multi-user.target
```

启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable shichen
sudo systemctl start shichen
sudo systemctl status shichen
```

## 5. 配置 Nginx 反向代理

创建 `/etc/nginx/sites-available/shichen`：

```nginx
server {
    listen 80;
    server_name your-domain.com;  # 替换为你的域名

    root /var/www/shichen;
    index index.html;

    # 静态文件
    location / {
        try_files $uri $uri/ =404;
    }

    # API 代理到 Node.js
    location /api/ {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }

    # 开启 gzip
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript application/javascript application/xml+rss application/json;
}
```

启用站点：

```bash
sudo ln -s /etc/nginx/sites-available/shichen /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

## 6. 防火墙配置

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp  # 如需 HTTPS
sudo ufw enable
```

## 7. 微信开放平台配置（生产环境必须）

1. 注册微信开放平台（需企业资质）
2. 创建网站应用
3. 获取 AppID 和 AppSecret
4. 配置授权回调域名（如 your-domain.com）
5. 修改 `server.js` 中的微信登录逻辑

## 8. 数据库备份

```bash
# 备份 SQLite
cp /var/www/shichen/server/data.db /var/www/shichen/server/data.db.backup.$(date +%Y%m%d)

# 恢复
# cp /var/www/shichen/server/data.db.backup.YYYYMMDD /var/www/shichen/server/data.db
```

## 9. 监控日志

```bash
# 查看后端日志
sudo journalctl -u shichen -f

# 查看 Nginx 日志
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

## 10. 一键启动脚本

创建 `/var/www/shichen/start.sh`：

```bash
#!/bin/bash
cd /var/www/shichen/server
npm install
sudo systemctl restart shichen
sudo systemctl restart nginx
```

```bash
chmod +x /var/www/shichen/start.sh
```

## 环境变量说明

| 变量 | 说明 | 默认值 |
|------|------|--------|
| PORT | 后端服务端口 | 3000 |
| JWT_SECRET | JWT 签名密钥 | shichen_secret_change_in_production |
| NODE_ENV | 环境模式 | production |

## 故障排查

1. **502 Bad Gateway**：检查 `sudo systemctl status shichen`
2. **404 Not Found**：检查 Nginx root 路径
3. **数据库权限**：确保 `www-data` 用户可读写 `data.db`
4. **端口占用**：`netstat -tlnp | grep :3000`