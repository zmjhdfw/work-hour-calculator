@echo off
chcp 65001 >nul
echo ============================================================
echo GitHub Release 创建助手
echo ============================================================
echo.
echo 本脚本将帮助您创建GitHub Release并上传exe文件
echo.
echo 步骤1：打开浏览器创建Release页面
echo.
start https://github.com/zmjhdfw/work-hour-calculator/releases/new
echo.
echo 浏览器已打开，请按照以下步骤操作：
echo.
echo 1. 填写Tag version: v1.0.0
echo 2. 填写Release title: 工时计算器 v1.0.0 - 首次发布
echo 3. 复制release_notes.md的内容到描述框
echo 4. 上传exe文件: dist\工时计算器.exe
echo 5. 点击 "Publish release" 按钮
echo.
echo ============================================================
echo exe文件位置
echo ============================================================
echo.
echo 文件路径: %CD%\dist\工时计算器.exe
echo 文件大小:
dir dist\工时计算器.exe | find "工时计算器.exe"
echo.
echo ============================================================
echo Release Notes
echo ============================================================
echo.
echo Release Notes已保存在: release_notes.md
echo 请复制该文件内容到GitHub Release描述框
echo.
echo ============================================================
echo 按任意键打开release_notes.md文件...
pause >nul
start notepad release_notes.md
echo.
echo 按任意键打开exe文件所在文件夹...
pause >nul
start explorer dist
echo.
echo 完成后请关闭此窗口
pause >nul
