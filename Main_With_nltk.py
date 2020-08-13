# -*- coding: utf-8 -*-
"""
Created on Aug 2020

@author: Anurag Joshi
"""
import string
import Twitter_analysis as twit_analysis
from collections import Counter
import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re


text = ""
def read_from_file(filename):
    file = open(filename,encoding='utf-8')
    text = file.read()
    return text

def fetch_twits(since,till,topic,quantity):
    text = ""
    text_tweets = twit_analysis.get_tweets(since,till,topic,quantity)
    for i in range(0,len(text_tweets)):
        text = text_tweets[i][0]+" "+text
    return text

def analyze(text,topic='text'):
    #converting all text to lower-case only:
    lower_text = text.lower()
    
    #removing punctuations or symbols from text
    cleaned_text = lower_text.translate(str.maketrans('','',string.punctuation));
    
    #tokens = cleaned_text.split() #it was slow so i used nltk word tokenizer
    #tokenizing cleaned_text into tokens list with specified language
    tokens = word_tokenize(cleaned_text,'english')
    
    #genrating final words by using nltk stopwords with specified language
    final_words = []
    for word in tokens:
        if word not in stopwords.words('english'):
            final_words.append(word)
            
    #the current step is most important where we mainly extract only words related to emotions/
    #or express emotions only.
    emotion_list = []
    with open('sentiments.txt','r') as emotionFile:
        for line in emotionFile:
            clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
            word,emotion = clear_line.split(':')
            word = word.strip()
            emotion = emotion.strip()
            if word in final_words:
                emotion_list.append(emotion)
                
    print('All Emotions list:',emotion_list)
    emotion_count = Counter(emotion_list)
    print('ans their counts:',emotion_count)
    
    #plotting main figure of sentimetal analysis:-    
    print('You would get a .png photo of analysis graph in your current directory named as:"emotionBar.png"')
    fig,ax1 = plt.subplots()
    ax1.bar(emotion_count.keys(),emotion_count.values())
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Emotions')
    ax1.set_title('sentiment analysis of '+topic)
    fig.autofmt_xdate()
    plt.savefig('emotionBar.png')
    plt.show();
    conclude_analysis(cleaned_text)

def conclude_analysis(text):
    print('CONCLUSION:-')
    vibes = SentimentIntensityAnalyzer().polarity_scores(text)
    print(vibes)
    if(vibes['pos']>vibes['neg']):
        print(':::::POSITIVE feed:::::)')
    elif(vibes['pos']<vibes['neg']):
        print(':::::NEGATIVE feed:::::(')
    else:
        print(':::::NEUTRAL:::::|')

def checkDate(date):
    pattern = re.compile("[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])")
    if pattern.match(date):
        return True
    else:
        print('Please enter valid date =>')
        return False
    

def Main():
    print('<------------------------------------------------------------>')
    print('Welcome to the sentimental analysis through text, \nand twitter twits on a topic within a period')
    print('<------------------------------------------------------------>\n')
    start = True
    while(start):
        print('\nChoose Option::>')
        print('\n1.Write something here for having analysis of that text (include some emotions):')
        print('2.Give input file(copy and paste any speech in that file) for analysis:')
        print('3.Twitter twits analysis on a topic within a period:')
        option = True
        while(option):
            print("Choose one option: from 1/2/3 and 0 for quit:- ")
            optionSelected = input()
            if optionSelected.isdigit():
                optionSelected = int(optionSelected)
                if(optionSelected==1 or optionSelected==2 or optionSelected==3 or optionSelected==0):
                    option = False
                else:
                    print('Enter 1/2/3/0 only.')
                
            else:
                print('Enter valid input')
                
        
        if optionSelected==1:
            print('Write anaything here: which express some emotions or paste anything')
            text = input()
            analyze(text)
            
        elif optionSelected == 2:
            filename = input('Enter full path of file: ')
            text = read_from_file(filename)
            analyze(text)
            
        elif optionSelected == 3:
            userInput = True
            print('Input start and end dates <yyyy-mm-dd form> till you want to analyze twitts:')
            since = ""
            while(userInput):
                since = input('\nStart date: ')
                if(checkDate(since)):
                    userInput = False
                    
            userInput = True
            till = ""
            while(userInput):
                till = input('\nEnd date: ')
                if(checkDate(till)):
                    userInput = False
                    
            topic = input('Enter the topic name: ')
            userInput =  True
            total = 0
            while(userInput):
                total = input('Enter the number of twitts on which you want to see analysis:/n \
                              < bigger the number more the time it would take and more accurate(<=100 for quick results) >\n ')
                if total.isdigit():
                    total = int(total)
                    userInput = False
            
            text = fetch_twits(since,till,topic,total)
            analyze(text,topic)
            
        elif optionSelected == 0:
            start = False
Main()

#i practiced with these stop_words then i got knowledge about nltk :|
#stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
