import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('SupyDokuWiki', True)

SupyDokuWiki = conf.registerPlugin('SupyDokuWiki')
conf.registerChannelValue(SupyDokuWiki,'enable',registry.Boolean('False',"""Enable displaying messages from SupyDokuWiki in channel?"""))
