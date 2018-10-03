# cording: utf-8

import subprocess
import time
import shlex

from slackbot.slackclient import SlackClient
from slackbot_settings import API_TOKEN
from .check_users import get_user_dict


def discussion(discussion_title):

    cmd = []
    cmd.append('echo "' + discussion_title + '" > commit.txt')

    try:
        cmd_return = subprocess.run(cmd, shell=True)
    except subprocess.SubprocessError as e:
        print("[Error] first echo command")
        return False

    return True


def loop():

    client = SlackClient(API_TOKEN)
    user_dict = get_user_dict()

    while True:
        events = SlackClient.rtm_read(client)

        for event in events:
            event_type = event.get('type')

            if event_type == 'message':
                message_text = event.get('text')

                if message_text == "議論を終了":
                    return '議論を終了しました！'
                else:
                    send_user_id = event.get('user')
                    send_user_name = user_dict[send_user_id]
                    add_commit_message = []
                    add_commit_message.append('echo "' + send_user_name + ': ' + message_text + '" >> commit.txt')
                    try:
                        cmd_return = subprocess.run(add_commit_message, shell=True)
                    except subprocess.SubprocessError as e:
                        return 'echo >> commit.txt の実行でエラーが発生しました。'

        time.sleep(1)


def push_discussion():
    git_add_cmd = 'git add --all'
    try:
        git_cmd_return = subprocess.run(shlex.split(git_add_cmd))
    except subprocess.CalledProcessError:
        return 'add コマンドでエラーが起きました'

    git_commit_cmd = 'git commit --allow-empty -F commit.txt'
    try:
        git_cmd_return = subprocess.run(shlex.split(git_commit_cmd))
    except subprocess.CalledProcessError:
        return 'commit コマンドでエラーが起きました'

    git_push_cmd = 'git push origin comhelper'
    try:
        git_cmd_return = subprocess.run(shlex.split(git_push_cmd))
    except subprocess.CalledProcessError:
        return 'push コマンドでエラーが起きました'

    return 'comhelper ブランチへの push が完了しました。'






