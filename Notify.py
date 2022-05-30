from plyer import notification
from datetime import datetime
import time

task = input("Enter the task:")
print("Enter the 24 hrs format")
time = input("At what time should I Remind (hh:mm:ss:):")
time_ = now = datetime.now()

while True:
    current_time = datetime.now().strftime('%H:%M:%S')
    print(current_time)
    if current_time == str(time):
        notification.notify(title="Reminder", message=task)
        break
    else:
        continue