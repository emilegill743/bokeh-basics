from bokeh.layouts import row
from bokeh.io import output_file, show
from create_sample_plots import generate_plots

p1, p2, p3 = generate_plots()

layout = row(p1, p2, p3)

output_file('row.html')
show(layout)