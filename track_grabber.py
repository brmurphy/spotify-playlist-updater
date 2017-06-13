import boto3
import os
import requests
import xml.etree.ElementTree as ET

streaming_url = os.environ['streaming_url']
sns_topic = os.environ['sns_topic']


def push_data(event, context):
    rq = requests.get(streaming_url)
    if rq.status_code == 200:
        tree = ET.fromstring(rq.text)
        if len(tree) < 2:
            # bad data, nothing to do here
            return
        song = tree[0][1].text
        artist = tree[0][2].text
        short_track = '{} {}'.format(artist, song)
        print("The track:", short_track)

        sns_client = boto3.client('sns')
        resp = sns_client.publish(TopicArn=sns_topic,
                                  Message=short_track,
                                  Subject=short_track)
        print('result ', resp)


if __name__ == "__main__":
    push_data(None, None)