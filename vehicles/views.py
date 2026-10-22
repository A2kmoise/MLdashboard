from django.shortcuts import render
import pandas as pd
from .dashboard import frequency_table

# Create your views here.

def dashboard_view(request):
  queryset = pd.read_csv("dummy_data/vehicles_ml_dataset.csv")
  df = pd.DataFrame(queryset)
  
  return render(request, "vehicles/index.html", {
    "frequency_table": frequency_table(df)
  })