# cording: utf-8

import subprocess


def createIssue():
    git_cmd = "git create issue -m '任意のissueタイトル'"
    git_cmd_return = subprocess.call(git_cmd.split())

    if git_cmd_return != 0:
        return 'git create issue -m の実行でエラーが発生しました。'
    else:
        return 'issueリンク'