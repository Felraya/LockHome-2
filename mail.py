import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#to accept less secure applications
#https://myaccount.google.com/lesssecureapps





#CONSTANTS
MY_ADDRESS = 'mylockhome@gmail.com'
PASSWORD = 'lockhome_85'


#VARIABLES
DEST_MAIL = 'adri85bernard@gmail.com'
MY_NAME = 'Adrien'



def read_template(filename):
    #Returns a Template object comprising the contents of the file specified by filename.
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_mail() :
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    
    msg = MIMEMultipart() # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=MY_NAME)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=DEST_MAIL
    msg['Subject']="Intrusion"
        
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
        
    # send the message via the server set up earlier.
    s.send_message(msg)
    print("mail send")
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
   

def main() :
	send_mail()



if __name__ == '__main__':
    main()

