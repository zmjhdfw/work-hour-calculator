"""
工时计算器 - Windows GUI版本
使用tkinter创建图形界面
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime, date
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from work_hour_calculator.data_manager import DataManager
from work_hour_calculator.work_calculator import WorkCalculator
from work_hour_calculator.report_generator import ReportGenerator


class WorkHourCalculatorGUI:
    """工时计算器GUI应用"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("工时计算器")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # 初始化管理器
        self.data_manager = DataManager()
        self.calculator = WorkCalculator()
        self.report_gen = ReportGenerator()
        
        # 创建界面
        self.create_widgets()
        
        # 加载数据
        self.refresh_records()
    
    def create_widgets(self):
        """创建界面组件"""
        # 标题
        title_frame = ttk.Frame(self.root, padding="10")
        title_frame.pack(fill=tk.X)
        
        title_label = ttk.Label(
            title_frame, 
            text="工时计算器", 
            font=("Arial", 20, "bold")
        )
        title_label.pack()
        
        # 创建notebook（标签页）
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 添加记录页
        self.create_add_tab()
        
        # 查看记录页
        self.create_view_tab()
        
        # 统计页
        self.create_stats_tab()
    
    def create_add_tab(self):
        """创建添加记录页"""
        add_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(add_frame, text="添加记录")
        
        # 日期
        ttk.Label(add_frame, text="日期 (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.date_entry = ttk.Entry(add_frame, width=30)
        self.date_entry.grid(row=0, column=1, pady=5)
        self.date_entry.insert(0, date.today().strftime('%Y-%m-%d'))
        
        # 开始时间
        ttk.Label(add_frame, text="开始时间 (HH:MM):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.start_entry = ttk.Entry(add_frame, width=30)
        self.start_entry.grid(row=1, column=1, pady=5)
        self.start_entry.insert(0, "09:00")
        
        # 结束时间
        ttk.Label(add_frame, text="结束时间 (HH:MM):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.end_entry = ttk.Entry(add_frame, width=30)
        self.end_entry.grid(row=2, column=1, pady=5)
        self.end_entry.insert(0, "17:00")
        
        # 项目
        ttk.Label(add_frame, text="项目名称:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.project_entry = ttk.Entry(add_frame, width=30)
        self.project_entry.grid(row=3, column=1, pady=5)
        
        # 描述
        ttk.Label(add_frame, text="工作描述:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.desc_entry = ttk.Entry(add_frame, width=30)
        self.desc_entry.grid(row=4, column=1, pady=5)
        
        # 添加按钮
        add_btn = ttk.Button(add_frame, text="添加记录", command=self.add_record)
        add_btn.grid(row=5, column=0, columnspan=2, pady=20)
    
    def create_view_tab(self):
        """创建查看记录页"""
        view_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(view_frame, text="查看记录")
        
        # 记录列表
        self.records_text = scrolledtext.ScrolledText(view_frame, width=60, height=20)
        self.records_text.pack(fill=tk.BOTH, expand=True)
        
        # 刷新按钮
        refresh_btn = ttk.Button(view_frame, text="刷新", command=self.refresh_records)
        refresh_btn.pack(pady=10)
    
    def create_stats_tab(self):
        """创建统计页"""
        stats_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(stats_frame, text="统计分析")
        
        # 统计信息
        self.stats_text = scrolledtext.ScrolledText(stats_frame, width=60, height=20)
        self.stats_text.pack(fill=tk.BOTH, expand=True)
        
        # 刷新按钮
        refresh_btn = ttk.Button(stats_frame, text="刷新统计", command=self.refresh_stats)
        refresh_btn.pack(pady=10)
    
    def add_record(self):
        """添加记录"""
        try:
            date_str = self.date_entry.get().strip()
            start_time = self.start_entry.get().strip()
            end_time = self.end_entry.get().strip()
            project = self.project_entry.get().strip()
            description = self.desc_entry.get().strip()
            
            if not all([date_str, start_time, end_time, project]):
                messagebox.showerror("错误", "请填写完整信息")
                return
            
            # 添加记录
            record = self.data_manager.add_record(
                date_str, start_time, end_time, project, description
            )
            
            # 显示成功
            messagebox.showinfo("成功", f"已添加！工时: {record.duration_hours:.2f}小时")
            
            # 清空输入
            self.project_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            
            # 刷新记录
            self.refresh_records()
            
        except Exception as e:
            messagebox.showerror("错误", str(e))
    
    def refresh_records(self):
        """刷新记录列表"""
        self.records_text.delete(1.0, tk.END)
        
        records = self.data_manager.get_all_records()
        
        if not records:
            self.records_text.insert(tk.END, "暂无记录\n")
            return
        
        for i, record in enumerate(records, 1):
            text = f"{i}. {record.date} {record.start_time}-{record.end_time}\n"
            text += f"   项目: {record.project}\n"
            text += f"   工时: {record.duration_hours:.2f}小时\n"
            if record.description:
                text += f"   描述: {record.description}\n"
            text += "\n"
            
            self.records_text.insert(tk.END, text)
    
    def refresh_stats(self):
        """刷新统计信息"""
        self.stats_text.delete(1.0, tk.END)
        
        records = self.data_manager.get_all_records()
        
        if not records:
            self.stats_text.insert(tk.END, "暂无记录\n")
            return
        
        stats = self.calculator.calculate_statistics(records)
        
        text = "工时统计\n"
        text += "=" * 40 + "\n\n"
        text += f"总工时: {stats.total_hours:.2f}小时\n"
        text += f"正常工时: {stats.normal_hours:.2f}小时\n"
        text += f"加班工时: {stats.overtime_hours:.2f}小时\n"
        text += f"工作天数: {stats.work_days}天\n"
        text += f"日均工时: {stats.average_hours_per_day:.2f}小时/天\n"
        
        self.stats_text.insert(tk.END, text)


def main():
    """主函数"""
    root = tk.Tk()
    app = WorkHourCalculatorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
