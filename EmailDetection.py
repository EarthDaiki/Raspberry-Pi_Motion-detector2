from datetime import datetime
import time
import RPi.GPIO as GPIO
import smtplib
import ssl


INTERVAL = 1

SLEEPTIME = 3

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

port = 587  
smtp_server = "smtp-mail.outlook.com"
sender = "email"
recipient = "email"
sender_password = "password"

def email():
    message = """検出"""
    SSL_context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=SSL_context)
        server.login(sender, sender_password)
        server.sendmail(sender, recipient, message)


if __name__ == '__main__':
    try:
        print ("Running Stop：CTRL+C")
        cnt = 1
        while True:
            # sensor
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') +
                "：" + str("{0:05d}".format(cnt)) + "回目の人感知")
                
                email()
                
                cnt = cnt + 1
                time.sleep(SLEEPTIME)
            else:
                print(GPIO.input(GPIO_PIN))
                time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Stopping Running")
    finally:
        GPIO.cleanup()
        print("GPIO clean completed")