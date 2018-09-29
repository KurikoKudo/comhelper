# coding: utf-8

from slackbot.bot import respond_to

from .download import download
from .create_issue import create_issue


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
    message.send('プルリクのリンクを返す')
    # TODO: git pull-request -m '任意のプルリクタイトル'


@respond_to('の議論を開始')
def mention_func(message):
    """
    議論開始コマンド用メソッド
    """
    message.send('議論を開始してください')
    # TODO: 議論が開始されていない時はエラー
    # TODO: echo 'issue番号　任意の議論タイトル' > commit.txt


@respond_to('議論を終了')
def mention_func(message):
    """
    議論終了コマンド用メソッド
    """
    message.send('議論を終了するよ')
    # TODO: git commit --allow-empty -F commit.txt
