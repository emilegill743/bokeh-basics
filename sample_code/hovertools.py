from bokeh.models import HoverTool

hover = HoverTool(tooltips=[
            ("index", "$index"),
            ("label", "@column_name"),
            ("label2", "@{multi-word column name}"),
            ("colour", "$color[hex, swatch]:fill_color")])