from otree.api import *

doc = """
a.k.a. Part II Encryption Instructions 
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = "encrypt_instructions"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES

class FirstTaskInstructions2(Page):
    pass


page_sequence = [FirstTaskInstructions2]
