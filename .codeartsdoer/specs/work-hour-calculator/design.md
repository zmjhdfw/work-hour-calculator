# 技术设计文档 - Python工时计算程序

## 文档信息
- **项目名称**: Python工时计算程序
- **版本**: 1.0
- **创建日期**: 2026-04-10
- **最后更新**: 2026-04-10

## 1. 设计概述

### 1.1 设计目标
- 实现一个简洁、易用的命令行工时管理工具
- 采用模块化设计，便于维护和扩展
- 使用纯Python标准库，无需第三方依赖
- 数据持久化采用JSON格式，便于阅读和迁移

### 1.2 技术栈
- **编程语言**: Python 3.8+
- **数据存储**: JSON文件
- **用户界面**: 命令行界面（CLI）
- **依赖**: 仅使用Python标准库

## 2. 系统架构

### 2.1 架构图
```
┌─────────────────────────────────────────────────┐
│              用户界面层 (CLI)                    │
│  ┌──────────────────────────────────────────┐  │
│  │         main.py (主程序入口)              │  │
│  └──────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│            业务逻辑层 (Business Logic)           │
│  ┌──────────────┐  ┌──────────────────────┐   │
│  │ work_calculator│  │  report_generator   │   │
│  │   (工时计算)   │  │    (报告生成)        │   │
│  └──────────────┘  └──────────────────────┘   │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│           数据访问层 (Data Access)               │
│  ┌──────────────────────────────────────────┐  │
│  │      data_manager (数据管理器)            │  │
│  └──────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│           数据存储层 (Data Storage)              │
│  ┌──────────────────────────────────────────┐  │
│  │         work_records.json                 │  │
│  └──────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

### 2.2 架构说明
系统采用分层架构设计：
- **用户界面层**：处理用户交互，显示菜单和接收输入
- **业务逻辑层**：实现工时计算、统计和报告生成等核心功能
- **数据访问层**：负责数据的读取、保存和管理
- **数据存储层**：使用JSON文件持久化存储数据

## 3. 模块设计

### 3.1 models.py (数据模型)
**职责**: 定义数据结构和实体类
**输入**: 无
**输出**: WorkRecord类、WorkStatistics类

**接口**:
```python
from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional

@dataclass
class WorkRecord:
    """工时记录数据类"""
    id: int                          # 记录ID
    date: date                       # 工作日期
    start_time: datetime             # 开始时间
    end_time: datetime               # 结束时间
    project: str                     # 项目名称
    description: str                 # 工作描述
    
    @property
    def duration_hours(self) -> float:
        """计算工时（小时）"""
        pass

@dataclass
class WorkStatistics:
    """工时统计数据类"""
    total_hours: float               # 总工时
    normal_hours: float              # 正常工时
    overtime_hours: float            # 加班工时
    work_days: int                   # 工作天数
    avg_hours_per_day: float         # 平均每日工时
```

### 3.2 data_manager.py (数据管理器)
**职责**: 负责数据的加载、保存和CRUD操作
**输入**: 文件路径、WorkRecord对象
**输出**: WorkRecord列表、操作结果

**接口**:
```python
class DataManager:
    """数据管理器"""
    
    def __init__(self, file_path: str = "work_records.json"):
        """初始化数据管理器"""
        pass
    
    def load_records(self) -> List[WorkRecord]:
        """加载所有工时记录"""
        pass
    
    def save_records(self, records: List[WorkRecord]) -> bool:
        """保存所有工时记录"""
        pass
    
    def add_record(self, record: WorkRecord) -> int:
        """添加工时记录，返回记录ID"""
        pass
    
    def get_record(self, record_id: int) -> Optional[WorkRecord]:
        """获取指定ID的工时记录"""
        pass
    
    def update_record(self, record: WorkRecord) -> bool:
        """更新工时记录"""
        pass
    
    def delete_record(self, record_id: int) -> bool:
        """删除工时记录"""
        pass
    
    def get_records_by_date(self, date: date) -> List[WorkRecord]:
        """获取指定日期的工时记录"""
        pass
    
    def get_records_by_range(self, start_date: date, end_date: date) -> List[WorkRecord]:
        """获取日期范围内的工时记录"""
        pass
    
    def get_records_by_project(self, project: str) -> List[WorkRecord]:
        """获取指定项目的工时记录"""
        pass
