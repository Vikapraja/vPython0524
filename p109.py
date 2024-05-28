import schedule #For automation
import time

def job():
    print("I'm working.....")
schedule.every().day.at("14:25").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
