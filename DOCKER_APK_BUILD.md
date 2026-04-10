# 🐳 使用Docker打包APK（推荐方案）

## 为什么使用Docker？

- ✅ 无需配置复杂的环境
- ✅ 一键打包，简单快速
- ✅ 环境隔离，不影响系统
- ✅ 可重复构建

## 🚀 快速开始

### 前提条件

安装Docker Desktop：https://www.docker.com/products/docker-desktop

### 一键打包命令

```bash
docker run --rm -v "%cd%":/home/user/app -w /home/user/app kivy/buildozer android debug
```

### 完整打包脚本

创建 `build_apk_docker.bat`：

```batch
@echo off
echo 正在使用Docker打包APK...
docker run --rm -v "%cd%":/home/user/app -w /home/user/app kivy/buildozer android debug
echo 打包完成！
pause
```

## 📦 Docker方案优势

1. **无需WSL** - 直接在Windows上运行
2. **无需配置** - Docker镜像已包含所有依赖
3. **快速可靠** - 避免环境配置问题
4. **可重复** - 每次构建结果一致

## 🔧 详细步骤

### 1. 安装Docker Desktop

下载并安装：https://www.docker.com/products/docker-desktop

### 2. 拉取Buildozer镜像

```bash
docker pull kivy/buildozer
```

### 3. 打包APK

```bash
# Debug版本
docker run --rm -v "%cd%":/home/user/app -w /home/user/app kivy/buildozer android debug

# Release版本
docker run --rm -v "%cd%":/home/user/app -w /home/user/app kivy/buildozer android release
```

### 4. 查看结果

APK文件将生成在 `bin/` 目录中。

## ⏱️ 时间预估

- **首次运行**：10-20分钟（拉取Docker镜像）
- **后续打包**：5-10分钟

## 🎯 推荐方案对比

| 方案 | 难度 | 时间 | 稳定性 |
|------|------|------|--------|
| Docker | ⭐ 简单 | 快 | ⭐⭐⭐⭐⭐ |
| WSL | ⭐⭐⭐ 中等 | 慢 | ⭐⭐⭐ |
| 虚拟机 | ⭐⭐⭐⭐ 困难 | 很慢 | ⭐⭐ |

## 📱 使用Docker打包

**推荐使用Docker方案！**

1. 安装Docker Desktop
2. 运行打包命令
3. 获取APK文件

简单、快速、可靠！
