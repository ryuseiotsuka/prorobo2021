#!/usr/bin/env python
# coding: utf-8

# ### Agent
# ここでは学習対象の行動を反映するを記述しています．

# ### インポートするモジュール
# ここでは迷路部分を実装しているMapをインポートしています

# In[ ]:


import math
from map import Map 


# ### Agent　行動の反映
# ここではAgentがどのように行動するのか，周囲の情報をどのように得ているのかについて記述しています．
# 
# -----
# * 周囲の情報の獲得　26-37行目\
# ここでは学習を行う際に必要な自己位置の情報を得る部分について記述しています．
# 参考のプログラムと異なる点は，自己位置の周囲1マス分しか得ていない点とゴールまでの距離を点数化したものを情報として与えている点です．
# 私のプログラムでは自己位置の情報が限定されても学習を行うことができるようにしたかったため周囲1マス分，計8マスの情報だけを与えるようにしました．これは自分の位置から見て周囲1マスそれぞれに壁があるかどうかを見ることで実現しています．matplotlibの描画と地図を生成する配列の向きが異なる都合で，それぞれの位置を表す1番目の配列は11から引くようにしています．
# また，これに追加してゴールまでの距離を点数化し足し合わせています．これは三平方の定理によってゴールまでの距離を求めているのではなく，縦と横の距離が最大10であることを利用し，周囲1マスの情報と同じ変数内で距離を記述できるよう工夫しています．
# このStateが最大で25856となるため，Q-leaningのQ-tableの大きさが25856となっています．
# 
# -----
# 

# In[ ]:


class Agent(object):
    ###インスタンス化
    def __init__(self,init_pos = [1,1],goal_pos = [10,10]):#スタート・ゴールの座標を指定
        #最初の自己位置をスタートに合わせる
        self.pos = [init_pos[0], init_pos[1]]
        #ゴールの設定
        self.goal_pos = goal_pos
        #移動の種類（上下左右）の数
        self.action_space = 4
        self.done = False
        
    ###移動   
    def action(self,a,d):
        #各方向で移動するフラグと行く先に壁がないことを確認し自己位置の配列を移動
        if a == 0 and d[0]:
            self.pos[1] += 1
        elif a == 1 and d[1]:
            self.pos[1] -= 1
        elif a == 2 and d[2]:
            self.pos[0] += 1
        elif a == 3 and d[3]:
            self.pos[0] -= 1
        else:
            pass

    ###自己位置の情報の獲得    
    def get_state(self,_map):#周囲1マスの情報とゴールまでの距離を点数化したものを得る
        state = (self.goal_pos[0]-self.pos[0])*10+(self.goal_pos[1]-self.pos[1])*2**8+\#ゴールまでの距離
        2**7*bool(_map[11-self.pos[0]+1][self.pos[1]+1])+\#右上のマス
        2**6*bool(_map[11-self.pos[0]+0][self.pos[1]+1])+\#上のマス
        2**5*bool(_map[11-self.pos[0]-1][self.pos[1]+1])+\#左上のマス
        2**4*bool(_map[11-self.pos[0]-1][self.pos[1]+0])+\#左のマス
        2**3*bool(_map[11-self.pos[0]-1][self.pos[1]-1])+\#左下のマス
        2**2*bool(_map[11-self.pos[0]+0][self.pos[1]-1])+\#下のマス
        2**1*bool(_map[11-self.pos[0]+1][self.pos[1]-1])+\#右下のマス
        2**0*bool(_map[11-self.pos[0]+1][self.pos[1]+0])　#右のマス
        return state 

    ###ゴールの判定
    def check_done(self):#自己位置の縦と横がそれぞれゴールにあるかを確認
        if self.pos[0] == self.goal_pos[0] and self.pos[1] == self.goal_pos[1]:
            done = True
        else: done = False
        return done

