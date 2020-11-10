from bokeh.io import output_file, show
from bokeh.plotting import figure
import numpy as np

x = np.linspace(0,10,1000)
y = np.sin(x)

plot = figure(plot_height=300, plot_width=600)
plot.line(x,y)

output_file('numpy.html')
show(plot)