import requests
from entityresult import EntityResult
        
class SongLink:
    def __init__(self, api_version='v1-alpha.1', key=None):
        self.base_url = 'https://api.song.link'
        self.api_version = api_version
        self.api_root =  f'{self.base_url}/{self.api_version}'
        self.endpoints = {'links': 'links'}
        self.key = key
    
    def _get(self, params):
        if self.key:
            params['key'] = self.key
        try:
            resultRequest = requests.get(f'{self.api_root}/{self.endpoints["links"]}', params=params)
            resultRequest.raise_for_status()
            result = resultRequest.json()
            return EntityResult.parse(result)
        except Exception as e:
            return None
    
    def getByUrl(self, url):
        return self._get({'url': url})