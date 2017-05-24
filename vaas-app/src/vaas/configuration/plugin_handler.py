# -*- coding: utf-8 -*-
import re
import os

from keyword import iskeyword

PLUGINS = tuple()
module_name = re.compile('^(?!_)[_a-z]+(?<!_)$')
plugin_dir = os.path.dirname(__file__) + "/../plugins"

for plugin_dir in os.listdir(plugin_dir):
    if not iskeyword(plugin_dir) and module_name.match(plugin_dir):
        app_name = "vaas.plugins.{}".format(plugin_dir)
        if not app_name in INSTALLED_APPS:
            PLUGINS += (app_name, )
