"""
命令行界面
提供用户交互界面和菜单系统
"""

from datetime import datetime, date, timedelta
from typing import Optional
from .data_manager import DataManager
from .work_calculator import WorkCalculator
from .report_generator import ReportGenerator
from .models import WorkRecord
from .utils import (
    validate_date, validate_time, validate_time_range,
    get_valid_input, display_error, display_success, display_info,
    confirm_action, pause, clear_screen, format_date
)
from .exceptions import WorkHourError


class CLI:
    """命令行界面类"""
    
    def __init__(self, data_manager: DataManager):
        """
        初始化CLI
        
        Args:
            data_manager: 数据管理器实例
        """
        self.data_manager = data_manager
        self.calculator = WorkCalculator()
        self.report_generator = ReportGenerator()
    
    def run(self) -> None:
        """主循环"""
        while True:
            try:
                self.display_menu()
                choice = self.get_menu_choice()
                
                if choice == 0:
                    print("\n感谢使用工时计算程序，再见！\n")
                    break
                elif choice == 1:
                    self.add_record_ui()
                elif choice == 2:
                    self.view_records_ui()
                elif choice == 3:
                    self.edit_record_ui()
                elif choice == 4:
                    self.delete_record_ui()
                elif choice == 5:
                    self.calculate_hours_ui()
                elif choice == 6:
                    self.generate_report_ui()
                elif choice == 7:
                    self.export_data_ui()
                
            except KeyboardInterrupt:
                print("\n\n操作已取消")
                if confirm_action("是否退出程序？"):
                    break
            except Exception as e:
                display_error(f"发生错误: {e}")
                pause()
    
    def display_menu(self) -> None:
        """显示主菜单"""
        clear_screen()
        print("=" * 60)
        print("               Python 工时计算程序 v1.0")
        print("=" * 60)
        print("\n【主菜单】\n")
        print("  1. 添加工时记录")
        print("  2. 查看工时记录")
        print("  3. 编辑工时记录")
        print("  4. 删除工时记录")
        print("  5. 计算工时统计")
        print("  6. 生成统计报告")
        print("  7. 导出数据")
        print("  0. 退出程序")
        print("\n" + "=" * 60)
    
    def get_menu_choice(self) -> int:
        """获取菜单选择"""
        while True:
            try:
                choice = input("\n请选择功能 (0-7): ").strip()
                choice_int = int(choice)
                if 0 <= choice_int <= 7:
                    return choice_int
                else:
                    display_error("请输入 0-7 之间的数字")
            except ValueError:
                display_error("请输入有效的数字")
    
    def add_record_ui(self) -> None:
        """添加记录界面"""
        print("\n" + "=" * 60)
        print("【添加工时记录】")
        print("=" * 60 + "\n")
        
        try:
            # 输入日期
            record_date = get_valid_input(
                "请输入日期 (YYYY-MM-DD，默认今天): ",
                lambda x: validate_date(x) if x else date.today()
            )
            
            # 输入开始时间
            start_time_str = input("请输入开始时间 (HH:MM): ").strip()
            start_time = validate_time(start_time_str)
            start_time = datetime.combine(record_date, start_time.time())
            
            # 输入结束时间
            end_time_str = input("请输入结束时间 (HH:MM): ").strip()
            end_time = validate_time(end_time_str)
            end_time = datetime.combine(record_date, end_time.time())
            
            # 验证时间范围
            validate_time_range(start_time, end_time)
            
            # 输入项目
            project = input("请输入项目名称: ").strip()
            if not project:
                display_error("项目名称不能为空")
                return
            
            # 输入描述
            description = input("请输入工作描述 (可选): ").strip()
            
            # 创建记录
            record = WorkRecord(
                id=0,  # ID将由DataManager分配
                date=record_date,
                start_time=start_time,
                end_time=end_time,
                project=project,
                description=description
            )
            
            # 保存记录
            record_id = self.data_manager.add_record(record)
            display_success(f"工时记录已添加，ID: {record_id}")
            
        except WorkHourError as e:
            display_error(str(e))
        except Exception as e:
            display_error(f"添加记录失败: {e}")
        
        pause()
    
    def view_records_ui(self) -> None:
        """查看记录界面"""
        print("\n" + "=" * 60)
        print("【查看工时记录】")
        print("=" * 60 + "\n")
        
        print("1. 查看所有记录")
        print("2. 按日期查看")
        print("3. 按日期范围查看")
        print("4. 按项目查看")
        
        try:
            choice = input("\n请选择查看方式 (1-4): ").strip()
            
            records = []
            if choice == '1':
                records = self.data_manager.get_all_records()
            elif choice == '2':
                target_date = get_valid_input(
                    "请输入日期 (YYYY-MM-DD): ",
                    validate_date
                )
                records = self.data_manager.get_records_by_date(target_date)
            elif choice == '3':
                start_date = get_valid_input(
                    "请输入开始日期 (YYYY-MM-DD): ",
                    validate_date
                )
                end_date = get_valid_input(
                    "请输入结束日期 (YYYY-MM-DD): ",
                    validate_date
                )
                records = self.data_manager.get_records_by_range(start_date, end_date)
            elif choice == '4':
                projects = self.data_manager.get_all_projects()
                if not projects:
                    display_info("暂无项目")
                    pause()
                    return
                
                print("\n现有项目:")
                for i, proj in enumerate(projects, 1):
                    print(f"  {i}. {proj}")
                
                project = input("\n请输入项目名称: ").strip()
                records = self.data_manager.get_records_by_project(project)
            else:
                display_error("无效的选择")
                pause()
                return
            
            # 显示记录
            if records:
                report = self.report_generator.generate_detailed_report(records)
                print("\n" + report)
            else:
                display_info("未找到符合条件的记录")
            
        except WorkHourError as e:
            display_error(str(e))
        
        pause()
    
    def edit_record_ui(self) -> None:
        """编辑记录界面"""
        print("\n" + "=" * 60)
        print("【编辑工时记录】")
        print("=" * 60 + "\n")
        
        try:
            # 输入记录ID
            record_id = int(input("请输入要编辑的记录ID: ").strip())
            
            # 获取记录
            record = self.data_manager.get_record(record_id)
            
            print(f"\n当前记录:")
            print(f"  日期: {format_date(record.date)}")
            print(f"  时间: {record.start_time.strftime('%H:%M')} - {record.end_time.strftime('%H:%M')}")
            print(f"  项目: {record.project}")
            print(f"  描述: {record.description}")
            print(f"  工时: {record.duration_hours:.2f} 小时")
            
            if not confirm_action("\n是否继续编辑？"):
                return
            
            # 输入新值（留空保持原值）
            print("\n请输入新值（直接回车保持原值）:\n")
            
            # 日期
            date_input = input(f"日期 [{format_date(record.date)}]: ").strip()
            if date_input:
                record.date = validate_date(date_input)
            
            # 开始时间
            start_input = input(f"开始时间 [{record.start_time.strftime('%H:%M')}]: ").strip()
            if start_input:
                start_time = validate_time(start_input)
                record.start_time = datetime.combine(record.date, start_time.time())
            
            # 结束时间
            end_input = input(f"结束时间 [{record.end_time.strftime('%H:%M')}]: ").strip()
            if end_input:
                end_time = validate_time(end_input)
                record.end_time = datetime.combine(record.date, end_time.time())
            
            # 验证时间范围
            validate_time_range(record.start_time, record.end_time)
            
            # 项目
            project_input = input(f"项目 [{record.project}]: ").strip()
            if project_input:
                record.project = project_input
            
            # 描述
            desc_input = input(f"描述 [{record.description}]: ").strip()
            if desc_input:
                record.description = desc_input
            
            # 更新记录
            self.data_manager.update_record(record)
            display_success("记录已更新")
            
        except ValueError:
            display_error("请输入有效的ID")
        except WorkHourError as e:
            display_error(str(e))
        except Exception as e:
            display_error(f"编辑记录失败: {e}")
        
        pause()
    
    def delete_record_ui(self) -> None:
        """删除记录界面"""
        print("\n" + "=" * 60)
        print("【删除工时记录】")
        print("=" * 60 + "\n")
        
        try:
            # 输入记录ID
            record_id = int(input("请输入要删除的记录ID: ").strip())
            
            # 获取记录
            record = self.data_manager.get_record(record_id)
            
            print(f"\n要删除的记录:")
            print(f"  日期: {format_date(record.date)}")
            print(f"  时间: {record.start_time.strftime('%H:%M')} - {record.end_time.strftime('%H:%M')}")
            print(f"  项目: {record.project}")
            print(f"  工时: {record.duration_hours:.2f} 小时")
            
            if confirm_action("\n确认删除此记录？"):
                self.data_manager.delete_record(record_id)
                display_success("记录已删除")
            else:
                display_info("已取消删除")
            
        except ValueError:
            display_error("请输入有效的ID")
        except WorkHourError as e:
            display_error(str(e))
        except Exception as e:
            display_error(f"删除记录失败: {e}")
        
        pause()
    
    def calculate_hours_ui(self) -> None:
        """计算工时界面"""
        print("\n" + "=" * 60)
        print("【计算工时统计】")
        print("=" * 60 + "\n")
        
        print("1. 按日期计算")
        print("2. 按日期范围计算")
        print("3. 按项目计算")
        print("4. 计算所有记录")
        
        try:
            choice = input("\n请选择计算方式 (1-4): ").strip()
            
            records = []
            stats = None
            
            if choice == '1':
                target_date = get_valid_input(
                    "请输入日期 (YYYY-MM-DD): ",
                    validate_date
                )
                records = self.data_manager.get_records_by_date(target_date)
                if records:
                    total = self.calculator.calculate_total_hours(records)
                    print(f"\n{format_date(target_date)} 的总工时: {total:.2f} 小时")
                else:
                    display_info("该日期无记录")
                    
            elif choice == '2':
                start_date = get_valid_input(
                    "请输入开始日期 (YYYY-MM-DD): ",
                    validate_date
                )
                end_date = get_valid_input(
                    "请输入结束日期 (YYYY-MM-DD): ",
                    validate_date
                )
                records = self.data_manager.get_records_by_range(start_date, end_date)
                if records:
                    stats = self.calculator.calculate_range(records, start_date, end_date)
                else:
                    display_info("该日期范围无记录")
                    
            elif choice == '3':
                projects = self.data_manager.get_all_projects()
                if not projects:
                    display_info("暂无项目")
                    pause()
                    return
                
                print("\n现有项目:")
                for i, proj in enumerate(projects, 1):
                    print(f"  {i}. {proj}")
                
                project = input("\n请输入项目名称: ").strip()
                records = self.data_manager.get_records_by_project(project)
                if records:
                    total = self.calculator.calculate_total_hours(records)
                    print(f"\n项目 '{project}' 的总工时: {total:.2f} 小时")
                else:
                    display_info("该项目无记录")
                    
            elif choice == '4':
                records = self.data_manager.get_all_records()
                if records:
                    min_date = min(r.date for r in records)
                    max_date = max(r.date for r in records)
                    stats = self.calculator.calculate_range(records, min_date, max_date)
                else:
                    display_info("暂无记录")
            else:
                display_error("无效的选择")
                pause()
                return
            
            # 显示统计结果
            if stats:
                print("\n" + str(stats))
            
        except WorkHourError as e:
            display_error(str(e))
        
        pause()
    
    def generate_report_ui(self) -> None:
        """生成报告界面"""
        print("\n" + "=" * 60)
        print("【生成统计报告】")
        print("=" * 60 + "\n")
        
        print("1. 生成摘要报告")
        print("2. 生成项目统计报告")
        print("3. 生成详细记录报告")
        
        try:
            choice = input("\n请选择报告类型 (1-3): ").strip()
            
            if choice == '1':
                start_date = get_valid_input(
                    "请输入开始日期 (YYYY-MM-DD): ",
                    validate_date
                )
                end_date = get_valid_input(
                    "请输入结束日期 (YYYY-MM-DD): ",
                    validate_date
                )
                records = self.data_manager.get_records_by_range(start_date, end_date)
                
                if records:
                    stats = self.calculator.calculate_range(records, start_date, end_date)
                    report = self.report_generator.generate_summary_report(records, stats)
                    print(report)
                else:
                    display_info("该日期范围无记录")
                    
            elif choice == '2':
                records = self.data_manager.get_all_records()
                if records:
                    project_stats = self.calculator.calculate_by_project(records)
                    report = self.report_generator.generate_project_report(project_stats)
                    print(report)
                else:
                    display_info("暂无记录")
                    
            elif choice == '3':
                records = self.data_manager.get_all_records()
                if records:
                    report = self.report_generator.generate_detailed_report(records)
                    print(report)
                else:
                    display_info("暂无记录")
            else:
                display_error("无效的选择")
                pause()
                return
            
        except WorkHourError as e:
            display_error(str(e))
        
        pause()
    
    def export_data_ui(self) -> None:
        """导出数据界面"""
        print("\n" + "=" * 60)
        print("【导出数据】")
        print("=" * 60 + "\n")
        
        print("1. 导出所有记录")
        print("2. 导出日期范围记录")
        
        try:
            choice = input("\n请选择导出方式 (1-2): ").strip()
            
            start_date = None
            end_date = None
            
            if choice == '1':
                records = self.data_manager.get_all_records()
            elif choice == '2':
                start_date = get_valid_input(
                    "请输入开始日期 (YYYY-MM-DD): ",
                    validate_date
                )
                end_date = get_valid_input(
                    "请输入结束日期 (YYYY-MM-DD): ",
                    validate_date
                )
                records = self.data_manager.get_records_by_range(start_date, end_date)
            else:
                display_error("无效的选择")
                pause()
                return
            
            if not records:
                display_info("无记录可导出")
                pause()
                return
            
            # 输入导出文件路径
            file_path = input("\n请输入导出文件路径 (例如: work_hours.csv): ").strip()
            if not file_path:
                file_path = "work_hours.csv"
            
            # 导出数据
            self.report_generator.export_to_csv(
                records, file_path, start_date, end_date
            )
            display_success(f"数据已导出到 {file_path}，共 {len(records)} 条记录")
            
        except WorkHourError as e:
            display_error(str(e))
        except Exception as e:
            display_error(f"导出失败: {e}")
        
        pause()
