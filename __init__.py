"""
This plugin looks up and parrots information from dokuwiki
"""

import supybot
import supybot.world as world

__version__ = "main"
__author__ = supybot.Author("Jacob Sanford","JS","jsanford@unb.ca")
__contributors__ = {}
__url__ = 'https://github.com/JacobSanford/SupyDokuWiki'

import config
import plugin
reload(plugin)

if world.testing:
    import test

Class = plugin.Class
configure = config.configure
