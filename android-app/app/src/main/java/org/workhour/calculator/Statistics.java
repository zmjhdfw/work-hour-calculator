package org.workhour.calculator;

public class Statistics {
    private double totalHours;
    private int totalRecords;
    private double averageHours;
    
    public Statistics() {}
    
    // Getters and Setters
    public double getTotalHours() { return totalHours; }
    public void setTotalHours(double totalHours) { this.totalHours = totalHours; }
    
    public int getTotalRecords() { return totalRecords; }
    public void setTotalRecords(int totalRecords) { this.totalRecords = totalRecords; }
    
    public double getAverageHours() { return averageHours; }
    public void setAverageHours(double averageHours) { this.averageHours = averageHours; }
}
