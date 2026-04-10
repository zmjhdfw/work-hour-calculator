"""
工具函数模块
提供输入验证、日期时间解析、格式化等功能
"""

from datetime import datetime, date
from typing import Callable, Optional, Any
from .config import DATE_FORMAT, TIME_FORMAT
from .exceptions import InvalidTimeError, ValidationError


def validate_date(date_str: str) -> date:
    """
    验证并解析日期字符串
    
    Args:
        date_str: 日期字符串，格式为 YYYY-MM-DD
        
    Returns:
        date对象
        
    Raises:
        ValidationError: 日期格式无效
    """
    try:
        return datetime.strptime(date_str, DATE_FORMAT).date()
    except ValueError:
        raise ValidationError(f"日期格式无效，请使用 {DATE_FORMAT} 格式，例如：2026-04-10")


def validate_time(time_str: str) -> datetime:
    """
    验证并解析时间字符串
    
    Args:
        time_str: 时间字符串，格式为 HH:MM
        
    Returns:
        datetime对象（日期为今天）
        
    Raises:
        ValidationError: 时间格式无效
    """
    try:
        return datetime.strptime(time_str, TIME_FORMAT)
    except ValueError:
        raise ValidationError(f"时间格式无效，请使用 {TIME_FORMAT} 格式，例如：09:00")


def validate_time_range(start_time: datetime, end_time: datetime) -> None:
    """
    验证时间范围的合理性
    
    Args:
        start_time: 开始时间
        end_time: 结束时间
        
    Raises:
        InvalidTimeError: 时间范围无效
    """
    if end_time <= start_time:
        raise InvalidTimeError("结束时间必须晚于开始时间")


def format_hours(hours: float) -> str:
    """
    格式化小时数显示
    
    Args:
        hours: 小时数
        
    Returns:
        格式化后的字符串，保留2位小数
    """
    return f"{hours:.2f}"


def format_datetime(dt: datetime) -> str:
    """
    格式化日期时间显示
    
    Args:
        dt: datetime对象
        
    Returns:
        格式化后的字符串
    """
    return dt.strftime("%Y-%m-%d %H:%M")


def format_date(d: date) -> str:
    """
    格式化日期显示
    
    Args:
        d: date对象
        
    Returns:
        格式化后的字符串
    """
    return d.strftime(DATE_FORMAT)


def get_valid_input(prompt: str, validator: Callable[[str], Any], 
                    error_msg: Optional[str] = None) -> Any:
    """
    获取有效输入的通用函数
    
    Args:
        prompt: 提示信息
        validator: 验证函数
        error_msg: 自定义错误消息
        
    Returns:
        验证通过后的值
    """
    while True:
        try:
            user_input = input(prompt)
            return validator(user_input)
        except (ValidationError, InvalidTimeError) as e:
            display_error(error_msg or str(e))
        except KeyboardInterrupt:
            print("\n操作已取消")
            raise


def display_error(msg: str) -> None:
    """
    显示错误消息
    
    Args:
        msg: 错误消息
    """
    print(f"\n❌ 错误: {msg}\n")


def display_success(msg: str) -> None:
    """
    显示成功消息
    
    Args:
        msg: 成功消息
    """
    print(f"\n✅ {msg}\n")


def display_info(msg: str) -> None:
    """
    显示信息消息
    
    Args:
        msg: 信息消息
    """
    print(f"\nℹ️  {msg}\n")


def confirm_action(msg: str) -> bool:
    """
    确认操作
    
    Args:
        msg: 确认消息
        
    Returns:
        True表示确认，False表示取消
    """
    while True:
        response = input(f"{msg} (y/n): ").strip().lower()
        if response in ['y', 'yes', '是']:
            return True
        elif response in ['n', 'no', '否']:
            return False
        else:
            display_error("请输入 y/n 进行确认")


def pause() -> None:
    """暂停等待用户按键"""
    input("\n按回车键继续...")


def clear_screen() -> None:
    """清空屏幕"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
