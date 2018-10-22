from django.test import TestCase
from tickets.models import Ticket
import datetime

from .charts import FPopularityBarChart, BPopularityBarChart, ActivityLineChart

class TestCharts(TestCase):
     """
     A class design to test passing data to a chart
     """
     def test_ActivityChartdata(self):
          """
          Tests updates chart data
          """
          ticket0 = Ticket(variety='B', issue='ticket0', verified = True, 
          date_verified=datetime.date.today(), date_start_dev=datetime.date.today())
          ticket0.save()
          ticket1 = Ticket.objects.create(
               variety = "F",
               issue = "ticket1",
               verified = True,
               date_verified=datetime.date.today(),
               date_start_dev=datetime.date.today(),
                date_done=datetime.date.today()
          )
          ticket2 = Ticket.objects.create(
               variety='B', 
               issue='ticket2',
               verified = True,
               date_verified=datetime.date.today()
               )
              
          chart = ActivityLineChart()
          
          assert(chart.get_data() == 
          {'ticket0': [datetime.date(2018, 10, 22), datetime.date(2018, 10, 22), None], 
          'ticket2': [datetime.date(2018, 10, 22), None, None], 
          'ticket1': [datetime.date(2018, 10, 22), datetime.date(2018, 10, 22), datetime.date(2018, 10, 22)]
               
          })
          
     def test_bar_charts(self):
          """
          Tests popularity charts data
          """
          ticket0 = Ticket(variety='B', issue='ticket0', verified = True, 
          date_verified=datetime.date.today(), date_start_dev=datetime.date.today())
          ticket0.save()
          ticket1 = Ticket.objects.create(
               variety = "F",
               issue = "ticket1",
               verified = True,
               upvotes=10
          )
          ticket2 = Ticket.objects.create(
               variety='B', 
               issue='ticket2',
               upvotes=5
               )
          ticket3 = Ticket.objects.create(
               variety='F', 
               issue='ticket3',
               upvotes=80
               )
          f_chart = FPopularityBarChart()
          b_chart = BPopularityBarChart()
          
          assert(f_chart.get_data()=={'ticket1': 10, 'ticket3': 80})
          assert(b_chart.get_data()=={'ticket2': 5, 'ticket0': 0})