# 📦 上传exe文件和创建Release指南

## 当前状态

✅ exe文件已生成：`dist/工时计算器.exe` (7.64 MB)
✅ 代码已推送到GitHub
❌ 需要创建Release并上传exe文件

## 🚀 创建Release并上传exe文件

### 方法1：通过GitHub网页（推荐）

#### 步骤1：访问Releases页面

打开浏览器访问：
**https://github.com/zmjhdfw/work-hour-calculator/releases/new**

#### 步骤2：填写Release信息

1. **Tag version**: `v1.0.0`
   - 点击 "Choose a tag"
   - 输入 `v1.0.0`
   - 点击 "Create new tag: v1.0.0 on publication"

2. **Release title**: `工时计算器 v1.0.0 - 首次发布`

3. **Describe this release**:
```markdown
# 工时计算器 v1.0.0

## 🎉 首次发布

一个简单易用的Python工时记录和统计工具。

## ✨ 功能特性

- ✅ 完整的工时记录管理（添加、查看、编辑、删除）
- ✅ 按日期、日期范围、项目查询记录
- ✅ 工时计算和统计（总工时、正常工时、加班工时）
- ✅ 生成统计报告（摘要报告、项目报告、详细报告）
- ✅ 数据导出为CSV格式
- ✅ 中文界面
- ✅ Windows可执行文件
- ✅ Web界面（移动端友好）

## 📥 下载安装

### Windows用户（推荐）

1. 下载 `工时计算器.exe`
2. 双击运行即可，无需安装Python

### 其他平台

```bash
# 克隆仓库
git clone https://github.com/zmjhdfw/work-hour-calculator.git
cd work-hour-calculator

# 命令行版本
python run.py

# Web版本（需要安装Flask）
pip install flask
python web_app.py
```

## 📖 使用文档

- [快速入门](https://github.com/zmjhdfw/work-hour-calculator/blob/master/QUICKSTART.md)
- [完整文档](https://github.com/zmjhdfw/work-hour-calculator/blob/master/README.md)
- [移动端说明](https://github.com/zmjhdfw/work-hour-calculator/blob/master/MOBILE_BUILD.md)

## 📊 项目信息

- 开发语言：Python 3.7+
- 支持平台：Windows, Web, 移动端
- 文件大小：7.64 MB
- 测试覆盖：9个单元测试全部通过

## 🐛 问题反馈

如遇到问题，请在 [Issues](https://github.com/zmjhdfw/work-hour-calculator/issues) 页面反馈。
```

#### 步骤3：上传exe文件

1. 在 "Attach binaries" 区域
2. 点击 "选择文件" 或拖拽文件
3. 选择 `C:\410\dist\工时计算器.exe`
4. 等待上传完成

#### 步骤4：发布Release

1. 选择 "Set as the latest release"
2. 点击 **"Publish release"** 按钮

### 方法2：使用GitHub CLI（如果已安装）

```bash
# 安装GitHub CLI
winget install GitHub.cli

# 登录
gh auth login

# 创建Release并上传文件
gh release create v1.0.0 \
  --title "工时计算器 v1.0.0 - 首次发布" \
  --notes-file release_notes.md \
  dist/工时计算器.exe
```

### 方法3：使用GitHub API

```bash
# 需要Personal Access Token
curl -X POST \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"tag_name":"v1.0.0","name":"工时计算器 v1.0.0"}' \
  https://api.github.com/repos/zmjhdfw/work-hour-calculator/releases
```

## 📱 关于APK文件

### 当前状态

由于工时计算程序是命令行/Web应用，没有直接生成APK文件。

### 解决方案

#### 方案1：使用Web版本（推荐）

Web版本已经创建，可以在手机浏览器中使用：

```bash
# 运行Web服务器
python web_app.py

# 手机访问（同一局域网）
http://<电脑IP>:5000
```

#### 方案2：打包成APK

如需打包成Android APK，可以选择：

1. **BeeWare** - Python移动应用框架
2. **Kivy** - 跨平台Python框架
3. **PWA** - 渐进式Web应用

详见：`MOBILE_BUILD.md`

#### 方案3：创建WebView APK

使用Android Studio创建WebView应用，加载Web版本。

## 📋 检查清单

创建Release前请确认：

- [ ] exe文件已生成（`dist/工时计算器.exe`）
- [ ] 代码已推送到GitHub
- [ ] 准备好Release Notes
- [ ] 准备好上传exe文件

创建Release后请确认：

- [ ] Release已发布
- [ ] exe文件已上传
- [ ] 可以从Release页面下载exe
- [ ] README中的下载链接正确

## 🔗 快速链接

- **创建Release**: https://github.com/zmjhdfw/work-hour-calculator/releases/new
- **Releases列表**: https://github.com/zmjhdfw/work-hour-calculator/releases
- **仓库主页**: https://github.com/zmjhdfw/work-hour-calculator

## 💡 提示

1. **文件大小限制**: GitHub单个文件限制100MB，exe文件7.64MB，可以正常上传
2. **Release数量**: 建议每个重要版本创建一个Release
3. **版本号**: 使用语义化版本号（v1.0.0, v1.1.0等）
4. **更新日志**: 每次Release都应包含更新日志

## 🎯 下一步

1. 按照上述步骤创建Release
2. 上传exe文件
3. 发布Release
4. 测试下载链接是否正常

完成后，用户就可以从GitHub Release页面下载exe文件了！
