FROM node:20-alpine

WORKDIR /app

# 先复制 server 依赖文件，利用 Docker 缓存
COPY server/package.json server/package-lock.json ./server/
RUN cd server && npm install

# 复制全部文件（index.html + server/）
COPY . .

# 工作目录设为 server，这样 __dirname 指向 /app/server
WORKDIR /app/server

EXPOSE 3000

CMD ["node", "server.js"]