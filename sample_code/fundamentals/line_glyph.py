from bokeh.io import output_file, show
from bokeh.plotting import figure

plot = figure()
plot.line(x=[1,2,3,4], y=[4,7,2,16])

output_file('line_glyph.html')
show(plot)