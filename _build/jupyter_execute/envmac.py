#!/usr/bin/env python
# coding: utf-8

# # macでのpython開発環境構築例
# 
# ## インストール用のソフトウェアHOMEBREW
# HOME BREWのインストール
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"  
#   
# ## python3
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
# ## Git
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
# ## 仮想環境
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
# ## notebook
# notebookのインストール  
# python3 -m pip install jupyter  
#   
# notebookの実行  
# python3 -m notebook  
#   
# ## VS codeのpython設定  
# python3の場所を設定する
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
# ## Jupyter Book
# Jupyter Bookのインストール  
# pip3 install -U jupyter-book  
#   
# Jupyter Book インストールの作成  
# jb create test_book  
#   
# Jupyter Book のビルド  
# cd test_book  
# jb build .  
# 
# Jupyter Bookのソースコードを更新する
# jb build --all .
# git checkout master
# git add .
# git commit -m "comment"
# git push origin master
# 
# GitHub Pagesを更新する
# cd test_book
# jb build --all .
# git checkout master
# ghp-import -n -p -f _build/html

# 
