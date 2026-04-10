# 🚀 快速打包APK指南

## ✅ 准备工作已完成

- ✅ Kivy主程序：`main_kivy.py`
- ✅ Buildozer配置：`buildozer.spec`
- ✅ WSL已安装：Ubuntu
- ✅ 核心模块：`work_hour_calculator/`

## 📋 打包步骤

### 方式1：使用批处理脚本（推荐）

直接双击运行：
```
build_kivy_apk.bat
```

### 方式2：手动执行

#### 步骤1：打开WSL

```bash
wsl
```

#### 步骤2：进入项目目录

```bash
cd /mnt/c/410
```

#### 步骤3：安装依赖（首次）

```bash
# 更新系统
sudo apt update

# 安装必要工具
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip \
    autoconf libtool pkg-config libncurses5-dev \
    libncursesw5-dev libtinfo5 cmake libffi-dev \
    libssl-dev automake build-essential

# 安装Buildozer和Cython
pip3 install --upgrade buildozer cython
```

#### 步骤4：打包APK

```bash
# 调试版本
buildozer android debug

# 或发布版本
buildozer android release
```

#### 步骤5：查看结果

```bash
ls -lh bin/*.apk
```

## 📱 APK文件位置

打包成功后，APK文件位于：
```
C:\410\bin\workhourcalculator-1.0.0-arm64-v8a-debug.apk
```

## ⏱️ 预计时间

- **首次打包**：30-60分钟（下载Android SDK/NDK）
- **后续打包**：5-10分钟

## 📦 APK信息

- **应用名称**：工时计算器
- **包名**：org.workhour.workhourcalculator
- **版本**：1.0.0
- **大小**：约20-30 MB（Debug版本）
- **支持架构**：arm64-v8a, armeabi-v7a

## 🔧 常见问题

### Q1: WSL未启动？

```bash
wsl --start
```

### Q2: 权限问题？

```bash
# 在WSL中执行
sudo chmod -R 755 /mnt/c/410
```

### Q3: 下载很慢？

首次打包需要下载Android SDK和NDK（约2-3GB），请耐心等待。

### Q4: 打包失败？

查看详细日志：
```bash
buildozer android debug --verbose
```

## 📤 安装APK

### 方式1：ADB安装

```bash
# 安装ADB
sudo apt install android-tools-adb

# 连接手机（开启USB调试）
adb devices

# 安装APK
adb install bin/workhourcalculator-1.0.0-arm64-v8a-debug.apk
```

### 方式2：直接安装

1. 将APK文件复制到手机
2. 在手机上打开文件管理器
3. 点击APK文件安装
4. 允许安装未知来源应用

## 🎯 下一步

1. 运行 `build_kivy_apk.bat` 开始打包
2. 等待打包完成
3. 将APK上传到GitHub Release
4. 或直接安装到手机测试

## 📖 详细文档

- 完整指南：`KIVY_BUILD_GUIDE.md`
- 项目说明：`README.md`

---

**提示**：首次打包需要较长时间，请确保网络连接稳定。
