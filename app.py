import pandas as pd
import plotly
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv("insurance.csv")

app = dash.Dash()

# creating options
features = df[['sex', 'age', 'charges']]
options = [{'label' : i, 'value' : i} for i in features]


app.layout = html.Div([
                        dcc.Graph(id= "box_plots_age",
                        figure = {
                        'data':[go.Box(
                        y= df.age,
                        boxpoints= "all",
                        jitter= 0.3,
                        pointpos= 0)],
                        'layout':{'title': "A look at the distribution of AGE"}
                                }
                                  ),

                        html.P([
                    html.Label("Choose a feature"),
                    dcc.Dropdown(
                    id = 'options_distribution',
                    options = options,
                    value = options[0])
                        ],
                    style = {'width': '400px',
                            'fontSize' : '20px',
                            'padding-left' : '100px',
                            'display': 'inline-block'})


                         ])
@app.callback(Output('box_plot_age', 'figure'),
              [Input('box_plot_input', 'value')])



# html.Div([
#                 dcc.Graph(id= "Smoker Heatmap",
#                     figure = {
#                         'data':[go.Heatmap(
#                             x=df["smoker"],
#                             y=df["age"],
#                             z = df["charges"].values.tolist()
#                             )],
#                         "layout": go.Layout(title = "Corrrelation between Smoker and Charges",
#                             xaxis = dict(title= "Age"),
#                             yaxis = dict(title='Charge'),
#                             hovermode = "closest")
#
#                             }
#                     )


# html.Div([dcc.Graph(id= "box_plot_age",
#                                   figure = {
#                                      'data':[go.Box(y= df.age, boxpoints= "all",jitter= 0.3, pointpos= 0)],
#                                       "layout": go.Layout(title = "A look at the distribution of AGE",
#                                   yaxis = dict(title='Age'),
#                                   hovermode = "closest")}
#                                 ),
#                 # scatterplots
#                 html.Div([dcc.Graph(id= "scatter_age_and_charges",
#                     figure = {'data':[
#                         go.Scatter(x= df.age, y = df.charges, mode= 'markers')],
#                         "layout":
#                             go.Layout(title = "Corrrelation between Age and Charges",
#                    xaxis = dict(title= "Age"),
#                    yaxis = dict(title='Charge'),
#                    hovermode = "closest")}
#                                     ),


                # html.Div([dcc.Graph(id= "Smoker Heatmap",
                #     figure = {'data':[
                #         go.Heatmap(x=df["smoker"],
                #    y=df["age"], z = df["charges"].values.tolist()),
                #         "layout":
                #             go.Layout(title = "Corrrelation between Age and Charges",
                #    xaxis = dict(title= "Age"),
                #    yaxis = dict(title='Charge'),
                #    hovermode = "closest")}),






if __name__ == '__main__':
    app.run_server(port = '33555')
