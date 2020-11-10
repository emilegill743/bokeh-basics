from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import row
from bokeh.io import output_file, show
from create_sample_plots import generate_plots

p1, p2, p3 = generate_plots()

first = Panel(child=row(p1, p2), title='first')
second = Panel(child=row(p3), title='second')

tabs = Tabs(tabs=[first, second])

output_file('tabbed.html')
show(tabs)