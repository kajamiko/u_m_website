import pygal

from tickets.models import Ticket


class TicketBarChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Ticket upvotes'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        for ticket in Ticket.objects.all():
            data[ticket.issue] = ticket.upvotes
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)