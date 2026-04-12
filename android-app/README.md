# Android 工时计算器

一个使用Java开发的Android工时计算应用。

## 功能特性

- ✅ 添加工时记录
- ✅ 查看所有记录
- ✅ 统计分析
- ✅ 数据持久化存储
- ✅ Material Design界面

## 技术栈

- **Java** - 开发语言
- **Android SDK** - Android开发框架
- **SQLite** - 数据存储
- **Material Design** - UI设计

## 项目结构

```
android-app/
├── app/
│   ├── src/main/
│   │   ├── java/org/workhour/calculator/
│   │   │   ├── MainActivity.java          # 主界面
│   │   │   ├── AddRecordActivity.java     # 添加记录
│   │   │   ├── ViewRecordsActivity.java   # 查看记录
│   │   │   ├── StatisticsActivity.java    # 统计分析
│   │   │   ├── WorkRecord.java            # 数据模型
│   │   │   ├── DataManager.java           # 数据管理
│   │   │   └── Statistics.java            # 统计模型
│   │   ├── res/layout/                    # 布局文件
│   │   └── AndroidManifest.xml
│   └── build.gradle
├── build.gradle
└── settings.gradle
```

## 构建APK

### 前提条件

- Android Studio Arctic Fox或更高版本
- JDK 8或更高版本
- Android SDK 33

### 构建步骤

1. **使用Android Studio**:
   - 打开Android Studio
   - 选择 "Open an Existing Project"
   - 选择 `android-app` 目录
   - 等待Gradle同步完成
   - Build → Build Bundle(s) / APK(s) → Build APK(s)

2. **使用命令行**:
   ```bash
   cd android-app
   ./gradlew assembleDebug
   ```

3. **APK位置**:
   ```
   android-app/app/build/outputs/apk/debug/app-debug.apk
   ```

## 安装运行

1. 构建APK
2. 传输到Android设备
3. 安装APK
4. 打开应用

## 使用说明

### 添加记录
- 点击"添加记录"按钮
- 填写日期、时间、项目等信息
- 点击"保存"

### 查看记录
- 点击"查看记录"按钮
- 查看所有工时记录列表

### 统计分析
- 点击"统计分析"按钮
- 查看总工时、记录数、平均工时

## 开发信息

- **包名**: org.workhour.calculator
- **最低SDK**: Android 5.0 (API 21)
- **目标SDK**: Android 13 (API 33)
- **版本**: 1.0

---

**使用Java原生开发，稳定可靠！**
