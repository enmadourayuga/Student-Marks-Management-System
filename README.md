📝 Student Marks Management System
A lightweight, high-efficiency full-stack web application designed to manage, evaluate, filter, and export student academic marks data.  
🚀 Features
📋 Data Entry & ValidationForm Inputs: Captures Student Name, Date of Birth, Semester, Subject dropdown selection, Marks, and Out Of Marks.  
Score Boundary Validation: Prevents form submission if "Out Of Marks" is numerically lower than "Marks".  
Duplicate Prevention Logic: Restricts the application from saving a duplicate subject record for the same student within the same semester.  
Automated Computations: Instantly processes percentage scores and determines "Pass" (40% and above) or "Fail" (below 40%) statuses.  

📊 Report MetricsDynamic Table Matrix: Displays student fields alongside calculated percentages, pass/fail indicators, and data removal actions.  
Interactive Utility: Supports ascending/descending sorting for all data columns. 
Multi-Input Filters: Filters database records instantly by Name, Semester, Subject, and Status.  
Pagination Layer: Segments records into sequential pages for performance optimization. 
Grand Totals: Computes and reflects cumulative sums for marks and total percentages in the footer area.  

🔄 Isolation & Export UtilitiesConditional Row Movement: Moves checked student records into a separate secondary table.  
Status Enforcement: Blocks the simultaneous selection of "Pass" and "Fail" students during batch relocation operations.  
PDF Engine: Generates a downloadable clean structured PDF mark sheet report.  

🛠️ Tech StackBackend Framework: Python (Flask)
Database Layer: SQLite (Persistent file-based storage)   
Frontend Design: HTML5, Tailwind CSS CDN
Client Scripts: Native JavaScript (ES6+), jsPDF, jsPDF-AutoTable
