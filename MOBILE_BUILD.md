# 移动端打包说明

## Web版本

本项目提供了Web版本的工时计算程序，可以通过以下方式在移动设备上使用：

### 运行Web版本

1. 安装依赖：
```bash
pip install flask
```

2. 运行Web服务器：
```bash
python web_app.py
```

3. 在浏览器中访问：`http://localhost:5000`

4. 在移动设备上访问：`http://<你的电脑IP>:5000`

### 打包成Android APK

有多种方式可以将Web应用打包成Android APK：

#### 方法1：使用BeeWare (推荐)

1. 安装Briefcase：
```bash
pip install briefcase
```

2. 创建Android应用：
```bash
briefcase create android
```

3. 构建APK：
```bash
briefcase build android
```

4. 运行应用：
```bash
briefcase run android
```

#### 方法2：使用Kivy + Buildozer

1. 安装Kivy：
```bash
pip install kivy
```

2. 创建main.py（Kivy版本）

3. 使用Buildozer打包：
```bash
buildozer init
buildozer android debug
```

#### 方法3：使用WebView包装器

使用Android Studio创建一个WebView应用，加载Web版本：

1. 创建Android项目
2. 添加WebView组件
3. 加载本地HTML或远程URL
4. 打包生成APK

#### 方法4：使用PWA (渐进式Web应用)

将Web应用转换为PWA，可以在移动设备上像原生应用一样使用：

1. 添加manifest.json
2. 添加Service Worker
3. 支持离线访问
4. 添加到主屏幕

## 当前推荐方案

由于工时计算程序主要是数据管理和统计功能，推荐以下方案：

1. **Windows用户**：使用已打包的exe文件
   - 文件位置：`dist/工时计算器.exe`
   - 双击运行即可

2. **移动端用户**：使用Web版本
   - 在电脑上运行 `python web_app.py`
   - 手机浏览器访问电脑IP地址
   - 或部署到云服务器，随时随地访问

3. **开发者**：根据需要选择打包方式
   - BeeWare：适合Python开发者
   - Kivy：适合需要原生UI的应用
   - PWA：适合Web应用快速部署

## Web版本特性

- ✅ 响应式设计，适配移动设备
- ✅ 美观的UI界面
- ✅ 完整的CRUD功能
- ✅ 实时统计和可视化
- ✅ 数据导出功能
- ✅ 支持多用户（需扩展）

## 部署建议

### 本地使用
```bash
python web_app.py
```

### 局域网访问
```bash
python web_app.py --host=0.0.0.0
```

### 云服务器部署
1. 使用Gunicorn或uWSGI
2. 配置Nginx反向代理
3. 启用HTTPS
4. 设置域名

示例：
```bash
gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
```
