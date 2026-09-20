# NEXUS TECH | 出海跨境双语极客硬件独立站工程

本项目为专为出海设计的极客数码、EDC 随身硬件与 AI 硬件跨境独立站（Direct from Huaqiangbei），支持 **中/英 双语动态一键无缝切换**，并已将项目中分散生成的 AI 硬件产品图规范重命名归档，替换了原有的 Emoji 占位。

---

## 📁 工程目录结构

```text
/Users/apple/googleDriver/
├── assets/
│   ├── images/
│   │   ├── banners/
│   │   │   └── cyber-chip-hero.png          # 赛博计算芯片背景/横幅图
│   │   └── products/                        # 规范化命名的 10 大硬件选品与图文看板
│   │       ├── 01-ai-voice-recorder.jpg     # 01 磁吸 AI 录音卡 (主推爆款实物)
│   │       ├── 02-retro-gaming-console.jpg  # 02 开源复古游戏掌机
│   │       ├── 03-pocket-thermal-printer.jpg# 03 迷你口袋热敏打印机
│   │       ├── 04-titanium-mini-flashlight.jpg # 04 钛合金 1000LM 迷你手电
│   │       ├── 05-cyberpunk-oled-clock.jpg  # 05 赛博朋克 OLED 桌面时钟
│   │       ├── 06-pet-gps-laser-collar.jpg  # 06 智能宠物 GPS 定位激光项圈
│   │       ├── 07-wearable-4k-bodycam.jpg   # 07 磁吸微型可穿戴 4K 记录相机
│   │       ├── 08-bone-conduction-sunglasses.jpg # 08 骨传导智能音频太阳镜
│   │       ├── 09-obd2-hud-projector.jpg    # 09 便携 OBD2 检测仪与 HUD 投影
│   │       ├── 10-electric-screwdriver-kit.jpg # 10 智能数显电动精细螺丝刀
│   │       ├── 10-electric-screwdriver-kit-alt.jpg # 10 螺丝刀与便携焊台套装特写
│   │       └── spotlight-recorder-infographic.jpg # 01 主推爆款 5 大卖点营销信息图
│   └── js/
│       └── app.js                           # 核心前端交互与双语 i18n 引擎
├── index.html                               # 标准入口页面（支持中英文切换、完整图片渲染）
├── nexus_tech_bilingual.html                # 原双语版本（已修复语法 Bug 并更新图片路径）
├── nexus_tech_chinese_default.html          # 原中文默认版本（已更新图片路径）
├── server.py                                # 轻量 Python HTTP 本地服务脚本
├── package.json                             # 前端工程配置与 npm scripts
└── README.md                                # 项目使用与维护文档
```

---

## 🚀 启动运行服务

在本项目根目录下，您可以通过以下任意方式启动本地 Web 服务：

### 方式 1：使用 Python（推荐，零第三方依赖）
```bash
python3 server.py
# 或指定端口启动：
python3 server.py 8080
```

### 方式 2：使用 npm 命令
```bash
npm start
# 或者
npm run dev
```

服务启动后，在浏览器中打开：
👉 **`http://localhost:8080`**

---

## 🌐 核心功能特色

1. **中英文双语平滑切换 (i18n Engine)**：
   - 导航栏右上角支持 `[EN]` / `[中文]` 分段式按钮一键切换；
   - 自动持久化保存语言选择到 `localStorage`，并在刷新后自动记忆；
   - 支持通过 URL 参数强制指定语言（如 `http://localhost:8080/?lang=zh` 或 `?lang=en`）。
2. **真实高质感硬件实物图接入**：
   - **Spotlight 爆款区**：支持主图与“5大卖点图文详情看板（`spotlight-recorder-infographic.jpg`）”一键切换查看；
   - **10 Curated Drops 选品区**：全部更换为规范比例的高清实物图，配有悬浮微缩放动效（Image Zoom）；
   - **单页极速结算区**：订单核对模块接入真实产品缩略图。
3. **加入购物车与交互反馈**：
   - 点击任意产品卡片的“Add to Cart”/“加入购物车”均会有赛博风动态 Toast 提示。
