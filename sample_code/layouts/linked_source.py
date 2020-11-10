import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.io import output_file, show

# Generate data
x = np.linspace(0,10,100)

data = {'x' : x,
        'y1' : np.sin(x),
        'y2' : np.cos(x)}

df = pd.DataFrame(data)
cds = ColumnDataSource(df)

tools="box_select,reset"

p1 = figure(plot_height=300, plot_width=300, title="y=sin(x)", tools=tools)
p1.circle('x','y1', source=cds)

p2 = figure(plot_height=300, plot_width=300, title="y=cos(x)", tools=tools)
p2.circle('x','y2', source=cds)

layout = row(p1, p2)

output_file('linked_source.html')
show(layout)

