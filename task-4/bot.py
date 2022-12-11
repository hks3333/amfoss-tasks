import os
import telebot
import requests
import json
import csv


yourkey = os.getenv('API_KEY')
bot_id = os.getenv('BOT_ID')
bot = telebot.TeleBot(bot_id)
@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')

    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    

@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    value=message.text.partition(' ')[2]
    url="http://www.omdbapi.com/?apikey="+yourkey +"&t="+value
    info=requests.get(url).json()
    st=''
    rows=[]
    for i in info:
        if i not in ("BoxOffice","Rated","Released","Runtime","Production","Website","Response","DVD","Type","imdbVotes","imdbID","Ratings","Country"):
            st=st+i+": "+str(info[i])+"\n"
            if i not in ("Poster","Director","Writer","Actors","Awards","Metascore"):
                rows.append(info[i])
    with open("movies.csv",'a') as file:
        wrt=csv.writer(file)
        wrt.writerow(rows)
    bot.reply_to(message, st)
    
  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    
    bot.reply_to(message, 'Generating file...')
    f=open("movies.csv",'r')
    bot.send_document(message.chat.id, document=f)
    

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
