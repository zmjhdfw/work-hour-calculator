package org.workhour.calculator;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class AddRecordActivity extends AppCompatActivity {
    
    private EditText etDate, etStartTime, etEndTime, etProject, etDescription;
    private DataManager dataManager;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_record);
        
        dataManager = new DataManager(this);
        
        // 初始化视图
        etDate = findViewById(R.id.etDate);
        etStartTime = findViewById(R.id.etStartTime);
        etEndTime = findViewById(R.id.etEndTime);
        etProject = findViewById(R.id.etProject);
        etDescription = findViewById(R.id.etDescription);
        Button btnSave = findViewById(R.id.btnSave);
        
        // 设置默认值
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault());
        etDate.setText(dateFormat.format(new Date()));
        etStartTime.setText("09:00");
        etEndTime.setText("17:00");
        
        // 保存按钮
        btnSave.setOnClickListener(v -> saveRecord());
    }
    
    private void saveRecord() {
        String date = etDate.getText().toString().trim();
        String startTime = etStartTime.getText().toString().trim();
        String endTime = etEndTime.getText().toString().trim();
        String project = etProject.getText().toString().trim();
        String description = etDescription.getText().toString().trim();
        
        if (date.isEmpty() || startTime.isEmpty() || endTime.isEmpty() || project.isEmpty()) {
            Toast.makeText(this, "请填写完整信息", Toast.LENGTH_SHORT).show();
            return;
        }
        
        WorkRecord record = new WorkRecord(date, startTime, endTime, project, description);
        dataManager.addRecord(record);
        
        Toast.makeText(this, String.format("已添加！工时: %.2f小时", record.getHours()), Toast.LENGTH_SHORT).show();
        finish();
    }
}
