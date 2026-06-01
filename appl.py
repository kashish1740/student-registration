from flask import Flask, render_template, request

import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    gender TEXT
)
""")

conn.commit()
conn.close()

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/submit", methods=["POST"])
@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    gender = request.form["gender"]

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (name,email,phone,gender)
        VALUES(?,?,?,?)
        """,
        (name,email,phone,gender)
    )

    conn.commit()
    conn.close()

    return f"""
    <h2>Registration Successful 🎉</h2>

    <p>Name: {name}</p>
    <p>Email: {email}</p>
    <p>Phone: {phone}</p>
    <p>Gender: {gender}</p>

    <a href="/">Go Back</a>
    """
@app.route("/students")
def students():

    conn = sqlite3.connect("student.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    data = cursor.fetchall()

    conn.close()

    return render_template(
        "students.html",
        students=data
    )
if __name__ == "__main__":
    app.run(debug=True)