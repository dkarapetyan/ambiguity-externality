from otree.api import *


doc = """
a.k.a. Encryption Game
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = "encrypt_I"
    letters_per_word = 5
    use_timeout = True
    seconds_per_period = 480


class Subsession(BaseSubsession):
    dictionary = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    performance = models.IntegerField(initial=0)
    mistakes = models.IntegerField(initial=0)
    bonus = models.IntegerField(initial=0)
    earnings = models.CurrencyField(initial=0)
    bonus_question = models.CurrencyField(initial=0)
    final = models.CurrencyField(initial=0)
    tokens = models.IntegerField(initial=0)

# PAGES


class BeginEncryptionTask(Page):
    pass


class Task(Page):
    form_model = "player"
    form_fields = ["performance", "mistakes"]
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {
            "legend_list": legend_list,
            "task_list": task_list,
            "task_width": task_width,
        }


class Hidden(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.tokens_I = int(2*player.performance)


class Results(Page):
    pass



page_sequence = [
    BeginEncryptionTask,
    Task,
    Hidden,
    Results,
]
