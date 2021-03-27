import requests
import logging

from pages import pages
from payload import payload

alarmUrl = 'https://events.pagerduty.com/x-ere/R018WTC0ITJUVR7I1OQQAHWKJ1ISX6X8'
baseUrl = 'https://azerbaijan-is.com'

for page in pages():
    try:
        url = baseUrl + page['uri']
        data = requests.get(url)
        status_code = data.status_code

        if 199 < status_code < 300:
            msg = '`' + page['name'] + '` page is OK'
            print(msg)
        elif 399 < status_code < 500:
            requests.post(alarmUrl, json=payload(url=url, page=page['name'], status_code=status_code))
        elif status_code > 499:
            requests.post(alarmUrl, json=payload(url=url, page=page['name'], status_code=status_code, level='critical'))
        else:
            requests.post(alarmUrl, json=payload(url=url, page=page['name'], status_code=status_code, level='warning'))

    except Exception as e:
        logging.error('Error during making http request occurred', extra={'error': e, 'name': page['name']})
