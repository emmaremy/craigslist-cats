from craigslist import CraigslistCommunity
from slackclient import SlackClient
import yaml

# Craigslist part
cl = CraigslistCommunity(site='washingtondc', area='doc', category='pet')
results = cl.get_results(sort_by='newest', limit='20')

# Slack part
# (slack doesn't want me to use API tokens anymore but I don't care)
with open('secrets.yaml', 'r') as f:
    secrets = yaml.load(f)
token = secrets['api_key']
channel = "#emmas-bots"
sc = SlackClient(token)

# Filter results
cat_s = ['kitten', 'cat', 'kitty', 'tabby', 'calico', 'tuxedo', 'tortie', 'torbie']
for result in results:
    if any(partial_cat in result['name'].lower() for partial_cat in cat_s):

        # Send to slack
        text = "{} | {} | <{}>".format(result['datetime'], result['name'], result['url'])
        sc.api_call(
                "chat.postMessage", channel=channel, text=text,
                username="catbot", icon_emoji=':leopard:'
                )
