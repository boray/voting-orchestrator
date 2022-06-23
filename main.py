import smtplib
import random
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'vote@buchain.org'
PASSWORD = 'password'

keys = []

def get_voters(filename):
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])
    return emails

def read_template(filename):
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    emails = get_voters('voters.txt') # read voter
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for  email in emails:

        randomGeneratedKey=random.randint(100000,999999)
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(VOTING_KEY=randomGeneratedKey)

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Your Voting Key - KEEP THIS KEY PRIVATE"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)

        keys.append(randomGeneratedKey)

        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    # Sort keylist in ascending order
    keys.sort()
    # Print keys for proof check
    print(keys)

if __name__ == '__main__':
    main()
