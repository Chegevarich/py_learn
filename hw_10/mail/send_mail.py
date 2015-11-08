import smtplib
import imaplib
import email
from email.mime.text import MIMEText

fromaddr = input('введите свою почту полностью')
password = input('введите пароль')

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(fromaddr.split('@')[0],password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()


def recive_mail():
	con=imaplib.IMAP4_SSL('imap.gmail.com')
	con.login(fromaddr.split('@')[0],password)
	con.list()
	con.select("INBOX")
	result, data = con.fetch()
	raw=email.message_from_bytes(data[0][1])

	print(raw["From"], raw["To"], raw["Subject"])
	#print(get_text(raw))

def recive():
	#создание подключения
	gmail = imaplib.IMAP4_SSL('imap.gmail.com', '993')
	#логин
	gmail.login(fromaddr.split('@')[0], password)
	#переходим в папку входящие
	gmail.select('INBOX')
	gmail.status('INBOX', "(UNSEEN)")
	#непрочитанные сообщения, статус - идентификаторы
	typ, data = gmail.search(None, '(UNSEEN)')
	#TODO how to parse
	gmail.close()

def get_text(msg):
    if msg.is_multipart():
        return get_text(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

while True:
	x = input('>>>')

	if x == 'send':
		toaddrs = input('введите свою почту(ы) получателя(ей) полностью')
		msg = input('Введите сообщение')
		send_mail()

	if x == 'recive':
		recive()

	if x == '1':
		break