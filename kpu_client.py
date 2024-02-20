import json
import os
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

class KPUClient:
    def __init__(self):
        self.urls = []

        try:
            with open(f'urls.json', 'r') as f:
                for step, x in enumerate(f):
                    self.urls.append(x.strip())
        except OSError in e:
            print(f"Error reading urls.json = {e}")

    
    def collect_data(self, filename):
        retrieved_data = {}
        if os.path.exists(f"{filename}"):
            with open(f"{filename}", 'r') as f:
                for x in f:
                    x = json.loads(x)
                    retrieved_data[x['url']] = x
        
        with open(f"{filename}", 'w') as f:
            for url in self.urls:
                if 'url' in retrieved_data:
                    x = retrieved_data[url]
                else:
                    count_data = self._get_data(url)
                    x = {'url': url, 'data': count_data}
                f.write(f"{json.dumps(x)}\n")

    @retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential(multiplier=1, min=1, max=60)
    )
    def _get_data(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            return {}
        else:
            return response.json()


    def extract_image(self, url=None, target_path=None):
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        if url==None:
            urls = self.urls
        else:
            urls = [url]

        for url in urls:
            polling_station_code = url.split('/')[10].replace('.json', '')
            count_data = self._get_data(url)

            for step, image_url in enumerate(count_data['images']):
                if image_url is None:
                    continue
                image_file_name = f"{target_path}/{polling_station_code}_{step+1}.jpg"
                self._get_image(image_url, image_file_name)


    @retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential(multiplier=1, min=1, max=60)
    )
    def _get_image(self, url, filename):
        img_data = requests.get(url).content
        with open(f"{filename}", 'wb') as handler:
            handler.write(img_data)