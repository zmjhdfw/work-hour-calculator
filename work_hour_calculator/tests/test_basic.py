"""
基础功能测试
"""

import unittest
from datetime import datetime, date
from work_hour_calculator.models import WorkRecord, WorkStatistics
from work_hour_calculator.work_calculator import WorkCalculator
from work_hour_calculator.utils import validate_date, validate_time


class TestModels(unittest.TestCase):
    """测试数据模型"""
    
    def test_work_record_duration(self):
        """测试工时记录时长计算"""
        record = WorkRecord(
            id=1,
            date=date(2026, 4, 10),
            start_time=datetime(2026, 4, 10, 9, 0),
            end_time=datetime(2026, 4, 10, 17, 30),
            project="测试项目",
            description="测试描述"
        )
        self.assertEqual(record.duration_hours, 8.5)
    
    def test_work_record_to_dict(self):
        """测试WorkRecord序列化"""
        record = WorkRecord(
            id=1,
            date=date(2026, 4, 10),
            start_time=datetime(2026, 4, 10, 9, 0),
            end_time=datetime(2026, 4, 10, 17, 0),
            project="测试项目",
            description="测试描述"
        )
        data = record.to_dict()
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['date'], '2026-04-10')
        self.assertEqual(data['start_time'], '09:00')
        self.assertEqual(data['end_time'], '17:00')
        self.assertEqual(data['project'], '测试项目')
    
    def test_work_record_from_dict(self):
        """测试WorkRecord反序列化"""
        data = {
            'id': 1,
            'date': '2026-04-10',
            'start_time': '09:00',
            'end_time': '17:00',
            'project': '测试项目',
            'description': '测试描述'
        }
        record = WorkRecord.from_dict(data)
        self.assertEqual(record.id, 1)
        self.assertEqual(record.date, date(2026, 4, 10))
        self.assertEqual(record.duration_hours, 8.0)


class TestWorkCalculator(unittest.TestCase):
    """测试工时计算器"""
    
    def setUp(self):
        """设置测试数据"""
        self.calculator = WorkCalculator()
        self.records = [
            WorkRecord(
                id=1,
                date=date(2026, 4, 10),
                start_time=datetime(2026, 4, 10, 9, 0),
                end_time=datetime(2026, 4, 10, 12, 0),
                project="项目A",
                description=""
            ),
            WorkRecord(
                id=2,
                date=date(2026, 4, 10),
                start_time=datetime(2026, 4, 10, 13, 0),
                end_time=datetime(2026, 4, 10, 18, 0),
                project="项目B",
                description=""
            )
        ]
    
    def test_calculate_total_hours(self):
        """测试总工时计算"""
        total = self.calculator.calculate_total_hours(self.records)
        self.assertEqual(total, 8.0)
    
    def test_calculate_single_day(self):
        """测试单日工时计算"""
        total = self.calculator.calculate_single_day(
            self.records, date(2026, 4, 10)
        )
        self.assertEqual(total, 8.0)
    
    def test_calculate_overtime(self):
        """测试加班工时计算"""
        # 正常工时
        normal, overtime = self.calculator.calculate_overtime(7.5)
        self.assertEqual(normal, 7.5)
        self.assertEqual(overtime, 0.0)
        
        # 加班
        normal, overtime = self.calculator.calculate_overtime(9.5)
        self.assertEqual(normal, 8.0)
        self.assertEqual(overtime, 1.5)
    
    def test_calculate_by_project(self):
        """测试项目工时统计"""
        project_stats = self.calculator.calculate_by_project(self.records)
        self.assertEqual(project_stats['项目A'], 3.0)
        self.assertEqual(project_stats['项目B'], 5.0)


class TestUtils(unittest.TestCase):
    """测试工具函数"""
    
    def test_validate_date(self):
        """测试日期验证"""
        result = validate_date('2026-04-10')
        self.assertEqual(result, date(2026, 4, 10))
    
    def test_validate_time(self):
        """测试时间验证"""
        result = validate_time('09:30')
        self.assertEqual(result.hour, 9)
        self.assertEqual(result.minute, 30)


if __name__ == '__main__':
    unittest.main()
