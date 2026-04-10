# 🌐 在线打包APK方案（最简单）

## 推荐方案：GitHub Actions自动打包

### 优势

- ✅ 完全自动化
- ✅ 无需本地环境
- ✅ 免费使用GitHub资源
- ✅ 每次推送自动构建

## 🚀 设置步骤

### 1. 创建GitHub Actions配置

在项目中创建 `.github/workflows/build-apk.yml`：

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
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install buildozer cython
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-11-jdk autoconf libtool pkg-config libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev automake build-essential

    - name: Build APK
      run: |
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk

    - name: Create Release
      if: startsWith(github.ref, 'refs/tags/')
      uses: softprops/action-gh-release@v1
      with:
        files: bin/*.apk
```

### 2. 推送到GitHub

```bash
git add .github/workflows/build-apk.yml
git commit -m "Add GitHub Actions for APK build"
git push
```

### 3. 触发构建

#### 方式1：创建Tag

```bash
git tag v1.0.0
git push --tags
```

#### 方式2：手动触发

1. 访问仓库的 Actions 页面
2. 选择 "Build Android APK"
3. 点击 "Run workflow"

### 4. 下载APK

构建完成后：
1. 进入 Actions 页面
2. 点击完成的workflow
3. 在 Artifacts 中下载 APK

## 📦 方案对比

| 方案 | 难度 | 时间 | 成本 |
|------|------|------|------|
| GitHub Actions | ⭐ 最简单 | 20-30分钟 | 免费 |
| Docker | ⭐⭐ 简单 | 10-20分钟 | 免费 |
| WSL | ⭐⭐⭐⭐ 复杂 | 1-2小时 | 免费 |
| 云服务器 | ⭐⭐⭐ 中等 | 30分钟 | 付费 |

## 🎯 推荐使用GitHub Actions

**最简单的方案！**

1. 创建配置文件
2. 推送到GitHub
3. 自动构建APK
4. 下载使用

无需任何本地环境配置！

## 📱 其他在线方案

### 1. GitLab CI/CD

类似GitHub Actions，在GitLab上自动构建。

### 2. CircleCI

提供免费的Android构建环境。

### 3. Bitrise

专门的移动应用CI/CD平台。

## 💡 建议

**强烈推荐使用GitHub Actions！**

- 完全自动化
- 无需配置本地环境
- 免费且可靠
- 与GitHub仓库完美集成

只需创建一个配置文件，推送后自动构建APK！
