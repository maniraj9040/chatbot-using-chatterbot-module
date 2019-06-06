from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# import time
import pyttsx3
import nltk

# timing = []
# def timer():
#
#     localtime = time.asctime( time.localtime(time.time()) )
#     print ("Local current time :", localtime)
#     timing.append(localtime.split(" "))
#     print(timing)
#     clock= timing[0][3]
#     return clock



def get_response(data):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'

        },

        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],

    trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    # hours = timer()
    # print(hours)
    # k = pyttsx3.init()
    while True:
        if usrText.strip() != 'Bye':
            result = bot.get_response(usrText)
            print(result)
            # reply = result

            # k.say(usrText)
            # k.runAndWait()
            return(result.capitalize())
        if usrText.strip() == 'Bye':
            print('Bye')
            break
        

        
