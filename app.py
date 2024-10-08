from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permette le richieste dal frontend

# Configurazione dell'email (usa il tuo server SMTP, ad esempio Gmail)
EMAIL_ADDRESS = "giustozzi.gabriele.03@gmail.com"
EMAIL_PASSWORD = "pahe kcdv buaq msul"

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json  # Ricevi i dati in formato JSON
    name = data.get('name')
    surname = data.get('surname')
    email = data.get('email')
    number = data.get('number')
    company_role =  data.get('company_role')
    message = data.get('message')

    # Creazione dell'email
    subject = f"NUOVO MESSAGGIO dal FORM"
    body = f"Nome: {name} {surname}\nRuolo Aziendale: {company_role}\nCellulare: {number}\nEmail: {email}\nMessaggio: {message}"

    # Configurazione del server SMTP
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = EMAIL_ADDRESS  # Può essere il tuo indirizzo o quello del destinatario
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Invia l'email usando SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        return jsonify({"message": "Email inviata con successo!"}), 200
    except Exception as e:
        print(f"Errore nell'invio dell'email: {e}")
        return jsonify({"error": "Errore durante l'invio dell'email"}), 500

if __name__ == '__main__':
    app.run(debug=True)
