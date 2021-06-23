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
    pass

class Group(BaseGroup):
    pass

        
class Player(BasePlayer):
   pass

