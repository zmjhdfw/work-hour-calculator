package org.workhour.calculator;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;
import java.util.List;

public class ViewRecordsActivity extends AppCompatActivity {
    
    private ListView listView;
    private DataManager dataManager;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_records);
        
        dataManager = new DataManager(this);
        listView = findViewById(R.id.listView);
        
        loadRecords();
    }
    
    @Override
    protected void onResume() {
        super.onResume();
        loadRecords();
    }
    
    private void loadRecords() {
        List<WorkRecord> records = dataManager.getAllRecords();
        List<String> displayList = new ArrayList<>();
        
        for (WorkRecord record : records) {
            String display = String.format("%s %s-%s\n%.2fh - %s",
                record.getDate(),
                record.getStartTime(),
                record.getEndTime(),
                record.getHours(),
                record.getProject());
            displayList.add(display);
        }
        
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this,
            android.R.layout.simple_list_item_1, displayList);
        listView.setAdapter(adapter);
    }
}
