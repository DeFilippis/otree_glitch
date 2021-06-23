from os import environ
import os

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
POINTS_DECIMAL_PLACES = 2
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="",
    use_browser_bots=False,
)

SESSION_CONFIGS = [
  
   dict(
        name='Glitch_Test',
        display_name="Glitch_Test",
        num_demo_participants=2,
        app_sequence=['consent_glitch', 'grouping_page_glitch', 'trivia_glitch'],
    ),

  ]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

OTREE_AUTH_LEVEL = 'STUDY'

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = "blahblah"

DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = "dog"

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


