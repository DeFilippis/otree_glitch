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
from datetime import datetime, timezone, timedelta

author = 'Evan DeFilippis'

doc = """
This application takes answers from an intake form in the previous app and asks shows those answers to another participant
"""


class Constants(BaseConstants):
    name_in_url = 'grouping_page_glitch'
    num_rounds = 1
    players_per_group = 2


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass       

class Player(BasePlayer):
    pass
      
