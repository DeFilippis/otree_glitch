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
    
    def is_displayed(self):
        return self.round_number == 1

class Phase_2(Page):
    timeout_seconds = 60
    template_name = 'trivia_main/Phase_2.html'
    
    def is_displayed(self):
        #return self.round_number == len(Constants.quiz_1_questions) +1
        return self.round_number == Constants.PHASE_1_LENGTH +1
 
class Phase_3(Page):
    timeout_seconds = 60 
    template_name = 'trivia_main/Phase_3.html'
    def is_displayed(self):
        return self.round_number == Constants.PHASE_1_LENGTH + Constants.PHASE_2_LENGTH + 1

class No_Cheating(Page):
    timeout_seconds = 60
    template_name = 'trivia_main/No_Cheating.html'
    
    form_model = 'player'
    form_fields = ['cheat_consent']
    
    def is_displayed(self):
        return self.round_number == 1
    
class Goodbye(Page):
    timeout_seconds = 60  * 2
    template_name = 'trivia_main/Goodbye.html'
    def is_displayed(self):
        return self.round_number == Constants.PHASE_1_LENGTH + Constants.PHASE_2_LENGTH + Constants.PHASE_3_LENGTH

class Set_Question(WaitPage):
    # def is_displayed(self):
    #     print("---------------------")
    #     print(self.round_number)
    #     print(Constants.num_rounds)
    #     print(len(Constants.phase_1_indices))
    #     print(len(Constants.phase_2_indices))
    #     print(len(Constants.phase_3_indices))

    #     print(self.participant.vars['q_order'])
    #     print(len(self.participant.vars['q_order']))
    #     print("---------------------")

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            qd = p.current_question()
            p.question_text = str(qd['question'])
            p.question_solution = str(qd['solution'])
            p.question_type = str(qd['type'])

            # Store answer choices for later
            p.question_choice_1 = str(qd['choice1'])
            p.question_choice_2 = str(qd['choice2'])

            # All questions for FB have four answer choices
            if p.question_type != "FB":
                p.question_choice_3 = str(qd['choice3'])
                p.question_choice_4 = str(qd['choice4'])

class Question_Page(Page): 
    def get(self, *args, **kwargs):
        self.participant.vars.setdefault(f'round_arrival_time_{self.round_number}', datetime.now(tz=timezone.utc))
        return super().get(*args,**kwargs)

    def get_choices(self):
        qd = self.player.current_question()
        answer_choices = [str(value) for key, value in qd.items() if "choice" in key]
        #random.shuffle(answer_choices)
        #self.participant.vars['answer_choices'] = answer_choices
        return answer_choices

    def vars_for_template(self):
        return {
                'total_score': sum([i.round_total for i in self.player.in_all_rounds()]),
                'total_payout': sum([i.round_payout for i in self.player.in_all_rounds()]),
                'question_content': self.player.question_text,
                'bonus': Constants.bonus_values.get(self.player.question_type),
                'go_to_end': self.player.participant.vars.get('go_to_the_end'),
                'arrival_time': self.player.participant.vars.get(f'round_arrival_time_{self.round_number}'),
            } 


class Question_Private(Question_Page):
    template_name = 'trivia_main/Question_Private_2.html'
    #timeout_seconds = 999
    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['submitted_answer_private', 'confidence_private', 'blur_count_private', 'idle_private']

    timeout_submission = {'submitted_answer_private': '999',
                          'confidence_private': 999}

    
    def submitted_answer_private_choices(self):
        return self.get_choices()

    def confidence_private_error_message(self, value):
        if value == 50:
            return 'Please indicate your confidence in your answer.  It is important you answer accurately.'
        
    def before_next_page(self):
        # Create time stamp for amount of time spent on page
        arrival_time =  self.participant.vars.get(f'round_arrival_time_{self.round_number}')
        now =  datetime.now(tz=timezone.utc)
        self.player.time_spent_on_page_private = (now - arrival_time).total_seconds()

        
class Partner_Abandoned(Page):
    template_name = 'trivia_main/Partner_Abandoned.html'

    def is_displayed(self):
        return self.player.participant.vars.get('partner_abandoned') == True

    # In the rare event that I manually forward an inactive participant
    def before_next_page(self):
        self.player.participant.vars['partner_abandoned'] = False
        self.player.participant.vars['abandoned'] = False



