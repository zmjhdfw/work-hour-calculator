# 工时计算器 v1.0

一个简单易用的工时记录和统计工具，支持多平台使用。

## 📥 下载

### Windows
- **文件**: `工时计算器.exe`
- **大小**: 8 MB
- **要求**: Windows 7 或更高版本
- **使用**: 双击运行，无需安装

### Android
- **文件**: `工时计算器.apk`
- **大小**: 5.3 MB
- **要求**: Android 5.0 (API 21) 或更高版本
- **使用**: 安装APK即可使用

## ✨ 功能特性

### 核心功能
- ✅ 添加工时记录（日期、时间、项目、描述）
- ✅ 查看所有工时记录
- ✅ 统计分析（总工时、平均工时、记录数）
- ✅ 数据持久化存储
- ✅ 清空数据功能

### 平台特性
- **Windows**: 完整的命令行界面，支持编辑、删除、报告生成、CSV导出
- **Android**: Material Design界面，SQLite数据库，触摸友好

## 🎨 界面预览

### Android应用
- 主界面：显示记录数量，四个功能按钮
- 添加记录：日期、时间、项目输入
- 查看记录：列表显示所有记录
- 统计分析：总工时、平均工时统计

### Windows应用
- 命令行菜单界面
- 交互式输入
- 彩色输出
- 分页显示

## 🚀 快速开始

### Windows用户
1. 下载 `工时计算器.exe`
2. 双击运行
3. 按菜单提示操作

### Android用户
1. 下载 `工时计算器.apk`
2. 传输到手机
3. 允许安装未知来源应用
4. 安装并打开
5. 点击"添加记录"开始使用

## 📖 使用说明

### 添加记录
- **日期**: 格式 YYYY-MM-DD（如 2026-04-13）
- **开始时间**: 格式 HH:MM（如 09:00）
- **结束时间**: 格式 HH:MM（如 17:30）
- **项目**: 项目名称
- **描述**: 可选的工作描述

### 查看统计
- 总工时：所有记录的工时总和
- 记录数：总记录条数
- 平均工时：总工时÷记录数

## 🔧 技术信息

### Android版本
- **开发语言**: Java
- **最低SDK**: Android 5.0 (API 21)
- **目标SDK**: Android 13 (API 33)
- **数据库**: SQLite
- **UI框架**: Material Design
- **架构**: Activity + SQLiteOpenHelper

### Windows版本
- **开发语言**: Python 3.10
- **打包工具**: PyInstaller
- **数据存储**: JSON文件
- **界面**: 命令行

## 📊 项目结构

```
work-hour-calculator/
├── dist/
│   ├── 工时计算器.exe        # Windows可执行文件
│   └── 工时计算器.apk        # Android应用
├── android-app/              # Android源代码
├── work_hour_calculator/     # Python源代码
├── web_app.py                # Web应用
└── README.md                 # 项目说明
```

## 🔄 更新历史

### v1.0 (2026-04-13)
- ✅ 初始发布
- ✅ Windows EXE版本
- ✅ Android APK版本
- ✅ 自定义时钟图标
- ✅ 完整的工时计算功能
- ✅ 数据持久化存储

## 📝 已知问题

暂无已知问题。如遇到问题，请在GitHub提交Issue。

## 🔗 相关链接

- **GitHub仓库**: https://github.com/zmjhdfw/work-hour-calculator
- **问题反馈**: https://github.com/zmjhdfw/work-hour-calculator/issues

## 📄 许可证

MIT License

## 👥 作者

Work Hour Calculator Team

---

**感谢使用工时计算器！**
