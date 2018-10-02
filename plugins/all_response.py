# coding: utf-8

from slackbot.bot import respond_to

from .download import download
from .create_issue import create_issue
from .discussion import discussion
from .create_pullrequest import create_pullrequest


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


@respond_to('の議論を開始')
def mention_func(message):
    """
    議論コマンド用メソッド
    """
    message.send('議論を開始してください')
    # TODO: 議論が開始されていない時はエラー
    # TODO: echo 'issue番号　任意の議論タイトル' > commit.txt

    discussion_title = message.body['text'].rstrip('の議論を開始')

    discussion(discussion_title)

    message.send('議論を終了するよ')
    # TODO: git commit --allow-empty -F commit.txt
