#!/usr/bin/env python
# coding: utf-8

# ### Map
# ここでは迷路に必要な地図を生成するためのプログラムを記述しています．

# ### インポートするモジュール
# 地図を表示したり，前の地図を消すために必要なdisplay, clear_outputと地図の表示を行うmatplotlib，数値計算を高速化するnumpyをインポートしています．

# In[ ]:


from ipywidgets import FloatProgress
from IPython.display import display, clear_output
import numpy as np
import matplotlib.pyplot as plt


# ### 地図の生成
# 
# -----
# * 迷路の表示　35-54行目\
# ここでは主にMatplotlibを利用し迷路を表示しています．36-38行目では迷路を生成する配列のサイズからマス目の数を計算し縦横に線を引いています．\
# 39-50行目では各マスのうち，壁，スタート地点，ゴール地点，自己位置を塗る処理をしています．

# In[ ]:


class Map(object):
    ###インスタンス化
    def __init__(self):
        self.init_pos = [1,1]#スタートの設定
        self.goal_pos = [10,10]#ゴールの設定
        self.map = np.random.randint(0,101,(12,12))#迷路生成用配列の生成
        self.size = self.map.shape[0]#迷路サイズの計算

        #壁のしきい値決定
        #1から100までの数字を,しきい値を決めて壁となにもない空間に分ける
        for i in range (self.size):
            for j in range (self.size):
                if self.map[i][j] <= 30:#配列内の数字が30以内で壁
                    self.map[i][j] = 0
                else :　　　　　　　　　#それ以外はなにもないマス
                    self.map[i][j] = 1
　　　　#迷路の四辺を壁で囲う
        for i in range (self.size):
            for j in range (self.size):
                if i == 11 or j == 11 or i == 0 or j == 0:#四辺は配列の0番目か11番目なので,その行と列をすべて壁にする
                    self.map[i][j] = 0
        #スタート、ゴールを壁にしない
        self.init_pos = [1,1]
        self.goal_pos = [10,10]
        #スタートとゴールを別途設定する
        self.map[11-self.init_pos[0]][self.init_pos[1]] = 2
        self.map[11-self.goal_pos[0]][self.goal_pos[1]] = 3
        #描画のための処理
        plt.ion()
        self.fig = plt.figure(figsize=(7,7))
        self.ax = self.fig.add_subplot(111)
　
　　###当たり判定
    def chack_movable(self,pos):
        #上下左右に移動可能か調べる
        #壁は0で表現されるので,falseが返ってきたら壁
        up    = bool(self.map[11-pos[1]-1][pos[0]])
        down  = bool(self.map[11-pos[1]+1][pos[0]])
        right = bool(self.map[11-pos[1]][pos[0]+1])
        left  = bool(self.map[11-pos[1]][pos[0]-1])

        return([up,down,right,left])

    ###迷路の描画
    def plot(self,pos=[1,1],q_table=[]):
        #迷路のマス目をカウント
        gpoint = np.arange(0, self.size, 1)
        #マス目の分だけ縦横に線を引く
        plt.vlines(gpoint, 0, self.size, linewidth=0.3, colors="k")
        plt.hlines(gpoint, 0, self.size, linewidth=0.3, colors="k")
        plt.xlim(0, self.size)
        plt.ylim(0, self.size)
        #配列を1つ1つ確認しマス目に色を塗る
        for i in range (self.size):
            for j in range (self.size):
                if self.map[11-j][i] == 0:#壁に色を塗る
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "k", alpha=0.9)
                elif self.map[11-j][i] == 2:#スタートに色を塗る
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "g", alpha=0.5)
                elif self.map[11-j][i] == 3:#ゴールに色を塗る
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "b", alpha=0.5)
                else:
                    pass
        #自己位置に色を塗る
        plt.axvspan(xmin=pos[0], xmax=pos[0]+1, ymin=pos[1]/self.size, ymax=(pos[1]+1)/self.size,                    color = "r", alpha=0.5)
        #迷路描画の更新
        clear_output(wait = True)
        plt.plot()
        display(self.fig)
        self.ax.cla()#次の更新のため描いたものを消す

if __name__ == "__main__":
    Map().plot()

