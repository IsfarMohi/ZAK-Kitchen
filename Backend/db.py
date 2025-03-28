import os 
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
KEY = os.getenv('KEY')

reservations_data = []
supabase = create_client(URL,KEY)

def add_data(name,email, phone, date, time, guests):
    data = {
        'name': name,
        'email': email,
        'phone': phone,
        'date': date,
        'time': time,
        'guests': guests
        }
    
    response = supabase.table("reservations").insert(data).execute()
    if "error" in response and response["error"]:
        return f"Error: {response['error']}"
    
    return "Reservation added successfully!"
    


