from bokeh.plotting import figure
import numpy as np

def generate_plots():

    x = np.linspace(0,10,1000)

    y1 = np.sin(x)
    y2 = x**2
    y3 = np.exp(x)

    p1 = figure(plot_height=300, plot_width=300, title="y = sin(x)")
    p1.line(x,y1)

    p2 = figure(plot_height=300, plot_width=300, title="y = x²")
    p2.line(x,y2)

    p3 = figure(plot_height=300, plot_width=300, title="y = eˣ")
    p3.line(x,y3)

    return(p1,p2, p3)