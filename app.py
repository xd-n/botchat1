#create dataset
import pandas as pd
import numpy as np

# Define the month names and product categories
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
categories = ['Category A', 'Category B', 'Category C']

# Define the total number of sales for each month and category
total_sales = np.random.randint(low=10000, high=25000, size=(len(months), len(categories)))

# Create a pandas DataFrame to store the sales data
df = pd.DataFrame(columns=['Month', 'Category', 'Sales'])

# Loop through the months and categories to add the sales data to the DataFrame
for i, month in enumerate(months):
    for j, category in enumerate(categories):
        sales = total_sales[i, j]
        df = df.append({'Month': month, 'Category': category, 'Sales': sales}, ignore_index=True)

# Write the DataFrame to a CSV file
#df.to_csv('sales_data_1.csv', index=False)


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Load data
#df = pd.read_csv('sales_data_1.csv')
df=df.copy()

# Create the Dash app
app = dash.Dash(__name__)
server = app.server

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Sales Dashboard'),
    
    # Graph 1: Total Sales by Month
    html.Div([
        html.H3('Total Sales by Month'),
        dcc.Graph(
            id='total-sales-graph',
            figure={
                'data': [
                    go.Bar(
                        x=df['Month'],
                        y=df['Sales']
                    )
                ],
                'layout': go.Layout(
                    title='Total Sales by Month',
                    xaxis={'title': 'Month'},
                    yaxis={'title': 'Total Sales ($USD)'}
                )
            }
        )
    ]),
    
    # Graph 2: Sales by Product Category
    html.Div([
        html.H3('Sales by Product Category'),
        dcc.Graph(
            id='sales-by-category-graph',
            figure={
                'data': [
                    go.Pie(
                        labels=df['Category'],
                        values=df['Sales']
                    )
                ],
                'layout': go.Layout(
                    title='Sales by Product Category'
                )
            }
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)  

    #changed by myself
    #app.run_server(debug=True, port=8049, use_reloader=False)
