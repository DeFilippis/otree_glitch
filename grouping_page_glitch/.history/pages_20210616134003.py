from otree.api import Currency as c, currency_range
import random
from ._builtin import Page, WaitPage
from .models import Constants
import string
import time
from datetime import datetime 
from leavable_wait_page.pages import LeavableWaitPage, SkippablePage
import numpy as np
from datetime import datetime, timezone


class Page(Page):
    def get_progress(self):
        totpages = self.participant._max_page_index
        curpage = self.participant._index_in_pages
        return f"{curpage / totpages * 100:.0f}"

# TO DO: Get total waiting time and store as a variable
# TO DO: Dynamically pair participants so even number of each category

# class Wait_Debug(WaitPage):
#     group_by_arrival_time = True

class Leavable_Wait_Custom(WaitPage):
    
    self.player.time_spent_on_page_private = (now - arrival_time).total_seconds()




class Wait_For_Partner(LeavableWaitPage):
    """First Leavable Wait Page to pair participant"""
    template_name = 'know_your_partner_new/LeavableWaitPageCustom.html'
    allow_leaving_after = 15 * 60
    group_by_arrival_time = True


    def is_displayed(self):
        now = datetime.now()
        self.participant.vars.setdefault('arrival_time', now)
        return(True)
    
    def vars_for_template(self):
        return dict(
            leavable_wait_page_success = '''<p>Thank you for completing the intake form. We are waiting for other mTurkers to complete the survey. The moment someone else completes their intake form you will be paired up with them. </p>
            
            <p>After 15 minutes of waiting, a button will appear allowing you to exit the game. You will be given a code that you should email to me at defilippis@gmail.com. I will then create a compensation HIT for $2.00 to compensate you for your time. Please note that if you arrived to this HIT over 20 minutes late, you will not be eligible for any payment, as mentioned during scheduling.</p>''',

            leavable_wait_page_warning = '''Please note that in the real game it's very important that you use the chat box to interact with your opponent as much as possible.'''
        )

    
class Dropouts2(Page):
    """This page is only shown to those who left the wait page."""
    def is_displayed(self) -> bool:
        return self.participant.vars.get('go_to_the_end', False)

    def vars_for_template(self):
        return dict(
            # TO DO: Put this in .yaml file
            completion_code = "AJFHBG897"
        )
    

class Results(Page):
    timeout_seconds = 60 * 3
    template_name = 'know_your_partner_new/Results.html'

    def vars_for_template(self):
        fields = ['superpower', 'season', 'fruit', 'vacation', 'politics', 'political_views']

        partner_data = self.player.partner.get_participant_data(fields)

        partner_data = dict(
            politics = f'''Your partner said that, as of today, they identify more closely with the: <b> {partner_data["politics"]} party </b>''',
            political_views = f'''Your partner considers themselves to be: <b> {partner_data["political_views"]} </b>''',
            superpower = f'''Your partner said they would most prefer to have the following superpower: <b> {partner_data["superpower"]} </b>''',
            season = f'''Your partner said their favorite season was: <b> {partner_data["season"]} </b>''',
            fruit = f'''Your partner said the fruit they most enjoy eating is: <b> {partner_data["fruit"]} </b>''',
            vacation = f'''Your partner said they would most enjoy vacationing here: <b> {partner_data["vacation"]} </b>''')

        return  dict(data = partner_data)

    def before_next_page(self):
        politics_fields = ['politics', 'political_views', 'superpower']
        partner_data = self.player.partner.get_participant_data(politics_fields)

        self.player.partner_politics = partner_data['politics']
        self.player.partner_superpower = partner_data['superpower']
        self.player.partner_political_views = partner_data['political_views']
        
        # Treatment Condition = First letter of your politics + First letter of partner politics
        try:
            self.player.treatment_condition = self.player.get_participant_data('politics')['politics'][0] + self.player.partner_politics[0]
        except:
            self.player.treatment_condition = "NA"


class Wait_For_Partner_2(WaitPage):
    template_name = 'know_your_partner_new/WaitPage2.html'
    
    def after_all_players_arrive(self):
        self.group.team_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) 

    
class Partner_Quiz(Page):
    timeout_seconds = 60 * 3 

    template_name = 'know_your_partner_new/PartnerQuiz.html'
    form_model = 'player'

    #players will only be quizzed on their partner's politics and superpower
    form_fields = ['kyp_politics', 'kyp_superpower']

    def error_message(self, values):
        solutions = dict(
            kyp_politics= self.player.partner_politics,
            kyp_superpower= self.player.partner_superpower
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'This answer is incorrect. Please try again'

                # If the incorrect answer was the politics field, increment incorrect submissions
                # if field_name == 'kyp_politics':
                self.player.number_incorrect_submissions +=1

        return error_messages

page_sequence = [
    Wait_For_Partner,
   # Wait_Debug,
    Dropouts2, 
    Results,
    Wait_For_Partner_2,
    Partner_Quiz,
    Wait_For_Partner_2,
]
