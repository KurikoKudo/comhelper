# coding: utf-8

from slackbot.bot import respond_to

from .download import download


@respond_to('を見せて')
def mention_func(message):

    doc_name = message.body['text'].rstrip('を見せて')

    # print(message.channel)
    # print(doc_name)

    download(message.channel, doc_name)

    message.send('ファイルを投稿する')

    # TODO: 任意のファイルをslackに投稿
    # メッセージからファイル名とchannelを取得 -> RTMorEventsを使えばできそう


@respond_to('のIssueを作成して')
def mention_func(message):
    message.send('issue番号を返す')
    # TODO: メッセージからissueタイトルを取得


@respond_to('のプルリクを作成して')
def mention_func(message):
    message.send('プルリクのリンクを返す')
    # TODO: git pull-request -m '任意のプルリクタイトル'


@respond_to('の議論を開始')
def mention_func(message):
    message.send('議論を開始してください')
    # TODO: 議論が開始されていない時はエラー
    # TODO: echo 'issue番号　任意の議論タイトル' > commit.txt


@respond_to('議論を終了')
def mention_func(message):
    message.send('議論を終了するよ')
    # TODO: git commit --allow-empty -F commit.txt
