from bokeh.io import output_file, show
from bokeh.plotting import figure

plot = figure(plot_height=300, plot_width=600)

plot.line(x=[1,2,3,4], y=[4,7,2,16])
plot.circle([1,2,3,4], [4,7,2,16], fill_color="white", size=10)

output_file('line_glyph.html')
show(plot)