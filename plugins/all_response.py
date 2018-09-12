# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                            文字列中に':'はいらない


@respond_to('を見せて')
def mention_func(message):
    message.send('ファイルを投稿する')
    # TODO: git pull origin master
    # TODO: 任意のファイルをslackに投稿


@respond_to('のIssueを作成して')
def mention_func(message):
    message.send('issue番号を返す')
    # TODO: git create issue -m '任意のissueタイトル'


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
