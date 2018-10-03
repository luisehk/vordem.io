from django.apps import AppConfig


class TeamsConfig(AppConfig):
    name = 'publicomex.apps.teams'
    label = 'publicomex_teams'
    verbose_name = 'Teams'

    def ready(self):
        pass
