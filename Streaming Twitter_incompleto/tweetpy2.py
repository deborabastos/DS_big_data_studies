#importa bibliotecas
import tweepy as tw
import socket #para ler portas, enviar e receber dados pela porta
import time
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Set up das credenciais
consumer_key = os.environ['api_key']
consumer_secret = os.environ['api_secret_key']
token = os.environ['beares_token']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

class TweetsListener(tw.Stream):
    def __init__(self, *args, csocket):  #construtor
        super().__init__(*args)
        self.client_socket = csocket
        self.count=0
        self.limit=10 #limite de 5 tweets apenas para não rodar infinito

    def on_data(self, data):
        try:
            print("entrou try") 
            msg = json.loads(data) 			#lê os twitters
            self.count+=1            			#incrementa o contador
            if self.count<=self.limit:    
                print(msg['text'].encode("utf-8"))	#verifica a quantidade de twitters lidos
                print("-----------------------------------------------------------")
                self.client_socket.send(msg['text'].encode("utf-8")) #envia a mensagem para o socket #ERRO AQUI!!!!! MANDANDO PARA EXCEPT ## Prov;avelmente por conta de unicode
                time.sleep(1)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            print("-----------------------------------------------------------")
        return True

    def on_error(self, status):
        print(status)
        return True

def sendData(c_socket):     				#define como os dados devem ser enviados

    try:
        twitter_stream = TweetsListener(
        consumer_key, consumer_secret,
        access_token, access_token_secret,
        csocket=c_socket
    )

        twitter_stream.filter(track=['BBB23'])  #define o filtro a ser utilizado 


    except Exception as e:
        print(f'Não foi possível estabelecer conexão com Twitter. ERRO: {e}')
    

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Cria o objeto socket (protocolo IPv6, TCP)
    host = "127.0.0.1"     # Obtém o "nome/endereço" local da maquina (localhost)
    port = 9995                 # Identifica e define a porta a ser utilizada.
    s.bind((host, port))        # Bind para a porta

    print("Listening on port: %s" % str(port))

    s.listen(5)                 # Aguarda a conexão.
    c, addr = s.accept()        # Estabelece a conexão.

    print("Received request from: " + str(addr))

    sendData(c)
