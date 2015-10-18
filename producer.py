import logging

__author__ = 'hiepsimu'
from kazoo.client import KazooState, KazooClient

logging.basicConfig(level=logging.DEBUG)

def my_listener(state):
    if state == KazooState.LOST:
        # Register somewhere that the session was lost
        print 'lost'
    elif state == KazooState.SUSPENDED:
        # Handle being disconnected from Zookeeper
        print 'suspend'
    else:
        # Handle being connected/reconnected to Zookeeper
        print 'connected/reconnected'


zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

zk.add_listener(my_listener)

zk.create('/client/cmd', 'cd /home/hiepsimu', sequence=True, makepath=True)
