from random import seed
from random import randint
import tweepy
import time
import datetime
from keys import *
seed(time.time())

day = datetime.date.today().strftime("%d-%m")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

cumples = {
    "12-04": "Vegetta @vegetta777",
    "09-05": "Willyrex @WillyrexYT",
    "21-05": "Alexby @aLexBY11",
    "03-08": "Luzu @LuzuGames",
    "13-02": "Rubius @Rubiu5",
    "26-05": "Mangel @mangelrogel",
    "06-07": "Fargan @xFaRgAnx",
    "13-08": "Lolito @LOLiTOFDEZ",
    "05-11": "Auron @auronplay"
}

print(day, flush=True)

msg = "Hoy no cumple años ningún miembro de Karmaland 4"
if(day in cumples):
    msg = "Hoy cumple años "+cumples[day]
api.update_status(msg)
