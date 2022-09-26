import datetime
import requests
from my_token import TOKEN
import time


def most_clever():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url)
    answer = []
    for superheroes in resp.json():
        name = superheroes["name"]
        if name in ["Hulk", "Captain America", "Thanos"]:
            intelligence = superheroes["powerstats"]["intelligence"]
            answer.append({"name": name, "intelligence": intelligence})
    return max(answer, key=lambda row: row["intelligence"])


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_files_list(self):
        files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": TOKEN}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


def stackoverflow():
    url = "https://api.stackexchange.com/2.3/questions?"
    page = 1
    num = 0
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    while True:
        params = {"page": page, "pagesize": '100', 'fromdate': yesterday, "todate": today,
                  "sort": "activity", "tagged": "Python", "site": "stackoverflow"}
        resp = requests.get(url, params=params)
        if resp.json()["has_more"]:
            time.sleep(1)
            for item in resp.json()["items"]:
                num += 1
                print(f'Статья {item["title"]}, под номером {num}')
            page += 1
        else:
            break


ya = YandexDisk(token=TOKEN)
ya.upload_file_to_disk("netology/response.txt", "response.txt")
stackoverflow()
