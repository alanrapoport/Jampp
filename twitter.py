# El siguiente script de Python recibe una lista de strings como argumento y almacena los twitts que contengan dichos strings.
# Utilizamos la librería Tweepy.
# Cada minuto se abre un nuevo archivo para almacenar los twitts. La forma de generar un nuevo archivo cada minuto se
# realiza asignándole al archivo a escribir un nombre con la fecha, hora y minutos actuales. Si bien es una forma sencilla
# de haccerlo, no es la manera más óptima, ya que este método no permite seleccionar una cantidad específica de segundos.

import tweepy
import json
import sys
import time

class MyListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        timestr = time.strftime("%Y%m%d-%H%M")
        file_name = 'tweets_' + timestr + '.json'
        with open(file_name, 'a') as out:
            out.write(raw_data)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False


class MyStream():

    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list)


if __name__ == "__main__":

    consumer_key = 'WHpxJQRlXQm3Jwk6maCwvCUdT'
    consumer_secret = 'BD0FKqOBmEHCSUKucBEhPtKPzFBHu8jljDH5KxoCTrfRWMJBoL'

    access_token = '1158958358466088961-xxqcvGzL938AFsxEepXPPePduCLefJ'
    access_token_secret = 'CW1K4vfSN82gsb7nnX4T9DbMW7lDiN9Z6QupLLWQG7zkU'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    listener = MyListener()
    stream = MyStream(auth, listener)
    stream.start(sys.argv[1:])
