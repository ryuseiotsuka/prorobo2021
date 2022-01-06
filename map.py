#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ipywidgets import FloatProgress
from IPython.display import display, clear_output


import numpy as np
import matplotlib.pyplot as plt

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

