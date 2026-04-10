# GitHub推送指南

## 方法1：手动创建GitHub仓库并推送

### 步骤1：在GitHub上创建仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - Repository name: `work-hour-calculator`
   - Description: `Python工时计算程序 - 记录、计算和统计工作工时`
   - 选择 Public 或 Private
   - **不要**勾选 "Add a README file"
   - **不要**勾选 "Add .gitignore"
   - **不要**选择 License
3. 点击 "Create repository"

### 步骤2：推送代码到GitHub

创建仓库后，GitHub会显示推送命令。使用以下命令：

```bash
# 添加远程仓库（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/work-hour-calculator.git

# 推送代码到GitHub
git push -u origin master
```

或者使用SSH（如果已配置SSH密钥）：

```bash
git remote add origin git@github.com:YOUR_USERNAME/work-hour-calculator.git
git push -u origin master
```

## 方法2：使用GitHub CLI（如果已安装）

### 安装GitHub CLI

Windows:
```bash
winget install GitHub.cli
```

或从 https://cli.github.com/ 下载安装

### 使用GitHub CLI创建并推送

```bash
# 登录GitHub
gh auth login

# 创建仓库并推送
gh repo create work-hour-calculator --public --source=. --remote=origin --push

# 或者创建私有仓库
gh repo create work-hour-calculator --private --source=. --remote=origin --push
```

## 方法3：使用GitHub Desktop

1. 下载并安装 GitHub Desktop: https://desktop.github.com/
2. 打开 GitHub Desktop
3. 登录GitHub账户
4. File → Add local repository → 选择 `C:\410` 目录
5. Publish repository → 填写仓库名称和描述 → Publish repository

## 推送后的操作

推送成功后，建议：

1. **添加仓库描述和主题标签**
   - Description: Python工时计算程序
   - Topics: python, work-hours, time-tracking, cli, web-app

2. **创建Release**
   - 进入仓库的 Releases 页面
   - 点击 "Draft a new release"
   - Tag version: v1.0.0
   - Release title: 工时计算器 v1.0.0
   - 上传 `dist/工时计算器.exe` 文件
   - 发布Release

3. **启用GitHub Pages（可选）**
   - 如果想展示Web版本，可以启用GitHub Pages
   - Settings → Pages → Source: Deploy from a branch

4. **添加徽章到README.md**
   ```markdown
   ![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/work-hour-calculator)
   ![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/work-hour-calculator)
   ![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/work-hour-calculator)
   ```

## 当前Git状态

```bash
# 查看当前状态
git status

# 查看提交历史
git log --oneline

# 查看远程仓库
git remote -v
```

## 常见问题

### Q: 推送时提示权限被拒绝？
A: 需要配置GitHub认证：
- 使用Personal Access Token (PAT)
- 或配置SSH密钥
- 或使用GitHub Desktop

### Q: 如何更新代码？
A:
```bash
git add .
git commit -m "更新说明"
git push
```

### Q: 如何添加exe文件到Release？
A: GitHub限制单个文件100MB，exe文件约7.6MB，可以直接上传到Release。

## 下一步

选择一种方法推送代码到GitHub后，您的工时计算程序就可以：
- ✅ 在GitHub上展示
- ✅ 其他人可以克隆和使用
- ✅ 下载exe可执行文件
- ✅ 查看Web版本演示
