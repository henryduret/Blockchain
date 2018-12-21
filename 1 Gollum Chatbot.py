#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nltk.download()


# In[ ]:


# nltk = Natural Langage Toolkit, see explanatory document for further development
import nltk 
import numpy as np
import random
# The import below enables to process standard python strings
import string 


# In[ ]:


# Path below is relative, to be able to chat with the both it's required to have the "lordofthering" text file in the same folder than Anaconda3
f=open('/Users/Henry/lordofthering.txt','r',errors = 'ignore') 
raw=f.read()
# Function below converts to lowercase
raw=raw.lower()
# Function below converts to list of sentences 
sent_precious = nltk.sent_tokenize(raw)
# Function below converts to list of words
word_precious = nltk.word_tokenize(raw)


# In[ ]:


#We use WordNet, an English dictionary included in NLTK
ring = nltk.stem.WordNetLemmatizer() 

# We need a function that lemmatize words of a sentence so that each one can be analyzed as a single item
def RingPrecious(swords):
    return [ring.lemmatize(sword) for sword in swords]

# We remove all the punts included in the text so that we are able to work with it
remove_dot_ring = dict((ord(dot), None) for dot in string.punctuation)

# We define the function that tokenize inputs, i.e. that creates a sequence of tokens
def RingNormalize(arrow):
    return RingPrecious(nltk.word_tokenize(arrow.lower().translate(remove_dot_ring)))


# In[ ]:


# We want our chatbot to be able to greet the user

# List below is all possible inputs that the chatbot will recognize
start_inputs = ("hello", "hey","hi","greetings","good morning", "good afternoon","good evening")
# List below is all possible outputs that the chatbot will be able to return
start_outputs = ["the Master is talking to me? I'm so glad", "Precious, ask us questions","GOLLUM GOLLUM GOLLUM","Where is the precious ?"]

# Function below check if the user input is a known greeting, if yes it randomly returns a greeting from our predefined list
def gollumanswer(inputs): 
    for word in inputs.split():
        if word.lower() in start_inputs:
            return random.choice(start_outputs)


# In[ ]:


# We want our chatbot to be able to identify if the user is asking a question

def last(master_input):
    splint_ring=[]
    Frodo=[]
    # We split all words of the user input in a list
    splint_ring=master_input.split()
    # We use the last item of the previously defined list. Later on, we will check if it's '?'. If yes, it means the user is asking a question.
    Frodo= splint_ring[len(splint_ring)-1]
    return (Frodo)


# In[ ]:


# The list below will be used in case we identify that the user input is a question
gollumpanic =["The Master is tough", "Master should be resting, Master needs to keep up his strength", "Stop asking questions you fat Hobbit"]


# In[ ]:


# We import a class that enables to get words that are distinctive and create a matrix
from sklearn.feature_extraction.text import TfidfVectorizer


# In[ ]:


# We import a class that enables to measure similarity between two vectors
from sklearn.metrics.pairwise import cosine_similarity


# In[ ]:


# Function below identifies what the user is asking for and return the appropriate part

def questofthering(master_input):
    gollum_output=''
    sent_precious.append(master_input)
    TfidfVec = TfidfVectorizer(tokenizer=RingNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_precious)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    # If we are not able to identify what the user is asking for, we tell the user that we are not able to fulfill her request
    if(req_tfidf==0):
        gollum_output=gollum_output+"YOU SHALL NOT PASS. Sméagol wants you to rephrase"
        return gollum_output
    # If we are able to identify what the user is asking for, we return the appropriate part
    else:
        gollum_output = gollum_output+sent_precious[idx]
        return gollum_output


# In[ ]:


# We are now ready to create the discussion flow between the user and our chatbot

# We define a value that will enable to stop, or not, the while loop that we want to use: indeed, as long as the user doesn't stop the conversation we want to continue 
flag=True

# Below is the welcoming message to give some brief instructions to the user
print("GOLLUM: Sméagol is here to serve the Master. Ask Sméagol about the precious: introduction, prologue, the fellowship, thetwotowers, thereturnoftheking, influences, legacy. Sméagol can develop further if you say more[categoryname]. I can also develop on each protagonist, just say 'allprotagonists' to have the list and then type first name. Finally, Sméagol knows 20 fun facts, just say funfact[number]. BE CAREFUL: Say 'precious' to stop talking to Sméagol.")

while(flag==True):
    master_input = input()
    master_input=master_input.lower()
    # In the following structure we try to identify different possibilites that are numbered
    # Possibility 1: is the user asking to stop the conversation by saying the stop word exposed in the welcoming message ?
    if(master_input!='precious'):
        # Possibility 2: is the user thanking the bot, meaning she doesn't want more information ?
        if(master_input=='thanks' or master_input=='thank you' ):
            flag=False
            print("GOLLUM: Let the precious be with you")
        else:
            # Possibility 3: is the user simply greeting the bot before beginning the conversation ?
            if(gollumanswer(master_input)!=None):
                print("GOLLUM: "+gollumanswer(master_input))
            else:
                # Possibility 4: is the user asking a question, i.e. ending her input with a '?' ?
                if (last(master_input)=='?'):
                    print("GOLLUM: "+random.choice(gollumpanic))
                # If the previous possibilites don't occur, it means we can run the algorithm previously elaborated for our chatbot
                else:
                    print("GOLLUM: ",end="")
                    print(questofthering(master_input))
                    sent_precious.remove(master_input)
    # If the user uses the stop word 'precious', it ends the conversation and our chatbot say goodbye
    else:
        flag=False
        print("GOLLUM: GIVE IT TO US !")

