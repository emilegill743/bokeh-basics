from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)

mapper = linear_cmap(field_name='y', palette=Spectral6, low=min(y), high=max(y))

plot = figure(plot_height=300, plot_width=600)
plot.circle(x,y, color=mapper, line_color='black', size=10)

output_file('color_mapper.html')
show(plot)