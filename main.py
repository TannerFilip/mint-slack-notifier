#!/usr/bin/python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import mintapi
import slackweb

# Credentials for Slack and Mint
# TODO: Don't hardcode Mint creds in
slack = slackweb.Slack(url="CHANGEME")
mint = mintapi.Mint('USERNAME','PASSWORD')

# I was going to do this with sqlite, but that's overkill for a single number
f = open('nw.txt', 'r+')

oldAccountTotal = f.readline()
newAccountTotal = mint.get_net_worth()


if str(oldAccountTotal) != str(newAccountTotal):
    accountTotalString = str(newAccountTotal)
    # Lazy workaround to send dynamic information to channel
    # TODO: actually fix this
    notifyTextRaw = "@channel: Account change detected.", "Old balance:", str(oldAccountTotal), "New balance:", accountTotalString
    notifyText = str(notifyTextRaw)
    slack.notify(text=notifyText)
    # Update the file with the new total
    wr = open('nw.txt', 'w')
    wr.write(accountTotalString)
    wr.close()
    f.close()

else:
    f.close()
