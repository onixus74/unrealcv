from test_common import *
import time


def MessageHandler(message):
    print message

if __name__ == '__main__':
    client = Client((HOST, PORT), MessageHandler)
    # Do connect automatically
    for i in range(100):
        response = client.request('vget /mode')
        # Need to lock until I got a reply
        # print reply
        time.sleep(1)
