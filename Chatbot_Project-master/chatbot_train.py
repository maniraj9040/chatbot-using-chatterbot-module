from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import os


def setup():
    chatbot = ChatBot('Bot',
                      storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      trainer='chatterbot.trainers.ListTrainer')
    chatbot.set_trainer(ListTrainer)
    # for file in os.listdir('D:/python/PycharmProjects/venv/Lib/site-packages/chatterbot_corpus/data/english/'):
    #     convData = open(r"D:/python/PycharmProjects/venv/Lib/site-packages/chatterbot_corpus/data/english/"+file,'r').readlines()
    #     chatbot.train(convData)

    # data = open(r"C:/Users/mlangaru.OSIUS/Desktop/New folder/tables.yml",'r').readlines()
    data ="i am maniraj from hyderabad"
    chatbot.train(data)


    print("Training completed")


setup()
