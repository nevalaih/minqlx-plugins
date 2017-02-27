# Created by naa on 27/02/2017 - naa@naa.fi
#
# Modified from autorestart.py plugin created by Thomas Jones
# https://github.com/tjone270/Quake-Live/blob/master/minqlx-plugins/autorestart.py
#
# rebootnotifier.py, a plugin for minqlx to inform all players on server that the underlying (Linux) server will reboot at a certain time.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS

"""
    You'll need to install the schedule library. 
    Enter the following command at your terminal to install: sudo python3.5 -m pip install schedule
    Times are specified in 24-hour time syntax, 13:00 for 1:00pm, 23:00 for 11:00pm, 02:00 for 2:00am etc.
    Check server time with "date" and adjust accordingly.

"""

import minqlx, time

try:
    import schedule
except ImportError:
    minqlx.CHAT_CHANNEL.reply("^1Error:^7 The ^4schedule^7 python library isn't installed.")
    minqlx.CHAT_CHANNEL.reply("^1Error:^7 Run the following on your server to install (in qlds dir): ^2sudo python3.5 -m pip install schedule^7")
    raise ImportError

class rebootnotifier(minqlx.Plugin):
    def __init__(self):
        self.set_cvar_once("qlx_rebootTime", "05:00") # set 5mins earlier than cron job
        self.initialize()
               
    def initialize(self):
        schedule.every().day.at(self.get_cvar("qlx_rebootTime")).do(self.reboot_notification)

        @minqlx.thread
        def loop():
            while True:
                schedule.run_pending()
                time.sleep(1)
        loop()
            
    def reboot_notification(self):
        self.center_print("^1SERVER REBOOT IN 5 MINUTES")