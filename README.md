# 工时计算器

一个简单易用的工时记录和统计工具，提供多种使用方式。

## 📥 快速获取

### 方式1：直接下载可执行文件（推荐）

- **Windows EXE**: [下载 工时计算器.exe](dist/工时计算器.exe) (8 MB)
- **Android APK**: [下载 工时计算器.apk](dist/工时计算器.apk) (5.3 MB)

无需安装，直接运行即可！

### 方式2：克隆仓库

```bash
git clone https://github.com/zmjhdfw/work-hour-calculator.git
cd work-hour-calculator
```

### 方式3：下载ZIP

点击页面右上角的 "Code" → "Download ZIP"

## ✨ 功能特性

- ✅ 添加、查看、编辑、删除工时记录
- ✅ 按日期、日期范围、项目查询记录
- ✅ 计算工时统计（总工时、正常工时、加班工时）
- ✅ 生成统计报告（摘要报告、项目报告、详细报告）
- ✅ 导出数据为CSV格式
- ✅ 支持中文界面
- ✅ 多平台支持

## 📱 支持平台

| 平台 | 文件 | 大小 | 说明 |
|------|------|------|------|
| **Windows** | `工时计算器.exe` | 8 MB | 双击运行，无需安装 |
| **Android** | `工时计算器.apk` | 5.3 MB | 安装即用，Java原生开发 |
| **Web** | `web_app.py` | - | Flask Web应用 |
| **CLI** | `main.py` | - | 命令行界面 |

## 🚀 使用方式

### Windows用户

1. 下载 `dist/工时计算器.exe`
2. 双击运行
3. 开始使用！

### Android用户

1. 下载 `dist/工时计算器.apk`
2. 传输到手机
3. 允许安装未知来源应用
4. 安装并打开

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
python main.py
```

## 📁 项目结构

```
work-hour-calculator/
├── dist/                          # 可执行文件
│   ├── 工时计算器.exe            # Windows可执行文件
│   └── 工时计算器.apk            # Android应用
├── android-app/                   # Android项目（Java）
│   ├── app/src/main/java/
│   │   └── org/workhour/calculator/
│   │       ├── MainActivity.java
│   │       ├── AddRecordActivity.java
│   │       ├── ViewRecordsActivity.java
│   │       ├── StatisticsActivity.java
│   │       ├── WorkRecord.java
│   │       ├── DataManager.java
│   │       └── Statistics.java
│   └── README.md
├── work_hour_calculator/          # Python核心模块
│   ├── models.py
│   ├── data_manager.py
│   ├── work_calculator.py
│   └── report_generator.py
├── templates/                     # Web模板
├── main.py                        # CLI入口
├── web_app.py                     # Web应用
└── README.md
```

## 📖 使用说明

### Android应用

1. **添加记录**：点击"添加记录"按钮，填写日期、时间、项目等信息
2. **查看记录**：点击"查看记录"查看所有工时记录
3. **统计分析**：点击"统计分析"查看总工时、平均工时等
4. **清空数据**：点击"清空数据"删除所有记录

### Windows/CLI应用

程序启动后，会显示主菜单：

```
1. 添加工时记录
2. 查看工时记录
3. 编辑工时记录
4. 删除工时记录
5. 计算工时统计
6. 生成统计报告
7. 导出数据
0. 退出程序
```

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
pyinstaller --onefile --windowed --name=工时计算器 main.py
```

## 📊 技术栈

- **Android**: Java, SQLite, Material Design
- **Python**: Python 3.10+, Flask
- **打包**: PyInstaller (Windows), Gradle (Android)

## 📝 数据存储

- **Android**: SQLite数据库
- **Python**: JSON文件 (`work_records.json`)

## 📄 许可证

MIT License

## 👥 作者

Work Hour Calculator Team

## 🔗 GitHub

https://github.com/zmjhdfw/work-hour-calculator

---

**多平台支持，开箱即用！**
