#!/usr/bin/env python
# coding: utf-8

# # 環境構築
# 
# ## シェル
# プログラミング自体には必須ではないが、環境構築で使うことがある。  
# シェルとはOSのカーネルを操作するソフトウェア。  
# シェルの入出力を表示するターミナルというソフトウェアを用いて操作する。  
# シェルにはいくつか種類があるが、環境構築の範囲であれば、標準のもので大丈夫。  
#   
# ## プログラミング言語
# 基本的にはどの言語でもできることは同じなので、
# 学習の範囲では、やりたい分野のサンプルが多いものを学べばいい。  
# 将来的には、ライブラリの充実度や計算速度も重要。
# 機械学習や量子コンピューティングの分野ではpythonのライブラリが充実している。
# 
# プログラミング学習で基本的に覚えること  
# ・変数の操作  
# ・for文による繰り返し  
# ・if文による分岐  
# ・配列、行列、辞書による操作の簡易化  
# ・関数による操作の再利用  
# ・クラスによる変数・関数の再利用  
#   
# ## 仮想環境
# プログラミング言語やライブラリの複数バージョンの切り替えや管理のために、  
# 仮想環境を構築すると再現性が高くなる。  
# プログラミング言語のバージョン管理とライブラリのバージョン管理を、  
# 別々の環境構築ライブラリで管理する場合と、同じ環境構築ライブラリで管理する場合がある、  
# 
# pythonは複数のバージョンをインストールでき、  
# 標準の仮想環境作成ライブラリvenvでpythonバージョンを指定できるので、
# 計算に使用する範囲では標準のvenvで十分な場合が多い。
# 
# ## Git  
# コードの履歴を管理できる  
# オンライン上に保管できるサービスとしてGithubが有名。  
#   
# ## IDE (Integrated Development Environment)
# 開発に必要な複数のソフトウェアをまとめたソフトウェア。  
# ・jupyter notebook
# ・VSCODE  
#   
# ## macでのpython開発環境構築例
# 
# インストール用のソフトウェアHOMEBREWのインストール  
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"  
#   
# python3のインストール  
# brew install python  
#   
# python3インストール場所確認  
# which python3  
#   
# python3バージョンの確認  
# python3 --version  
#   
# pip（pythonライブラリインストール用のライブラリ）のアップグレード  
# python3 -m pip install --upgrade pip  
#   
# Gitのインストール  
# brew install git  
#   
# Gitのインストール場所確認  
# which git  
#   
# Gitのバージョン確認  
# git --version  
#   
# Gitの設定  
# git config --global user.name value  
# git config --global user.email value  
#   
# Gitの設定確認  
# git config --global user.name xxx    
# git config --global user.email xxx@xxx.xxx  
#   
# venvで仮想環境を作成する  
# python3.10 -m venv .**** (例：.venv)  
#   
# 仮想環境を確認する  
# ls -a  
#   
# 仮想環境の中を確認する  
# ls .venv  
# ls .venv/bin  
#   
# 仮想環境を反映する  
# source .venv/bin/activate  
#   
# 仮想環境から出る  
# deactivate  
#   
# 仮想環境を消す  
# rm -rf .venv  
#   
# ライブラリの出力  
# pip3 freeze > requirements.txt  
#   
# ライブラリ出力リストをインストール  
# pip3 install -r requirements.txt  
#   
# notebook（ブラウザ上で実行できるIDE）  
# python3 -m pip install jupyter  
#   
# notebookの実行  
# python3 -m notebook  
#   
# VS codeのpython設定（インストールはHP）  
# setting > command palette > python select interpreter >  
#   
# VS codeの設定確認  
# VS code > terminal > which python  
# VS code > terminal > python --version  
# VS code > terminal > pip --version  
#   
# VS codeのエディタ設定  
# setting > command palette > python linting enabled  
# setting > command palette > python linting flake8  
#   
# VS code で git clone  
# setting > command palette > git clone  
# 
# Jupyter Book インストール
# pip3 install -U jupyter-book
# 
# Jupyter Book インストールの作成
# jb create test_book
# 
# Jupyter Book のビルド
# cd test_book
# jb build .
# _config.yml>execute_notebooks>"off"
# jb build --all .

# 
