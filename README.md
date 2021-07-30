# Slackbot for cats on craigslist

I'm hoping to rescue a cat in the next month or two. This very simple Slackbot tells me what cats are on Craigslist in my area. Created using [this as reference](https://www.dataquest.io/blog/apartment-finding-slackbot/).

![catbot](https://github.com/emmaremy/craigslist-cats/blob/main/catbot.png)

To use:
* Install `requirements.txt` (uses Python 2.7)
* Create a file named `secrets.yaml` containing [your API token](https://api.slack.com/custom-integrations/legacy-tokens), following the example in `example.yaml`
* Run `nohup python cats.py &` [(if you close your terminal or restart or something you'll have to run it again)](https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day)

This was created primarily for personal educational purpose. I'm not trying to make any money or get large amounts of information from craigslist (please don't sue me).
