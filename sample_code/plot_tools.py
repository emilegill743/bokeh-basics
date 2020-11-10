from bokeh.plotting import figure, show

p = figure(toolbar_location="left",
           tools="pan,wheel_zoom,lasso_select,tap,undo,reset")
        
show(p)