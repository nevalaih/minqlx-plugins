# Created by naa on 17/07/2018
# This is a modified version of the original locations.py plugin by Thomas Jones.
# The old freegeoip API is now deprecated and was discontinued on July 1st, 2018
# This plugin uses the new endpoint at http://api.ipstack.com with the legacy attribute in use.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 40-44 and the !tomtec_versions / !naa_versions code.

#******************************************************************************************************************************
# Comments from original locations.py below this comment block will be retained in this plugin as a thank you to Thomas Jones *
#******************************************************************************************************************************

# Created by Thomas Jones on 22/12/2015 - thomas@tomtecsolutions.com
# locations.py, a plugin for minqlx to approximately geo-locate players.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

# This plugin uses the free Geo-IP API from http://freegeoip.net.

#***************************
# End of original comments *
#***************************

"""
The following cvars are used on this plugin:
    qlx_locationCommandPermissionRequired: Required permission level to run the !loc and !location commands. Default: 1
    qlx_locationApiKey: Required to use the api at ipstack.com. Register for a free account on https://ipstack.com to get your own api key. Default: none
"""

import minqlx
import requests
import json
import threading

class loc(minqlx.Plugin):
    def __init__(self):
        self.set_cvar_once("qlx_locationCommandPermissionRequired", "1")
        self.set_cvar_once("qlx_locationApiKey", "NONE")

        self.add_command(("loc", "location"), self.cmd_location, (self.get_cvar("qlx_locationCommandPermissionRequired", int)), usage="<id>")
        self.add_command("tomtec_versions", self.cmd_showversion)
        self.add_command("naa_versions", self.cmd_naaversion)

        self.plugin_version = "1.1"
        self.plugin_naaversion = "0.3"
        self.location_api_key = self.get_cvar("qlx_locationApiKey")

    @minqlx.thread
    def cmd_location(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.RET_USAGE

        try:
            player_ip = self.player(int(msg[1])).ip
            player_name = self.player(int(msg[1])).name
        except:
            channel.reply("^1Invalid Client ID.^7 Enter a valid client ID to see their approximate location.")
            return

        ipData = requests.get('http://api.ipstack.com/{}?access_key={}&output=json&legacy=1'.format(player_ip, self.location_api_key), stream=True)
        ipData = str(ipData.text)
        ipDataParsed = json.loads(ipData)

        channel.reply("{}^7's location: {}".format(player_name, ipDataParsed['country_name']))

        return minqlx.RET_STOP_ALL

    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4locations.py^7 - version {}, created by Thomas Jones on 22/01/2016.".format(self.plugin_version))

    def cmd_naaversion(self, player, msg, channel):
        channel.reply("loc.py - version {}, by naa on 17/07/2018 modified from locations.py (Thomas Jone)".format(self.plugin_naaversion))
