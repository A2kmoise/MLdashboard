from django.shortcuts import render
import pandas as pd
from .dashboard import frequency_table, vehicles_over_5000_table, total_price_by_manufacturer

# Create your views here.

def dashboard_view(request):
  queryset = pd.read_csv("dummy_data/vehicles_ml_dataset.csv")
  df = pd.DataFrame(queryset)
  
  return render(request, "vehicles/index.html", {
    "frequency_table": frequency_table(df),
    "vehicles_over_5000_table": vehicles_over_5000_table(df),
    "total_price_by_manufacturer_table": total_price_by_manufacturer(df)
  })