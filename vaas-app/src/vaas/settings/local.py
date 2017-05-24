# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import re
import os

from .base import *
from keyword import iskeyword

DEBUG = True
TEMPLATE_DEBUG = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--exclude-dir=vaas/settings']

module_name = re.compile('^(?!_)[_a-z]+(?<!_)$')
plugin_dir = os.path.dirname(__file__) + "/../plugins"

for plugin_dir in os.listdir(plugin_dir):
    if not iskeyword(plugin_dir) and module_name.match(plugin_dir):
        app_name = "vaas.plugins.{}".format(plugin_dir)
        if not app_name in INSTALLED_APPS:
            INSTALLED_APPS += (app_name, )

from .ldap import *
