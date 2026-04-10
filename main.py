"""
Kivy版本的工时计算程序
用于打包成Android APK
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from datetime import datetime, date, timedelta
import json
import os

# 导入核心功能
from work_hour_calculator.models import WorkRecord
from work_hour_calculator.work_calculator import WorkCalculator


class WorkHourApp(App):
    """Kivy工时计算应用"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_file = 'work_records.json'
        self.records = []
        self.calculator = WorkCalculator()
        self.load_records()

    def build(self):
        """构建应用界面"""
        self.title = '工时计算器'

        # 主布局
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 标题
        title = Label(
            text='⏰ 工时计算器',
            size_hint_y=None,
            height=50,
            font_size='24sp'
        )
        layout.add_widget(title)

        # 菜单按钮
        menu_layout = GridLayout(cols=2, size_hint_y=None, height=150, spacing=5)

        btn_add = Button(text='添加记录', font_size='16sp')
        btn_add.bind(on_press=self.show_add_record)
        menu_layout.add_widget(btn_add)

        btn_view = Button(text='查看记录', font_size='16sp')
        btn_view.bind(on_press=self.show_records)
        menu_layout.add_widget(btn_view)

        btn_stats = Button(text='统计分析', font_size='16sp')
        btn_stats.bind(on_press=self.show_statistics)
        menu_layout.add_widget(btn_stats)

        btn_export = Button(text='导出数据', font_size='16sp')
        btn_export.bind(on_press=self.export_data)
        menu_layout.add_widget(btn_export)

        layout.add_widget(menu_layout)

        # 信息显示区域
        self.info_label = Label(
            text='欢迎使用工时计算器！\n\n点击上方按钮开始使用',
            font_size='16sp',
            halign='center',
            valign='middle'
        )
        self.info_label.bind(size=self.info_label.setter('text_size'))
        layout.add_widget(self.info_label)

        return layout

    def load_records(self):
        """加载记录"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.records = [WorkRecord.from_dict(item) for item in data]
            except:
                self.records = []
        else:
            self.records = []

    def save_records(self):
        """保存记录"""
        data = [record.to_dict() for record in self.records]
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_next_id(self):
        """获取下一个ID"""
        if not self.records:
            return 1
        return max(r.id for r in self.records) + 1

    def show_add_record(self, instance):
        """显示添加记录界面"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 日期输入
        content.add_widget(Label(text='日期 (YYYY-MM-DD):', size_hint_y=None, height=40))
        date_input = TextInput(
            text=date.today().strftime('%Y-%m-%d'),
            multiline=False,
            size_hint_y=None,
            height=40
        )
        content.add_widget(date_input)

        # 开始时间
        content.add_widget(Label(text='开始时间 (HH:MM):', size_hint_y=None, height=40))
        start_input = TextInput(text='09:00', multiline=False, size_hint_y=None, height=40)
        content.add_widget(start_input)

        # 结束时间
        content.add_widget(Label(text='结束时间 (HH:MM):', size_hint_y=None, height=40))
        end_input = TextInput(text='17:00', multiline=False, size_hint_y=None, height=40)
        content.add_widget(end_input)

        # 项目
        content.add_widget(Label(text='项目名称:', size_hint_y=None, height=40))
        project_input = TextInput(text='', multiline=False, size_hint_y=None, height=40)
        content.add_widget(project_input)

        # 描述
        content.add_widget(Label(text='工作描述:', size_hint_y=None, height=40))
        desc_input = TextInput(text='', multiline=False, size_hint_y=None, height=40)
        content.add_widget(desc_input)

        # 按钮
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=5)

        def add_record(instance):
            try:
                record_date = datetime.strptime(date_input.text, '%Y-%m-%d').date()
                start_time = datetime.strptime(
                    f"{date_input.text} {start_input.text}", '%Y-%m-%d %H:%M'
                )
                end_time = datetime.strptime(
                    f"{date_input.text} {end_input.text}", '%Y-%m-%d %H:%M'
                )

                record = WorkRecord(
                    id=self.get_next_id(),
                    date=record_date,
                    start_time=start_time,
                    end_time=end_time,
                    project=project_input.text,
                    description=desc_input.text
                )

                self.records.append(record)
                self.save_records()
                popup.dismiss()
                self.show_message('成功', f'记录已添加！\n工时: {record.duration_hours:.2f}小时')
            except Exception as e:
                self.show_message('错误', f'添加失败: {str(e)}')

        btn_add = Button(text='添加')
        btn_add.bind(on_press=add_record)
        btn_layout.add_widget(btn_add)

        btn_cancel = Button(text='取消')
        btn_cancel.bind(on_press=lambda x: popup.dismiss())
        btn_layout.add_widget(btn_cancel)

        content.add_widget(btn_layout)

        popup = Popup(title='添加工时记录', content=content, size_hint=(0.9, 0.9))
        popup.open()

    def show_records(self, instance):
        """显示记录列表"""
        if not self.records:
            self.show_message('提示', '暂无记录')
            return

        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 滚动视图
        scroll = ScrollView()
        record_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        record_layout.bind(minimum_height=record_layout.setter('height'))

        for record in sorted(self.records, key=lambda x: (x.date, x.start_time), reverse=True):
            record_text = (
                f"ID: {record.id} | {record.date}\n"
                f"{record.start_time.strftime('%H:%M')}-{record.end_time.strftime('%H:%M')} | "
                f"{record.duration_hours:.2f}h\n"
                f"项目: {record.project}"
            )
            record_label = Label(
                text=record_text,
                size_hint_y=None,
                height=80,
                font_size='14sp'
            )
            record_layout.add_widget(record_label)

        scroll.add_widget(record_layout)
        content.add_widget(scroll)

        btn_close = Button(text='关闭', size_hint_y=None, height=50)
        btn_close.bind(on_press=lambda x: popup.dismiss())
        content.add_widget(btn_close)

        popup = Popup(title='工时记录', content=content, size_hint=(0.9, 0.9))
        popup.open()

    def show_statistics(self, instance):
        """显示统计信息"""
        if not self.records:
            self.show_message('提示', '暂无记录')
            return

        total_hours = self.calculator.calculate_total_hours(self.records)
        work_days = len(set(r.date for r in self.records))
        avg_hours = total_hours / work_days if work_days > 0 else 0

        # 计算加班
        from collections import defaultdict
        daily_hours = defaultdict(float)
        for record in self.records:
            daily_hours[record.date] += record.duration_hours

        normal_hours = 0
        overtime_hours = 0
        for hours in daily_hours.values():
            if hours <= 8:
                normal_hours += hours
            else:
                normal_hours += 8
                overtime_hours += (hours - 8)

        # 项目统计
        project_stats = self.calculator.calculate_by_project(self.records)

        stats_text = (
            f"📊 工时统计\n\n"
            f"总工时: {total_hours:.2f} 小时\n"
            f"正常工时: {normal_hours:.2f} 小时\n"
            f"加班工时: {overtime_hours:.2f} 小时\n"
            f"工作天数: {work_days} 天\n"
            f"日均工时: {avg_hours:.2f} 小时/天\n\n"
            f"📁 项目分布:\n"
        )

        for project, hours in sorted(project_stats.items(), key=lambda x: x[1], reverse=True):
            percentage = (hours / total_hours * 100) if total_hours > 0 else 0
            stats_text += f"{project}: {hours:.2f}h ({percentage:.1f}%)\n"

        self.show_message('统计分析', stats_text)

    def export_data(self, instance):
        """导出数据"""
        if not self.records:
            self.show_message('提示', '暂无数据可导出')
            return

        try:
            import csv
            csv_file = 'work_hours_export.csv'

            with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', '日期', '开始时间', '结束时间', '工时', '项目', '描述'])

                for record in sorted(self.records, key=lambda x: (x.date, x.start_time)):
                    writer.writerow([
                        record.id,
                        record.date.strftime('%Y-%m-%d'),
                        record.start_time.strftime('%H:%M'),
                        record.end_time.strftime('%H:%M'),
                        f"{record.duration_hours:.2f}",
                        record.project,
                        record.description
                    ])

            self.show_message('成功', f'数据已导出到:\n{csv_file}')
        except Exception as e:
            self.show_message('错误', f'导出失败: {str(e)}')

    def show_message(self, title, message):
        """显示消息弹窗"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        msg_label = Label(text=message, font_size='16sp')
        content.add_widget(msg_label)

        btn_close = Button(text='关闭', size_hint_y=None, height=50)
        btn_close.bind(on_press=lambda x: popup.dismiss())
        content.add_widget(btn_close)

        popup = Popup(title=title, content=content, size_hint=(0.8, 0.6))
        popup.open()


if __name__ == '__main__':
    WorkHourApp().run()
