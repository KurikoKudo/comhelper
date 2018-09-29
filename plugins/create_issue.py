# cording: utf-8

import subprocess



def create_issue(issue_title):
    git_cmd = "hub issue create -m " + issue_title

    try:
        git_cmd_return = subprocess.check_output(git_cmd.split())
    except subprocess.CalledProcessError as e:
        return 'hub issue create -m の実行でエラーが発生しました。'

    return git_cmd_return
