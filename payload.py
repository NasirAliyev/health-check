from datetime import datetime


def payload(url: str, page: str, status_code: int, level: str = 'error'):
    return {
        "url": url,
        "page": page,
        "status_code": status_code,
        "level": level,
        "timestamp": str(datetime.now())
    }
