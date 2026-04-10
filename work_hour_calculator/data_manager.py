"""
数据管理器
负责数据的持久化存储和CRUD操作
"""

import json
import os
from datetime import date
from typing import List, Optional
from .models import WorkRecord
from .config import DATA_FILE
from .exceptions import DataFileError, RecordNotFoundError


class DataManager:
    """数据管理器类"""
    
    def __init__(self, file_path: str = DATA_FILE):
        """
        初始化数据管理器
        
        Args:
            file_path: 数据文件路径
        """
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """确保数据文件存在"""
        if not os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump([], f, ensure_ascii=False, indent=2)
            except IOError as e:
                raise DataFileError(f"无法创建数据文件: {e}")
    
    def load_records(self) -> List[WorkRecord]:
        """
        从JSON文件加载所有记录
        
        Returns:
            WorkRecord列表
            
        Raises:
            DataFileError: 文件读取失败
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [WorkRecord.from_dict(item) for item in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            raise DataFileError(f"数据文件格式错误: {e}")
        except IOError as e:
            raise DataFileError(f"读取数据文件失败: {e}")
    
    def save_records(self, records: List[WorkRecord]) -> None:
        """
        保存所有记录到JSON文件
        
        Args:
            records: WorkRecord列表
            
        Raises:
            DataFileError: 文件写入失败
        """
        try:
            data = [record.to_dict() for record in records]
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            raise DataFileError(f"保存数据文件失败: {e}")
    
    def _get_next_id(self, records: List[WorkRecord]) -> int:
        """
        获取下一个可用ID
        
        Args:
            records: 现有记录列表
            
        Returns:
            新的ID
        """
        if not records:
            return 1
        return max(record.id for record in records) + 1
    
    def add_record(self, record: WorkRecord) -> int:
        """
        添加新记录
        
        Args:
            record: WorkRecord对象（id字段将被忽略）
            
        Returns:
            新记录的ID
            
        Raises:
            DataFileError: 保存失败
        """
        records = self.load_records()
        new_id = self._get_next_id(records)
        record.id = new_id
        records.append(record)
        self.save_records(records)
        return new_id
    
    def get_record(self, record_id: int) -> WorkRecord:
        """
        根据ID获取记录
        
        Args:
            record_id: 记录ID
            
        Returns:
            WorkRecord对象
            
        Raises:
            RecordNotFoundError: 记录不存在
        """
        records = self.load_records()
        for record in records:
            if record.id == record_id:
                return record
        raise RecordNotFoundError(record_id)
    
    def update_record(self, record: WorkRecord) -> None:
        """
        更新记录
        
        Args:
            record: WorkRecord对象
            
        Raises:
            RecordNotFoundError: 记录不存在
            DataFileError: 保存失败
        """
        records = self.load_records()
        found = False
        for i, r in enumerate(records):
            if r.id == record.id:
                records[i] = record
                found = True
                break
        
        if not found:
            raise RecordNotFoundError(record.id)
        
        self.save_records(records)
    
    def delete_record(self, record_id: int) -> None:
        """
        删除记录
        
        Args:
            record_id: 记录ID
            
        Raises:
            RecordNotFoundError: 记录不存在
            DataFileError: 保存失败
        """
        records = self.load_records()
        original_count = len(records)
        records = [r for r in records if r.id != record_id]
        
        if len(records) == original_count:
            raise RecordNotFoundError(record_id)
        
        self.save_records(records)
    
    def get_records_by_date(self, target_date: date) -> List[WorkRecord]:
        """
        查询指定日期的记录
        
        Args:
            target_date: 目标日期
            
        Returns:
            WorkRecord列表
        """
        records = self.load_records()
        return [r for r in records if r.date == target_date]
    
    def get_records_by_range(self, start_date: date, end_date: date) -> List[WorkRecord]:
        """
        查询日期范围内的记录
        
        Args:
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            WorkRecord列表
        """
        records = self.load_records()
        return [r for r in records if start_date <= r.date <= end_date]
    
    def get_records_by_project(self, project: str) -> List[WorkRecord]:
        """
        查询项目的记录
        
        Args:
            project: 项目名称
            
        Returns:
            WorkRecord列表
        """
        records = self.load_records()
        return [r for r in records if r.project == project]
    
    def get_all_projects(self) -> List[str]:
        """
        获取所有项目列表
        
        Returns:
            项目名称列表（去重）
        """
        records = self.load_records()
        projects = set(r.project for r in records)
        return sorted(list(projects))
    
    def get_all_records(self) -> List[WorkRecord]:
        """
        获取所有记录
        
        Returns:
            WorkRecord列表
        """
        return self.load_records()
