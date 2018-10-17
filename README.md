# Slackbot for cats on craigslist

I'm hoping to rescue a cat in the next month or two. This very simple Slackbot tells me what cats are on Craigslist in my area. Created using [this as reference](https://www.dataquest.io/blog/apartment-finding-slackbot/).

To use or adapt for your own purposes:
* Install `requirements.txt` (uses Python 2.7)
* Create a file named `secrets.yaml` containing your API token, following the example in `secrets.yaml`
* Run `nohup python cats.py &` [(if you close your terminal or restart or something you'll have to run it again)](https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day)
