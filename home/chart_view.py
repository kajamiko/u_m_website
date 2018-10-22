from django.views.generic import TemplateView
from pygal.style import LightSolarizedStyle
from datetime import date 

from .charts import FPopularityBarChart, BPopularityBarChart, ActivityLineChart


class StatsView(TemplateView):
    template_name = 'stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)

        f_tickets = FPopularityBarChart(

            x_title='feature ID',
            y_title='Upvotes',
            explicit_size=False,
            style=LightSolarizedStyle,
        )
        
        b_tickets = BPopularityBarChart(

            x_title='Issue ID',
            y_title='Upvotes',
            explicit_size=False,
        )
        
        updates = ActivityLineChart(
            
            x_labels = [
                        date(2018, 7, 1),
                        date(2018, 8, 1),
                        date(2018, 9, 1),
                        date(2018, 10, 1)
                ],
            )
        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['f_tickets'] = f_tickets.generate()
        context['b_tickets'] = b_tickets.generate()
        context['updates'] = updates.generate()
        return context