import bokeh.sampledata
import os

# Download Bokeh sample data to default directory ($HOME/.bokeh/data)
bokeh.sampledata.download()

# Move data to current project
dirname = os.path.dirname(__file__)

os.rename(
    os.path.expanduser('~/.bokeh/data'),
    f'{dirname}/data')