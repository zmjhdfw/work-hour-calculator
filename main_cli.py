"""
工时计算器 - 命令行版本
用于Windows EXE打包
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from work_hour_calculator.data_manager import DataManager
from work_hour_calculator.work_calculator import WorkCalculator
from work_hour_calculator.report_generator import ReportGenerator
from datetime import datetime, date

def main():
    """主函数"""
    print("=" * 50)
    print("        工时计算器")
    print("=" * 50)
    print()
    
    # 初始化
    data_manager = DataManager()
    calculator = WorkCalculator()
    report_gen = ReportGenerator()
    
    while True:
        print("\n1. 添加工时记录")
        print("2. 查看工时记录")
        print("3. 计算工时统计")
        print("4. 生成统计报告")
        print("5. 导出数据")
        print("0. 退出程序")
        print()
        
        try:
            choice = input("请选择操作 (0-5): ").strip()
            
            if choice == '0':
                print("\n感谢使用，再见！")
                break
            elif choice == '1':
                add_record(data_manager)
            elif choice == '2':
                view_records(data_manager)
            elif choice == '3':
                show_statistics(data_manager, calculator)
            elif choice == '4':
                generate_report(data_manager, report_gen)
            elif choice == '5':
                export_data(data_manager)
            else:
                print("\n无效选择，请重新输入")
        except KeyboardInterrupt:
            print("\n\n程序已退出")
            break
        except Exception as e:
            print(f"\n错误: {e}")

def add_record(data_manager):
    """添加记录"""
    print("\n--- 添加工时记录 ---")
    try:
        date_str = input("日期 (YYYY-MM-DD，默认今天): ").strip()
        if not date_str:
            date_str = date.today().strftime('%Y-%m-%d')
        
        start_time = input("开始时间 (HH:MM): ").strip()
        end_time = input("结束时间 (HH:MM): ").strip()
        project = input("项目名称: ").strip()
        description = input("工作描述 (可选): ").strip()
        
        # 创建记录
        record = data_manager.add_record(
            date_str, start_time, end_time, project, description
        )
        
        print(f"\n✅ 已添加！工时: {record.duration_hours:.2f}小时")
    except Exception as e:
        print(f"\n❌ 添加失败: {e}")

def view_records(data_manager):
    """查看记录"""
    print("\n--- 工时记录 ---")
    records = data_manager.get_all_records()
    
    if not records:
        print("暂无记录")
        return
    
    for i, record in enumerate(records, 1):
        print(f"\n{i}. {record.date} {record.start_time}-{record.end_time}")
        print(f"   项目: {record.project}")
        print(f"   工时: {record.duration_hours:.2f}小时")
        if record.description:
            print(f"   描述: {record.description}")

def show_statistics(data_manager, calculator):
    """显示统计"""
    print("\n--- 工时统计 ---")
    records = data_manager.get_all_records()
    
    if not records:
        print("暂无记录")
        return
    
    stats = calculator.calculate_statistics(records)
    
    print(f"\n总工时: {stats.total_hours:.2f}小时")
    print(f"正常工时: {stats.normal_hours:.2f}小时")
    print(f"加班工时: {stats.overtime_hours:.2f}小时")
    print(f"工作天数: {stats.work_days}天")
    print(f"日均工时: {stats.average_hours_per_day:.2f}小时/天")

def generate_report(data_manager, report_gen):
    """生成报告"""
    print("\n--- 统计报告 ---")
    records = data_manager.get_all_records()
    
    if not records:
        print("暂无记录")
        return
    
    report = report_gen.generate_summary_report(records)
    print("\n" + report)

def export_data(data_manager):
    """导出数据"""
    print("\n--- 导出数据 ---")
    try:
        filename = data_manager.export_to_csv()
        print(f"\n✅ 已导出到: {filename}")
    except Exception as e:
        print(f"\n❌ 导出失败: {e}")

if __name__ == '__main__':
    main()
