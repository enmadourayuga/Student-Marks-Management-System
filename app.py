from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS marks 
                        (id INTEGER PRIMARY KEY, name TEXT, dob TEXT, semester TEXT, 
                         subject TEXT, marks REAL, out_of REAL, percentage REAL, status TEXT)''')

init_db()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/marks', methods=['GET', 'POST'])
def manage_marks():
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        if request.method == 'POST':
            data = request.json
            
            # Validation Constraints
            if data['out_of'] < data['marks']:
                return jsonify({"error": "Out of marks cannot be less than obtained marks."}), 400
            
            if not data.get('id'): # Check for duplicates only on new inserts
                cur.execute("SELECT id FROM marks WHERE name=? AND semester=? AND subject=?", 
                            (data['name'], data['semester'], data['subject']))
                if cur.fetchone():
                    return jsonify({"error": "Duplicate subject entry for this semester."}), 400
            
            # Logic Processing
            pct = round((data['marks'] / data['out_of']) * 100, 2)
            status = "Pass" if pct >= 40 else "Fail"
            
            if data.get('id'): # Edit existing record
                cur.execute('''UPDATE marks SET name=?, dob=?, semester=?, subject=?, marks=?, out_of=?, percentage=?, status=? WHERE id=?''',
                            (data['name'], data['dob'], data['semester'], data['subject'], data['marks'], data['out_of'], pct, status, data['id']))
            else: # Insert new record
                cur.execute('''INSERT INTO marks (name, dob, semester, subject, marks, out_of, percentage, status) 
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                            (data['name'], data['dob'], data['semester'], data['subject'], data['marks'], data['out_of'], pct, status))
            
            return jsonify({"success": True})
        
        # GET Request
        cur.execute("SELECT * FROM marks")
        return jsonify([dict(row) for row in cur.fetchall()])

@app.route('/api/marks/<int:id>', methods=['DELETE'])
def delete_mark(id):
    with sqlite3.connect('database.db') as conn:
        conn.execute("DELETE FROM marks WHERE id=?", (id,))
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True, port=3000)