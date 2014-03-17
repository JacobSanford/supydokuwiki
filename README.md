# SupyDokuWiki
Supybot plugin to query and parrot information from a dokuwiki instance.

The plugin supports dokuwiki authentication through the 'requests' module. 

Supybot will respond to a message in the channel ending in two question marks.
The plugin then takes that entire message and searches the dokuwiki instance for a matching page.
It will relay any text that is in the first paragraph immediately following a level1 header.

## Setup
Edit dokuConfig.py.example as appropriate and save as dokuConfig.py 

## Requirements
### python
- BeautifulSoup (https://pypi.python.org/pypi/BeautifulSoup/)
- requests (https://pypi.python.org/pypi/requests/)
