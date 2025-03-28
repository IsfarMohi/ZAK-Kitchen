from flask import Flask, render_template, request

from Backend.db import add_data

app = Flask(__name__)

reservations_data = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/reservations', methods=['GET', 'POST'])
def make_reservation():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']
        
        add_data(name, email, phone, date, time, guests)
 
        return "<h1>Reservation Sent!</h1><p>We have received your booking.</p><a href='/'>Back to Home</a>"
    
    return render_template('reservations.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"New Message from {name} ({email}): {message}")
    return render_template('contact.html')

# @app.route("/test-db")
# def test_db():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM reservations;")  # Adjust table name
#     data = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return str(data)


if __name__ == "__main__":
    app.run(debug=True)
