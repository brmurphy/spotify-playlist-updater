## Synopsis

Two scripts. One captures public traffic from Triton Digital, and fires off an AWS SNS message. The other listens for this SNS message, and adds the song to a Spotify playlist. I have this running as two AWS Lambda services.

## Motivation

I love Classic Rock. And was an avid radio listener. But then, thanks to MP3s, Netflix and Spotify, I realized I hate commercials. But this was a solvable problem.

## Installation

Requires Python 3.3 or later.

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Create a Spotify dev account, and create a Web Api project to support the [Authorization Code Flow](https://developer.spotify.com/web-api/authorization-guide/#authorization-code-flow).

Set the environment variable for your Spotify user

    export spotify_user="example.com"
    python token_grabber.py

Set all required environment variables, including the token from above, URL endpoint of your favorite radio station that is using Triton Digital to stream "on air now"

## AWS Setup

Create an AWS account

Create a User

Grant SNS and Lambda permissions

Create an SNS topic

Create two Lambda services

Package zips correctly and deliver

**TODO**: Terraform (most of) these steps.

## Testing

To see the latest track

    $ python track_grabber.py
    SURVIVOR EYE OF THE TIGER

To add the latest track

    $ python track_grabber.py | grep "The track" | awk -F":" '{print $2}' > python update_playlist.py

or

    $ python update_playlist.py "Led Zeppelin Tangerine"

## Contributors

I am interested in adding more URLs to the list of known Triton Digital stations.

## TODO

[Spotipy](https://github.com/plamere/spotipy) assumes this is running on a machine that can launch a web browser in order to grant user access.
This means that I have to run the token_grabber.py script locally every now and then in order to update the access token. I'm sure there is a way to read from the Spotipy cache file in Lambda, just haven't figured it out yet.

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.