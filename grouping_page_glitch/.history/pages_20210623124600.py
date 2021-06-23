from otree.api import Currency as c, currency_range
import random
from ._builtin import Page, WaitPage
from .models import Constants
import string
import time
from datetime import datetime 
from leavable_wait_page.pages import LeavableWaitPage, SkippablePage
import numpy as np
import datetime


class Page(Page):
    def get_progress(self):
        totpages = self.participant._max_page_index
        curpage = self.participant._index_in_pages
        return f"{curpage / totpages * 100:.0f}"

# TO DO: Get total waiting time and store as a variable
# TO DO: Dynamically pair participants so even number of each category

# class Wait_Debug(WaitPage):
#     group_by_arrival_time = True

class Grouping_Page(WaitPage):
    group_by_arrival_time = True


class Grouping_Debug(Page):
    template_name = "grouping_page_glitch/grouping_debug.html"

    def vars_for_template(self):
        return dict(id_in_group = self.player.id_in_group)


page_sequence = [
    WaitPage,
    Grouping_Page,
    Grouping_Debug,
]
