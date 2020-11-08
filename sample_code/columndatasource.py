from bokeh.models import ColumnDataSource
# From a dictonary
source_from_dict = ColumnDataSource(data={
                                'x' : [1,2,3,4,5],
                                'y' : [1,4,9,16,25]})
# From a DataFrame
source_from_df = ColumnDataSource(df)