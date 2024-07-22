from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute('INSERT INTO contacts (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    
    return 'Form submitted!'

if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True)
