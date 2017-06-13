import os
import spotipy.util as util

scope = 'playlist-read-private playlist-modify-private playlist-modify-public'
spotify_user = os.environ['spotify_user']

token = util.prompt_for_user_token(spotify_user, scope)
print(token)
