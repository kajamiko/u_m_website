from django.test import TestCase
from tickets.models import Ticket
from datetime import date

from .charts import FPopularityBarChart, BPopularityBarChart, ActivityLineChart

class TestCharts(TestCase):
     """
     A class design to test passing data to 
     """
     def test_data(self):
          ticket = Ticket(variety='B', issue='ticket0', date_verified=date.today(), date_start_dev=date.today())
          ticket.save()
          ticket2 = Ticket.objects.create(
               variety = "F",
               issue = "ticket1",
               date_verified=date.today(),
               date_start_dev=date.today(),
                date_done=date.today()
          )
          ticket3 = Ticket.object.create(
               variety='B', 
               issue='ticket3',
               date_verified=date.today()
               )
          chart = ActivityLineChart()
          print(chart.get_data())