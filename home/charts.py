from collections import OrderedDict
import pygal
from tickets.models import Ticket


class FPopularityBarChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Features popularity'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        for ticket in Ticket.objects.all().filter(variety__exact="F").order_by('upvotes'):
            data[ticket.issue] = ticket.upvotes
        return OrderedDict(data)

    def generate(self):
        # Get chart data
        chart_data = self.get_data()
    
        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)
        
        # Return the rendered SVG
        return self.chart.render(is_unicode=True)
        
class BPopularityBarChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Issues popularity'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        for ticket in Ticket.objects.all().filter(variety__exact="B").order_by('upvotes'):
            data[ticket.issue] = ticket.upvotes
        return OrderedDict(data)

    def generate(self):
        # Get chart data
        chart_data = self.get_data()
        # chart_data = OrderedDict(chart_data)
        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)
        
        # Return the rendered SVG
        return self.chart.render(is_unicode=True)
        