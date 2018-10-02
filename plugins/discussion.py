# cording: utf-8

import subprocess
import time
from slackbot.slackclient import SlackClient
from slackbot.dispatcher import MessageDispatcher


def discussion(discussion_title):
    cmd = 'echo ' + discussion_title + ' > commit.txt'

    try:
        cmd_return = subprocess.check_call(cmd.split())
    except subprocess.CalledProcessError as e:
        return 'echo > commit.txt の実行でエラーが発生しました。'

        # return cmd_return

        while True:
            events = SlackClient.rtm_read()
            time.sleep(1)




