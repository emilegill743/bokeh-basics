from bokeh.layouts import gridplot
from bokeh.io import output_file, show
from create_sample_plots import generate_plots

p1, p2, p3 = generate_plots()

layout = gridplot([[None, p1], [p2, p3]],
                  toolbar_location=None)

output_file = ('nested.html')
show(layout)