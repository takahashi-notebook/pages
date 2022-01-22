#!/usr/bin/env python
# coding: utf-8

# # python開発環境
# 
# ## インストール用のソフトウェアHOMEBREW
# HOME BREWのインストール
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"  
#   
# バージョン確認  
# brew -v  
#   
# ## python3
# pythonのバージョン指定してインストール  
# brew install python@3.9  
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
# git config --global user.name "xxx"  
# git config --global user.email xxx@xxx.xxx  
#   
# Gitの設定確認  
# git config --list 
#   
# ## 仮想環境
# venvで仮想環境を作成する  
# python3.10 -m venv .**** (例：.venv)  
#   
# ## notebook
# notebookのインストール  
# python3 -m pip install jupyter  
#   
# ## VS codeのpython設定  
# VS codeのインストール  
# 解凍しアプリケーションフォルダに移動  
#   
# pythonのextensionをインストール
# Extensions >  Python
#   
# python3の場所を設定する  
# setting > command palette > python select interpreter >  
#   
# VS codeの設定確認  
# VS code > terminal > which python  
# VS code > terminal > python --version  
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
# Jupyter Bookの更新パッケージ  
# pip3 install ghp-import  

# 
