"""
工时计算器
提供工时计算和统计功能
"""

from datetime import date
from typing import List, Dict
from collections import defaultdict
from .models import WorkRecord, WorkStatistics
from .config import STANDARD_WORK_HOURS


class WorkCalculator:
    """工时计算器类"""
    
    def __init__(self, standard_hours: float = STANDARD_WORK_HOURS):
        """
        初始化工时计算器
        
        Args:
            standard_hours: 标准工作日时长（小时）
        """
        self.standard_hours = standard_hours
    
    def calculate_single_day(self, records: List[WorkRecord], target_date: date) -> float:
        """
        计算单日总工时
        
        Args:
            records: WorkRecord列表
            target_date: 目标日期
            
        Returns:
            总工时（小时）
        """
        total = 0.0
        for record in records:
            if record.date == target_date:
                total += record.duration_hours
        return total
    
    def calculate_total_hours(self, records: List[WorkRecord]) -> float:
        """
        计算记录列表总工时
        
        Args:
            records: WorkRecord列表
            
        Returns:
            总工时（小时）
        """
        return sum(record.duration_hours for record in records)
    
    def calculate_overtime(self, hours: float) -> tuple:
        """
        区分正常工时和加班工时
        
        Args:
            hours: 总工时
            
        Returns:
            (正常工时, 加班工时)
        """
        if hours <= self.standard_hours:
            return hours, 0.0
        else:
            return self.standard_hours, hours - self.standard_hours
    
    def calculate_range(self, records: List[WorkRecord], 
                       start_date: date, end_date: date) -> WorkStatistics:
        """
        计算时间段统计
        
        Args:
            records: WorkRecord列表
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            WorkStatistics对象
        """
        # 筛选日期范围内的记录
        filtered_records = [r for r in records 
                          if start_date <= r.date <= end_date]
        
        # 计算总工时
        total_hours = self.calculate_total_hours(filtered_records)
        
        # 计算工作天数
        work_days = len(set(r.date for r in filtered_records))
        
        # 计算日均工时
        avg_hours = total_hours / work_days if work_days > 0 else 0.0
        
        # 计算正常工时和加班工时
        normal_hours = 0.0
        overtime_hours = 0.0
        
        # 按日期分组计算
        daily_hours = defaultdict(float)
        for record in filtered_records:
            daily_hours[record.date] += record.duration_hours
        
        for daily_total in daily_hours.values():
            normal, overtime = self.calculate_overtime(daily_total)
            normal_hours += normal
            overtime_hours += overtime
        
        # 计算项目分布
        project_distribution = self.calculate_by_project(filtered_records)
        
        return WorkStatistics(
            total_hours=total_hours,
            normal_hours=normal_hours,
            overtime_hours=overtime_hours,
            work_days=work_days,
            avg_hours_per_day=avg_hours,
            project_distribution=project_distribution
        )
    
    def calculate_by_project(self, records: List[WorkRecord]) -> Dict[str, float]:
        """
        按项目统计工时
        
        Args:
            records: WorkRecord列表
            
        Returns:
            项目工时字典 {项目名: 工时}
        """
        project_hours = defaultdict(float)
        for record in records:
            project_hours[record.project] += record.duration_hours
        return dict(project_hours)
    
    def calculate_daily_average(self, records: List[WorkRecord]) -> float:
        """
        计算日均工时
        
        Args:
            records: WorkRecord列表
            
        Returns:
            日均工时
        """
        if not records:
            return 0.0
        
        total_hours = self.calculate_total_hours(records)
        work_days = self.get_work_days(records)
        
        return total_hours / work_days if work_days > 0 else 0.0
    
    def get_work_days(self, records: List[WorkRecord]) -> int:
        """
        获取实际工作天数
        
        Args:
            records: WorkRecord列表
            
        Returns:
            工作天数
        """
        unique_dates = set(r.date for r in records)
        return len(unique_dates)
    
    def get_project_distribution(self, records: List[WorkRecord]) -> Dict[str, float]:
        """
        获取项目工时占比
        
        Args:
            records: WorkRecord列表
            
        Returns:
            项目工时占比字典 {项目名: 占比百分比}
        """
        if not records:
            return {}
        
        total_hours = self.calculate_total_hours(records)
        project_hours = self.calculate_by_project(records)
        
        distribution = {}
        for project, hours in project_hours.items():
            percentage = (hours / total_hours * 100) if total_hours > 0 else 0
            distribution[project] = percentage
        
        return distribution
    
    def identify_overtime_days(self, records: List[WorkRecord]) -> List[tuple]:
        """
        识别加班日期
        
        Args:
            records: WorkRecord列表
            
        Returns:
            加班日期列表 [(日期, 工时)]
        """
        daily_hours = defaultdict(float)
        for record in records:
            daily_hours[record.date] += record.duration_hours
        
        overtime_days = []
        for work_date, hours in sorted(daily_hours.items()):
            if hours > self.standard_hours:
                overtime_days.append((work_date, hours))
        
        return overtime_days