class Abandoned(Page):
    template_name = 'trivia_main/Abandoned.html'

    def is_displayed(self):
        return self.player.participant.vars.get('abandoned') == True
    
    # In the rare event that I manually forward an inactive participant
    def before_next_page(self):
        self.player.participant.vars['partner_abandoned'] = False
        self.player.participant.vars['abandoned'] = False

class Basic_Wait_2(WaitPage):
    template_name = 'trivia_main/Wait_With_Chat.html'

class Basic_Wait(WaitPage):
    title_text = "Waiting for your Partner"
    body_text = "You are waiting on you partner to finish selecting their private answer. This should take a maximum of 60 seconds. Please refresh the webpage after 60 seconds. If, after several refreshes, you are still stuck on this page, please contact me at defilippis@gmail.com. <p></p>."

class Question_Joint(Question_Page):
    template_name = 'trivia_main/Question_Joint.html'
    timeout_seconds = 60 * 2 # Two minutes to discuss

    timeout_submission = {'submitted_answer_joint': '999',
                          'confidence_joint': 999}

    form_model = 'player'
    form_fields = ['submitted_answer_joint', 'confidence_joint', 'blur_count_joint', 'chat_content_joint', 'my_chat_joint', 'idle_joint']

    def submitted_answer_joint_choices(self):
        return self.get_choices()
        #return self.participant.vars.get('answer_choices') 


    def before_next_page(self):
        arrival_time =  self.participant.vars.get(f'round_arrival_time_{self.round_number}')
        now =  datetime.now(tz=timezone.utc)
        self.player.time_spent_on_page_joint = (now - arrival_time).total_seconds()

        # Set partner as inactive for this round if they didn't submit in time
        # Consider whether we should consider inactivity for private answers, or just joint
        if self.player.submitted_answer_joint == '999':
            self.player.is_inactive = True

        if self.player.round_number > 1:
            last_inactive = self.player.in_round(self.player.round_number-1).is_inactive

            if self.player.is_inactive and last_inactive:
                self.player.participant.vars['abandoned'] = True
                self.player.partner.participant.vars['partner_abandoned'] = True


  

class Results(Question_Page):
    template_name = 'trivia_main/Results.html'
    timeout_seconds = 60 * 2 # Two minutes to discuss

    form_model = 'player'
    form_fields = ['my_chat_results', 'chat_content_results']


    def before_next_page(self):
        self.player.rescue_event = self.player.is_rescue
        self.player.drag_down = self.player.is_drag_down
        self.player.corrected_private = self.player.is_corrected_private
        self.player.uncorrected_private = self.player.is_uncorrected_private


    def vars_for_template(self):
        submitted_answer_private = self.player.submitted_answer_private
        submitted_answer_joint = self.player.submitted_answer_joint
        consensus = submitted_answer_joint == self.player.partner.submitted_answer_joint
        solution =  self.player.question_solution
        correct_answer = self.player.submitted_answer_joint == solution

        # set the scores
        if consensus and correct_answer:
            self.player.round_total = 1
            self.player.round_payout = Constants.bonus_values.get(self.player.question_type)

        else:
            self.player.round_total = -1
            self.player.round_payout = Constants.bonus_values.get(self.player.question_type) * -1

        # set the total score
        self.player.total_score = sum([i.round_total for i in self.player.in_all_rounds()])
        
        return {
            'choices': self.get_choices(),
            'consensus': consensus,
            'score_points': consensus and correct_answer,
            #'total_score': sum([i.round_total for i in self.player.in_all_rounds()]),
            'total_score': self.player.total_score,
            #'total_payout': sum([i.round_payout for i in self.player.in_all_rounds()]),
            'total_payout': max(sum([i.round_payout for i in self.player.in_all_rounds()]), 0),
            'solution': solution
        }


page_sequence = [
    Phase_1,
    Phase_2,
    Phase_3,
    No_Cheating,
    Goodbye,
    Basic_Wait,
    Set_Question,
    Question_Private,
    Basic_Wait,
    Question_Joint,
    Basic_Wait_2,
    Partner_Abandoned,
    Abandoned,
    Results,
    Basic_Wait_2,
]
