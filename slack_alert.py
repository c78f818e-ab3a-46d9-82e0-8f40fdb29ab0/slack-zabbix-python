#!/usr/bin/env python

# imoprt
from slacker import Slacker
import logging
import json
import sys

# variables
token = 'xoxb-27998482242-wEajhKb8yWwP705MM6WPrUnK'
incomingwebhook = 'https://hooks.slack.com/services/T050VB4F4/B0TVBUZTL/zkJY65jflX7HxX14tW98
lNMW'
username = 'Zabbix'

# functions
def parse_alert_message(raw):
    color = None
    emoji = None
    if raw['Status'] == 'PROBLEM':
        color = 'danger'
        emoji = ':frowning:'
    elif raw['Status'] == 'OK':
        color = 'good'
        emoji = ':smile:'
    attach = [
                {
                    'color': color,
                    'fallback': '[' + raw['Status'] + '] ' + raw['Trigger'],
                    'title': raw['Trigger'],
                    'title_link': raw['URL'],
                    'fields': [
                        {   'title': 'Status',
                            'value': raw['Status'],
                            'short': True
                        },
                        {   'title': 'Severity',
                            'value': raw['Severity'],
                            'short': True
                        },
                        {   'title': 'EventID',
                            'value': raw['EventID'],
                            'short': True
                        },
                        {   'title': 'ItemValue',
                            'value': '\n'.join(raw['ItemValues']),
                            'short': False
                        }
                   ]
              }
            ]
    return emoji, attach

# Main
argv = sys.argv

channel = argv[1]
text = argv[2]
raw = json.loads(argv[3])
s = Slacker(token = token, incoming_webhook_url = incomingwebhook)

text = '[' + raw['Status'] + '] ' + raw['Trigger'] + ' - ' + raw['Hostname'] + ' (' + \
        raw['IP'] + ')'
emoji, attach = parse_alert_message(raw)

r = s.chat.post_message(
    channel = channel, \
    text = text, \
    attachments = attach, \
    username = username, \
    icon_emoji = emoji)

logging.basicConfig(filename='/var/log/zabbix/zabbix_slack_v2.log',level=logging.DEBUG)
logging.debug(argv)
logging.debug(r.successful)

# vim: tabstop=4 softtabstop=4 shiftwidth=4 expandtab autoindent
