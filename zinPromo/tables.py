from Api.models import *
from table import Table
from table.columns import Column


class WeeklyDrawTable(Table):
    id = Column(field='id')
    name = Column(field='weekly_winner')

    class Meta:
        model = PromotionWeeklyDraw
