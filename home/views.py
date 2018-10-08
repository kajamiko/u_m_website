from django.shortcuts import render
from tickets.models import Ticket
from chartit import PivotDataPool, PivotChart

def homepage(request):
     
     
     return render(request, 'index.html' )

def project_info(request):
    
    return render(request, 'project_info.html')
     
def show_stats(request):
     
     
# Step 1: Create a PivotDataPool with the data we want to retrieve.
     ticketpivotdata = PivotDataPool(
        series=[{
            'options': {
                'source': Ticket.objects.all(),
                'categories': ['date_created'],
                'legend_by': 'variety',
                'top_n_per_cat': 3,
            },
            'terms': {
                'upvotes': 'upvotes',
            }
        }]
    )

    # Step 2: Create the PivotChart object
     ticketcht = PivotChart(
        datasource=ticketpivotdata,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['upvotes']
        }],
        chart_options={
            'title': {
                'text': 'Tickets_by_month'
            },
            'xAxis': {
                'title': {
                    'text': 'Month'
                }
            }
        }
    )
                       
     return render(request, 'stats.html', {'ticketcht': ticketcht})