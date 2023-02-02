from bs4 import BeautifulSoup
from urllib.parse import urlparse
from core import database
from core import logs
from models import urls
import requests
import csv
import datetime as dt


HEADERS = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}


def get_info_about_url(url: str) -> dict:
    result = dict()
    request = requests.get(url, timeout=2, headers=HEADERS)

    if request.history:
        result["final_url"] = request.url

    if request.ok:
        soup = BeautifulSoup(request.text, "html.parser")
        title = soup.title

        if title:
            result["page_title"] = soup.title.get_text()

    result.update(
        {
            "domain_name": urlparse(url).netloc,
            "status_code": request.status_code,
            "url": url,
        }
    )

    logs.log.info(f"parsed url: {result}")

    return result


def parse_urls() -> None:
    parsed_urls: list[urls.Urls] = []

    with open("urls.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for i, row in enumerate(reader, start=1):
            try:
                parsed_urls.append(
                    urls.Urls(
                        **{
                            **get_info_about_url(row["URL"]),
                            "visit_date": row["Datetime"],
                            "parse_date": dt.datetime.now(),
                        }
                    )
                )

                if i % 1000 == 0:
                    with database.SessionLocal.begin() as db:
                        db.add_all(parsed_urls)
                    parsed_urls.clear()
                    logs.log.info("committed last 1000 parsed urls")

            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.TooManyRedirects,
            ) as ex:
                logs.log.error(str(ex))
