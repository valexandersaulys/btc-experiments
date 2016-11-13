import requests
from subprocess import Popen, PIPE

# First we create the amount we want for a given transaction in BTC
AMOUNT = 0.0;

# Generate the keys
session = Popen(['./keyconv','-G'],stdout=PIPE,stderr=PIPE)   # generate the key
stdout,stderr = session.communicate()
public_key = stdout.split('\n')[2][9:]  # get public key
private_key = stdout.split('\n')[2][9:]  # get private_key
# (NOTE: you'd probably want to store the private key somewhere too for periodic sweeping)

# Then we check for a transaction on the Blockchain.info API
r = requests.get("https://blockchain.info/rawaddr/%s" % public_key)
print r.json()
"""
{
u'total_sent': 0, 
u'total_received': 0, 
u'final_balance': 0, 
u'address': u'1PHsaVve49JoWXdMr9iHdAAkZn4mg71qWJ', 
u'hash160': u'f483a485181e6351e20f8b6b10a0b7baa0bf33ca', 
u'txs': [], 
u'n_tx': 0
}
"""

# Check and run a sweep if its good
if r.json()['final_balance']==AMOUNT:
    # sweep the wallet(s)...good way to do this?
    # http://docs.electrum.org/en/latest/merchant.html
