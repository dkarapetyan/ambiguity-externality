from otree.api import *
import csv
import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'T_PartII_Treatments'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice_info = models.BooleanField()
    part_rate = models.CurrencyField()


def creating_session(subsession):
    import itertools
    choice = itertools.cycle([True, False])
    for player in subsession.get_players():
        player.choice_info = next(choice)
        print('choice information is ', player.choice_info)


# PAGES
class Hidden(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.part_rate = 0.1
        player.participant.externality_II = 0
        player.participant.ext_choice = 1
        if player.session.config['name'] == "victim":
            player.participant.externality_II = cu(20*player.session.config['real_world_currency_per_point'])
        else:
            if player.participant.externality_II == 2:
                player.part_rate = 0.08
        player.participant.payoff_II = cu(max(((player.participant.performance_II * player.part_rate)-player.participant.externality_II), 0))


class ChoiceTreatment(Page):
    pass


page_sequence = [Hidden, ChoiceTreatment]