```

### 3.3 work_calculator.py (工时计算器)
**职责**: 执行工时计算和统计逻辑
**输入**: WorkRecord列表、日期范围
**输出**: WorkStatistics对象、计算结果

**接口**:
```python
class WorkCalculator:
    """工时计算器"""
    
    STANDARD_WORK_HOURS = 8.0  # 标准工作时间
    
    @staticmethod
    def calculate_single_day(records: List[WorkRecord], target_date: date) -> float:
        """计算单日工时"""
        pass
    
    @staticmethod
    def calculate_range(records: List[WorkRecord], start_date: date, end_date: date) -> WorkStatistics:
        """计算时间段工时统计"""
        pass
    
    @staticmethod
    def calculate_overtime(hours: float) -> tuple[float, float]:
        """计算加班工时，返回(正常工时, 加班工时)"""
        pass
    
    @staticmethod
    def calculate_by_project(records: List[WorkRecord]) -> dict[str, float]:
        """按项目统计工时"""
        pass
```

### 3.4 report_generator.py (报告生成器)
**职责**: 生成工时报告和导出数据
**输入**: WorkRecord列表、WorkStatistics对象
**输出**: 格式化报告文本、CSV文件

**接口**:
```python
class ReportGenerator:
    """报告生成器"""
    
    @staticmethod
    def generate_summary_report(records: List[WorkRecord], stats: WorkStatistics) -> str:
        """生成摘要报告"""
        pass
    
    @staticmethod
    def generate_project_report(project_stats: dict[str, float]) -> str:
        """生成项目统计报告"""
        pass
    
    @staticmethod
    def export_to_csv(records: List[WorkRecord], file_path: str) -> bool:
        """导出为CSV文件"""
        pass
```

### 3.5 cli.py (命令行界面)
**职责**: 处理用户交互和界面显示
**输入**: 用户输入
**输出**: 界面显示、功能调用

**接口**:
```python
class CLI:
    """命令行界面"""
    
    def __init__(self, data_manager: DataManager):
        """初始化CLI"""
        pass
    
    def run(self):
        """运行主循环"""
        pass
    
    def display_menu(self):
        """显示主菜单"""
        pass
    
    def add_record_ui(self):
        """添加记录界面"""
        pass
    
    def view_records_ui(self):
        """查看记录界面"""
        pass
    
    def edit_record_ui(self):
        """编辑记录界面"""
        pass
    
    def delete_record_ui(self):
        """删除记录界面"""
        pass
    
    def calculate_hours_ui(self):
        """计算工时界面"""
        pass
    
    def generate_report_ui(self):
        """生成报告界面"""
        pass
```

### 3.6 utils.py (工具函数)
**职责**: 提供通用工具函数
**输入**: 各种输入数据
**输出**: 验证结果、格式化数据

**接口**:
```python
def validate_date(date_str: str) -> Optional[date]:
    """验证并解析日期字符串"""
    pass

def validate_time(time_str: str) -> Optional[datetime]:
    """验证并解析时间字符串"""
    pass

def format_hours(hours: float) -> str:
    """格式化小时数显示"""
    pass

def format_datetime(dt: datetime) -> str:
    """格式化日期时间显示"""
    pass
