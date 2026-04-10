# 编码任务文档 - Python工时计算程序

## 文档信息
- **项目名称**: Python工时计算程序
- **版本**: 1.0
- **创建日期**: 2026-04-10
- **最后更新**: 2026-04-10

## 任务概述
本文档将技术设计转化为具体的编码任务，按照依赖关系和优先级进行组织。共包含8个主任务，涵盖项目初始化、核心模块开发、测试和文档编写。

---

## 任务 1: 项目初始化与基础结构搭建

### 任务描述
创建项目目录结构，初始化Python项目，配置开发环境，建立基础文件框架。

### 输入
- 技术设计文档中的项目结构定义

### 输出
- 完整的项目目录结构
- 配置文件和初始化文件
- 基础代码框架

### 验收标准
- Given: 项目目录不存在
- When: 执行项目初始化
- Then: 创建完整的目录结构，包含所有必需的Python文件和__init__.py

### 子任务

#### 1.1 创建项目目录结构
创建以下目录和文件：
```
work_hour_calculator/
    ├── __init__.py
    ├── main.py
    ├── config.py
    ├── models.py
    ├── data_manager.py
    ├── work_calculator.py
    ├── report_generator.py
    ├── cli.py
    ├── utils.py
    ├── exceptions.py
    └── tests/
        └── __init__.py
```

#### 1.2 创建配置文件
编写config.py，定义以下配置项：
- DATA_FILE: 数据文件路径
- STANDARD_WORK_HOURS: 标准工作时间（8小时）
- 日期时间格式常量
- 界面语言配置

#### 1.3 创建自定义异常类
编写exceptions.py，定义以下异常类：
- WorkHourError: 基础异常
- InvalidTimeError: 无效时间异常
- RecordNotFoundError: 记录未找到异常
- DataFileError: 数据文件异常

### 代码生成提示
```
创建Python项目基础结构，包含：
1. 主包目录work_hour_calculator
2. 配置文件config.py定义常量
3. 自定义异常类exceptions.py
4. 所有模块的初始化文件
```

---

## 任务 2: 数据模型实现

### 任务描述
实现WorkRecord和WorkStatistics数据类，定义核心数据结构。

### 输入
- 设计文档中的数据模型定义

### 输出
- models.py模块，包含完整的数据类定义

### 验收标准
- Given: 需要表示工时记录
- When: 创建WorkRecord实例
- Then: 能够正确计算duration_hours属性

### 子任务

#### 2.1 实现WorkRecord数据类
使用@dataclass装饰器创建WorkRecord类：
- 定义字段：id, date, start_time, end_time, project, description
- 实现duration_hours属性，计算工作时长
- 添加to_dict()和from_dict()方法用于JSON序列化

#### 2.2 实现WorkStatistics数据类
创建WorkStatistics类用于统计数据：
- 定义字段：total_hours, normal_hours, overtime_hours, work_days, avg_hours_per_day
- 添加格式化输出方法

### 代码生成提示
```
使用Python dataclass实现数据模型：
1. WorkRecord包含id, date, start_time, end_time, project, description
2. 实现duration_hours属性计算时间差
3. 实现JSON序列化方法to_dict和from_dict
4. WorkStatistics用于存储统计结果
```

---

## 任务 3: 工具函数模块实现

### 任务描述
实现输入验证、日期时间解析、格式化等工具函数。

### 输入
- 用户输入的日期时间字符串
- 需要格式化的数值

### 输出
- utils.py模块，提供验证和格式化功能

### 验收标准
- Given: 用户输入日期字符串"2026-04-10"
- When: 调用validate_date函数
- Then: 返回对应的date对象

### 子任务

#### 3.1 实现日期时间验证函数
编写以下验证函数：
- validate_date(date_str): 验证并解析日期字符串
- validate_time(time_str): 验证并解析时间字符串
- validate_time_range(start, end): 验证时间范围合理性

#### 3.2 实现格式化函数
编写以下格式化函数：
- format_hours(hours): 格式化小时数显示（保留2位小数）
- format_datetime(dt): 格式化日期时间显示
- format_date(d): 格式化日期显示

