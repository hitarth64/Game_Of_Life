#Game of life implementation with periodic boundaries or wrapped up boundaries
#Hitarth Choubisa

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.ndimage import convolve

length_of_grid = 5 #assuming a rectangular grid
width_of_grid = 5

class Game_Of_Life():

    def __init__(self, width, length, p=0.7):
        self.width = width
        self.length = length
        self.state = np.zeros((length,width))
        self.initial_distribution(1,length,width,p)
        self.im = plt.imshow(self.state)
        
    def initial_distribution(self,choice,length,width,p):
        if choice==0:
            self.state[1,2]=1;
            self.state[2,2]=1;
            self.state[3,2]=1;
        else:
            self.state = np.random.choice(a=[1, 0], size=(length,width), p=[p, 1 - p])
    
    
    def start(self):
        self.plot()
        self.ani= FuncAnimation(plt.gcf(), self.evolution, repeat=False, interval=500 )
        plt.show()

    def evolution(self, n):
        KERNEL = np.array([[1, 1, 1],[1, 0, 1],[1, 1, 1]])
        c = convolve(self.state, KERNEL, mode='wrap')        
        new = np.zeros_like(self.state)
        new[c == 3] = 1
        new[c < 2] = 0
        new[c > 3] = 0
        new[(self.state == 1) & (c == 2)] = 1
        self.state = new
        self.plot()


    def plot(self):
        self.im.set_data(self.state)

gol = Game_Of_Life(width=100,length=100)
gol.start()
