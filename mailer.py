import smtplib
import sqlite3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

to = 'receiver@gmail.com'
gmail_user = 'sender@gmail.com'
gmail_pwd = 'passwprd'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
conn = sqlite3.connect("padakalibot/padakalidata")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
update_cur = conn.cursor()
mail_text = ""
cur.execute("select * from words where is_sent = 0 order by pub_date asc limit 5")
row = cur.fetchone()
while row:
    mail_text += "<h2> " + row['title'] + "</h2> <br>"
    mail_text += "<div> " + row['explanation'] + " </div> "
    mail_text += "Permalink : " + row['url']
    update_cur.execute("update words set is_sent = 1 where url ='" +  row['url'] + "'")
    row = cur.fetchone()
conn.commit()
conn.close()
msg = MIMEMultipart() 
msg['Subject'] = "Todays words to learn from padakali.com"
msg['From'] = gmail_user
msg['To'] = to
part = MIMEText(mail_text.encode('utf-8'), 'html', _charset='utf-8')
msg.attach(part)
smtpserver.sendmail(gmail_user, to, msg.as_string())
print 'done!'
smtpserver.close()
