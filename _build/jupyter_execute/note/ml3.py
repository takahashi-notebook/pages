#!/usr/bin/env python
# coding: utf-8

# # Natural Language Processing
# 
# Natural Language Processingの種類  
# ・シソーラス（上位・下位概念の辞書）  
# ・カウントベース  単語の類似性性をベクトルで表現する。単語数が多いと計算時間がかかる。オンライン学習できない。  
# ・推論ベース  ミニバッチで計算できるため、オンライン学習できる。  
# ・カウントベース  
# 
# ある単語の付近で使用される単語をカウントしてベクトル表示する  
# co-occurance matrix:  
# ある単語の付近で使用された単語の回数を表すの2次元行列（ベクトル表示を並べて行列表示したもの）    
#   
# Pointwise Mutual Information：  
# co-occurance matrixを同時に使用される確率に変更したもの  
#   
# Positive PMI :  
# 対数の発散対策のため、PMIで0以下を0としたもの  
# ppmi = max(0, PMI(x,y))   
# Singurar Value Decomposition  
# U, S, V = np.linalg.svd(W)  
# で変換したうちの最初の方を使用することで圧縮できる。  
# SVDの計算はO(N^3)  
# 高速化したtruncated SVD  
# 
# 手順  
# 文章から単語idとword変換辞書を作成する。  
# 文章を単語idの順に変換する。  
# co-occurence-matrixを作成する。  
# ppmiに変換する。  
# SVD変換する。  
# 
# ・推論ベース  word2vec  
# continuous bag-of-words  
# 2つの単語から挟まれる単語を推論する。入力層が2つ、出力層が１つ。  
# P(w_t|w_t-1,w_t+1)  
# L = -logP(w_t|w_t-1,w_t+1)  
# skip-gram  
# １つの単語から前後の単語を推測する。入力層が１つ、出力層が２つ  
# P(w_t-1,w_t+1|w_t)  
# L = -logP(w_t-1,w_t+1|w_t)  
#   = -logP(w_t-1|w_t)P(w_t+1|w_t)  
#   = -logP(w_t-1|w_t)-logP(w_t+1|w_t)
# 
# 計算の簡略化  
# ・Embedding  
# 入力が単語idを表すone-hotの場合、ある列を指定して抜き取れば、最初の層は行列計算する必要がない。  
# ・negative sampling  
# 単語idの数に伴い行列の大きさ増えないように、正解とコーパスの頻度に応じたサンプルされた複数の不正解で計算する。  

# 

# 
