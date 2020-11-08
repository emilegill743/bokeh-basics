from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import pandas as pd
import os

# Import Apple Stock Sample Data
dirname = os.path.dirname(__file__)

df = pd.read_csv(
        os.path.join(dirname,'../sample_data/data/AAPL.csv'))

df['Date'] = pd.to_datetime(df['Date'])

# Convert to ColumnDataSource
source = ColumnDataSource(df)

plot = figure(x_axis_type='datetime')
plot.line(x='Date', y='Open', source=source)

output_file('cds_glyph.html')
show(plot)

