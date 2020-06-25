import time
import os

from dotenv import load_dotenv
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

load_dotenv()
pnconfig = PNConfiguration()
pnconfig.subscribe_key = os.getenv("SUB_KEY")
pnconfig.publish_key = os.getenv("PUB_KEY")
pubnub = PubNub(pnconfig)

CHANNELS = {'TEST': 'TEST', 'BLOCK': 'BLOCK'}


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(
            f"\n-- Channel: {message_object.channel} | Message: {message_object.message}")


class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """

    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})


if __name__ == '__main__':
    main()
