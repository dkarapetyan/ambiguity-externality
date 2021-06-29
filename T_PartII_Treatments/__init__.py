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
    with open('T_partII_Treatments/bluematch.csv', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))


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
            player.participant.ext_choice = int(Constants.rows[random.randint(0, (len(Constants.rows) - 1))]['R_PartII_EncryptionTask.1.player.externality'])
            print('externality choice is', player.participant.ext_choice)
            player.participant.externality_II = cu((2-player.participant.ext_choice)*(int(Constants.rows[random.randint(0, (len(Constants.rows) - 1))]['R_PartII_EncryptionTask.1.player.performance'])*player.session.config['real_world_currency_per_point']))
        else:
            if player.participant.externality_II == 2:
                player.part_rate = 0.08
        player.participant.payoff_II = cu(max(((player.participant.performance_II * player.part_rate)-player.participant.externality_II), 0))


class ChoiceTreatment(Page):
    pass


page_sequence = [Hidden, ChoiceTreatment]
