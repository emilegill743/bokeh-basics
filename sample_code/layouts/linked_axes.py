from bokeh.layouts import row
from bokeh.io import output_file, show
from bokeh.plotting import figure
import numpy as np

x = np.linspace(0,10,1000)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

p1 = figure(plot_height=300, plot_width=300, title="y=sin(x)")
p1.line(x,y1)

p2 = figure(plot_height=300, plot_width=300, title="y=cos(x)")
p2.line(x,y2)


p2.x_range = p1.x_range
p2.y_range = p1.y_range

layout = row(p1, p2)

output_file('row_linked.html')
show(layout)