Readme
=======

This will hold all my little bitcoin experiments. In particular, I'm interested
in how Bitcoin brings back a sense of decentralization that the internet was
well known for in addition to its more libertarian implications i.e. we don't
need government fiat money anymore. So I've decided to play around with my little
diddlies to do so.


`setup.sh`
----------
This will install all the requirements we need. Not perfect as I don't build for
symbolic links.



`accept_payments.py`
---------------------
Inspired by [this post](http://incoherency.co.uk/blog/stories/how-to-accept-bitcoin-payments.html).

Idea is to create wallets for every transaction, which then get periodically sweeped.
I use the `Blockchain.info` API to check for transactions on a given wallet.

Apparently, there's a better [way](http://docs.electrum.org/en/latest/merchant.html) to do this with electrum.

