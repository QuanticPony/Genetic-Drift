import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as Animation
from random import random

N_INDVIDUALS = 20
BINS = 10
HISTOGRAM = True

def check_if_homogeneus(array):
    sum_ = array.sum()
    return sum_==array.size or sum_==0

    
class Alelos:
    def __init__(self, n_individuals, initial_alelos_frecuency, fig, ax) -> None:
        self.n_individuals = n_individuals
        self.initial_alelos_frecuency = initial_alelos_frecuency
        self.fig = fig
        self.ax = ax
        
        self.time = 0
        self.simulation_count = 0
        
        self.individuals = np.zeros((n_individuals, 2), np.int8)
        self._individuals = np.zeros((n_individuals, 2), np.int8)
        self.prepare_individuals()

        if HISTOGRAM:
            self.saved_time_lasted = np.zeros((BINS, 2))
        
        self.prepare_canvas()
        
    def initial_frecuency_to_index(self, x):
        y = int(np.floor(x*BINS))
        return y if y!=BINS else BINS-1
    
    def prepare_individuals(self):
        if HISTOGRAM:
            self.initial_alelos_frecuency = random()
        
        for i in range(self.n_individuals):
            for j in range(2):
                self.individuals[i,j] = 1 if random()<self.initial_alelos_frecuency else 0
                
        if HISTOGRAM:
            self.index = self.initial_frecuency_to_index(self.individuals.sum()/(2*self.n_individuals))
    
    
    def prepare_canvas(self):
        if HISTOGRAM:
            self.ax.set_title('Alelos\n')
            self.ax.set_ylabel('Tiempo medio')
            self.ax.set_xlabel('Frecuencia de alelos inicial')
            self.animation = Animation.FuncAnimation(fig, self.__call__, interval=1)
        else:
            self.ax.set_title('Alelos\n')
            self.ax.set_xlabel('Tiempo medio')
            self.ax.set_ylabel('Frecuencia de alelos inicial')
            self.animation = Animation.FuncAnimation(fig, self.__call__, interval=50)

    def __call__(self, *args, **kwds):
        if HISTOGRAM:
            while not check_if_homogeneus(self.individuals):
                parents = np.random.randint(self.n_individuals, size=(self.n_individuals, 2))
                choices = np.random.randint(2, size=(self.n_individuals, 2))

                for i in range(self.n_individuals):
                    self._individuals[i,:] = np.array([self.individuals[parents[i,l]][choices[i,l]] for l in range(2)])

                self.individuals = self._individuals.copy()


                # self.ax.plot(self.time, self.individuals.sum()/(2*N_INDVIDUALS), '.', color='red')
                # self.ax.set_ylim(0, 1)
                self.time += 1

            self.simulation_over()
            
        else:
            if not check_if_homogeneus(self.individuals):
                parents = np.random.randint(self.n_individuals, size=(self.n_individuals, 2))
                choices = np.random.randint(2, size=(self.n_individuals, 2))

                for i in range(self.n_individuals):
                    self._individuals[i,:] = np.array([self.individuals[parents[i,l]][choices[i,l]] for l in range(2)])

                self.individuals = self._individuals.copy()
                
                self.ax.plot(self.time, self.individuals.sum()/(2*N_INDVIDUALS), '.', color='red')
                self.ax.set_ylim(0, 1)
                self.time += 1
            else:
                self.simulation_over()
            
        
    def simulation_over(self):
        self.simulation_count += 1
        
        if HISTOGRAM:
            self.saved_time_lasted[self.index][0] += self.time
            self.saved_time_lasted[self.index][1] += 1
            
            a = np.arange(0,1,step=1/BINS)
            b = (self.saved_time_lasted[:,0]/self.saved_time_lasted[:,1])
            
            self.ax.clear()
            self.ax.bar(a, b, 
                    width=1/BINS, align='edge')
            self.ax.set_xlim(0, 1)
        else:
            self.animation.pause()
            end = self.ax.text(0.5, 0.5, 'SIMULATION OVER, RESTARTING...', horizontalalignment='center', verticalalignment='center', transform=self.ax.transAxes, size=25, color='red')
            plt.pause(1)
            end.remove()
        
        self.time = 0
        self.ax.set_title('Alelos\n' + f'Current simulations: {self.simulation_count}')
        self.prepare_individuals()
        
        if not HISTOGRAM:
            self.animation.resume()
    
if __name__=='__main__':
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    alelos = Alelos(N_INDVIDUALS, 0.5, fig, ax)
    plt.show()