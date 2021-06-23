#from ._builtin import Page
from django.forms.models import modelform_factory
from django.conf import settings
from django.utils import translation
from datetime import datetime, timezone
import time, random
from otree.api import Page


class Page(Page):

    def get_progress(self):
        totpages = self.participant._max_page_index
        curpage = self.participant._index_in_pages
        return f"{curpage / totpages * 100:.0f}"


#class Page(Page):
    # def get(self, *args, **kwargs):
    #     t, _ = TimeTracker.objects.get_or_create(owner=self.participant,
    #                                              page=self.__class__.__name__,
    #                                              period=self.player.round_number,
    #                                              defaults=dict(get_time=datetime.now(timezone.utc), ))
    #     return super().get(*args, **kwargs)

    # def post(self, *args, **kwargs):
    #     # if self.participant.is_browser_bot:
    #     #     time.sleep(2)
    #     try:
    #         t = TimeTracker.objects.get(owner=self.participant,
    #                                     page=self.__class__.__name__,
    #                                     period=self.player.round_number,
    #                                     )
    #         t.post_time = datetime.now(timezone.utc)
    #         t.seconds_on_page = (t.post_time - t.get_time).seconds
    #         t.save()
    #     except TimeTracker.DoesNotExist:
    #         pass

    #     return super().post(*args, **kwargs)
