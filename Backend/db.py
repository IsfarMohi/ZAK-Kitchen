from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="your-username.mysql.pythonanywhere-services.com",
        user="your-username",
        password="your-password",
        database="your-username$your-database-name"
    )

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    date = request.form["date"]
    time = request.form["time"]
    guests = request.form["guests"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reservations (name, email, phone, date, time, guests) VALUES (%s, %s, %s, %s, %s, %s)",
        (name, email, phone, date, time, guests)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return "Reservation Successful!"

if __name__ == "__main__":
    app.run()
