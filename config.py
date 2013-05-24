import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('supydokuwiki', True)

supydokuwiki = conf.registerPlugin('supydokuwiki')
conf.registerChannelValue(supydokuwiki,'enable',registry.Boolean('False',"""Enable displaying messages from supydokuwiki in channel?"""))
