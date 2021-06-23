from otree.api import Currency as c, currency_range

from ._builtin import WaitPage
from helper_files.generic_pages import Page
from .models import Constants
from django.http import HttpResponse
from datetime import datetime, timezone
import random, string
from otree.models_concrete import ChatMessage

# To do:
# Notes on various stages


class Phase_1(Page):
    timeout_seconds = 120
    template_name = 'trivia_main/Phase_1.html'

class Phase_2(Page):
    timeout_seconds = 60
    template_name = 'trivia_main/Phase_2.html'
    
class Basic_Wait_2(WaitPage):
    template_name = 'trivia_main/Wait_With_Chat.html'


page_sequence = [
    Phase_1,
    Basic_Wait_2,
    Phase_2,
    
    No_Cheating,
    Goodbye,
    Basic_Wait,
    Set_Question,
    Question_Private,
    Basic_Wait,
    Question_Joint,
    Basic_Wait_2,
    Partner_Abandoned,
    #Abandoned,
    Results,
    Basic_Wait_2,
]
