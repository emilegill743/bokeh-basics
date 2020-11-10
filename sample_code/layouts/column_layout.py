from bokeh.layouts import column
from bokeh.io import output_file, show
from create_sample_plots import generate_plots

p1, p2, p3 = generate_plots()

layout = column(p1, p2, p3)

output_file('column.html')
show(layout)