#### 3.3 实现输入辅助函数
编写以下辅助函数：
- get_valid_input(prompt, validator): 获取有效输入的通用函数
- display_error(msg): 显示错误消息
- confirm_action(msg): 确认操作

### 代码生成提示
```
实现工具函数模块：
1. 日期时间验证和解析（使用datetime.strptime）
2. 数值格式化输出
3. 输入验证循环
4. 错误提示和确认对话框
```

---

## 任务 4: 数据管理器实现

### 任务描述
实现DataManager类，负责数据的持久化存储和CRUD操作。

### 输入
- WorkRecord对象
- 查询条件（ID、日期、项目等）

### 输出
- data_manager.py模块，提供完整的数据管理功能

### 验收标准
- Given: 添加一条工时记录
- When: 调用add_record方法
- Then: 记录被保存到JSON文件，并返回有效ID

### 子任务

#### 4.1 实现数据加载和保存
编写DataManager基础方法：
- __init__(file_path): 初始化，设置文件路径
- load_records(): 从JSON文件加载所有记录
- save_records(records): 保存所有记录到JSON文件
- _ensure_file_exists(): 确保数据文件存在

#### 4.2 实现CRUD操作
编写数据操作方法：
- add_record(record): 添加新记录，返回ID
- get_record(record_id): 根据ID获取记录
- update_record(record): 更新记录
- delete_record(record_id): 删除记录

#### 4.3 实现查询功能
编写查询方法：
- get_records_by_date(date): 查询指定日期的记录
- get_records_by_range(start_date, end_date): 查询日期范围
- get_records_by_project(project): 查询项目记录
- get_all_projects(): 获取所有项目列表

### 代码生成提示
```
实现数据管理器类：
1. 使用json模块读写JSON文件
2. 维护记录列表和自增ID
3. 实现CRUD操作和多种查询方式
4. 处理文件不存在等异常情况
```

---

## 任务 5: 工时计算器实现

### 任务描述
实现WorkCalculator类，提供工时计算和统计功能。

### 输入
- WorkRecord列表
- 日期范围参数

### 输出
- work_calculator.py模块，提供计算和统计功能

### 验收标准
- Given: 某日有两条记录，分别为4小时和5小时
- When: 调用calculate_single_day
- Then: 返回9.0小时

### 子任务

#### 5.1 实现基础计算方法
编写计算方法：
- calculate_single_day(records, date): 计算单日总工时
- calculate_total_hours(records): 计算记录列表总工时
- calculate_overtime(hours): 区分正常工时和加班工时

#### 5.2 实现统计方法
编写统计方法：
- calculate_range(records, start_date, end_date): 计算时间段统计
- calculate_by_project(records): 按项目统计工时
- calculate_daily_average(records): 计算日均工时

#### 5.3 实现辅助统计功能
编写辅助方法：
- get_work_days(records): 获取实际工作天数
- get_project_distribution(records): 获取项目工时占比
- identify_overtime_days(records): 识别加班日期

### 代码生成提示
```
实现工时计算器类：
1. 定义STANDARD_WORK_HOURS常量（8小时）
2. 计算单日、时间段工时
3. 区分正常工时和加班工时
4. 按项目统计工时分布
5. 返回WorkStatistics对象
```

---

## 任务 6: 报告生成器实现

### 任务描述
实现ReportGenerator类，生成工时报告和数据导出功能。

### 输入
- WorkRecord列表
- WorkStatistics统计对象

### 输出
- report_generator.py模块，提供报告生成和导出功能

### 验收标准
- Given: 存在工时记录和统计数据
- When: 调用generate_summary_report
- Then: 返回格式化的报告文本

### 子任务

#### 6.1 实现报告生成方法
编写报告生成方法：
- generate_summary_report(records, stats): 生成摘要报告
- generate_project_report(project_stats): 生成项目统计报告
- generate_detailed_report(records): 生成详细记录报告

#### 6.2 实现数据导出功能
编写导出方法：
- export_to_csv(records, file_path): 导出为CSV文件
- format_csv_row(record): 格式化CSV行

