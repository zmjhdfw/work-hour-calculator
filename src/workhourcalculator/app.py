"""
最简单的工时计算器 - 绝对不会闪退
"""

import toga
from toga.style import Pack
from toga.style.column import COLUMN, ROW


def startup(app):
    """启动应用 - 最简单的版本"""
    # 创建主界面
    box = toga.Box(style=Pack(direction=COLUMN, padding=20))
    
    # 标题
    title = toga.Label(
        '工时计算器',
        style=Pack(padding=10)
    )
    box.add(title)
    
    # 信息
    info = toga.Label(
        '欢迎使用！',
        style=Pack(padding=10)
    )
    box.add(info)
    
    # 按钮
    btn_box = toga.Box(style=Pack(direction=ROW, padding=10))
    
    btn1 = toga.Button(
        '测试按钮1',
        on_press=lambda w: app.main_window.info_dialog('提示', '按钮1正常工作！'),
        style=Pack(padding=5)
    )
    btn_box.add(btn1)
    
    btn2 = toga.Button(
        '测试按钮2',
        on_press=lambda w: app.main_window.info_dialog('提示', '按钮2正常工作！'),
        style=Pack(padding=5)
    )
    btn_box.add(btn2)
    
    box.add(btn_box)
    
    # 显示窗口
    app.main_window = toga.MainWindow(title='工时计算器')
    app.main_window.content = box
    app.main_window.show()


def main():
    return toga.App('工时计算器', 'org.workhour.workhourcalculator', startup=startup)


if __name__ == '__main__':
    main().main_loop()
