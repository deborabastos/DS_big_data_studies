#importa bibliotecas
import tweepy as tw
import os
from dotenv import load_dotenv
load_dotenv()

# Set up das credenciais
consumer_key = os.environ['api_key']
consumer_secret = os.environ['api_secret_key']
token = os.environ['beares_token']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

# Conecta com API do Twitter
client = tw.Client(token, consumer_key, consumer_secret, access_token, access_token_secret)

# Esse código somente é usado se for necessários usar algumas funções da antiga versão do tweepy
auth = tw.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tw.API(auth)

