import os
import spotipy
import sys

scope = 'playlist-read-private playlist-modify-private playlist-modify-public'
token = os.environ['spotify_token']
spotify_user = os.environ['spotify_user']
playlist_id = os.environ['playlist_id']


def add_track(event, context):
    track_data = event.get('Records')[0].get('Sns').get('Message')
    sp = spotipy.Spotify(auth=token)
    print('Searching for matches for ', track_data)
    # get first matching track
    track = sp.search(track_data, limit=1, type='track')
    if track.get('tracks').get('total') > 0:
        track_id = track.get('tracks').get('items')[0].get('id')
        # add track
        result = sp.user_playlist_add_tracks(spotify_user,
                                             playlist_id=playlist_id,
                                             tracks=[track_id])
        print('result:', result)
    else:
        print('No matches for ', track_data)

if __name__ == "__main__":
    event = {'Records':
                 [{'Sns':
                      {'Message':sys.argv[1]}
                   }
                  ]
             }
    add_track(event=event, context=None)
