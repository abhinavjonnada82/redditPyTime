import dash
import dash_core_components as dcc
import dash_html_components as html

graphy = dash.Dash()
graphy.layout = html.Div([
    html.Div(
        className="row",
        children=[
            html.Div(
                className="six columns",
                children=[
                    html.Div(
                        children=dcc.Graph(
                            id='right-graph',
                            figure={
                                'data': [{
                                    'x': x1List,
                                    'y': y1List,
                                    'type': 'scatter',
                                    'color': 'red',
                                }],
                                'layout': {
                                    'height': 400,

                                }
                            }
                        )
                    )
                ]
            ),
            html.Div(
                className="six columns",
                children=html.Div([
                    dcc.Graph(
                        id='right-top-graph',
                        figure={
                            'data': [{
                                'x': y2List,
                                'y': x2List,
                                'type': 'bar',
                                'name': 'Score v. Submissions'

                            }],
                            'layout': {
                                'height': 400,
                                'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10}

                            }
                        }
                    ),
                    dcc.Graph(
                        id='right-bottom-graph',
                        figure={
                            'data': [{
                                'x': 'yList',
                                'y': 'xList',
                                'type': 'bar'
                            }],
                            'layout': {
                                'height': 400,
                                'margin': {'l': 10, 'b': 20, 't': 0, 'r': 0}
                            }
                        }
                    ),

                ])
            )
        ]
    )
])

graphy.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    graphy.run_server(debug=True)