from django.views.generic import TemplateView
from pygal.style import LightSolarizedStyle

from .charts import FPopularityBarChart, BPopularityBarChart


class StatsView(TemplateView):
    template_name = 'stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
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
        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['f_tickets'] = f_tickets.generate()
        context['b_tickets'] = b_tickets.generate()
        return context