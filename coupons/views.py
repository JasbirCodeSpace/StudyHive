from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent


@login_required(login_url='/login/')
def show_coupons(request):
    coupons = read_coupons()
    return render(request, 'coupons/show.html', {'coupons': coupons})


def read_coupons():
    coupons = pd.read_csv(BASE_DIR/'coupons/coupons.csv')
    coupons.dropna(subset=['code', 'link', 'name'], inplace=True)
    
    # parsing the DataFrame in json format.
    json_records = coupons.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    return data

