##installing cron

- run "crontab -e"

Set following commands inside:
- */3 * * * * python3 /var/www/health-check/index.py > /var/log/cron/$(date +\%Y-\%m-\%d_\%H:\%M)-cron.log 2>&1
- 0 1 * * * /var/log/cron/clean.sh