"""
数据模型
定义核心数据结构
"""

from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Dict, Any, Optional


@dataclass
class WorkRecord:
    """工时记录数据类"""
    id: int
    date: date
    start_time: datetime
    end_time: datetime
    project: str
    description: str = ""
    
    @property
    def duration_hours(self) -> float:
        """计算工作时长（小时）"""
        delta = self.end_time - self.start_time
        return delta.total_seconds() / 3600
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式，用于JSON序列化"""
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'start_time': self.start_time.strftime('%H:%M'),
            'end_time': self.end_time.strftime('%H:%M'),
            'project': self.project,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'WorkRecord':
        """从字典创建WorkRecord实例"""
        record_date = date.fromisoformat(data['date'])
        
        # 解析时间字符串，需要结合日期
        start_time_str = data['start_time']
        end_time_str = data['end_time']
        
        start_time = datetime.strptime(
            f"{data['date']} {start_time_str}", 
            "%Y-%m-%d %H:%M"
        )
        end_time = datetime.strptime(
            f"{data['date']} {end_time_str}", 
            "%Y-%m-%d %H:%M"
        )
        
        return cls(
            id=data['id'],
            date=record_date,
            start_time=start_time,
            end_time=end_time,
            project=data['project'],
            description=data.get('description', '')
        )


@dataclass
class WorkStatistics:
    """工时统计数据类"""
    total_hours: float = 0.0
    normal_hours: float = 0.0
    overtime_hours: float = 0.0
    work_days: int = 0
    avg_hours_per_day: float = 0.0
    project_distribution: Dict[str, float] = field(default_factory=dict)
    
    def __str__(self) -> str:
        """格式化输出统计信息"""
        result = [
            f"总工时: {self.total_hours:.2f} 小时",
            f"正常工时: {self.normal_hours:.2f} 小时",
            f"加班工时: {self.overtime_hours:.2f} 小时",
            f"工作天数: {self.work_days} 天",
            f"日均工时: {self.avg_hours_per_day:.2f} 小时/天"
        ]
        
        if self.project_distribution:
            result.append("\n项目工时分布:")
            for project, hours in sorted(self.project_distribution.items(), 
                                         key=lambda x: x[1], reverse=True):
                percentage = (hours / self.total_hours * 100) if self.total_hours > 0 else 0
                result.append(f"  {project}: {hours:.2f} 小时 ({percentage:.1f}%)")
        
        return '\n'.join(result)
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            'total_hours': self.total_hours,
            'normal_hours': self.normal_hours,
            'overtime_hours': self.overtime_hours,
            'work_days': self.work_days,
            'avg_hours_per_day': self.avg_hours_per_day,
            'project_distribution': self.project_distribution
        }
