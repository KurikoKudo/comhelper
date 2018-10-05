# ベースイメージの指定
FROM python:3.6-alpine

# ソースを置くディレクトリを変数として格納
ARG project_dir=/python_app/comhelper/

# 必要なファイルをローカルからコンテナにコピー
ADD . $project_dir
ADD requirements.txt $project_dir

# requirements.txtに記載されたパッケージをインストール
WORKDIR $project_dir
RUN pip3 install -r requirements.txt

# （コンテナ内で作業する場合）必要なパッケージをインストール
RUN apk update
RUN apk add zsh vim tmux git tig