```

## 4. 数据模型

### 4.1 实体关系图
```
┌─────────────────────┐
│    WorkRecord       │
├─────────────────────┤
│ id: int (PK)        │
│ date: date          │
│ start_time: datetime│
│ end_time: datetime  │
│ project: str        │
│ description: str    │
└─────────────────────┘
```

### 4.2 数据结构

#### WorkRecord (工时记录)
```python
{
    "id": 1,
    "date": "2026-04-10",
    "start_time": "2026-04-10T09:00:00",
    "end_time": "2026-04-10T17:30:00",
    "project": "项目A",
    "description": "开发功能模块"
}
```

#### JSON存储格式
```json
{
    "records": [
        {
            "id": 1,
            "date": "2026-04-10",
            "start_time": "2026-04-10T09:00:00",
            "end_time": "2026-04-10T17:30:00",
            "project": "项目A",
            "description": "开发功能模块"
        }
    ],
    "next_id": 2
}
```

## 5. API设计

### 5.1 内部API（模块间接口）

#### DataManager API
- **add_record(record: WorkRecord) -> int**: 添加记录，返回ID
- **get_record(record_id: int) -> Optional[WorkRecord]**: 获取记录
- **update_record(record: WorkRecord) -> bool**: 更新记录
- **delete_record(record_id: int) -> bool**: 删除记录
- **get_records_by_date(date: date) -> List[WorkRecord]**: 按日期查询
- **get_records_by_range(start: date, end: date) -> List[WorkRecord]**: 按范围查询

#### WorkCalculator API
- **calculate_single_day(records, date) -> float**: 计算单日工时
- **calculate_range(records, start, end) -> WorkStatistics**: 计算范围统计
- **calculate_overtime(hours) -> tuple**: 计算加班工时
- **calculate_by_project(records) -> dict**: 按项目统计

#### ReportGenerator API
- **generate_summary_report(records, stats) -> str**: 生成摘要报告
- **generate_project_report(project_stats) -> str**: 生成项目报告
- **export_to_csv(records, file_path) -> bool**: 导出CSV

## 6. 流程设计

### 6.1 添加工时记录流程
```
用户选择添加 → 输入日期 → 输入开始时间 → 输入结束时间
    ↓
验证时间有效性 → 输入项目名称 → 输入描述
    ↓
创建WorkRecord对象 → DataManager.add_record() → 显示成功消息
```

### 6.2 计算工时统计流程
```
用户选择计算 → 选择计算类型（单日/时间段/项目）
    ↓
输入日期参数 → DataManager查询记录
    ↓
WorkCalculator计算 → 生成WorkStatistics → 显示结果
```

### 6.3 生成报告流程
```
用户选择报告 → 输入时间范围 → DataManager查询记录
    ↓
WorkCalculator计算统计 → ReportGenerator生成报告
    ↓
显示报告 → 询问是否导出CSV
```

## 7. 异常处理

### 7.1 异常类型
```python
class WorkHourError(Exception):
    """工时计算基础异常"""
    pass

class InvalidTimeError(WorkHourError):
    """无效时间异常"""
    pass

class RecordNotFoundError(WorkHourError):
    """记录未找到异常"""
    pass

class DataFileError(WorkHourError):
    """数据文件异常"""
    pass
```

### 7.2 异常处理策略
- 输入验证失败：显示错误提示，要求重新输入
- 文件操作失败：显示错误信息，提供重试选项
- 记录不存在：显示提示，返回主菜单
- 时间逻辑错误：显示具体错误，要求修正

## 8. 配置管理

### 8.1 配置文件 (config.py)
```python
# 数据文件配置
DATA_FILE = "work_records.json"

# 工时计算配置
STANDARD_WORK_HOURS = 8.0
OVERTIME_MULTIPLIER = 1.5

# 界面配置
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"
DATETIME_FORMAT = "%Y-%m-%d %H:%M"

# 支持的语言
LANGUAGE = "zh_CN"
```

## 9. 测试策略

### 9.1 单元测试
- 测试WorkRecord的duration_hours计算
- 测试WorkCalculator的各项计算方法
- 测试DataManager的CRUD操作
- 测试输入验证函数

### 9.2 集成测试
- 测试完整的添加-查询-删除流程
- 测试数据持久化（保存后重新加载）
- 测试报告生成功能

### 9.3 测试文件结构
```
tests/
    test_models.py
    test_data_manager.py
    test_work_calculator.py
    test_report_generator.py
    test_utils.py
```

## 10. 项目结构

```
work_hour_calculator/
    ├── main.py              # 主程序入口
    ├── config.py            # 配置文件
    ├── models.py            # 数据模型
    ├── data_manager.py      # 数据管理器
    ├── work_calculator.py   # 工时计算器
    ├── report_generator.py  # 报告生成器
    ├── cli.py               # 命令行界面
    ├── utils.py             # 工具函数
    ├── exceptions.py        # 自定义异常
    └── tests/               # 测试目录
        ├── __init__.py
        ├── test_models.py
        ├── test_data_manager.py
        ├── test_work_calculator.py
        ├── test_report_generator.py
        └── test_utils.py
```
