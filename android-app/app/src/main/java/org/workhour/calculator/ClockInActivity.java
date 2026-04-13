package org.workhour.calculator;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class ClockInActivity extends AppCompatActivity {
    
    private TextView tvStatus, tvClockInTime, tvClockOutTime, tvWorkHours;
    private Button btnClockIn, btnClockOut;
    private DataManager dataManager;
    private String currentDate;
    private String clockInTime;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_clock_in);
        
        dataManager = new DataManager(this);
        
        // 初始化视图
        tvStatus = findViewById(R.id.tvStatus);
        tvClockInTime = findViewById(R.id.tvClockInTime);
        tvClockOutTime = findViewById(R.id.tvClockOutTime);
        tvWorkHours = findViewById(R.id.tvWorkHours);
        btnClockIn = findViewById(R.id.btnClockIn);
        btnClockOut = findViewById(R.id.btnClockOut);
        
        // 获取当前日期
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault());
        currentDate = dateFormat.format(new Date());
        
        // 设置标题
        setTitle("打卡 - " + currentDate);
        
        // 检查今日打卡状态
        checkTodayStatus();
        
        // 打卡按钮
        btnClockIn.setOnClickListener(v -> clockIn());
        
        // 签退按钮
        btnClockOut.setOnClickListener(v -> clockOut());
    }
    
    private void checkTodayStatus() {
        // 这里可以检查今天是否已打卡
        // 简化版本：显示未打卡状态
        tvStatus.setText("今日未打卡");
        tvClockInTime.setText("上班打卡: --:--");
        tvClockOutTime.setText("下班打卡: --:--");
        tvWorkHours.setText("工作时长: --");
        btnClockOut.setEnabled(false);
    }
    
    private void clockIn() {
        SimpleDateFormat timeFormat = new SimpleDateFormat("HH:mm", Locale.getDefault());
        clockInTime = timeFormat.format(new Date());
        
        tvClockInTime.setText("上班打卡: " + clockInTime);
        tvStatus.setText("已打卡，工作中...");
        btnClockIn.setEnabled(false);
        btnClockOut.setEnabled(true);
        
        Toast.makeText(this, "上班打卡成功: " + clockInTime, Toast.LENGTH_SHORT).show();
    }
    
    private void clockOut() {
        if (clockInTime == null) {
            Toast.makeText(this, "请先上班打卡", Toast.LENGTH_SHORT).show();
            return;
        }
        
        SimpleDateFormat timeFormat = new SimpleDateFormat("HH:mm", Locale.getDefault());
        String clockOutTime = timeFormat.format(new Date());
        
        // 计算工作时长
        double hours = calculateWorkHours(clockInTime, clockOutTime);
        
        // 保存记录
        WorkRecord record = new WorkRecord(currentDate, clockInTime, clockOutTime, "日常工作", "打卡记录");
        dataManager.addRecord(record);
        
        // 更新UI
        tvClockOutTime.setText("下班打卡: " + clockOutTime);
        tvWorkHours.setText(String.format("工作时长: %.2f小时", hours));
        tvStatus.setText("今日已完成");
        btnClockOut.setEnabled(false);
        
        Toast.makeText(this, String.format("下班打卡成功！工作时长: %.2f小时", hours), Toast.LENGTH_LONG).show();
    }
    
    private double calculateWorkHours(String startTime, String endTime) {
        try {
            SimpleDateFormat sdf = new SimpleDateFormat("HH:mm", Locale.getDefault());
            Date start = sdf.parse(startTime);
            Date end = sdf.parse(endTime);
            if (start != null && end != null) {
                long diff = end.getTime() - start.getTime();
                return diff / (1000.0 * 60 * 60);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return 0;
    }
}
