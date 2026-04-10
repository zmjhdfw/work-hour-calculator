# 🔧 APK构建故障排查指南

## 常见失败原因

### 1. buildozer.spec配置问题

**问题**: 配置文件格式错误或缺少必要字段

**解决方案**:
检查 `buildozer.spec` 文件，确保包含：
```ini
[app]
title = 工时计算器
package.name = workhourcalculator
package.domain = org.workhour
source.dir = .
version = 1.0.0
requirements = python3,kivy
orientation = portrait
```

### 2. 依赖缺失

**问题**: 缺少必要的Python包或系统库

**解决方案**:
在 `.github/workflows/build-apk.yml` 中添加：
```yaml
- name: Install Python dependencies
  run: |
    pip install --upgrade pip
    pip install buildozer cython
    pip install kivy
```

### 3. 源文件路径问题

**问题**: 找不到main.py或源文件

**解决方案**:
- 确保项目根目录有 `main_kivy.py`
- 或在buildozer.spec中指定：
```ini
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
```

### 4. Android SDK/NDK下载失败

**问题**: 网络问题导致下载失败

**解决方案**:
- GitHub Actions会自动重试
- 或使用缓存加速：
```yaml
- name: Cache Buildozer
  uses: actions/cache@v3
  with:
    path: ~/.buildozer
    key: ${{ runner.os }}-buildozer
```

## 🚀 快速修复方案

### 方案1：更新workflow配置

创建更完善的构建配置：

```yaml
name: Build Android APK

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-11-jdk \
          autoconf libtool pkg-config libncurses5-dev \
          libncursesw5-dev libtinfo5 cmake libffi-dev \
          libssl-dev automake build-essential

    - name: Install Buildozer
      run: |
        pip install --upgrade pip
        pip install buildozer cython

    - name: Build APK
      run: |
        buildozer android debug

    - uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk
```

### 方案2：使用预构建Docker镜像

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    container: kivy/buildozer

    steps:
    - uses: actions/checkout@v3

    - name: Build APK
      run: buildozer android debug

    - uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk
```

### 方案3：使用现成的Action

```yaml
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Build with Buildozer Action
      uses: ArtemSBulgakov/buildozer-action@v1
      with:
        command: android debug

    - uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk
```

## 📋 检查清单

构建前请确认：

- [ ] `main_kivy.py` 存在且可运行
- [ ] `buildozer.spec` 配置正确
- [ ] `work_hour_calculator/` 模块完整
- [ ] GitHub Actions配置正确
- [ ] 仓库有正确的文件结构

## 🔍 查看错误日志

1. 访问 Actions 页面
2. 点击失败的workflow
3. 展开失败的步骤
4. 查看详细错误信息

## 💡 常见错误信息

### "No main.py found"
**解决**: 重命名 `main_kivy.py` 为 `main.py`

### "Buildozer failed"
**解决**: 检查buildozer.spec配置

### "Permission denied"
**解决**: 添加权限到workflow

### "Out of memory"
**解决**: 使用更小的构建配置

## 🎯 推荐方案

**最可靠的方案：使用Docker容器**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    container: kivy/buildozer

    steps:
    - uses: actions/checkout@v3
    - run: buildozer android debug
    - uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk
```

## 📞 获取帮助

如果仍然失败：

1. 查看完整错误日志
2. 检查GitHub Actions文档
3. 查看Buildozer文档
4. 在Issues中提问

## 🔄 重新构建

修复问题后：

```bash
# 删除旧tag
git tag -d v1.0.0-apk
git push --delete origin v1.0.0-apk

# 创建新tag
git tag v1.0.1-apk
git push --tags
```

或手动触发workflow。

---

**提示**: 大多数构建失败都是配置问题，仔细检查buildozer.spec和workflow配置。
