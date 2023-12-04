import tkinter as tk
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 


data = {'time': [], 'distance' : [], 'acceleration': [], 'velocity': []}

class Varibels():
  def ___init___(self):
    pass

dataframe = pd.DataFrame(data)
main_window = tk.Tk()

figure = plt.Figure(figsize=(5,5), dpi=100)
figure_plot = figure.add.subplot(5,5,5)
figure_plot.set_ylabel('distance')
line_graph = FigureCanvasTkAgg(figure, main_window)
line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
dataframe = dataframe[[]].groupby('time').sum()
dataframe.plot(kind='line', legend=True, ax=figure_plot, color='r', marker='0', fontsize='10')
figure_plot.set_title('Distance over time')
main_window.mainloop()
