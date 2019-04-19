import plotly.plotly as py
import plotly.graph_objs as go
# import plotly
#
# plotly.tools.set_credentials_file(username='xdream', api_key='5WoW0Clj1LZO3D24UAjf')

import pandas as pd
import colorlover as cl

colors = cl.scales['5']['seq']['Blues']
data = {'Year' : [2010, 2011, 2012, 2013, 2014],
        'Color' : colors}
df = pd.DataFrame(data)


trace0 = go.Table(
  header = dict(
    values = ["Color", "<b>YEAR</b>"],
    line = dict(color = 'white'),
    fill = dict(color = 'white'),
    align = ['center'],
    font = dict(color = 'black', size = 12)
  ),
  cells = dict(
    values = [df.Color, df.Year],
    line = dict(color = [df.Color]),
    fill = dict(color = [df.Color]),
    align = 'center',
    font = dict(color = 'black', size = 11)
    ))

data = [trace0]

py.iplot(data, filename = "row variable color")