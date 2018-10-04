# cording: utf-8

import subprocess


def create_pullrequest(pr_title):

    git_cmd = "hub pull-request -m " + pr_title

    try:
        git_cmd_return = subprocess.check_output(git_cmd.split())
    except subprocess.CalledProcessError as e:
        return 'hub pull-request -m の実行でエラーが発生しました。'

    return git_cmd_return
