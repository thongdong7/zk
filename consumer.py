import logging
from time import sleep

from client import ClientCommandHandler

__author__ = 'hiepsimu'
from kazoo.client import KazooClient

logging.basicConfig(level=logging.DEBUG)

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

cmd_path = '/client'

client_path = '/info'
client_name = 'server-01'

client_full_path = client_path + '/' + client_name

ClientCommandHandler(zk, cmd_path, client_path, client_name)
# event = zk.get_children('/client', watch=my_listener)
# print 'event', event
# my_listener(event)

while True:
    sleep(1000)
