# cording: utf-8

import subprocess
import requests

from ..slackbot_settings import API_TOKEN


def download(channel, doc_name):
    git_cmd = "git pull origin master"
    git_cmd_return = subprocess.call(git_cmd.split())

    doc_path = 'docs/' + doc_name + '.md'

    if git_cmd_return != 0:
        return 'git pull origin master の実行でエラーが発生しました。'
    else:

        files = {'file': open(doc_path, 'rb')}
        param = {
            'token': API_TOKEN,
            'channels': channel,
        }
        requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
