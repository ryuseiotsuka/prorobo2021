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
# -----
# * インスタンス化　1-27行目\
# 3-6行目ではクラスのインスタンス化とスタートとゴールの座標，迷路となる配列の生成，マップサイズの計算を行っています．\
# 参考のプログラムと異なる点は，地図となる配列の生成をランダムにしたところです．迷路のもととなる12×12の配列の各要素に0以上101未満の100種類の数字をランダム割り当てるようにしました．\
# 8-18行目では迷路を生成するための配列の各要素のどこが壁でどこがなにもない空間かを決めるためのしきい値を設定し、それに応じて配列を変えています．\
# 16-19行目では迷路の四辺が壁で囲まれるようにするための処理を行っています．迷路の四辺は必ず配列の0番目または11番目なのでこれを用いて条件分岐を行っています．
# 21-26行目ではスタート地点とゴール地点の設定と，それぞれが壁に埋まらないように処理を行っています．また，迷路の表示サイズの設定を行っています．
# 
# -----
# * 当たり判定　28-33行目\
# ここでは上下左右に移動可能かをboolで判断しています．壁があるところの配列が0となっているためFaithが返ってくるとそこに行くことができないと判断します．
# 
# -----
# * 迷路の表示　35-54行目\
# ここでは主にMatplotlibを利用し迷路を表示しています．36-38行目では迷路を生成する配列のサイズからマス目の数を計算し縦横に線を引いています．\
# 39-50行目では各マスのうち，壁，スタート地点，ゴール地点，自己位置を塗る処理をしています．

# In[ ]:


class Map(object):
    def __init__(self):
        self.init_pos = [1,1]
        self.goal_pos = [10,10]
        self.map = np.random.randint(0,101,(12,12))
        self.size = self.map.shape[0]

        #壁のしきい値設定
        for i in range (self.size):
            for j in range (self.size):
                if self.map[i][j] <= 30:
                    self.map[i][j] = 0
                else :
                    self.map[i][j] = 1

        for i in range (self.size):
            for j in range (self.size):
                if i == 11 or j == 11 or i == 0 or j == 0:
                    self.map[i][j] = 0
        #スタート、ゴールを壁にしない
        self.init_pos = [1,1]
        self.goal_pos = [10,10]
        self.map[11-self.init_pos[0]][self.init_pos[1]] = 2
        self.map[11-self.goal_pos[0]][self.goal_pos[1]] = 3
        plt.ion()
        self.fig = plt.figure(figsize=(7,7))
        self.ax = self.fig.add_subplot(111)

    def chack_movable(self,pos):
        up    = bool(self.map[11-pos[1]-1][pos[0]])
        down  = bool(self.map[11-pos[1]+1][pos[0]])
        right = bool(self.map[11-pos[1]][pos[0]+1])
        left  = bool(self.map[11-pos[1]][pos[0]-1])

        return([up,down,right,left])

    def plot(self,pos=[1,1],q_table=[]):
        gpoint = np.arange(0, self.size, 1)
        plt.vlines(gpoint, 0, self.size, linewidth=0.3, colors="k")
        plt.hlines(gpoint, 0, self.size, linewidth=0.3, colors="k")
        plt.xlim(0, self.size)
        plt.ylim(0, self.size)
        for i in range (self.size):
            for j in range (self.size):
                if self.map[11-j][i] == 0:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "k", alpha=0.9)
                elif self.map[11-j][i] == 2:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "g", alpha=0.5)
                elif self.map[11-j][i] == 3:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "b", alpha=0.5)
                else:
                    pass
        plt.axvspan(xmin=pos[0], xmax=pos[0]+1, ymin=pos[1]/self.size, ymax=(pos[1]+1)/self.size,                    color = "r", alpha=0.5)
        clear_output(wait = True)
        plt.plot()
        display(self.fig)
        self.ax.cla()

if __name__ == "__main__":
    Map().plot()

