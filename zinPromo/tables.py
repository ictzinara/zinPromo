from Api.models import *
import django_tables2 as tables

class WeeklyDrawTable(tables.Table):

    class Meta:
        model = PromotionWeeklyDraw
        template_name = "django_tables2/bootstrap.html"
        fields = ('weekly_winner',)
