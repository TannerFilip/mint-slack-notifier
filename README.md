This script uses a Mint API to check if your account balances have changed, and notifies you on Slack if it has.

## Setup
The setup is pretty straightforward. Just setup an incoming webhook on Slack - you can do so at `https://$YOURTEAM.slack.com/services/`. Add the URL to line 12 where it says `CHANGEME` - keep it wrapped in quotes. Put your Mint username and password on the line directly following the URL, and you should be good.

Note, by default this script runs once and exits. If you want it to regularly check, the easiest way would be to set up a cronjob. This is what I use, to run it hourly:

`0 * * * * python PATH_TO_DIRECTORY/main.py > /var/log/mint-notifier.log`

