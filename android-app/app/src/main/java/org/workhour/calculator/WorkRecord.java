package org.workhour.calculator;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class WorkRecord {
    private int id;
    private String date;
    private String startTime;
    private String endTime;
    private String project;
    private String description;
    private double hours;
    
    public WorkRecord() {}
    
    public WorkRecord(String date, String startTime, String endTime, String project, String description) {
        this.date = date;
        this.startTime = startTime;
        this.endTime = endTime;
        this.project = project;
        this.description = description;
        this.hours = calculateHours(startTime, endTime);
    }
    
    private double calculateHours(String start, String end) {
        try {
            SimpleDateFormat sdf = new SimpleDateFormat("HH:mm", Locale.getDefault());
            Date startDate = sdf.parse(start);
            Date endDate = sdf.parse(end);
            if (startDate != null && endDate != null) {
                long diff = endDate.getTime() - startDate.getTime();
                return diff / (1000.0 * 60 * 60);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return 0;
    }
    
    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    
    public String getDate() { return date; }
    public void setDate(String date) { this.date = date; }
    
    public String getStartTime() { return startTime; }
    public void setStartTime(String startTime) { this.startTime = startTime; }
    
    public String getEndTime() { return endTime; }
    public void setEndTime(String endTime) { this.endTime = endTime; }
    
    public String getProject() { return project; }
    public void setProject(String project) { this.project = project; }
    
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    
    public double getHours() { return hours; }
    public void setHours(double hours) { this.hours = hours; }
    
    @Override
    public String toString() {
        return String.format("%s %s-%s (%.2fh) - %s", 
            date, startTime, endTime, hours, project);
    }
}
