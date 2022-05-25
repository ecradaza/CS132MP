import tweepy
import logging
import json
from datetime import datetime
import random
# Authenticate to Twitter
auth = tweepy.OAuthHandler("9BIQxQx1gg3DLVlU3bHBeHRjC", "ZIxQ029NBCkcGwbhmgPwKLC11psfNfuSALeBSvvQTlkgcyCtt4")
auth.set_access_token("1417308731725942791-jf347s0CqwVzVk1Ri85lsbazkdf1bx", "bHQ5n6GxPYq8LHB9368k0kxPYPLeIySrwMt76X5fFmrVg")
api = tweepy.API(auth)
#bot main
