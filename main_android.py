"""
Android工时计算应用
简化版本，专为Android打包优化
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from datetime import datetime, date
import json
import os


class WorkHourApp(App):
    """工时计算应用"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_file = 'work_records.json'
        self.records = []
        self.load_records()
    
    def build(self):
        """构建界面"""
        self.title = '工时计算器'
        
        # 主布局
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 标题
        title = Label(
            text='工时计算器',
            size_hint_y=None,
            height=50,
            font_size='24sp'
        )
        layout.add_widget(title)
        
        # 菜单按钮
        menu = BoxLayout(size_hint_y=None, height=200, spacing=5)
        
        btn_add = Button(text='添加记录', font_size='18sp')
        btn_add.bind(on_press=self.show_add)
        menu.add_widget(btn_add)
        
        btn_view = Button(text='查看记录', font_size='18sp')
        btn_view.bind(on_press=self.show_records)
        menu.add_widget(btn_view)
        
        btn_stats = Button(text='统计', font_size='18sp')
        btn_stats.bind(on_press=self.show_stats)
        menu.add_widget(btn_stats)
        
        btn_clear = Button(text='清空', font_size='18sp')
        btn_clear.bind(on_press=self.clear_data)
        menu.add_widget(btn_clear)
        
        layout.add_widget(menu)
        
        # 信息显示
        self.info = Label(
            text='欢迎使用工时计算器！',
            font_size='16sp',
            halign='center'
        )
        self.info.bind(size=self.info.setter('text_size'))
        layout.add_widget(self.info)
        
        return layout
    
    def load_records(self):
        """加载记录"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.records = json.load(f)
        except:
            self.records = []
    
    def save_records(self):
        """保存记录"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.records, f)
        except Exception as e:
            self.show_msg('错误', f'保存失败: {e}')
    
    def show_add(self, instance):
        """添加记录"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        content.add_widget(Label(text='日期 (YYYY-MM-DD):', size_hint_y=None, height=40))
        date_input = TextInput(
            text=date.today().strftime('%Y-%m-%d'),
            multiline=False,
            size_hint_y=None,
            height=40
        )
        content.add_widget(date_input)
        
        content.add_widget(Label(text='开始时间 (HH:MM):', size_hint_y=None, height=40))
        start_input = TextInput(text='09:00', multiline=False, size_hint_y=None, height=40)
        content.add_widget(start_input)
        
        content.add_widget(Label(text='结束时间 (HH:MM):', size_hint_y=None, height=40))
        end_input = TextInput(text='17:00', multiline=False, size_hint_y=None, height=40)
        content.add_widget(end_input)
        
        content.add_widget(Label(text='项目:', size_hint_y=None, height=40))
        project_input = TextInput(text='', multiline=False, size_hint_y=None, height=40)
        content.add_widget(project_input)
        
        def add_record(instance):
            try:
                d = datetime.strptime(date_input.text, '%Y-%m-%d').date()
                s = datetime.strptime(f"{date_input.text} {start_input.text}", '%Y-%m-%d %H:%M')
                e = datetime.strptime(f"{date_input.text} {end_input.text}", '%Y-%m-%d %H:%M')
                
                hours = (e - s).total_seconds() / 3600
                
                record = {
                    'date': date_input.text,
                    'start': start_input.text,
                    'end': end_input.text,
                    'hours': hours,
                    'project': project_input.text
                }
                
                self.records.append(record)
                self.save_records()
                popup.dismiss()
                self.show_msg('成功', f'已添加！工时: {hours:.2f}小时')
            except Exception as ex:
                self.show_msg('错误', str(ex))
        
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=5)
        btn_add = Button(text='添加')
        btn_add.bind(on_press=add_record)
        btn_layout.add_widget(btn_add)
        
        btn_cancel = Button(text='取消')
        btn_cancel.bind(on_press=lambda x: popup.dismiss())
        btn_layout.add_widget(btn_cancel)
        
        content.add_widget(btn_layout)
        
        popup = Popup(title='添加记录', content=content, size_hint=(0.9, 0.9))
        popup.open()
    
    def show_records(self, instance):
        """查看记录"""
        if not self.records:
            self.show_msg('提示', '暂无记录')
            return
        
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        scroll = ScrollView()
        record_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        record_layout.bind(minimum_height=record_layout.setter('height'))
        
        for r in self.records:
            text = f"{r['date']} {r['start']}-{r['end']}\n{r['hours']:.2f}h - {r['project']}"
            label = Label(text=text, size_hint_y=None, height=60, font_size='14sp')
            record_layout.add_widget(label)
        
        scroll.add_widget(record_layout)
        content.add_widget(scroll)
        
        btn_close = Button(text='关闭', size_hint_y=None, height=50)
        btn_close.bind(on_press=lambda x: popup.dismiss())
        content.add_widget(btn_close)
        
        popup = Popup(title='工时记录', content=content, size_hint=(0.9, 0.9))
        popup.open()
    
    def show_stats(self, instance):
        """显示统计"""
        if not self.records:
            self.show_msg('提示', '暂无记录')
            return
        
        total = sum(r['hours'] for r in self.records)
        days = len(set(r['date'] for r in self.records))
        avg = total / days if days > 0 else 0
        
        # 项目统计
        projects = {}
        for r in self.records:
            p = r['project']
            projects[p] = projects.get(p, 0) + r['hours']
        
        text = f"总工时: {total:.2f}h\n工作天数: {days}\n日均: {avg:.2f}h\n\n项目分布:\n"
        for p, h in sorted(projects.items(), key=lambda x: x[1], reverse=True):
            pct = (h / total * 100) if total > 0 else 0
            text += f"{p}: {h:.2f}h ({pct:.1f}%)\n"
        
        self.show_msg('统计', text)
    
    def clear_data(self, instance):
        """清空数据"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        content.add_widget(Label(text='确定要清空所有记录吗？', font_size='18sp'))
        
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=5)
        
        def clear(instance):
            self.records = []
            self.save_records()
            popup.dismiss()
            self.show_msg('成功', '已清空')
        
        btn_yes = Button(text='确定')
        btn_yes.bind(on_press=clear)
        btn_layout.add_widget(btn_yes)
        
        btn_no = Button(text='取消')
        btn_no.bind(on_press=lambda x: popup.dismiss())
        btn_layout.add_widget(btn_no)
        
        content.add_widget(btn_layout)
        
        popup = Popup(title='确认', content=content, size_hint=(0.8, 0.4))
        popup.open()
    
    def show_msg(self, title, message):
        """显示消息"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        content.add_widget(Label(text=message, font_size='16sp'))
        
        btn = Button(text='关闭', size_hint_y=None, height=50)
        btn.bind(on_press=lambda x: popup.dismiss())
        content.add_widget(btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.6))
        popup.open()


if __name__ == '__main__':
    WorkHourApp().run()
