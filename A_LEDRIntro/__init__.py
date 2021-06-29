from otree.api import *

c = Currency

author = 'LEDR Team'

doc = """
Standard welcome pages for LEDR experiments
"""


class Constants(BaseConstants):
    name_in_url = 'A_LEDRIntro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific = models.IntegerField(label="Your Prolific ID:")


# PAGES

class Welcome(Page):
    form_model = 'player'
    form_fields = ['prolific']

page_sequence = [Welcome]
