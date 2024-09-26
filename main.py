import requests

#Pegar Infomações Da API
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)

#Enviar email
import smtplib
import email.message

def enviar_email(cotacao):  
    corpo_email = f"""
    <p>O valor Do Dolar Está Abaixo de 6$.: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dolar Abaixo De 6$ Reais"
    msg['From'] = 'remetente'
    msg['To'] = 'destinatario'
    password = 'senha' #Senha do Gmail 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

#Logica Do Sistema
if cotacao < 6.00:
    enviar_email(cotacao)

