import requests

# make logger

class Entity:
    def __init__(self, id, title, artistName, linksByPlatform):
        self.id = id
        self.title = title
        self.artistName = artistName
        self.linksByPlatform = linksByPlatform
    
    @staticmethod
    def parse(rawEntity, linksByPlatform):
        links = {}
        for platform in rawEntity.get('platforms', []):
            links[platform] = linksByPlatform.get(platform, {}).get('url', '')
        return Entity(rawEntity.get('id', ''), rawEntity.get('title', ''), 
                      rawEntity.get('artistName', ''), links)
        
        
class EntityResult:
    def __init__(self, type, userCountry, pageUrl, entitiesByProvider):
        self.type = type
        self.userCountry = userCountry
        self.pageUrl = pageUrl
        self.entitiesByProvider = entitiesByProvider
    
    @staticmethod
    def parse(result):
        type = result.get('entitiesByUniqueId', {}).get(result.get('entityUniqueId', ''), {}).get('type', '')
        userCountry = result.get('userCountry', '')
        pageUrl = result.get('pageUrl', '')
        linksByPlatform = result.get('linksByPlatform', {})
        entitiesByProvider = {}
        for _,rawEntity in result.get('entitiesByUniqueId', {}).items():
            entity = Entity.parse(rawEntity, linksByPlatform)
            entitiesByProvider[rawEntity.get('apiProvider', '')] = entity
        return EntityResult(type, userCountry, pageUrl, entitiesByProvider)


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