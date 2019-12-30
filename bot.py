from random import seed
from random import randint
import tweepy
import time
from keys import *
seed(1)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print('this is my twitter bot', flush=True)
api.update_status('Hoy no cumple años ningún miembro de Karmalaand 4' + str(randint(0,600)))