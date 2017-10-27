import datetime
import json

from django import template
from django.utils import timezone

from ..forms import ThoughtForm

register = template.Library()


@register.inclusion_tag('thoughts/_form.html')
def thought_form():
    form = ThoughtForm
    return {"form": form}


@register.simple_tag(takes_context=True)
def chart_data(context):
    user = context['user']
    days_ago = timezone.now() - datetime.timedelta(days=5)
    thoughts = user.thoughts.filter(recorded_at__gte=days_ago).order_by('recorded_at')
    return json.dumps({
        'labels': [thought.recorded_at.strftime("%m-%d %H:%H:%S") for thought in thoughts],
        'series': [[thought.condition * -1 for thought in thoughts]]
    })
