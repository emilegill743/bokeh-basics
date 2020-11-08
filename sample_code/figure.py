from bokeh.io import output_file, show
from bokeh.plotting import figure

plot = figure()

output_file('figure.html')
show(plot)