#### 6.3 实现报告格式化
编写格式化辅助方法：
- _format_header(title): 格式化报告标题
- _format_separator(): 格式化分隔线
- _format_statistics(stats): 格式化统计数据

### 代码生成提示
```
实现报告生成器类：
1. 生成文本格式的摘要报告
2. 生成项目工时分布报告
3. 使用csv模块导出CSV文件
4. 格式化输出，包含标题、分隔线、对齐
```

---

## 任务 7: 命令行界面实现

### 任务描述
实现CLI类，提供用户交互界面和菜单系统。

### 输入
- 用户键盘输入

### 输出
- cli.py模块，提供完整的命令行交互功能

### 验收标准
- Given: 程序启动
- When: 显示主菜单
- Then: 显示所有功能选项并等待用户选择

### 子任务

#### 7.1 实现主菜单和主循环
编写主界面方法：
- run(): 主循环
- display_menu(): 显示主菜单
- get_menu_choice(): 获取菜单选择

#### 7.2 实现工时记录管理界面
编写记录管理界面：
- add_record_ui(): 添加记录界面
- view_records_ui(): 查看记录界面
- edit_record_ui(): 编辑记录界面
- delete_record_ui(): 删除记录界面

#### 7.3 实现计算和报告界面
编写计算报告界面：
- calculate_hours_ui(): 计算工时界面
- generate_report_ui(): 生成报告界面
- export_data_ui(): 导出数据界面

#### 7.4 实现界面辅助功能
编写辅助方法：
- display_records_table(records): 表格形式显示记录
- display_statistics(stats): 显示统计数据
- pause(): 暂停等待用户按键

### 代码生成提示
```
实现命令行界面类：
1. 主菜单循环，支持中文显示
2. 各功能的交互界面
3. 输入验证和错误提示
4. 表格化显示记录列表
5. 调用DataManager、WorkCalculator、ReportGenerator
```

---

## 任务 8: 主程序集成与测试

### 任务描述
编写主程序入口，集成所有模块，编写单元测试。

### 输入
- 所有已实现的模块

### 输出
- main.py主程序
- tests/目录下的测试文件

### 验收标准
- Given: 运行python main.py
- When: 程序启动
- Then: 显示主菜单并能正常执行所有功能

### 子任务

#### 8.1 实现主程序入口
编写main.py：
- 导入所有模块
- 创建DataManager、CLI实例
- 启动主循环
- 添加异常处理和优雅退出

#### 8.2 编写单元测试
编写测试文件：
- test_models.py: 测试数据模型
- test_data_manager.py: 测试数据管理器
- test_work_calculator.py: 测试工时计算器
- test_report_generator.py: 测试报告生成器
- test_utils.py: 测试工具函数

#### 8.3 集成测试和调试
执行集成测试：
- 测试完整工作流程
- 修复发现的bug
- 优化用户体验
- 添加必要的错误处理

### 代码生成提示
```
实现主程序和测试：
1. main.py作为程序入口
2. 使用unittest编写单元测试
3. 测试所有核心功能
4. 处理异常和边界情况
```

---

## 任务依赖关系

```
任务1 (项目初始化)
  ↓
任务2 (数据模型) + 任务3 (工具函数)
  ↓
任务4 (数据管理器)
  ↓
任务5 (工时计算器) + 任务6 (报告生成器)
  ↓
任务7 (命令行界面)
  ↓
任务8 (主程序集成与测试)
```

## 任务优先级说明

- **高优先级**: 任务1、2、3、4、5、7、8（核心功能）
- **中优先级**: 任务6（报告生成）
- **低优先级**: 无

## 预计工作量

- 任务1: 0.5小时
- 任务2: 1小时
- 任务3: 1小时
- 任务4: 2小时
- 任务5: 1.5小时
- 任务6: 1小时
- 任务7: 2小时
- 任务8: 2小时

**总计**: 约11小时

## 执行建议

1. 按照依赖关系顺序执行任务
2. 每完成一个模块立即编写对应的单元测试
3. 优先实现核心功能（数据管理和计算）
4. 及时进行集成测试，确保模块间协作正常
5. 注意异常处理和边界情况的测试
