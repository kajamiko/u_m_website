from django.views.generic import TemplateView
from pygal.style import DarkStyle

from .charts import TicketBarChart


class StatsView(TemplateView):
    template_name = 'stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
        cht_tickets = TicketBarChart(
            height=600,
            width=800,
            x_title='ticket ID',
          #   include_x_axis=True,
            y_title='Upvotes',
            explicit_size=True,
          #   style=DarkStyle
        )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context['cht_tickets'] = cht_tickets.generate()
        return context