from datetime import datetime, timedelta


def calc_thresh_date():
    return (datetime.today() - timedelta(days=3)).date()

thresh_date = calc_thresh_date()

def check_for_rss(page):
    title = page["title"]
    date = page["date"]
    if date >= thresh_date:
        print(title, type(date))