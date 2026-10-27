import plotly.express as px
import plotly.offline as ps
import plotly.graph_objects as go
import pandas as pd
def frequency_table(df):
  # Simple counts
  manufacturer_counts = df['manufacturer'].value_counts().reset_index()
  manufacturer_counts.columns = ['Manufacturer', 'Count']
  
  
  # Convert to HTML using the correct method name: .to_html()
  table_html = manufacturer_counts.to_html(
    classes="table table-bordered table-striped table-sm",
    float_format='%.2f',
    justify='center'
    )
  
  
  return table_html

def vehicles_over_5000_table(df):
  price_filtered_df = df.loc[df.selling_price < 20000]   
  
  price_filtered_table_html = price_filtered_df.to_html(
    classes="table table-bordered table-striped table-sm",
    float_format='%.2f',
    justify='center'
  )
  
  return price_filtered_table_html

def total_price_by_manufacturer(df):
  total_price_table_html = df.groupby(['manufacturer', 'transmission'])[['selling_price']].sum().to_html(
    classes="table table-bordered table-striped table-sm",
    float_format='%.2f',
    justify='center'
  )
  return total_price_table_html