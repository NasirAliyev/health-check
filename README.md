# Simple health checker
It is a simple health checker script. For making it working on *NIX systems please follow all steps below.

## Python and requirements
- Ensure python3 has been installed on the system. `python3 --version`
- Install pip using those commands (more: https://pip.pypa.io/en/stable/installing/):
````shell script
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
````
- Use the following command to check whether pip is installed: `python3 -m pip --version`
- And finally run this command in order to install required packages: `python3 -m pip install -r requirements.txt`

## Preparing app
- Create some directory for your script. E.g: `mkdir /var/www/`
- Download/Clone project to the directory. E.g: `health-check`
- Create new .env file from .env.example and set variables e.g:
````dotenv
ALARM_URL=https://events.pagerduty.com/x-ere/REWWTSDFSFSGTH34535SDFDSF435
BASE_URL=https://google.com
````
- Add all pages to the pages.py. E.g: `{'name': 'index', 'uri': '/error'},`

## Setting cron for scheduling health checks
- Create log folder for cron `mkdir /var/log/cron`
- Copy `clean.sh` to the created directory.
- Set execution permission for root user `chmod 700 /var/log/cron/clean.sh`
- Run   `crontab -e`
- Set following commands inside:
````text
*/3 * * * * python3 /var/www/health-check/index.py > /var/log/cron/$(date +\%Y-\%m-\%d_\%H:\%M)-cron.log 2>&1
0 1 * * * /var/log/cron/clean.sh
````

### All are done!
- The script will be run every 3 minutes and will log output to the files with format: `2021-03-02_21:33-cron.log`
- All logs older than 2 days will be deleted automatically by `clean.sh`
 