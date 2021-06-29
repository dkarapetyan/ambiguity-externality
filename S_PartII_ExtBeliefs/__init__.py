from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'S_PartII_ExtBeliefs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice_guess = models.IntegerField(
        label="Do you think the blue player decreased your earnings in Part 2?",
        widget=widgets.RadioSelect,
        choices=[[1, "No"], [2, "Yes"]],
    )
    externality_guess2 = models.CurrencyField(label="How much do you think the blue player decreased your earnings by in Part 2?")


# PAGES
class ExtBeliefs2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim"
    form_model = "player"
    form_fields = ['choice_guess']


class ExtBeliefs2a(Page):
    @staticmethod
    def is_displayed(player: Player):
        if player.session.config['name'] == "victim" and player.choice_guess == 2:
            return True
    form_model = "player"
    form_fields = ['externality_guess2']


page_sequence = [ExtBeliefs2, ExtBeliefs2a]
