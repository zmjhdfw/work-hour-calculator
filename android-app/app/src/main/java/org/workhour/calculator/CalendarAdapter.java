package org.workhour.calculator;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class CalendarAdapter extends BaseAdapter {
    
    private Context context;
    private List<Date> dates;
    private Map<String, Double> workHoursMap;
    private SimpleDateFormat dateFormat;
    private Date today;
    
    public CalendarAdapter(Context context, List<Date> dates, List<WorkRecord> records) {
        this.context = context;
        this.dates = dates;
        this.dateFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault());
        this.today = new Date();
        
        // 构建工时映射
        workHoursMap = new HashMap<>();
        for (WorkRecord record : records) {
            String date = record.getDate();
            double hours = workHoursMap.getOrDefault(date, 0.0);
            workHoursMap.put(date, hours + record.getHours());
        }
    }
    
    @Override
    public int getCount() {
        return dates.size();
    }
    
    @Override
    public Object getItem(int position) {
        return dates.get(position);
    }
    
    @Override
    public long getItemId(int position) {
        return position;
    }
    
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.calendar_item, parent, false);
        }
        
        TextView tvDay = convertView.findViewById(R.id.tvDay);
        TextView tvHours = convertView.findViewById(R.id.tvHours);
        
        Date date = dates.get(position);
        String dateStr = dateFormat.format(date);
        
        // 显示日期
        SimpleDateFormat dayFormat = new SimpleDateFormat("d", Locale.getDefault());
        tvDay.setText(dayFormat.format(date));
        
        // 显示工时
        Double hours = workHoursMap.get(dateStr);
        if (hours != null && hours > 0) {
            tvHours.setText(String.format("%.1fh", hours));
            tvHours.setVisibility(View.VISIBLE);
            convertView.setBackgroundColor(Color.parseColor("#E8F5E9")); // 浅绿色背景
        } else {
            tvHours.setVisibility(View.GONE);
            convertView.setBackgroundColor(Color.TRANSPARENT);
        }
        
        // 高亮今天
        String todayStr = dateFormat.format(today);
        if (dateStr.equals(todayStr)) {
            tvDay.setTextColor(Color.parseColor("#6200EE")); // 紫色
            tvDay.setTextSize(16);
        } else {
            tvDay.setTextColor(Color.BLACK);
            tvDay.setTextSize(14);
        }
        
        return convertView;
    }
}
