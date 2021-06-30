from django.shortcuts import render, HttpResponse
from .models import CompanyStock
import plotly.graph_objects as go
import plotly.offline
import pandas as pd
def index(request):
    return HttpResponse("Started Server")
def get(request):
    toget=request.GET.get("type", "")
    if(toget=="all"):
        company_object={}
        company_names=[]
        company_stocks=[]
        objects=CompanyStock.objects.all()
        print(objects)
        for a in objects:
            lst=a.company_stocks_as_comma_seperated_numbers.split(",")
            latest=int(lst[len(lst)-1])
            print(latest)
            company_names.append(a.company_name)
            company_stocks.append(int(latest))
        df=pd.DataFrame(company_object)
        print(df)
        zipped_lists=zip(company_names, company_stocks)
        sorted_pairs = sorted(zipped_lists)
        tuples = zip(*sorted_pairs)
        list1, list2 = [ list(tuple) for tuple in tuples]
        print(list1, list2)
        fig=go.Figure(data=[go.Bar(x=list1, y=list2)])
        fig.update_layout(height=400, width=500)
        graph_div=plotly.offline.plot(fig, auto_open = False, output_type="div")
        return HttpResponse(graph_div)