from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
from pandas import *
from collections import OrderedDict
import random
import collections
import copy
import string
from django import forms as djforms
import yaml
import json
from itertools import groupby
from epistemic_baseline_new.widgets import DefaultSlider, LabeledSlider
from otree.models_concrete import ChatMessage
from otree.models import Session

author = 'Evan DeFilippis'

doc = """
The quiz app main mechanics.  
"""

class Constants(BaseConstants):
    name_in_url = 'trivia_glitch'
    num_rounds = 1
    players_per_group = 2

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number==1:
            for g in self.get_groups():

                # phase_1_indices = Constants.phase_1_indices.copy()[0:Constants.PHASE_1_LENGTH]
                # phase_2_indices = Constants.phase_2_indices.copy()[0:Constants.PHASE_2_LENGTH]
                # phase_3_indices = Constants.phase_3_indices.copy()[0:Constants.PHASE_3_LENGTH]

                # random.shuffle(phase_1_indices)
                # random.shuffle(phase_2_indices)
                # random.shuffle(phase_3_indices)

                # combined_indices = phase_1_indices + phase_2_indices + phase_3_indices
                # print("-------------------------------")
                # print(combined_indices)
                # print("-------------------------------")

                # for p in g.get_players():
                #     p.participant.vars['q_order']  = combined_indices

                phase_1_temp = Constants.phase_1_indices.copy()
                random.shuffle(phase_1_temp)

                phase_1_indices = phase_1_temp[0:Constants.PHASE_1_LENGTH]
                phase_2_indices = Constants.phase_2_indices.copy()[0:Constants.PHASE_2_LENGTH]
                phase_3_indices = Constants.phase_3_indices.copy()[0:Constants.PHASE_3_LENGTH]

                random.shuffle(phase_1_indices)
                random.shuffle(phase_2_indices)
                random.shuffle(phase_3_indices)

                combined_indices = phase_1_indices + phase_2_indices + phase_3_indices
                # print("-------------------------------")
                # print(combined_indices)
                # print("-------------------------------")

                for p in g.get_players():
                    p.participant.vars['q_order']  = combined_indices

class Group(BaseGroup):
    def set_payoffs(self):
        for player in self.get_players():
            if player.is_correct and player.is_consensus:
                player.round_total = 1
            try:
                player.round_payout = Constants.bonus_values.get(player.question_type)
            except: 
                player.round_payout = .5
            else:
                player.round_total -=1
                try:
                    player.round_payout = Constants.bonus_values.get(player.question_type) * -1
                except: 
                    player.round_payout = .5

    # def create_question_list(self):
    #     qs = Constants.questions.copy()
    #     final_list = []
    #     for key, group in groupby(qs, lambda x: x.get('type')):
    #         c = list(group)[:Constants.round_lengths[key]] 
    #         random.shuffle(c)
    #         final_list.extend(c)

    #     aaa = list(groupby(qs, lambda x: x.get('type')))
    #     print(len(aaa))
            
    #     self.questions_for_group = json.dumps(final_list)



        
class Player(BasePlayer):
    # Storing all question values
    question_id = models.StringField()
    question_text = models.StringField()
    question_solution = models.StringField()
    question_type = models.StringField()

    # Storing all the question choices
    question_choice_1 = models.StringField()
    question_choice_2 = models.StringField()
    question_choice_3 = models.StringField()
    question_choice_4 = models.StringField()


    # Round data
    round_total = models.FloatField(initial = 0)
    round_payout = models.FloatField(initial = 0)



    my_chat_joint = models.StringField()
    chat_content_joint = models.StringField()

    my_chat_results = models.StringField()
    chat_content_results = models.StringField()

    blur_count_private = models.IntegerField(initial=0)
    blur_count_joint = models.IntegerField(initial=0)

    idle_private = models.IntegerField(initial=0)
    idle_joint = models.IntegerField(initial=0)

    time_spent_on_page_private = models.FloatField()
    time_spent_on_page_joint = models.FloatField()

    trial_counter = models.IntegerField(initial=0)
    
    # Tracks whether participant is active
    is_inactive = models.BooleanField(initial = False)

    # Submitted Answers
    submitted_answer_private = models.StringField(widget=widgets.RadioSelect)
    submitted_answer_joint = models.StringField(widget=widgets.RadioSelect)

    # Confidence
    # confidence_private = models.FloatField(
    #     label = "How confident do you feel in this answer, prior to discussing with your partner?",
    #     widget=DefaultSlider(
    #     )
    # )

    # confidence_joint = models.FloatField(
    #     label = "How confident do you feel in this answer now that you have discussed with your partner?",
    #     widget=DefaultSlider(
    #     )
    # )

    # confidence_private = models.FloatField(
    #     label = "How confident do you feel in this answer, prior to discussing with your partner?",
    #     widget=widgets.Slider(attrs={'step': '.01'},
    #                         show_value=True)
    # )

    confidence_private = models.IntegerField(
        label = "How confident do you feel in this answer, prior to discussing with your partner?",
        widget=LabeledSlider(
            before = "Not Confident",
            after = "Extremely Confident"
        )
    )


    confidence_joint = models.IntegerField(
        label = "How confident do you feel in this answer now that you have discussed with your partner?",
        widget=LabeledSlider(
            before = "Not Confident",
            after = "Extremely Confident"
        )
    )


    #track question importance
    #importance = models.FloatField(widget=widgets.Slider(attrs={'step': '0.01'}))

    total_score = models.FloatField(initial = 0.0)

    #track the number of rescue events and drag-downs
    rescue_event = models.BooleanField()
    drag_down = models.BooleanField()

    #track number of times private was corrected
    corrected_private = models.BooleanField()
    uncorrected_private = models.BooleanField()


    #tracks whether participant has consented to not cheat
    cheat_consent = models.BooleanField(widget=djforms.CheckboxInput,
                                  initial=False
                                  )
    @property
    def partner(self):
        return self.get_others_in_group()[0]
    
    @property
    def is_correct(self):
        return self.submitted_answer_joint == self.question_solution
    
    @property
    def is_consensus(self):
        return self.submitted_answer_joint == self.partner.submitted_answer_joint

    @property
    def is_corrected_private(self):
        return self.submitted_answer_private != self.question_solution and self.submitted_answer_joint == self.question_solution

    @property
    def is_rescue(self):
        return self.is_corrected_private and self.partner.submitted_answer_private == self.question_solution
   
    @property
    def is_uncorrected_private(self):
        return self.submitted_answer_private == self.question_solution and self.submitted_answer_joint != self.question_solution

    @property
    def is_drag_down(self):
        return self.is_uncorrected_private and self.partner.submitted_answer_private == self.submitted_answer_joint

    @property
    def get_phase(self):
        if self.player.question_type == "EZ": 
            return 1
        elif self.player.question_type == "KD":
            return 2
        else:
            return 3

    def current_question(self):
        qid = self.participant.vars['q_order'][self.round_number-1]
        return Constants.questions[qid]

    def get_current_solution(self):
        return self.current_question()['solution']

    def get_current_question(self):
        return self.current_question()['question']

    def initial_wrong(self):
        return self.submitted_answer != self.solution
        
    def check_partner_correspondence(self):
        return self.submitted_answer == self.get_others_in_group()[0].submitted_answer
        
    def consensus_but_wrong(self):
        return self.get_others_in_group()[0].submitted_answer == self.submitted_answer != self.solution 
        
    def no_consensus(self):
        return self.get_others_in_group()[0].submitted_answer != self.submitted_answer
    
    def set_payoff(self):
        if(self.check_if_awarded_points()):
            self.total_score +=1


