"""
Web版本工时计算程序
提供移动端友好的Web界面
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime, date, timedelta
import os
import sys

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from work_hour_calculator.models import WorkRecord
from work_hour_calculator.data_manager import DataManager
from work_hour_calculator.work_calculator import WorkCalculator
from work_hour_calculator.report_generator import ReportGenerator

app = Flask(__name__)
app.secret_key = 'work_hour_calculator_secret_key_2026'

# 初始化
data_manager = DataManager('web_work_records.json')
calculator = WorkCalculator()
report_gen = ReportGenerator()


@app.route('/')
def index():
    """主页"""
    records = data_manager.get_all_records()
    projects = data_manager.get_all_projects()
    
    # 计算今日统计
    today = date.today()
    today_records = data_manager.get_records_by_date(today)
    today_hours = calculator.calculate_total_hours(today_records)
    
    # 计算本周统计
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    week_records = data_manager.get_records_by_range(week_start, week_end)
    week_stats = calculator.calculate_range(week_records, week_start, week_end) if week_records else None
    
    return render_template('index.html', 
                         records=records[:10],  # 最近10条记录
                         projects=projects,
                         today_hours=today_hours,
                         week_stats=week_stats,
                         today=today)


@app.route('/add', methods=['GET', 'POST'])
def add_record():
    """添加记录"""
    if request.method == 'POST':
        try:
            # 获取表单数据
            record_date = request.form.get('date')
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')
            project = request.form.get('project')
            description = request.form.get('description', '')
            
            # 解析日期和时间
            record_date = datetime.strptime(record_date, '%Y-%m-%d').date()
            start_dt = datetime.strptime(f"{record_date} {start_time}", '%Y-%m-%d %H:%M')
            end_dt = datetime.strptime(f"{record_date} {end_time}", '%Y-%m-%d %H:%M')
            
            # 创建记录
            record = WorkRecord(
                id=0,
                date=record_date,
                start_time=start_dt,
                end_time=end_dt,
                project=project,
                description=description
            )
            
            # 保存记录
            record_id = data_manager.add_record(record)
            flash(f'记录添加成功！ID: {record_id}', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            flash(f'添加失败: {str(e)}', 'error')
    
    # GET请求，显示添加表单
    projects = data_manager.get_all_projects()
    today = date.today().strftime('%Y-%m-%d')
    return render_template('add.html', projects=projects, today=today)


@app.route('/records')
def view_records():
    """查看所有记录"""
    records = data_manager.get_all_records()
    return render_template('records.html', records=records)


@app.route('/statistics')
def statistics():
    """统计页面"""
    records = data_manager.get_all_records()
    
    if not records:
        return render_template('statistics.html', stats=None, project_stats=None)
    
    # 计算总体统计
    min_date = min(r.date for r in records)
    max_date = max(r.date for r in records)
    stats = calculator.calculate_range(records, min_date, max_date)
    
    # 项目统计
    project_stats = calculator.calculate_by_project(records)
    
    return render_template('statistics.html', 
                         stats=stats, 
                         project_stats=project_stats,
                         total_records=len(records))


@app.route('/edit/<int:record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    """编辑记录"""
    try:
        record = data_manager.get_record(record_id)
    except:
        flash('记录不存在', 'error')
        return redirect(url_for('view_records'))
    
    if request.method == 'POST':
        try:
            # 获取表单数据
            record.date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')
            
            record.start_time = datetime.strptime(f"{record.date} {start_time}", '%Y-%m-%d %H:%M')
            record.end_time = datetime.strptime(f"{record.date} {end_time}", '%Y-%m-%d %H:%M')
            record.project = request.form.get('project')
            record.description = request.form.get('description', '')
            
            # 更新记录
            data_manager.update_record(record)
            flash('记录更新成功！', 'success')
            return redirect(url_for('view_records'))
            
        except Exception as e:
            flash(f'更新失败: {str(e)}', 'error')
    
    # GET请求，显示编辑表单
    projects = data_manager.get_all_projects()
    return render_template('edit.html', record=record, projects=projects)


@app.route('/delete/<int:record_id>', methods=['POST'])
def delete_record(record_id):
    """删除记录"""
    try:
        data_manager.delete_record(record_id)
        flash('记录已删除', 'success')
    except Exception as e:
        flash(f'删除失败: {str(e)}', 'error')
    
    return redirect(url_for('view_records'))


@app.route('/export')
def export_data():
    """导出数据"""
    records = data_manager.get_all_records()
    
    if not records:
        flash('没有数据可导出', 'error')
        return redirect(url_for('index'))
    
    # 生成CSV数据
    import io
    import csv
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # 写入表头
    writer.writerow(['ID', '日期', '开始时间', '结束时间', '工时(小时)', '项目', '描述'])
    
    # 写入数据
    for record in sorted(records, key=lambda x: (x.date, x.start_time)):
        writer.writerow([
            record.id,
            record.date.strftime('%Y-%m-%d'),
            record.start_time.strftime('%H:%M'),
            record.end_time.strftime('%H:%M'),
            f"{record.duration_hours:.2f}",
            record.project,
            record.description
        ])
    
    output.seek(0)
    return jsonify({
        'data': output.getvalue(),
        'filename': 'work_hours_export.csv'
    })


if __name__ == '__main__':
    # 创建templates目录
    os.makedirs('templates', exist_ok=True)
    
    print("=" * 60)
    print("工时计算程序 - Web版本")
    print("=" * 60)
    print("\n启动Web服务器...")
    print("访问地址: http://localhost:5000")
    print("按 Ctrl+C 停止服务器\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
