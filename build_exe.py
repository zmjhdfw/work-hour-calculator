"""
PyInstaller打包脚本
用于将工时计算程序打包成Windows exe可执行文件
"""

import os
import sys
import shutil

def clean_build():
    """清理构建目录"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"已清理: {dir_name}")
    
    # 清理.spec文件
    spec_file = 'work_hour_calculator.spec'
    if os.path.exists(spec_file):
        os.remove(spec_file)
        print(f"已清理: {spec_file}")

def build_exe():
    """构建exe文件"""
    print("\n" + "=" * 60)
    print("开始打包工时计算程序...")
    print("=" * 60)
    
    # 清理旧的构建文件
    print("\n[1/3] 清理旧的构建文件...")
    clean_build()
    
    # 执行PyInstaller打包
    print("\n[2/3] 执行PyInstaller打包...")
    cmd = (
        'pyinstaller --name="工时计算器" '
        '--onefile '
        '--console '
        '--clean '
        '--noconfirm '
        '--add-data "work_hour_calculator;work_hour_calculator" '
        'run.py'
    )
    
    result = os.system(cmd)
    
    if result == 0:
        print("\n[3/3] 打包成功！")
        print("\n" + "=" * 60)
        print("打包完成！")
        print("=" * 60)
        
        # 检查生成的文件
        exe_path = os.path.join('dist', '工时计算器.exe')
        if os.path.exists(exe_path):
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"\n可执行文件位置: {os.path.abspath(exe_path)}")
            print(f"文件大小: {size_mb:.2f} MB")
            print("\n使用方法:")
            print("  1. 双击运行 '工时计算器.exe'")
            print("  2. 或在命令行中运行: 工时计算器.exe")
        else:
            print("\n警告: 未找到生成的exe文件")
    else:
        print("\n错误: 打包失败")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()
