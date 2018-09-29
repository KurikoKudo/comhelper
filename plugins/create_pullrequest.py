# cording: utf-8

import subprocess


def create_pullrequest(pr_title):
    git_cmd = "hub pull-request -m " + pr_title
    git_cmd_return = subprocess.call(git_cmd.split())

    if git_cmd_return != 0:
        return 'hub pull-request -m の実行でエラーが発生しました。'
    else:
        return git_cmd_return
