import random

from otree.api import *

author = 'LEDR Team'

doc = """
Standard welcome pages for LEDR experiments
"""


class Constants(BaseConstants):
    name_in_url = 'outro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


def creating_session(subsession):
    for player in subsession.get_players():
        player.participant.random_part = random.choice(['I', 'II'])


#PAGES

class Hidden(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.participant.random_part == 'I':
            if player.session.config['name'] == "victim":
                player.participant.payoff = player.participant.payoff_I + player.participant.dictator_I + \
                                        player.session.config['participation_fee']
            else:
                player.participant.payoff = player.participant.payoff_I + \
                                        player.session.config['participation_fee']
        else:
            if player.session.config['name'] == "victim":
                player.participant.payoff = player.participant.payoff_II + player.participant.dictator_II + \
                                        player.session.config['participation_fee']
            else:
                player.participant.payoff = player.participant.payoff_II + \
                                        player.session.config['participation_fee']



class ThankYou(Page):
    pass


page_sequence = [Hidden, ThankYou]
