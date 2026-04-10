"""
报告生成器
生成工时报告和数据导出功能
"""

import csv
from datetime import date
from typing import List, Dict, Optional
from .models import WorkRecord, WorkStatistics
from .config import REPORT_WIDTH


class ReportGenerator:
    """报告生成器类"""
    
    def __init__(self, width: int = REPORT_WIDTH):
        """
        初始化报告生成器
        
        Args:
            width: 报告宽度（字符数）
        """
        self.width = width
    
    def _format_header(self, title: str) -> str:
        """
        格式化报告标题
        
        Args:
            title: 标题文本
            
        Returns:
            格式化后的标题
        """
        separator = "=" * self.width
        centered_title = title.center(self.width)
        return f"\n{separator}\n{centered_title}\n{separator}\n"
    
    def _format_separator(self) -> str:
        """
        格式化分隔线
        
        Returns:
            分隔线字符串
        """
        return "-" * self.width
    
    def _format_statistics(self, stats: WorkStatistics) -> str:
        """
        格式化统计数据
        
        Args:
            stats: WorkStatistics对象
            
        Returns:
            格式化后的统计信息
        """
        lines = [
            f"总工时: {stats.total_hours:.2f} 小时",
            f"正常工时: {stats.normal_hours:.2f} 小时",
            f"加班工时: {stats.overtime_hours:.2f} 小时",
            f"工作天数: {stats.work_days} 天",
            f"日均工时: {stats.avg_hours_per_day:.2f} 小时/天"
        ]
        return '\n'.join(lines)
    
    def generate_summary_report(self, records: List[WorkRecord], 
                               stats: WorkStatistics,
                               title: str = "工时统计报告") -> str:
        """
        生成摘要报告
        
        Args:
            records: WorkRecord列表
            stats: WorkStatistics对象
            title: 报告标题
            
        Returns:
            格式化的报告文本
        """
        report_lines = []
        
        # 标题
        report_lines.append(self._format_header(title))
        
        # 统计信息
        report_lines.append("\n【统计概览】")
        report_lines.append(self._format_statistics(stats))
        
        # 项目分布
        if stats.project_distribution:
            report_lines.append("\n\n【项目工时分布】")
            report_lines.append(self._format_separator())
            
            total_hours = stats.total_hours
            for project, hours in sorted(stats.project_distribution.items(), 
                                        key=lambda x: x[1], reverse=True):
                percentage = (hours / total_hours * 100) if total_hours > 0 else 0
                bar_length = int(percentage / 100 * 30)
                bar = "#" * bar_length + "-" * (30 - bar_length)
                report_lines.append(
                    f"{project:20s} | {bar} | {hours:6.2f}h ({percentage:5.1f}%)"
                )
        
        report_lines.append("\n" + self._format_separator())
        
        return '\n'.join(report_lines)
    
    def generate_project_report(self, project_stats: Dict[str, float],
                               title: str = "项目工时统计") -> str:
        """
        生成项目统计报告
        
        Args:
            project_stats: 项目工时字典
            title: 报告标题
            
        Returns:
            格式化的报告文本
        """
        report_lines = []
        
        # 标题
        report_lines.append(self._format_header(title))
        
        if not project_stats:
            report_lines.append("暂无项目数据")
            return '\n'.join(report_lines)
        
        # 计算总工时
        total_hours = sum(project_stats.values())
        
        # 项目列表
        report_lines.append(f"\n{'项目名称':<20s} {'工时(h)':<10s} {'占比':<10s}")
        report_lines.append(self._format_separator())
        
        for project, hours in sorted(project_stats.items(), 
                                     key=lambda x: x[1], reverse=True):
            percentage = (hours / total_hours * 100) if total_hours > 0 else 0
            report_lines.append(f"{project:<20s} {hours:<10.2f} {percentage:<10.1f}%")
        
        report_lines.append(self._format_separator())
        report_lines.append(f"{'总计':<20s} {total_hours:<10.2f} {'100.0':<10s}%")
        
        return '\n'.join(report_lines)
    
    def generate_detailed_report(self, records: List[WorkRecord],
                                title: str = "工时详细记录") -> str:
        """
        生成详细记录报告
        
        Args:
            records: WorkRecord列表
            title: 报告标题
            
        Returns:
            格式化的报告文本
        """
        report_lines = []
        
        # 标题
        report_lines.append(self._format_header(title))
        
        if not records:
            report_lines.append("暂无记录")
            return '\n'.join(report_lines)
        
        # 表头
        report_lines.append(
            f"\n{'ID':<5s} {'日期':<12s} {'时间':<15s} {'工时':<8s} {'项目':<15s} {'描述':<20s}"
        )
        report_lines.append(self._format_separator())
        
        # 记录列表
        for record in sorted(records, key=lambda x: (x.date, x.start_time)):
            time_range = f"{record.start_time.strftime('%H:%M')}-{record.end_time.strftime('%H:%M')}"
            desc = record.description[:18] + "..." if len(record.description) > 18 else record.description
            
            report_lines.append(
                f"{record.id:<5d} {record.date.strftime('%Y-%m-%d'):<12s} "
                f"{time_range:<15s} {record.duration_hours:<8.2f} "
                f"{record.project:<15s} {desc:<20s}"
            )
        
        report_lines.append(self._format_separator())
        report_lines.append(f"共 {len(records)} 条记录")
        
        return '\n'.join(report_lines)
    
    def export_to_csv(self, records: List[WorkRecord], 
                     file_path: str,
                     start_date: Optional[date] = None,
                     end_date: Optional[date] = None) -> None:
        """
        导出为CSV文件
        
        Args:
            records: WorkRecord列表
            file_path: 导出文件路径
            start_date: 开始日期（可选）
            end_date: 结束日期（可选）
        """
        # 筛选日期范围
        if start_date and end_date:
            records = [r for r in records if start_date <= r.date <= end_date]
        
        try:
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
                fieldnames = ['ID', '日期', '开始时间', '结束时间', '工时(小时)', '项目', '描述']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for record in sorted(records, key=lambda x: (x.date, x.start_time)):
                    writer.writerow({
                        'ID': record.id,
                        '日期': record.date.strftime('%Y-%m-%d'),
                        '开始时间': record.start_time.strftime('%H:%M'),
                        '结束时间': record.end_time.strftime('%H:%M'),
                        '工时(小时)': f"{record.duration_hours:.2f}",
                        '项目': record.project,
                        '描述': record.description
                    })
        except IOError as e:
            raise Exception(f"导出CSV文件失败: {e}")
