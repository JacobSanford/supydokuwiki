from BeautifulSoup import BeautifulSoup
import dokuConfig as dokuConfig
import os
import re
import requests
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
from supybot.commands import *
import urllib

class supydokuwiki(callbacks.Plugin) :
    """Add the help for "@plugin help supydokuwiki" here
    This should describe *how* to use this plugin."""
    threaded = True

    def doPrivmsg(self, irc, msg) :
        if(self.registryValue('enable', msg.args[0])):
            match = re.search(
                              '^(.*)\?\?$',
                              msg.args[1],
                              re.IGNORECASE
                              )
            if match:
                query_string = match.group(1)
                irc.queueMsg(
                             ircmsgs.privmsg(
                                             msg.args[0],
                                             self.get_auery_summary_string(
                                                                           query_string
                                                                           )
                                             )
                             )

    def get_best_link_on_page(self,session,raw_search_page_html):
        first_href = False
        soup = BeautifulSoup(raw_search_page_html)
        results_dl = soup.find('ul', attrs = {'class' : 'search_quickhits'})
        if results_dl :
            first_link = results_dl.find('a')
            if first_link :
                first_href = first_link.get('href')
        return first_href

    def get_entry_summary_string(self, session, target_page_url) :
        target_page_get_result = session.get(
                                             os.path.join(
                                                          dokuConfig.root_url,
                                                          target_page_url
                                                         )
                                            )
        target_page_tree = BeautifulSoup(target_page_get_result.text)
        first_div = target_page_tree.find(
                                          'div',
                                          attrs = { 'class': 'level1' }
                                          )
        paragraph_to_return = first_div.find('p')
        if paragraph_to_return :
            return BeautifulSoup(
                                 paragraph_to_return.text,
                                 convertEntities = BeautifulSoup.HTML_ENTITIES
                                 ).contents[0]
        else:
            return 'No summary, but visit ' + os.path.join(
                                                           dokuConfig.root_url,
                                                           target_page_url
                                                           )

    def get_auery_summary_string(self, query_string) :
        session = requests.session()
        target_article_link = self.get_best_link_on_page(
                                   session,
                                   self.get_search_result_page(
                                                               session,
                                                               query_string
                                                               )
                                   )
        if target_article_link :
            return self.get_entry_summary_string(
                                                 session,
                                                 target_article_link.lstrip('/')
                                                 )
        return "No docs found for " + query_string

    def get_search_result_page(self, session, query_string) :
        login_url = os.path.join(
                                 dokuConfig.root_url,
                                 dokuConfig.base_path,
                                 dokuConfig.login_path
                                 )
        search_url = os.path.join(
                                  dokuConfig.root_url,
                                  dokuConfig.base_path,
                                  dokuConfig.search_path,
                                  urllib.quote_plus(query_string)
                                  )
        login_data = {
            'u': dokuConfig.user_name,
            'p': dokuConfig.password,
            'submit': 'Login',
        }
        login_page_get_result = session.get(login_url)
        login_post_result = session.post(login_url, data = login_data)
        return session.get(search_url).text

Class = supydokuwiki
