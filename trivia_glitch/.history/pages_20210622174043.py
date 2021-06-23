from ._builtin import WaitPage
from helper_files.generic_pages import Page
from .models import Constants
from django.http import HttpResponse
from datetime import datetime, timezone
import random, string
rom typing_extensions import Protocol
# To do:
# Notes on various stages


class Phase_1(Page):
    timeout_seconds = 120
    template_name = 'trivia_main/Phase_1.html'
    
    def is_displayed(self):
        return self.round_number == 1

class Phase_2(Page):
    timeout_seconds = 60
    template_name = 'trivia_main/Phase_2.html'
    
    def is_displayed(self):
        #return self.round_number == len(Constants.quiz_1_questions) +1
        return self.round_number == Constants.PHASE_1_LENGTH +1

class Basic_Wait_2(WaitPage):
    template_name = 'trivia_main/Wait_With_Chat.html'

class Basic_Wait(WaitPage):
    title_text = "Waiting for your Partner"
    body_text = "You are waiting on you partner to finish selecting their private answer. This should take a maximum of 60 seconds. Please refresh the webpage after 60 seconds. If, after several refreshes, you are still stuck on this page, please contact me at defilippis@gmail.com."



page_sequence = [
    Phase_1,
    Basic_Wait_2,
    Phase_2,
]
