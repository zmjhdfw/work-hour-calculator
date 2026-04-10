"""
主程序入口
Python工时计算程序
"""

import sys
from .data_manager import DataManager
from .cli import CLI
from .exceptions import WorkHourError


def main():
    """主函数"""
    try:
        # 创建数据管理器
        data_manager = DataManager()
        
        # 创建CLI界面
        cli = CLI(data_manager)
        
        # 运行主循环
        cli.run()
        
    except WorkHourError as e:
        print(f"\n程序错误: {e}\n")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n程序已终止\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n发生未知错误: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
