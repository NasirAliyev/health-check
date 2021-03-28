from dotenv import load_dotenv
import requests

from configs import BASE_URL, ALARM_URL
from pages import pages
from payload import payload

load_dotenv()


def check():
    for page in pages():
        try:
            url = BASE_URL + page['uri']
            data = requests.get(url)
            status_code = data.status_code

            if 199 < status_code < 300:
                msg = '`{}` page is OK'.format(page['name'])
            else:
                level = get_error_level(status_code)
                json = payload(url=url, page=page['name'], status_code=status_code, level=level)
                requests.post(ALARM_URL, json=json)
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
