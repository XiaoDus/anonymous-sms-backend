---

# 📨 Anonymous SMS Backend 项目介绍

`anonymous-sms-backend` 是一个基于 Python（ Django 框架）开发的短信发送后端系统，支持用户以匿名方式发送短信。该系统旨在保护用户隐私，同时提供一个简洁高效的接口，适用于匿名反馈、舆情采集、临时通知等敏感信息传递场景。

---

## ✨ 项目亮点

- 📦 **模块化设计**：项目划分为 `smsApp`（核心逻辑）和 `smsTool`（短信工具模块），清晰可维护。
- 🔒 **匿名保护机制**：从架构设计上确保用户身份不被泄露，强化隐私保护。
- ⚙️ **快速部署**：轻量级 SQLite 支持，无需额外配置即可本地运行。
- 📤 **短信发送逻辑独立封装**：便于后续替换短信服务提供商或扩展功能。
- 📚 **打包支持**：存在 `.spec` 文件和压缩包，说明你已经考虑了项目的打包与发布流程。

---

## 🧱 项目结构简要说明

```
anonymous-sms-backend/
├── smsApp/               # 主要功能模块，例如视图、模型、路由等
├── smsTool/              # 封装的短信发送逻辑
├── db.sqlite3            # 默认数据库文件（SQLite）
├── manage.py             # 启动 Django 项目的脚本
├── smsApp.spec           # 用于 PyInstaller 打包的配置
└── smsTool.zip           # 工具模块的归档备份
```

---

## 🚀 启动方式

1. 安装依赖（如果你有 `requirements.txt`）：
   ```bash
   pip install -r requirements.txt
   ```

2. 进行数据库迁移：
   ```bash
   python manage.py migrate
   ```

3. 启动开发服务器：
   ```bash
   python manage.py runserver
   ```

默认监听地址为：`http://127.0.0.1:8000/`

---

## 🔮 未来优化建议

- ✅ 接入短信平台（如阿里云、腾讯云、Twilio 等）
- ✅ 添加 Web 前端配套管理界面（支持用户投递、日志查看）
- ✅ 接入 JWT 或 OAuth2 进行权限控制（匿名逻辑可以做更灵活的策略配置）
- ⏳ 添加 API 文档支持（建议集成 Swagger / drf-yasg）
- ⏳ 引入日志持久化和审计（如日志记录到 MongoDB 或 ELK）

---
