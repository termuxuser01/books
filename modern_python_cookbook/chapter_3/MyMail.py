import cmd
import shlex

EMAILS = [
    {'sender': 'author1@domain.com', 'subject': 'First email',
     'body': 'This is my first email'},
    {'sender': 'author2@domain.com', 'subject': 'Second email',
     'body': 'This is my second email'},
]

class MyMail(cmd.Cmd):
    intro = 'Simple mail client'
    prompt = 'mymail>'

    def __init__(self, *args, **kwargs):
        super(MyMail, self).__init__(*args, **kwargs)
        self.selected_email = None

    def do_list(self, line):
        """List emails currently in the inbox"""
        for i, email in enumerate(EMAILS):
            print('[{i}] From: {e[sender]} - {e[subject]}'.format(i=i, e=email))
    
    def do_read(self, emailnum):
        """read the nth email from the inbox"""
        try:
            idx = int(emailnum.strip())
        except:
            print('Invalid email index {}'.format(emailnum))
            return

        try:
            email = EMAILS[idx]
        except IndexError:
            print(f'Email index {idx} not found')
            return

        print('From: {e[sender]}\n'
              'Subject: {e[subject]}\n'
              '\n{e[body]}'.format(e=email))
        # Track the last read email as the selected one for reply.
        self.selected_email = idx

    def do_reply(self, message):
        """send an email to the author of the recieved email"""
        if self.selected_email is None:
            print('no email selected for reply')
            return

        email = EMAILS[self.selected_email]

        subject = input('type the subject of your email')
        message = input('type the message of your email')
        print('Replied to {} with: \nSubject: {}\nMessage:\n{}'.format(email[sender], subject, message))

    def do_send(self, arguments):
        """create a new email and send to recipient"""
        #split with shlex to allow spaces in message and subject
        args = shlex.split(arguments)
        if len(args) < 3:
            print('A message, recipient and subject are requiered')
            return

        recipient, subject, message = args[:3]
        if len(args) > 3:
            message += ' '.join(args[3:])

        print('Sending email {} to {}: {}'.format(subject, recipient, message))
                
    def complete_send(self, text, line, begidx, endidx):
        # Provide autocompletion of recipients for send command.
        return [e['sender'] for e in EMAILS if e['sender'].startswith(text)]

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    MyMail().cmdloop()


