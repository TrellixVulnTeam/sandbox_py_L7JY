import imaplib

USERNAME = 'your.user.name@gmail.com'
PASSWORD = 'yourpassword'

URL = 'imap.gmail.com'
PORT = 993

svr = imaplib.IMAP4_SSL(URL, PORT)

print(svr.login(USERNAME, PASSWORD))

print(svr.list())

print(svr.select('INBOX'))

print(svr.search(None, 'ALL'))  # None: UTF-8
print(svr.search(None, 'UNSEEN'))

message = svr.fetch(b'2', '(BODY[])')
data = message[1][0][1]

print(data.decode('utf-8'))

print(svr.search(None, 'UNSEEN'))
print(svr.search(None, 'SEEN'))
