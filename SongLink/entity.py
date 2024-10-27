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