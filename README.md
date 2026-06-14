# 📝 Student Marks Management System

A lightweight, high-efficiency full-stack web application designed to manage, evaluate, filter, and export student academic marks data.

---

## 🚀 Features

### 📋 Data Entry & Validation
* [cite_start]**Form Inputs**: Captures Student Name [cite: 7][cite_start], Date of Birth [cite: 8][cite_start], Semester [cite: 9][cite_start], Subject dropdown selection [cite: 10][cite_start], Marks [cite: 11][cite_start], and Out Of Marks[cite: 12].
* [cite_start]**Score Boundary Validation**: Prevents form submission if "Out Of Marks" is numerically lower than "Marks"[cite: 13].
* [cite_start]**Duplicate Prevention Logic**: Restricts the application from saving a duplicate subject record for the same student within the same semester[cite: 14, 15].
* [cite_start]**Automated Computations**: Instantly processes percentage scores [cite: 32] [cite_start]and determines "Pass" (40% and above) [cite: 34] [cite_start]or "Fail" (below 40%) statuses[cite: 33].

### 📊 Report Metrics
* [cite_start]**Dynamic Table Matrix**: Displays student fields alongside calculated percentages, pass/fail indicators, and data removal actions[cite: 19, 21, 22, 23, 24, 25, 26, 27, 28, 30].
* [cite_start]**Interactive Utility**: Supports ascending/descending sorting for all data columns[cite: 41].
* [cite_start]**Multi-Input Filters**: Filters database records instantly by Name [cite: 36][cite_start], Semester [cite: 37][cite_start], Subject [cite: 38][cite_start], and Status[cite: 39].
* [cite_start]**Pagination Layer**: Segments records into sequential pages for performance optimization[cite: 42].
* [cite_start]**Grand Totals**: Computes and reflects cumulative sums for marks and total percentages in the footer area[cite: 43].

### 🔄 Isolation & Export Utilities
* [cite_start]**Conditional Row Movement**: Moves checked student records into a separate secondary table[cite: 45, 46, 47].
* [cite_start]**Status Enforcement**: Blocks the simultaneous selection of "Pass" and "Fail" students during batch relocation operations[cite: 48, 49].
* [cite_start]**PDF Engine**: Generates a downloadable clean structured PDF mark sheet report[cite: 50, 51].

---

## 🛠️ Tech Stack

* **Backend Framework**: Python (Flask)
* [cite_start]**Database Layer**: SQLite (Persistent file-based storage) [cite: 17]
* **Frontend Design**: HTML5, Tailwind CSS CDN
* **Client Scripts**: Native JavaScript (ES6+), jsPDF, jsPDF-AutoTable

---
##📈 Future Architectural Improvements
* Unique Student Identification Keys: Implement a mandatory student_id primary/foreign key data constraint rather than relying strictly on text-string matching names, preventing data overlap if two distinct students share an identical name.
* Relational Database Schema Design: Separate data records into distinct, normalized database tables (Students, Semesters, Subjects, and Marks) to optimize query indexing and eliminate flat-file data redundancy.
* Data Persistence for Relocated Records: Modify the schema constraints so that records shifted to the secondary isolated table retain their state within a database table column rather than resetting upon browser refreshes.
* User Editing Form Pipeline: Build an inline asynchronous modal to allow direct backend editing for pre-existing records.
