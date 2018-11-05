# coding: utf-8

from slackbot.bot import respond_to
from requests import get

from .download import download
from .create_issue import create_issue
from .discussion import discussion, loop
from .create_pullrequest import create_pullrequest
from .check_users import check_all_users_by_slack
from .commit import commit
from slackbot_settings import USER_TOKEN, WORKING_DIRECTORY


@respond_to('を見せて')
def mention_download(message):
    """
    成果物ダウンロードコマンド用メソッド
    """
    doc_name = message.body['text'].rstrip('を見せて')
    download(message.channel, doc_name)

    message.send(doc_name + 'を投稿したよ')


@respond_to('のIssueを作成して')
def mention_issue(message):
    """
    Issue作成コマンド用メソッド
    """
    issue_title = message.body['text'].rstrip('のIssueを作成して')

    issue_link = create_issue(issue_title)
    message.send(issue_link)


@respond_to('のプルリクを作成して')
def mention_pr(message):
    """
    プルリクエスト作成コマンド用メソッド
    """
    pr_title = message.body['text'].rstrip('のプルリクを作成して')

    pr_link = create_pullrequest(pr_title)
    message.send(pr_link)


@respond_to('ユーザー情報を確認して')
def mention_user(message):
    """
    ユーザー情報確認コマンド用メソッド
    """
    users = check_all_users_by_slack()
    message.send(users)
    message.send('上記のメンバーでユーザー情報を更新したよ！')


@respond_to('の議論を開始して')
def mention_discussion(message):
    """
    議論コマンド用メソッド
    """
    discussion_title = message.body['text'].rstrip('の議論を開始')
    discussion_process_ready = discussion(discussion_title)

    if discussion_process_ready:
        message.send('議論を開始してください！')
        loop_return = loop()

        message.send(loop_return)

    else:
        message.send('すでに議論が開始されているようです...\n終了してから議論を行なってください！')


@respond_to('コミットして')
def mention_commit(message):
    """
    コミットコマンド用メソッド
    """
    message_body = message.body
    path = WORKING_DIRECTORY + '/docs/'

    if 'files' in message_body.keys():
        file_names = []
        for file in message_body['files']:
            file_names.append(file['name'])
            url_private = file['url_private']

            f = open(path + file['name'], mode='w', encoding='utf-8')
            resp = get(url_private, headers={'Authorization': 'Bearer %s' % USER_TOKEN}, stream=True)

            f.write(resp.text)

            f.close()

        for file_name in file_names:
            message.send(file_name)
        message.send('の編集をコミットします！')

    commit_return = commit()

    message.send(commit_return)









