# GitHub推送操作指南

## 当前Git状态

✅ Git仓库已初始化
✅ 所有代码已提交（3个提交）
✅ 准备推送到GitHub

## 推送步骤

### 步骤1：在GitHub上创建仓库

1. 打开浏览器，访问：https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `work-hour-calculator`
   - **Description**: `Python工时计算程序 - 记录、计算和统计工作工时`
   - **Visibility**: 选择 Public（公开）或 Private（私有）
   - **重要**: ❌ 不要勾选以下选项：
     - Add a README file
     - Add .gitignore
     - Choose a license
3. 点击 **"Create repository"** 按钮

### 步骤2：获取仓库地址

创建完成后，GitHub会显示仓库地址，类似：
- HTTPS: `https://github.com/YOUR_USERNAME/work-hour-calculator.git`
- SSH: `git@github.com:YOUR_USERNAME/work-hour-calculator.git`

### 步骤3：添加远程仓库

在命令行中执行（替换YOUR_USERNAME为您的GitHub用户名）：

```bash
# 使用HTTPS（推荐）
git remote add origin https://github.com/YOUR_USERNAME/work-hour-calculator.git

# 或使用SSH（如果已配置SSH密钥）
git remote add origin git@github.com:YOUR_USERNAME/work-hour-calculator.git
```

### 步骤4：推送代码

```bash
git push -u origin master
```

## 认证方式

### 方式1：Personal Access Token（推荐）

如果推送时提示输入密码，需要使用Personal Access Token：

1. 访问：https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 设置：
   - Note: "Work Hour Calculator"
   - Expiration: 选择有效期
   - Select scopes: 勾选 `repo`（完整仓库权限）
4. 点击 "Generate token"
5. **重要**: 复制token（只显示一次）
6. 推送时，在密码处粘贴token

### 方式2：SSH密钥

如果您配置了SSH密钥，可以使用SSH地址推送：

```bash
git remote set-url origin git@github.com:YOUR_USERNAME/work-hour-calculator.git
git push -u origin master
```

### 方式3：GitHub Desktop

1. 打开GitHub Desktop
2. File → Add local repository → 选择 `C:\410`
3. Publish repository → 填写信息 → Publish

## 推送后操作

### 1. 添加仓库描述和主题

进入仓库设置，添加：
- Description: `Python工时计算程序 - 记录、计算和统计工作工时`
- Website: （可选）
- Topics: `python`, `work-hours`, `time-tracking`, `cli`, `web-app`, `chinese`

### 2. 创建第一个Release

1. 进入仓库的 "Releases" 页面
2. 点击 "Draft a new release"
3. 填写：
   - Tag version: `v1.0.0`
   - Release title: `工时计算器 v1.0.0 - 首次发布`
   - Description:
     ```
     ## 功能特性
     - ✅ 完整的工时记录管理
     - ✅ 工时计算和统计
     - ✅ 报告生成
     - ✅ 数据导出
     - ✅ Windows可执行文件
     - ✅ Web界面

     ## 下载
     - Windows用户：下载 `工时计算器.exe` 直接运行
     - 其他平台：克隆仓库后运行 `python run.py`
     ```
4. 上传文件：`dist/工时计算器.exe`
5. 点击 "Publish release"

### 3. 添加徽章到README

在README.md顶部添加：

```markdown
![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/work-hour-calculator?style=social)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/work-hour-calculator?style=social)
![GitHub release](https://img.shields.io/github/release/YOUR_USERNAME/work-hour-calculator)
![GitHub license](https://img.shields.io/github/license/YOUR_USERNAME/work-hour-calculator)
```

## 常见问题

### Q: 推送时提示 "remote: Repository not found"
A: 仓库未创建或地址错误，请检查仓库地址

### Q: 推送时提示 "Permission denied"
A: 需要认证，请使用Personal Access Token或SSH密钥

### Q: 推送时提示 "fatal: remote origin already exists"
A: 远程仓库已添加，可以更新地址：
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/work-hour-calculator.git
```

### Q: 如何查看当前远程仓库？
A: 执行：
```bash
git remote -v
```

## 快速命令

如果您已经创建好仓库，可以直接执行：

```bash
# 替换YOUR_USERNAME为您的GitHub用户名
git remote add origin https://github.com/YOUR_USERNAME/work-hour-calculator.git
git push -u origin master
```

## 需要帮助？

- GitHub文档：https://docs.github.com
- Git教程：https://git-scm.com/book
- 项目文档：查看 `GITHUB_PUSH.md` 和 `PROJECT_SUMMARY.md`
