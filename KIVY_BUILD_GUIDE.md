# Kivy APK打包指南

## 📋 准备工作

### 1. 安装依赖

#### Windows系统

Kivy打包APK需要在Linux环境下进行。推荐使用WSL（Windows Subsystem for Linux）或虚拟机。

#### 使用WSL（推荐）

```bash
# 1. 启用WSL
wsl --install

# 2. 安装Ubuntu
wsl --install -d Ubuntu-22.04

# 3. 进入WSL
wsl
```

#### Linux系统（Ubuntu/Debian）

```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装依赖
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev automake build-essential

# 安装Buildozer
pip3 install buildozer

# 安装Cython
pip3 install cython
```

### 2. 配置环境变量

```bash
# 设置Java环境
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin
```

## 🚀 打包步骤

### 步骤1：准备项目文件

确保以下文件存在：
- `main_kivy.py` - Kivy主程序
- `buildozer.spec` - Buildozer配置
- `work_hour_calculator/` - 核心模块

### 步骤2：初始化Buildozer

```bash
# 进入项目目录
cd /mnt/c/410  # WSL中访问Windows目录

# 初始化（如果还没有buildozer.spec）
buildozer init

# 或者直接使用已有的buildozer.spec
```

### 步骤3：调试模式打包

```bash
# 首次打包（会自动下载Android SDK/NDK，需要较长时间）
buildozer android debug

# 或者只打包不部署
buildozer android debug deploy
```

### 步骤4：发布模式打包

```bash
# 生成签名的APK
buildozer android release

# 或者使用AAB格式（Google Play推荐）
buildozer android release aab
```

## 📱 打包输出

打包完成后，APK文件位于：
```
bin/workhourcalculator-1.0.0-arm64-v8a-debug.apk
bin/workhourcalculator-1.0.0-arm64-v8a-release.apk
```

## ⚙️ 配置说明

### buildozer.spec 关键配置

```ini
[app]
# 应用名称
title = 工时计算器

# 包名
package.name = workhourcalculator
package.domain = org.workhour

# 版本
version = 1.0.0

# 依赖
requirements = python3,kivy

# 权限
android.permissions = INTERNET

# Android API版本
android.api = 31
android.minapi = 21

# 支持的架构
android.archs = arm64-v8a, armeabi-v7a
```

## 🔧 常见问题

### Q1: 下载SDK/NDK很慢怎么办？

使用国内镜像：
```bash
# 设置环境变量
export GRADLE_OPTS="-Dorg.gradle.jvmargs=-Xmx2048m"
```

### Q2: 打包失败提示缺少依赖？

安装所有依赖：
```bash
buildozer android debug --verbose
```

### Q3: 如何减小APK大小？

在buildozer.spec中：
```ini
# 只包含需要的架构
android.archs = arm64-v8a

# 排除不需要的文件
source.exclude_dirs = tests, dist, build
```

### Q4: 如何添加图标和启动画面？

```ini
icon.filename = icon.png
presplash.filename = presplash.png
```

## 📦 快速打包脚本

创建 `build_apk.sh`：

```bash
#!/bin/bash

echo "=========================================="
echo "Kivy APK打包脚本"
echo "=========================================="

# 检查环境
if ! command -v buildozer &> /dev/null; then
    echo "安装Buildozer..."
    pip3 install buildozer cython
fi

# 清理旧文件
echo "清理旧的构建文件..."
rm -rf .buildozer bin

# 打包APK
echo "开始打包APK..."
buildozer android debug

# 检查结果
if [ -f "bin/"*.apk ]; then
    echo "=========================================="
    echo "打包成功！"
    echo "=========================================="
    echo "APK文件："
    ls -lh bin/*.apk
else
    echo "打包失败！"
fi
```

## 🎯 完整打包流程

### 在WSL中执行：

```bash
# 1. 进入WSL
wsl

# 2. 进入项目目录
cd /mnt/c/410

# 3. 安装依赖（首次）
sudo apt update
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip
pip3 install buildozer cython

# 4. 打包APK
buildozer android debug

# 5. 查看结果
ls -lh bin/*.apk
```

## 📱 安装测试

### 使用ADB安装

```bash
# 安装ADB
sudo apt install android-tools-adb

# 连接手机（开启USB调试）
adb devices

# 安装APK
adb install bin/workhourcalculator-1.0.0-arm64-v8a-debug.apk
```

### 直接传输安装

1. 将APK文件传输到手机
2. 在手机上打开文件管理器
3. 点击APK文件安装
4. 允许安装未知来源应用

## 🔄 更新版本

修改 `buildozer.spec`：
```ini
version = 1.1.0
```

重新打包：
```bash
buildozer android debug
```

## 📤 上传到GitHub

打包完成后，将APK上传到GitHub Release：

1. 创建新Release
2. 上传APK文件
3. 发布Release

## 🎊 完成！

按照以上步骤，您就可以成功打包APK文件了！

### 预计时间

- 首次打包：30-60分钟（下载SDK/NDK）
- 后续打包：5-10分钟

### APK大小

- Debug版本：约20-30 MB
- Release版本：约15-20 MB
