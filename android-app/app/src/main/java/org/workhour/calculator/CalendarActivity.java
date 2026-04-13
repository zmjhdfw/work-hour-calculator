package org.workhour.calculator;

import android.os.Bundle;
import android.widget.GridView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class CalendarActivity extends AppCompatActivity {
    
    private GridView gridView;
    private TextView tvMonth;
    private CalendarAdapter adapter;
    private DataManager dataManager;
    private Calendar currentDate;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calendar);
        
        dataManager = new DataManager(this);
        currentDate = Calendar.getInstance();
        
        gridView = findViewById(R.id.gridView);
        tvMonth = findViewById(R.id.tvMonth);
        
        findViewById(R.id.btnPrev).setOnClickListener(v -> previousMonth());
        findViewById(R.id.btnNext).setOnClickListener(v -> nextMonth());
        
        updateCalendar();
    }
    
    private void updateCalendar() {
        SimpleDateFormat monthFormat = new SimpleDateFormat("yyyy年MM月", Locale.getDefault());
        tvMonth.setText(monthFormat.format(currentDate.getTime()));
        
        List<Date> dates = getMonthDates(currentDate);
        List<WorkRecord> records = dataManager.getAllRecords();
        
        adapter = new CalendarAdapter(this, dates, records);
        gridView.setAdapter(adapter);
    }
    
    private List<Date> getMonthDates(Calendar calendar) {
        List<Date> dates = new ArrayList<>();
        Calendar cal = (Calendar) calendar.clone();
        
        // 设置到月初
        cal.set(Calendar.DAY_OF_MONTH, 1);
        int firstDayOfWeek = cal.get(Calendar.DAY_OF_WEEK) - 1;
        
        // 添加前面的空白
        cal.add(Calendar.DAY_OF_MONTH, -firstDayOfWeek);
        
        // 添加6周的日期
        for (int i = 0; i < 42; i++) {
            dates.add(cal.getTime());
            cal.add(Calendar.DAY_OF_MONTH, 1);
        }
        
        return dates;
    }
    
    private void previousMonth() {
        currentDate.add(Calendar.MONTH, -1);
        updateCalendar();
    }
    
    private void nextMonth() {
        currentDate.add(Calendar.MONTH, 1);
        updateCalendar();
    }
}