def custom_export(players):
    # header row
    yield ['session', 'session_name', 'participant_code', 'round_number', 'id_in_group', 'turk_id', 'politics', 'political_views', 'superpower', 'season', 'fruit', 'vacation', 'question_id', 'question_text', 'question_solution', 'question_choice_1', 'question_choice_2', 'question_choice_3', 'question_choice_4', 'question_type', 'my_chat_joint', 'chat_content_joint', 'my_chat_results', 'chat_content_results', 'blur_count_private', 'blur_count_joint', 'idle_private', 'idle_joint', 'time_spent_on_page_private', 'time_spent_on_page_joint', 'submitted_answer_private', 'submitted_answer_joint', 'confidence_private', 'confidence_joint', 'total_score', 'rescue_event', 'drag_down', 'corrected_private', 'uncorrected_private', 'partner_submitted_answer_private','partner_submitted_answer_joint', 'partner_confidence_private', 'partner_confidence_joint', 'partner_rescue_event', 'partner_drag_down' , 'partner_corrected_private', 'partner_uncorrected_private', 'sex', 'birth', 'race', 'income', 'education', 'zip_code',
    'partner_turk_id', 'partner_sex', 'partner_birth', 'partner_race', 'partner_income', 'partner_education', 'partner_zip_code', 'partner_politics']
    for p in players:
        yield [p.session.code, p.session.config.get('name'), p.participant.code, p.round_number, p.id_in_group, p.participant.vars.get('turk_id'), p.participant.vars.get('politics'), p.participant.vars.get('political_views'), p.participant.vars.get('superpower'), p.participant.vars.get('season'), p.participant.vars.get('fruit'), p.participant.vars.get('vacation'), p.question_id, p.question_text, p.question_solution, p.question_choice_1, p.question_choice_2, p.question_choice_3, p.question_choice_4, p.question_type, p.my_chat_joint, p.chat_content_joint, p.my_chat_results, p.chat_content_results, p.blur_count_private, p.blur_count_joint, p.idle_private, p.idle_joint, p.time_spent_on_page_private, p.time_spent_on_page_joint, p.submitted_answer_private, p.submitted_answer_joint, p.confidence_private, p.confidence_joint, p.total_score, p.rescue_event, p.drag_down, p.corrected_private, p.uncorrected_private, p.partner.submitted_answer_private, p.partner.submitted_answer_joint, p.partner.confidence_private, p.partner.confidence_joint, p.partner.rescue_event, p.partner.drag_down, p.partner.corrected_private, p.partner.uncorrected_private, p.participant.vars.get('sex'), p.participant.vars.get('birth'), p.participant.vars.get('race'), p.participant.vars.get('income'), p.participant.vars.get('education'), p.participant.vars.get('zip_code'), p.partner.participant.vars.get('turk_id'), p.partner.participant.vars.get('sex'), p.partner.participant.vars.get('birth'), p.partner.participant.vars.get('race'), p.partner.participant.vars.get('income'), p.partner.participant.vars.get('education'), p.partner.participant.vars.get('zip_code'), p.partner.participant.vars.get('politics')]
