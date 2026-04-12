package org.workhour.calculator;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    
    private TextView tvRecordCount;
    private DataManager dataManager;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        dataManager = new DataManager(this);
        
        // 初始化视图
        tvRecordCount = findViewById(R.id.tvRecordCount);
        Button btnAdd = findViewById(R.id.btnAdd);
        Button btnView = findViewById(R.id.btnView);
        Button btnStats = findViewById(R.id.btnStats);
        Button btnClear = findViewById(R.id.btnClear);
        
        // 更新记录数量
        updateRecordCount();
        
        // 设置按钮点击事件
        btnAdd.setOnClickListener(v -> {
            Intent intent = new Intent(MainActivity.this, AddRecordActivity.class);
            startActivity(intent);
        });
        
        btnView.setOnClickListener(v -> {
            Intent intent = new Intent(MainActivity.this, ViewRecordsActivity.class);
            startActivity(intent);
        });
        
        btnStats.setOnClickListener(v -> {
            Intent intent = new Intent(MainActivity.this, StatisticsActivity.class);
            startActivity(intent);
        });
        
        btnClear.setOnClickListener(v -> {
            dataManager.clearAllRecords();
            updateRecordCount();
        });
    }
    
    @Override
    protected void onResume() {
        super.onResume();
        updateRecordCount();
    }
    
    private void updateRecordCount() {
        List<WorkRecord> records = dataManager.getAllRecords();
        tvRecordCount.setText("当前记录: " + records.size() + " 条");
    }
}
