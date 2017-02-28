# minqlx-plugins
This is a collection of plugin for [minqlx](https://github.com/MinoMino/minqlx).

This repository only contains plugins created by me. Useful plugins, created by other can be found [here](https://github.com/MinoMino/minqlx/wiki/Useful-Plugins)

## Plugins
List of plugins and their cvars. Set the cvars by passing them as a command line argument (preferred method) or add them to `server.cfg`.

- **rebootnotifier**: Displays a center print message, that the server will reboot in 5 minutes. Currently this uses a cron job to do the actual reboot.  
    - `qlx_rebootTime`: A string in 24-hours format (23:00, 05:00 etc) to set time when reboot message is displayed. Set to 5min before cron job.
        - Default: `04:55` (utc)
        - Cron job: `0 5 * * * /sbin/shutdown -r` (add cron job with `sudo crontab -e` or `crontab -e`)
