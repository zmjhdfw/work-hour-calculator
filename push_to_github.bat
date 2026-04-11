@echo off
chcp 65001 >nul
echo ============================================================
echo GitHub推送助手
echo ============================================================
echo.
echo 本脚本将帮助您将工时计算程序推送到GitHub
echo.
echo 请按照以下步骤操作：
echo.
echo 1. 在GitHub上创建新仓库
echo    - 访问: https://github.com/new
echo    - Repository name: work-hour-calculator
echo    - Description: Python工时计算程序
echo    - 不要勾选任何初始化选项
echo.
echo 2. 创建完成后，输入您的GitHub用户名：
echo.
set /p username="zmjhdfw"
echo.
echo 3. 添加远程仓库...
git remote add origin https://github.com/%username%/work-hour-calculator.git
echo.
echo 4. 推送代码到GitHub...
git push -u origin master
echo.
if %errorlevel% equ 0 (
    echo ============================================================
    echo 推送成功！
    echo ============================================================
    echo.
    echo 您的仓库地址: https://github.com/%username%/work-hour-calculator
    echo.
    echo 下一步建议：
    echo 1. 添加仓库描述和主题标签
    echo 2. 创建v1.0.0 Release并上传exe文件
    echo 3. 添加README徽章
    echo.
) else (
    echo ============================================================
    echo 推送失败
    echo ============================================================
    echo.
    echo 可能的原因：
    echo 1. 仓库未创建
    echo 2. 需要GitHub认证（Personal Access Token或SSH密钥）
    echo 3. 网络连接问题
    echo.
    echo 请查看 GITHUB_PUSH.md 获取详细帮助
    echo.
)
pause
