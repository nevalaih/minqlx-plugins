# minqlx-plugins
This is a collection of my plugins for [minqlx](https://github.com/MinoMino/minqlx).

This repository only contains plugins created by me. Useful plugins, created by others can be found [here](https://github.com/MinoMino/minqlx/wiki/Useful-Plugins)

## Plugins
List of plugins and their cvars. Set the cvars by passing them as a command line argument (preferred method) or add them to `server.cfg`.

- **rebootnotifier**: Display a center print message to all players, that the server will reboot in 5 minutes. Actual server reboot done with a cron job.  

    - `qlx_rebootTime`: A string in 24-hours format (23:00, 05:00 etc) to set time when reboot message is displayed. Set to 5min before cron job.
        - Default: `04:55` (utc)
        - Cron job: `0 5 * * * /sbin/shutdown -r` (add cron job with `sudo crontab -e` or `crontab -e`)


 - **loc**: Display the location (country) of a player based on their IP. Also has the optional ability to change the players flag.

 	- `qlx_locationCommandPermissionRequired`: The required permission level to run the !loc and !location commands.
 		- Default: `1`

    - `qlx_locationApiKey`: API Access Key from ipstack.com. Register for a free key at [ipstack.com](https://ipstack.com).
        - Default: `NONE`
        - Note: Plugin doesn't work without this.
	
	- `qlx_locationChangePlayerFlag`: Int flag to indicate where to change the players flag that location is checked on.
		- Default: `0` (off)
