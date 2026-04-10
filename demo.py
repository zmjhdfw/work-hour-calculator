"""
快速演示脚本
展示工时计算程序的核心功能
"""

from datetime import datetime, date, timedelta
from work_hour_calculator.models import WorkRecord
from work_hour_calculator.data_manager import DataManager
from work_hour_calculator.work_calculator import WorkCalculator
from work_hour_calculator.report_generator import ReportGenerator


def main():
    print("=" * 60)
    print("Python 工时计算程序 - 功能演示")
    print("=" * 60)
    
    # 创建数据管理器（使用演示数据文件）
    dm = DataManager("demo_data.json")
    calculator = WorkCalculator()
    report_gen = ReportGenerator()
    
    # 添加一些示例记录
    print("\n【1. 添加工时记录】")
    today = date.today()
    
    records_data = [
        (today, "09:00", "12:00", "项目A", "开发新功能"),
        (today, "13:00", "18:30", "项目A", "代码审查"),
        (today - timedelta(days=1), "09:00", "17:00", "项目B", "文档编写"),
        (today - timedelta(days=2), "09:00", "20:00", "项目A", "紧急修复"),
    ]
    
    for record_date, start, end, project, desc in records_data:
        start_time = datetime.strptime(f"{record_date} {start}", "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(f"{record_date} {end}", "%Y-%m-%d %H:%M")
        
        record = WorkRecord(
            id=0,
            date=record_date,
            start_time=start_time,
            end_time=end_time,
            project=project,
            description=desc
        )
        
        record_id = dm.add_record(record)
        print(f"  [OK] 添加记录 ID={record_id}: {record_date} {start}-{end} ({project})")
    
    # 查看所有记录
    print("\n【2. 查看所有记录】")
    all_records = dm.get_all_records()
    for record in all_records:
        print(f"  ID={record.id}: {record.date} "
              f"{record.start_time.strftime('%H:%M')}-{record.end_time.strftime('%H:%M')} "
              f"{record.duration_hours:.2f}h - {record.project}")
    
    # 计算统计
    print("\n【3. 计算工时统计】")
    start_date = today - timedelta(days=7)
    end_date = today
    stats = calculator.calculate_range(all_records, start_date, end_date)
    
    print(f"  总工时: {stats.total_hours:.2f} 小时")
    print(f"  正常工时: {stats.normal_hours:.2f} 小时")
    print(f"  加班工时: {stats.overtime_hours:.2f} 小时")
    print(f"  工作天数: {stats.work_days} 天")
    print(f"  日均工时: {stats.avg_hours_per_day:.2f} 小时/天")
    
    # 项目统计
    print("\n【4. 项目工时分布】")
    project_stats = calculator.calculate_by_project(all_records)
    for project, hours in sorted(project_stats.items(), key=lambda x: x[1], reverse=True):
        percentage = (hours / stats.total_hours * 100) if stats.total_hours > 0 else 0
        print(f"  {project}: {hours:.2f} 小时 ({percentage:.1f}%)")
    
    # 生成报告
    print("\n【5. 生成统计报告】")
    report = report_gen.generate_summary_report(all_records, stats, "工时统计报告")
    print(report)
    
    # 导出CSV
    print("\n【6. 导出数据】")
    csv_file = "demo_export.csv"
    report_gen.export_to_csv(all_records, csv_file)
    print(f"  [OK] 数据已导出到 {csv_file}")
    
    # 清理演示数据
    import os
    print("\n【清理演示数据】")
    for file in ["demo_data.json", "demo_export.csv"]:
        if os.path.exists(file):
            os.remove(file)
            print(f"  [OK] 已删除 {file}")
    
    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)
    print("\n要运行完整程序，请执行: python run.py")


if __name__ == "__main__":
    main()
