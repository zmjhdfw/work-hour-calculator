@echo off
chcp 65001 >nul
echo ============================================================
echo Kivy APK打包助手
echo ============================================================
echo.
echo 本脚本将帮助您使用Kivy打包Android APK
echo.
echo 注意：APK打包需要在Linux环境下进行
echo 将使用WSL (Windows Subsystem for Linux)
echo.
echo ============================================================
echo 步骤1：检查WSL
echo ============================================================
echo.
wsl --list --verbose 2>nul
if %errorlevel% neq 0 (
    echo WSL未安装，正在安装...
    wsl --install -d Ubuntu-22.04
    echo.
    echo WSL已安装，请重启电脑后再次运行此脚本
    pause
    exit /b
)
echo.
echo ============================================================
echo 步骤2：准备打包环境
echo ============================================================
echo.
echo 正在WSL中安装依赖...
wsl bash -c "sudo apt update && sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev automake build-essential"
wsl bash -c "pip3 install --upgrade buildozer cython"
echo.
echo ============================================================
echo 步骤3：打包APK
echo ============================================================
echo.
echo 开始打包APK（首次打包需要下载SDK/NDK，请耐心等待）...
echo.
wsl bash -c "cd /mnt/c/410 && buildozer android debug"
echo.
echo ============================================================
echo 步骤4：检查结果
echo ============================================================
echo.
if exist bin\*.apk (
    echo 打包成功！
    echo.
    echo APK文件：
    dir bin\*.apk
    echo.
    echo 您可以将APK文件传输到手机安装
) else (
    echo 打包失败，请查看错误信息
)
echo.
echo ============================================================
echo 完成
echo ============================================================
echo.
echo 详细说明请查看：KIVY_BUILD_GUIDE.md
echo.
pause
