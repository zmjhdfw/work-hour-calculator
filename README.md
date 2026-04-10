# Python 工时计算程序

一个简单易用的工时记录和统计工具，提供命令行界面、Web界面和Windows可执行文件。

## 📥 快速获取

### 方式1：直接下载exe文件（推荐）

访问 [Releases](https://github.com/zmjhdfw/work-hour-calculator/releases) 页面下载最新的 `工时计算器.exe`，双击运行即可，无需安装Python。

### 方式2：克隆仓库

```bash
git clone https://github.com/zmjhdfw/work-hour-calculator.git
cd work-hour-calculator
```

### 方式3：下载ZIP

点击页面右上角的 "Code" → "Download ZIP"

## 功能特性

- ✅ 添加、查看、编辑、删除工时记录
- ✅ 按日期、日期范围、项目查询记录
- ✅ 计算工时统计（总工时、正常工时、加班工时）
- ✅ 生成统计报告（摘要报告、项目报告、详细报告）
- ✅ 导出数据为CSV格式
- ✅ 支持中文界面
- ✅ 提供Windows exe可执行文件
- ✅ 提供移动端友好的Web界面

## 项目结构

```
work_hour_calculator/
├── __init__.py          # 包初始化
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
    └── __init__.py
```

## 安装和运行

### 方式1：使用Windows可执行文件（推荐）

1. 从 [Releases](../../releases) 页面下载最新的 `工时计算器.exe`
2. 双击运行即可，无需安装Python

### 方式2：使用Python源码

#### 前置要求

- Python 3.7 或更高版本

#### 运行命令行版本

```bash
python run.py
```

或者：

```bash
python -m work_hour_calculator.main
```

#### 运行Web版本（移动端友好）

```bash
# 安装Flask
pip install flask

# 运行Web服务器
python web_app.py

# 访问 http://localhost:5000
```

## 使用说明

### 主菜单

程序启动后，会显示主菜单：

```
1. 添加工时记录
2. 查看工时记录
3. 编辑工时记录
4. 删除工时记录
5. 计算工时统计
6. 生成统计报告
7. 导出数据
0. 退出程序
```

### 添加工时记录

选择菜单项 1，按照提示输入：
- 日期（格式：YYYY-MM-DD，如 2026-04-10）
- 开始时间（格式：HH:MM，如 09:00）
- 结束时间（格式：HH:MM，如 17:30）
- 项目名称
- 工作描述（可选）

### 查看工时记录

选择菜单项 2，可以选择：
- 查看所有记录
- 按日期查看
- 按日期范围查看
- 按项目查看

### 计算工时统计

选择菜单项 5，可以计算：
- 按日期计算单日工时
- 按日期范围计算统计
- 按项目计算工时
- 计算所有记录统计

统计结果包括：
- 总工时
- 正常工时（8小时以内）
- 加班工时（超过8小时部分）
- 工作天数
- 日均工时
- 项目工时分布

### 生成统计报告

选择菜单项 6，可以生成：
- 摘要报告：包含统计概览和项目分布
- 项目统计报告：按项目统计工时
- 详细记录报告：列出所有记录详情

### 导出数据

选择菜单项 7，可以将数据导出为CSV格式：
- 导出所有记录
- 导出指定日期范围的记录

## 数据存储

工时记录保存在 `work_records.json` 文件中，采用JSON格式存储。

## 配置说明

可以在 `config.py` 中修改以下配置：

- `STANDARD_WORK_HOURS`: 标准工作日时长（默认8小时）
- `DATE_FORMAT`: 日期格式
- `TIME_FORMAT`: 时间格式
- `PAGE_SIZE`: 分页显示每页记录数
- `REPORT_WIDTH`: 报告宽度

## 示例

### 添加一条记录

```
请输入日期 (YYYY-MM-DD，默认今天): 2026-04-10
请输入开始时间 (HH:MM): 09:00
请输入结束时间 (HH:MM): 18:30
请输入项目名称: 项目A
请输入工作描述 (可选): 开发新功能

✅ 工时记录已添加，ID: 1
```

### 查看统计

```
总工时: 9.50 小时
正常工时: 8.00 小时
加班工时: 1.50 小时
工作天数: 1 天
日均工时: 9.50 小时/天

项目工时分布:
  项目A: 9.50 小时 (100.0%)
```

## 开发

### 运行测试

```bash
python -m pytest work_hour_calculator/tests/
```

### 代码结构

- **models.py**: 定义 `WorkRecord` 和 `WorkStatistics` 数据类
- **data_manager.py**: 负责数据的CRUD操作和持久化
- **work_calculator.py**: 提供工时计算和统计功能
- **report_generator.py**: 生成各种格式的报告
- **cli.py**: 提供命令行用户界面
- **utils.py**: 提供验证、格式化等工具函数

## 许可证

MIT License

## 作者

Work Hour Calculator Team
