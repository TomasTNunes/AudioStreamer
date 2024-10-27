from entity import Entity

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