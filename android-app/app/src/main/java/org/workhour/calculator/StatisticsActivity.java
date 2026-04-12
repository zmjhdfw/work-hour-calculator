package org.workhour.calculator;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class StatisticsActivity extends AppCompatActivity {
    
    private TextView tvStats;
    private DataManager dataManager;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_statistics);
        
        dataManager = new DataManager(this);
        tvStats = findViewById(R.id.tvStats);
        
        showStatistics();
    }
    
    private void showStatistics() {
        Statistics stats = dataManager.getStatistics();
        
        StringBuilder sb = new StringBuilder();
        sb.append("统计分析\n\n");
        sb.append(String.format("总工时: %.2f 小时\n", stats.getTotalHours()));
        sb.append(String.format("记录数: %d 条\n", stats.getTotalRecords()));
        sb.append(String.format("平均工时: %.2f 小时\n", stats.getAverageHours()));
        
        tvStats.setText(sb.toString());
    }
}
