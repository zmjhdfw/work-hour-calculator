# 工时计算器

一个简单易用的工时记录和统计工具，提供多种使用方式。

## 📥 快速获取

### 方式1：直接下载可执行文件（推荐）

- **Windows EXE**: [下载 工时计算器.exe](dist/工时计算器.exe) (10 MB)
- **Android APK**: [下载 工时计算器.apk](dist/工时计算器.apk) (6.5 MB)

无需安装，直接运行即可！

### 方式2：克隆仓库

```bash
git clone https://github.com/zmjhdfw/work-hour-calculator.git
cd work-hour-calculator
```

### 方式3：下载ZIP

点击页面右上角的 "Code" → "Download ZIP"

## ✨ 功能特性

### 核心功能
- ✅ 添加、查看、编辑、删除工时记录
- ✅ 按日期、日期范围、项目查询记录
- ✅ 计算工时统计（总工时、正常工时、加班工时）
- ✅ 生成统计报告（摘要报告、项目报告、详细报告）
- ✅ 导出数据为CSV格式
- ✅ 支持中文界面
- ✅ 多平台支持

### Android专属功能
- ✅ **打卡功能** - 快速上下班打卡，自动计算工时
- ✅ **日历视图** - 月历显示，可视化工时分布
- ✅ 数据持久化（SQLite）
- ✅ Material Design界面

### Windows专属功能
- ✅ GUI图形界面（tkinter）
- ✅ 标签页设计
- ✅ 中文完美支持

## 📱 支持平台

| 平台 | 文件 | 大小 | 说明 |
|------|------|------|------|
| **Windows** | `工时计算器.exe` | 10 MB | GUI界面，双击运行 |
| **Android** | `工时计算器.apk` | 6.5 MB | 打卡、日历、统计 |
| **Web** | `web_app.py` | - | Flask Web应用 |
| **CLI** | `main_cli.py` | - | 命令行界面 |

## 🚀 使用方式

### Windows用户

1. 下载 `dist/工时计算器.exe`
2. 双击运行
3. 使用GUI界面：
   - **添加记录页**：填写日期、时间、项目信息
   - **查看记录页**：查看所有工时记录
   - **统计分析页**：查看统计数据

### Android用户

1. 下载 `dist/工时计算器.apk`
2. 传输到手机
3. 允许安装未知来源应用
4. 安装并打开
5. 使用功能：
   - **添加记录**：手动添加工时记录
   - **打卡**：快速上下班打卡
   - **日历**：查看月历和工时分布
   - **查看记录**：查看所有记录
   - **统计分析**：查看统计数据

### Web应用

```bash
# 安装Flask
pip install flask

# 运行Web服务器
python web_app.py

# 访问 http://localhost:5000
```

### 命令行版本

```bash
# 安装依赖
pip install -r requirements.txt

# 运行
python main_cli.py
```

## 📁 项目结构

```
work-hour-calculator/
├── dist/                          # 可执行文件
│   ├── 工时计算器.exe            # Windows GUI应用
│   └── 工时计算器.apk            # Android应用
├── android-app/                   # Android项目（Java）
│   ├── app/src/main/java/
│   │   └── org/workhour/calculator/
│   │       ├── MainActivity.java          # 主界面
│   │       ├── AddRecordActivity.java     # 添加记录
│   │       ├── ClockInActivity.java       # 打卡功能
│   │       ├── CalendarActivity.java      # 日历功能
│   │       ├── ViewRecordsActivity.java   # 查看记录
│   │       ├── StatisticsActivity.java    # 统计分析
│   │       ├── WorkRecord.java            # 数据模型
│   │       ├── DataManager.java           # 数据管理
│   │       └── Statistics.java            # 统计模型
│   └── README.md
├── work_hour_calculator/          # Python核心模块
│   ├── models.py
│   ├── data_manager.py
│   ├── work_calculator.py
│   └── report_generator.py
├── templates/                     # Web模板
├── main_gui.py                    # Windows GUI入口
├── main_cli.py                    # CLI入口
├── web_app.py                     # Web应用
└── README.md
```

## 🎨 界面预览

### Android应用
- **主界面**：6个功能按钮
- **打卡界面**：上班/下班打卡，显示工作时长
- **日历界面**：月历视图，绿色标记有工时的日期
- **添加记录**：日期、时间、项目输入
- **查看记录**：列表显示所有记录
- **统计分析**：总工时、平均工时统计

### Windows应用
- **标签页设计**：添加记录、查看记录、统计分析
- **GUI界面**：tkinter图形界面
- **中文支持**：完美显示

## 🔧 开发

### Android开发

```bash
cd android-app
# 使用Android Studio打开项目
# 或使用命令行构建
./gradlew assembleDebug
```

### Python开发

```bash
# 运行测试
python -m pytest work_hour_calculator/tests/

# 打包Windows EXE
pyinstaller --onefile --windowed --name=工时计算器 main_gui.py
```

## 📊 技术栈

- **Android**: Java, SQLite, Material Design
- **Windows**: Python 3.10+, tkinter
- **Web**: Flask
- **打包**: PyInstaller (Windows), Gradle (Android)

## 📝 数据存储

- **Android**: SQLite数据库
- **Windows/CLI**: JSON文件 (`work_records.json`)

## 🔄 更新历史

### v1.1 (2026-04-13)
- ✅ Android添加打卡功能
- ✅ Android添加日历视图
- ✅ Windows GUI版本
- ✅ 自定义时钟图标

### v1.0 (2026-04-13)
- ✅ 初始发布
- ✅ Windows EXE版本
- ✅ Android APK版本
- ✅ 完整的工时计算功能
- ✅ 数据持久化存储

## 📄 许可证

MIT License

## 👥 作者

Work Hour Calculator Team

## 🔗 GitHub

https://github.com/zmjhdfw/work-hour-calculator

---

**多平台支持，功能丰富，开箱即用！**
