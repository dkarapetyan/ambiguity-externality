from otree.api import *
import csv
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'I_PartI_RevealEarnings'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES


class Hidden(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        #the variable name at the end of the next line might change when we run it properly with a "H_" prefix
        player.participant.externality_I = cu(0)
        if player.session.config['name'] == "victim":
            player.participant.externality_I = cu(20*player.session.config['real_world_currency_per_point'])
        player.participant.payoff_I = cu(max((player.participant.tokens_I*player.session.config['real_world_currency_per_point'])-player.participant.externality_I, 0))


class Results(Page):
    pass


page_sequence = [Hidden, Results]
