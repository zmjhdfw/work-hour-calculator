"""
自定义异常类
定义程序中使用的各种异常类型
"""


class WorkHourError(Exception):
    """工时计算程序基础异常类"""
    pass


class InvalidTimeError(WorkHourError):
    """无效时间异常"""
    def __init__(self, message="无效的时间格式或时间范围"):
        self.message = message
        super().__init__(self.message)


class RecordNotFoundError(WorkHourError):
    """记录未找到异常"""
    def __init__(self, record_id=None):
        if record_id:
            self.message = f"未找到ID为 {record_id} 的记录"
        else:
            self.message = "未找到指定记录"
        super().__init__(self.message)


class DataFileError(WorkHourError):
    """数据文件异常"""
    def __init__(self, message="数据文件操作失败"):
        self.message = message
        super().__init__(self.message)


class ValidationError(WorkHourError):
    """输入验证异常"""
    def __init__(self, message="输入验证失败"):
        self.message = message
        super().__init__(self.message)
