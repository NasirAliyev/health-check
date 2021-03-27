import requests

from pages import pages
from payload import payload


def check():
    alarm_url = 'https://events.pagerduty.com/x-ere/R018WTC0ITJUVR7I1OQQAHWKJ1ISX6X8'
    base_url = 'https://azerbaijan-is.com'

    for page in pages():
        try:
            url = base_url + page['uri']
            data = requests.get(url)
            status_code = data.status_code

            if 199 < status_code < 300:
                msg = '`{}` page is OK'.format(page['name'])
            else:
                level = get_error_level(status_code)
                requests.post(alarm_url, json=payload(url=url, page=page['name'], status_code=status_code, level=level))
                msg = '`{}` page is down. Status code: {}'.format(page['name'], status_code)

            print(msg)

        except Exception as e:
            print('Error occurred during making http request to `{}` page. Exception: {}'.format(page['name'], e))


def get_error_level(code: int):
    if 399 < code < 500:
        return 'error'
    if code > 499:
        return 'critical'
    return 'warning'


check()
