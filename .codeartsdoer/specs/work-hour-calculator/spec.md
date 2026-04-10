# 需求规格文档 - Python工时计算程序

## 文档信息
- **项目名称**: Python工时计算程序
- **版本**: 1.0
- **创建日期**: 2026-04-10
- **最后更新**: 2026-04-10

## 1. 概述

### 1.1 项目背景
开发一个Python程序，用于计算和管理工作时间。该程序将帮助用户记录工作时间、计算总工时、支持不同计费模式，并生成工时报告。

### 1.2 系统范围
- 工时记录的输入和管理
- 工时计算（包括加班、节假日等特殊情况）
- 工时统计和报告生成
- 数据持久化存储
- 基本的命令行交互界面

### 1.3 排除范围
- 图形用户界面（GUI）
- 多用户权限管理
- 网络远程访问功能
- 与外部考勤系统集成

## 2. 功能需求

### 2.1 工时记录管理

#### 需求ID: REQ-001
**描述**: 添加工时记录
**优先级**: 高
**EARS格式**: When the user inputs work time entry data the system shall create a new work time record with the provided information

**验收标准**:
- Given: 用户启动程序并选择添加工时功能
- When: 用户输入日期、开始时间、结束时间、项目名称和描述
- Then: 系统创建一条新的工时记录并显示成功消息

#### 需求ID: REQ-002
**描述**: 查看工时记录
**优先级**: 高
**EARS格式**: When the user requests to view work records the system shall display all stored work time records in chronological order

**验收标准**:
- Given: 系统中存在工时记录
- When: 用户选择查看所有记录功能
- Then: 系统按时间顺序显示所有工时记录，包括日期、时间、项目和描述

#### 需求ID: REQ-003
**描述**: 删除工时记录
**优先级**: 中
**EARS格式**: When the user selects a specific work record for deletion the system shall remove that record from storage

**验收标准**:
- Given: 系统中存在工时记录
- When: 用户选择要删除的记录ID并确认删除
- Then: 系统删除该记录并显示删除成功消息

#### 需求ID: REQ-004
**描述**: 修改工时记录
**优先级**: 中
**EARS格式**: When the user selects a work record for editing the system shall allow modification of all record fields

**验收标准**:
- Given: 系统中存在工时记录
- When: 用户选择要修改的记录并更新字段内容
- Then: 系统保存修改后的记录并显示更新成功消息

### 2.2 工时计算

#### 需求ID: REQ-005
**描述**: 计算单日工时
**优先级**: 高
**EARS格式**: The system shall calculate the total work hours for a single day by summing all work entries for that day

**验收标准**:
- Given: 某日期存在多条工时记录
- When: 用户查询该日期的总工时
- Then: 系统计算并显示该日期的总工作小时数

#### 需求ID: REQ-006
**描述**: 计算时间段工时
**优先级**: 高
**EARS格式**: When the user specifies a date range the system shall calculate total work hours within that range

**验收标准**:
- Given: 用户输入开始日期和结束日期
- When: 系统执行时间段工时计算
- Then: 系统显示该时间段内的总工时、工作天数和平均每日工时

#### 需求ID: REQ-007
**描述**: 识别加班工时
**优先级**: 中
**EARS格式**: Where daily work hours exceed the standard work hours the system shall identify and mark overtime hours

**验收标准**:
- Given: 标准工作时间为8小时
- When: 某日工时超过8小时
- Then: 系统区分正常工时和加班工时，并分别显示

#### 需求ID: REQ-008
**描述**: 项目工时统计
**优先级**: 高
**EARS格式**: When the user requests project statistics the system shall aggregate work hours by project name

**验收标准**:
- Given: 系统中存在多个项目的工时记录
- When: 用户选择按项目统计功能
- Then: 系统显示每个项目的总工时和占比

### 2.3 数据持久化

#### 需求ID: REQ-009
**描述**: 保存工时数据
**优先级**: 高
**EARS格式**: The system shall persist all work time records to a local file storage

**验收标准**:
- Given: 用户添加或修改工时记录
- When: 操作完成
- Then: 系统自动将数据保存到本地文件

#### 需求ID: REQ-010
**描述**: 加载历史数据
**优先级**: 高
**EARS格式**: When the system starts the system shall load all previously saved work time records

**验收标准**:
- Given: 存在历史保存的工时数据文件
- When: 程序启动
- Then: 系统自动加载所有历史记录到内存

### 2.4 报告生成

#### 需求ID: REQ-011
**描述**: 生成工时报告
**优先级**: 中
**EARS格式**: When the user requests a report the system shall generate a formatted summary of work hours

**验收标准**:
- Given: 系统中存在工时记录
- When: 用户选择生成报告功能并指定时间范围
- Then: 系统生成包含总工时、项目分布、加班情况的格式化报告

#### 需求ID: REQ-012
**描述**: 导出数据
**优先级**: 低
**EARS格式**: When the user requests data export the system shall export work records in CSV format

**验收标准**:
- Given: 系统中存在工时记录
- When: 用户选择导出功能
- Then: 系统生成CSV文件包含所有工时记录

### 2.5 用户界面

#### 需求ID: REQ-013
**描述**: 命令行菜单
**优先级**: 高
**EARS格式**: The system shall display a command-line menu with all available operations

**验收标准**:
- Given: 程序启动
- When: 显示主菜单
- Then: 系统显示所有功能选项供用户选择

#### 需求ID: REQ-014
**描述**: 输入验证
**优先级**: 高
**EARS格式**: When the user enters invalid data the system shall reject the input and display an error message

**验收标准**:
- Given: 用户输入数据
- When: 输入不符合格式要求（如无效日期、结束时间早于开始时间）
- Then: 系统拒绝输入并显示明确的错误提示

## 3. 非功能需求

### 3.1 性能需求
- 系统应能在1秒内完成单次工时计算
- 支持1000条以上的工时记录存储
- 数据加载时间不超过2秒

### 3.2 可用性需求
- 提供清晰的操作提示和错误信息
- 支持中文界面
- 操作流程简单直观

### 3.3 可维护性需求
- 代码遵循PEP 8规范
- 模块化设计，便于扩展
- 提供完整的代码注释

## 4. 约束条件
- 使用Python 3.8或更高版本
- 仅使用Python标准库，不依赖第三方包
- 数据存储使用JSON文件格式
- 运行环境为命令行终端

## 5. 假设与依赖
- 用户具备基本的命令行操作能力
- 系统运行环境有文件读写权限
- 用户输入的时间采用24小时制

## 6. 术语表
- **工时记录**: 一条包含日期、开始时间、结束时间、项目名称和描述的工作时间记录
- **标准工时**: 每天8小时的工作时间
- **加班工时**: 超过标准工时的工作时间
- **项目**: 工作任务的分类标识
