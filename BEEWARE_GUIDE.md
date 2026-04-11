# BeeWare APK构建指南

## 🎯 BeeWare优势

相比Kivy，BeeWare有以下优势：
- ✅ 更简单的配置
- ✅ 原生UI外观
- ✅ 更好的文档
- ✅ 活跃的社区支持
- ✅ 一条命令打包

## 📋 准备工作

### 安装Briefcase

```bash
pip install briefcase
```

### 验证安装

```bash
briefcase --version
```

## 🚀 构建步骤

### 步骤1：创建应用

```bash
briefcase create
```

### 步骤2：构建Android应用

```bash
briefcase create android
```

### 步骤3：构建APK

```bash
briefcase build android
```

### 步骤4：运行APK（可选）

```bash
briefcase run android
```

## 📦 完整流程

```bash
# 1. 安装Briefcase
pip install briefcase

# 2. 进入项目目录
cd c:\410

# 3. 创建Android项目
briefcase create android

# 4. 构建APK
briefcase build android

# 5. 查看APK
# APK位置：android/gradle/workhourcalculator/build/outputs/apk/
```

## 🔧 配置说明

### pyproject.toml

```toml
[tool.briefcase]
project_name = "工时计算器"
bundle = "org.workhour"
version = "1.0.0"

[tool.briefcase.app.workhourcalculator]
formal_name = "工时计算器"
description = "Python工时计算程序"
sources = ['app.py']
requires = []
```

### app.py

使用Toga框架构建UI：
- 原生外观
- 跨平台支持
- 简单易用

## 📱 支持平台

BeeWare支持：
- ✅ Android (APK)
- ✅ iOS (IPA)
- ✅ Windows (EXE)
- ✅ macOS (APP)
- ✅ Linux (DEB/RPM)

## ⏱️ 构建时间

- **首次构建**：10-15分钟
- **后续构建**：2-5分钟

## 🎯 GitHub Actions自动构建

创建 `.github/workflows/build-beeware.yml`：

```yaml
name: Build APK with BeeWare

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install Briefcase
      run: |
        pip install --upgrade pip
        pip install briefcase

    - name: Create Android Project
      run: |
        briefcase create android

    - name: Build APK
      run: |
        briefcase build android

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: work-hour-calculator-apk
        path: android/gradle/workhourcalculator/build/outputs/apk/**/*.apk
```

## 💡 常见问题

### Q: 构建失败？

确保：
- Python 3.8-3.11
- Java 11或17
- Android SDK已安装

### Q: 如何调试？

```bash
briefcase run android --log
```

### Q: 如何更新？

```bash
briefcase update android
briefcase build android
```

## 📊 BeeWare vs Kivy

| 特性 | BeeWare | Kivy |
|------|---------|------|
| UI外观 | 原生 | 自定义 |
| 学习曲线 | 简单 | 中等 |
| 配置复杂度 | 低 | 高 |
| 构建时间 | 快 | 慢 |
| 文档质量 | 优秀 | 良好 |

## 🎯 推荐使用BeeWare

对于工时计算应用，BeeWare是更好的选择：
- ✅ 配置简单
- ✅ 原生UI
- ✅ 构建快速
- ✅ 维护容易

---

**使用BeeWare，APK构建将更加简单可靠！**
