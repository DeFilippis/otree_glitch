import csv
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import random, string

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.db import models as djmodels
from datetime import datetime, timezone

author = 'Evan DeFilippis'

doc = """
This application takes answers from an intake form in the previous app and asks shows those answers to another participant
"""


class Constants(BaseConstants):
    name_in_url = 'know_your_partner_new'
    num_rounds = 1
    players_per_group = 2


class Subsession(BaseSubsession):
    def extra_task_to_decorate_start_of_get_players_for_group(self, waiting_players):
        app_name = self._meta.app_label
        round_number = self.round_number
        endofgamers = [p for p in waiting_players if (
                p.participant.vars.get('go_to_the_end') or p.participant.vars.get(
            'skip_the_end_of_app_{}'.format(app_name)) or p.participant.vars.get(
            'skip_the_end_of_app_{}_round_{}'.format(app_name, round_number))
        )]
        if endofgamers:
            return endofgamers
    
    # def group_by_arrival_time_method(self, waiting_players):
    #     grouped = self.extra_task_to_decorate_start_of_get_players_for_group(waiting_players)
    #     if grouped:
    #         # form groups of only one when a players decides to finish the experiment--> otherwise,
    #         # there might be problems later during ordinary wait pages
    #         return [grouped[0]]
        
    #     if len(waiting_players)>1:
    #         return waiting_players[:2]
        
    def group_by_arrival_time_method(self, waiting_players):
        if len(waiting_players) > 1:
            return waiting_players[:2]
        for player in waiting_players:
            if player.waiting_too_long():
                # make a single-player group.
                player.participant.vars['go_to_end'] = True
                return [player]

class Group(BaseGroup):
    team_id = models.CharField()
       
class Player(BasePlayer):
    def waiting_too_long(self):
        arrival_time =  datetime.now(tz=timezone.utc)
        # change to 15 minutes...
        diff = (arrival_time - self.participant.vars.get('arrival_time_on_leavable_wait_page')).total_seconds() >  20
        return diff

    def get_participant_data(self, fields):
        fields = [fields] if isinstance(fields, str) else fields
        res = {f: self.participant.vars.get(f) for f in fields}
        return res
    
    @property
    def partner(self):
        return self.get_others_in_group()[0]
    
    partner_politics = models.StringField()
    partner_political_views = models.StringField()
    partner_superpower = models.StringField()
    treatment_condition = models.StringField()

    #total_waiting_time = models.FloatField()
    #payment_for_wait = models.FloatField()
    
    # Tracks the total number of times they incorrectly submitted answers to the know-your-partner quiz
    number_incorrect_submissions = models.IntegerField(initial = 0)

    # Variables for generating form fields on know your partner quiz 
    kyp_politics =  models.StringField(
        label = "As of today, does your partner lean more to the Republican Party or more to the Democratic Party?",
        choices=['Republican', 'Democrat'],
        widget=widgets.RadioSelect) 
    
    kyp_superpower =  models.StringField(
        label = "Which of the following superpowers would your partner most prefer to have?", 
        choices= ["Invisibility", "Super Strength", "Ultra High Intelligence", "Flight"],
        widget=widgets.RadioSelect) 

    def other_player(self):
        return self.get_others_in_group()[0]
    

      
