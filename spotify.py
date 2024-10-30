import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="1a62eb08efa54d41b2c86e867c6ecc93",
                                               client_secret="b3e1f1c81b884046af72bd17e797651b",
                                               redirect_uri="http://localhost:1234",
                                               scope="user-library-read"))

search = 'run'

results = sp.search(q=search, type='track', limit=2)

for item in results['tracks']['items']:
    artist_str = ''
    for artist in item['artists']:
        artist_str = artist_str + artist['name'] + ', '
    print(f'{item["name"]} - {artist_str}')

#print(results['tracks']['items'])

# for i in results:
#     print(results[i][''])