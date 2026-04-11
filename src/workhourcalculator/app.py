"""
BeeWare版本的工时计算应用
使用Toga框架构建跨平台UI
"""

import toga
from toga.style import Pack
from toga.style.column import COLUMN, ROW
from datetime import datetime, date
import json
import os


class WorkHourApp(toga.App):
    """工时计算应用"""
    
    def startup(self):
        """启动应用"""
        try:
            # 数据文件 - 使用更安全的路径
            try:
                data_dir = self.paths.data
            except:
                data_dir = os.path.expanduser('~')
            
            self.data_file = os.path.join(data_dir, 'work_records.json')
            self.records = []
            self.load_records()
            
            # 主容器
            main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
            
            # 标题
            title_label = toga.Label(
                '工时计算器',
                style=Pack(padding=10, font_size=20)
            )
            main_box.add(title_label)
            
            # 信息显示
            self.info_label = toga.Label(
                f'欢迎使用工时计算器！\n当前记录: {len(self.records)}条',
                style=Pack(padding=10)
            )
            main_box.add(self.info_label)
            
            # 按钮容器
            button_box1 = toga.Box(style=Pack(direction=ROW, padding=5))
            
            add_button = toga.Button(
                '添加记录',
                on_press=self.show_add,
                style=Pack(flex=1, padding=5)
            )
            button_box1.add(add_button)
            
            view_button = toga.Button(
                '查看记录',
                on_press=self.show_records,
                style=Pack(flex=1, padding=5)
            )
            button_box1.add(view_button)
            
            main_box.add(button_box1)
            
            button_box2 = toga.Box(style=Pack(direction=ROW, padding=5))
            
            stats_button = toga.Button(
                '统计分析',
                on_press=self.show_stats,
                style=Pack(flex=1, padding=5)
            )
            button_box2.add(stats_button)
            
            clear_button = toga.Button(
                '清空数据',
                on_press=self.clear_data,
                style=Pack(flex=1, padding=5)
            )
            button_box2.add(clear_button)
            
            main_box.add(button_box2)
            
            # 创建主窗口
            self.main_window = toga.MainWindow(title=self.formal_name)
            self.main_window.content = main_box
            self.main_window.show()
            
        except Exception as e:
            # 如果出错，显示简单界面
            error_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
            error_label = toga.Label(
                f'启动出错: {str(e)}',
                style=Pack(padding=10)
            )
            error_box.add(error_label)
            
            self.main_window = toga.MainWindow(title=self.formal_name)
            self.main_window.content = error_box
            self.main_window.show()
    
    def load_records(self):
        """加载记录"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.records = json.load(f)
        except:
            self.records = []
    
    def save_records(self):
        """保存记录"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.records, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.main_window.info_dialog('错误', f'保存失败: {e}')
    
    def show_add(self, widget):
        """添加记录"""
        try:
            # 创建输入框
            date_input = toga.TextInput(
                value=date.today().strftime('%Y-%m-%d'),
                placeholder='YYYY-MM-DD',
                style=Pack(padding=5)
            )
            
            start_input = toga.TextInput(
                value='09:00',
                placeholder='HH:MM',
                style=Pack(padding=5)
            )
            
            end_input = toga.TextInput(
                value='17:00',
                placeholder='HH:MM',
                style=Pack(padding=5)
            )
            
            project_input = toga.TextInput(
                placeholder='项目名称',
                style=Pack(padding=5)
            )
            
            # 创建布局
            box = toga.Box(style=Pack(direction=COLUMN, padding=10))
            
            box.add(toga.Label('日期:', style=Pack(padding=5)))
            box.add(date_input)
            
            box.add(toga.Label('开始时间:', style=Pack(padding=5)))
            box.add(start_input)
            
            box.add(toga.Label('结束时间:', style=Pack(padding=5)))
            box.add(end_input)
            
            box.add(toga.Label('项目:', style=Pack(padding=5)))
            box.add(project_input)
            
            def add_record(widget):
                try:
                    d = datetime.strptime(date_input.value, '%Y-%m-%d').date()
                    s = datetime.strptime(f"{date_input.value} {start_input.value}", '%Y-%m-%d %H:%M')
                    e = datetime.strptime(f"{date_input.value} {end_input.value}", '%Y-%m-%d %H:%M')
                    
                    hours = (e - s).total_seconds() / 3600
                    
                    record = {
                        'date': date_input.value,
                        'start': start_input.value,
                        'end': end_input.value,
                        'hours': hours,
                        'project': project_input.value
                    }
                    
                    self.records.append(record)
                    self.save_records()
                    
                    self.info_label.text = f'已添加记录: {project_input.value} - {hours:.2f}h\n当前记录: {len(self.records)}条'
                    self.main_window.info_dialog('成功', f'已添加！工时: {hours:.2f}小时')
                except Exception as ex:
                    self.main_window.info_dialog('错误', str(ex))
            
            # 添加按钮
            add_button = toga.Button('添加', on_press=add_record, style=Pack(padding=10))
            box.add(add_button)
            
            # 显示对话框
            self.main_window.info_dialog('添加记录', box)
        except Exception as e:
            self.main_window.info_dialog('错误', f'打开添加界面失败: {e}')
    
    def show_records(self, widget):
        """查看记录"""
        try:
            if not self.records:
                self.main_window.info_dialog('提示', '暂无记录')
                return
            
            text = "工时记录:\n\n"
            for r in self.records[-10:]:  # 只显示最近10条
                text += f"{r['date']} {r['start']}-{r['end']}\n"
                text += f"{r['hours']:.2f}h - {r['project']}\n\n"
            
            if len(self.records) > 10:
                text += f"...还有{len(self.records)-10}条记录"
            
            self.main_window.info_dialog('工时记录', text)
        except Exception as e:
            self.main_window.info_dialog('错误', str(e))
    
    def show_stats(self, widget):
        """显示统计"""
        try:
            if not self.records:
                self.main_window.info_dialog('提示', '暂无记录')
                return
            
            total = sum(r['hours'] for r in self.records)
            days = len(set(r['date'] for r in self.records))
            avg = total / days if days > 0 else 0
            
            # 项目统计
            projects = {}
            for r in self.records:
                p = r['project']
                projects[p] = projects.get(p, 0) + r['hours']
            
            text = f"总工时: {total:.2f}h\n"
            text += f"工作天数: {days}\n"
            text += f"日均: {avg:.2f}h\n\n"
            text += "项目分布:\n"
            
            for p, h in sorted(projects.items(), key=lambda x: x[1], reverse=True)[:5]:
                pct = (h / total * 100) if total > 0 else 0
                text += f"{p}: {h:.2f}h ({pct:.1f}%)\n"
            
            self.main_window.info_dialog('统计分析', text)
        except Exception as e:
            self.main_window.info_dialog('错误', str(e))
    
    def clear_data(self, widget):
        """清空数据"""
        try:
            self.records = []
            self.save_records()
            self.info_label.text = f'数据已清空\n当前记录: 0条'
            self.main_window.info_dialog('成功', '已清空所有记录')
        except Exception as e:
            self.main_window.info_dialog('错误', str(e))


def main():
    """主函数"""
    return WorkHourApp('工时计算器', 'org.workhour.workhourcalculator')


if __name__ == '__main__':
    main().main_loop()
