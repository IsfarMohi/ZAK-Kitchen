import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
from email.mime.multipart import MIMEMultipart
from email_template import html_content

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'E:\DEV\Development\PythonDev\WebDev\ZAK-Kitchen\credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
            
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def create_message(sender, to, subject, message_text):
    # Create a multipart message
    message = MIMEMultipart()
    
    # Attach the plain text and HTML parts
    message.attach(MIMEText(message_text, "plain"))
    message.attach(MIMEText(html_content, "html"))
    
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f'Message Id: {message["id"]}')
        return message
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def main():
    service = get_gmail_service()
    
    sender = "majindevil164@gmail.com" 
    to = "isfarmohi.im@gmail.com"     
    subject = "Test Email from Gmail API"
    message_text = "This is a test email sent using the Gmail API"
    
    message = create_message(sender, to, subject, message_text)
    send_message(service, "me", message)

if __name__ == '__main__':
    main()
