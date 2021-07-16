import smtplib
import os
from os.path import expanduser

#function that configures the user's gmail account with this script
def systemConfig():
    os.system("clear")
    mailadress = str(input("your gmail adress: "))
    pass_code = str(input("your pass code: "))
    
    checkEnvironVarExistence(mailadress, pass_code)
    

#fucntion checks if the users gmail is already configured
def checkEnvironVarExistence(mailadress, pass_code):
    home = expanduser("~")
    os.chdir(home)
    with open(".bash_profile", 'r') as variables:
        lines = variables.readlines()

    if not pass_code in lines:
        os.system(f'echo "export AUTO_MAIL_SENDER_ADRESS="{mailadress}""  >> .bash_profile')
        os.system(f'echo "export AUTO_MAIL_SENDER_PASS="{pass_code}""  >> .bash_profile')
        print("your gmail is configured")
        print("YOU HAVE TO RESTART YOUR COMPUTER BEFORE IT WILL WORK")
    else:
        print("This pass code has already been linked to the script")
        print("you can change the pass code in '~/.bash_profile'")
        print("if sending mail doesn't work you might want to try the help option in the home menu")

    returnHome()


#mainfunction that handles the automation of mail sending
def composeMails():
    os.system("clear")
    EMAIL = os.environ.get('AUTO_MAIL_SENDER_ADRESS')
    PASS_CODE = os.environ.get('AUTO_MAIL_SENDER_PASS')
    
    print("email process started.")
    print("You are currently here:")
    os.system("pwd")
    RECEIVERS = str(input("path of file with email adresses: "))
    AMOUNT = int(input("amount of mails each person will receive: "))
    SUBJECT = str(input("Subject:"))
    BODY_PATH = str(input("path of file with email body: "))
    print("sending...")
    
    
    with open(BODY_PATH, 'r') as body_content:
        CONTENT = body_content.readlines()
        BODY = ""
        for line in CONTENT:
            BODY += line

    with open(RECEIVERS, 'r') as f:
        RECEIVER_SET = f.readlines()
        for RECEIVER in RECEIVER_SET:
            i = 1
            while i <= AMOUNT:
                i+=1
                sendMails(EMAIL, PASS_CODE,SUBJECT, BODY, RECEIVER)
    f.close()
    print(f"Mails sent to {RECEIVER_SET}")
    returnHome()
    


#function that sends an email
def sendMails(EMAIL, PASS_CODE, SUBJECT, BODY, RECEIVER):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL, PASS_CODE)
        mail_content = f'Subject: {SUBJECT}\n\n{BODY}'
        smtp.sendmail(EMAIL, RECEIVER, mail_content)


def help():
    os.system("clear")
    print("CONFIGURATION HELP:")
    print("this script is made for mac and linux users")
    print("If you want to use this script you will have to connect your gmail account with it")
    print("You can do this by choosing the configure option")
    print("you will have to enter your gmail adress and your pass code")
    print("your passcode is not your password")
    print("you can get your passcode by going to your gmail account security settings")
    print("you will have to turn on 'Acces to less secure apps'")
    print("then you will have to go to 'App passwords' and generate your pass code")
    print("after configuring you will have to restart your computer")
    print()

    print("HOW DOES THE SCRIPT WORK:")
    print("after your gmail has been succesfully linked this script will automatically use your email adress to send emails")
    print("all you have to do is make two text files")
    print("one file that contains the email adresses of all the people you want to send a mail to (each email adress in the file must be on a separate line)")
    print("and one text file that contains the body of your mail")
    print("it's recommended to keep those files in the same directory as this script")
    print("the script will ask you for the path of both files and use the one file to send a variable amount of mails to every person who's email adress is in it")
    print("and it will use the other file as the content of the mail")
    returnHome()


#function that lets you return to the home menu
def returnHome():
    print()
    input("hit enter to go back to the home menu")
    main()


#function that defines the home menu
def main():
    
    os.system("clear")

    #let the user pick between configure and continue
    print("Link your gmail account with this script if this is the first time using it\nyou can do that by choosing the continue option\notherwise continue if you've already configured:")
    print()
    print("1) configure")
    print("2) continue")
    print("3) help")
    print("4) quit")
    user_input = int(input("Enter the number of your choice: "))

    #check the user's choice
    if user_input == 1:
        systemConfig()
    elif user_input == 2:
        composeMails()
    elif user_input == 3:
        help()
    elif user_input == 4:
        os.system("clear")
        os.system("echo script ended.")

main()
