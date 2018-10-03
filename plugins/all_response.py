# coding: utf-8

from slackbot.bot import respond_to

from .download import download
from .create_issue import create_issue
from .discussion import discussion, loop, push_discussion
from .create_pullrequest import create_pullrequest
from .check_users import check_all_users_by_slack


@respond_to('を見せて')
def mention_func(message):
    """
    成果物ダウンロードコマンド用メソッド
    """
    doc_name = message.body['text'].rstrip('を見せて')
    download(message.channel, doc_name)

    message.send(doc_name + 'を投稿したよ')


@respond_to('のIssueを作成して')
def mention_func(message):
    """
    Issue作成コマンド用メソッド
    """
    issue_title = message.body['text'].rstrip('のIssueを作成して')

    issue_link = create_issue(issue_title)
    message.send(issue_link)


@respond_to('のプルリクを作成して')
def mention_func(message):
    """
    プルリクエスト作成コマンド用メソッド
    """
    pr_title = message.body['text'].rstrip('のプルリクを作成して')

    pr_link = create_pullrequest(pr_title)
    message.send(pr_link)


@respond_to('ユーザー情報を確認して')
def mention_func(message):
    """
    ユーザー情報確認コマンド用メソッド
    """
    users = check_all_users_by_slack()
    message.send(users)
    message.send('上記のメンバーでユーザー情報を更新したよ！')


@respond_to('の議論を開始')
def mention_func(message):
    """
    議論コマンド用メソッド
    """
    discussion_title = message.body['text'].rstrip('の議論を開始')
    discussion_process_ready = discussion(discussion_title)

    if discussion_process_ready:
        message.send('議論を開始してください！')
        loop_return = loop()

        message.send(loop_return)

        push_status = push_discussion()
        message.send(push_status)

    else:
        message.send('echo > commit.txt の実行でエラーが発生しました。')
