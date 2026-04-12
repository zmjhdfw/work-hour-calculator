package org.workhour.calculator;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import java.util.ArrayList;
import java.util.List;

public class DataManager {
    private static final String DATABASE_NAME = "WorkHourDB";
    private static final int DATABASE_VERSION = 1;
    private static final String TABLE_RECORDS = "records";
    
    private static final String KEY_ID = "id";
    private static final String KEY_DATE = "date";
    private static final String KEY_START_TIME = "start_time";
    private static final String KEY_END_TIME = "end_time";
    private static final String KEY_PROJECT = "project";
    private static final String KEY_DESCRIPTION = "description";
    private static final String KEY_HOURS = "hours";
    
    private DatabaseHelper dbHelper;
    private SQLiteDatabase database;
    
    public DataManager(Context context) {
        dbHelper = new DatabaseHelper(context);
        database = dbHelper.getWritableDatabase();
    }
    
    public void addRecord(WorkRecord record) {
        ContentValues values = new ContentValues();
        values.put(KEY_DATE, record.getDate());
        values.put(KEY_START_TIME, record.getStartTime());
        values.put(KEY_END_TIME, record.getEndTime());
        values.put(KEY_PROJECT, record.getProject());
        values.put(KEY_DESCRIPTION, record.getDescription());
        values.put(KEY_HOURS, record.getHours());
        database.insert(TABLE_RECORDS, null, values);
    }
    
    public List<WorkRecord> getAllRecords() {
        List<WorkRecord> records = new ArrayList<>();
        Cursor cursor = database.query(TABLE_RECORDS, null, null, null, null, null, KEY_DATE + " DESC");
        
        if (cursor.moveToFirst()) {
            do {
                WorkRecord record = new WorkRecord();
                record.setId(cursor.getInt(cursor.getColumnIndexOrThrow(KEY_ID)));
                record.setDate(cursor.getString(cursor.getColumnIndexOrThrow(KEY_DATE)));
                record.setStartTime(cursor.getString(cursor.getColumnIndexOrThrow(KEY_START_TIME)));
                record.setEndTime(cursor.getString(cursor.getColumnIndexOrThrow(KEY_END_TIME)));
                record.setProject(cursor.getString(cursor.getColumnIndexOrThrow(KEY_PROJECT)));
                record.setDescription(cursor.getString(cursor.getColumnIndexOrThrow(KEY_DESCRIPTION)));
                record.setHours(cursor.getDouble(cursor.getColumnIndexOrThrow(KEY_HOURS)));
                records.add(record);
            } while (cursor.moveToNext());
        }
        cursor.close();
        return records;
    }
    
    public void deleteRecord(int id) {
        database.delete(TABLE_RECORDS, KEY_ID + " = ?", new String[]{String.valueOf(id)});
    }
    
    public void clearAllRecords() {
        database.delete(TABLE_RECORDS, null, null);
    }
    
    public Statistics getStatistics() {
        List<WorkRecord> records = getAllRecords();
        Statistics stats = new Statistics();
        
        double totalHours = 0;
        for (WorkRecord record : records) {
            totalHours += record.getHours();
        }
        
        stats.setTotalHours(totalHours);
        stats.setTotalRecords(records.size());
        stats.setAverageHours(records.isEmpty() ? 0 : totalHours / records.size());
        
        return stats;
    }
    
    private class DatabaseHelper extends SQLiteOpenHelper {
        public DatabaseHelper(Context context) {
            super(context, DATABASE_NAME, null, DATABASE_VERSION);
        }
        
        @Override
        public void onCreate(SQLiteDatabase db) {
            String CREATE_TABLE = "CREATE TABLE " + TABLE_RECORDS + "("
                + KEY_ID + " INTEGER PRIMARY KEY AUTOINCREMENT,"
                + KEY_DATE + " TEXT,"
                + KEY_START_TIME + " TEXT,"
                + KEY_END_TIME + " TEXT,"
                + KEY_PROJECT + " TEXT,"
                + KEY_DESCRIPTION + " TEXT,"
                + KEY_HOURS + " REAL)";
            db.execSQL(CREATE_TABLE);
        }
        
        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            db.execSQL("DROP TABLE IF EXISTS " + TABLE_RECORDS);
            onCreate(db);
        }
    }
}
