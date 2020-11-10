from bokeh.plotting import figure, show

p = figure(
        plot_width=500,
        plot_height=500,
        x_axis_label="X Label",
        y_axis_label="Y Label",
        title="My custom plot",
        toolbar_location="left",
        tools="pan,wheel_zoom,reset")
show(p)