import os

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
LOCAL = os.environ.get('LOCAL', 'False').lower() == 'true'
SHOW_DEBUG_TOOLBAR = os.environ.get(
    'SHOW_DEBUG_TOOLBAR', 'False').lower() == 'true'


def custom_show_toolbar(self):
    return SHOW_DEBUG_TOOLBAR


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

ADMINS = []
admins = os.environ.get('ADMINS', '')
if admins:
    ADMINS = [
        (
            admin.strip(),
            admin.strip(),
        ) for admin in admins.strip(',').split(',')
    ]
