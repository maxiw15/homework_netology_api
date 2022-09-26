import requests
from pprint import pprint
import os
from my_token import TOKEN


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
        headers = headers = {"Authorization": TOKEN}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, "rb"))
        response.raise_for_status()


ya = YandexDisk(token=TOKEN)
ya.upload_file_to_disk("netology/response.txt", "response.txt")

