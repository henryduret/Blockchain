#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nltk.download()


# In[ ]:


import nltk
import numpy as np
import random
import string #To process standard python strings


# In[ ]:


f=open('/Users/Henry/lordofthering.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
sent_precious = nltk.sent_tokenize(raw)# converts to list of sentences 
word_precious = nltk.word_tokenize(raw)# converts to list of words


# In[ ]:


ring = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def RingPrecious(swords):
    return [ring.lemmatize(sword) for sword in swords]

remove_dot_ring = dict((ord(dot), None) for dot in string.punctuation)

def RingNormalize(arrow):
    return RingPrecious(nltk.word_tokenize(arrow.lower().translate(remove_dot_ring)))


# In[ ]:


start_inputs = ("hello", "hey","hi","greetings","good morning", "good afternoon","good evening")
start_outputs = ["the Master is talking to me? I'm so glad", "Precious, ask us questions","GOLLUM GOLLUM GOLLUM","Where is the precious ?"]

def gollumanswer(inputs): 
    for word in inputs.split():
        if word.lower() in start_inputs:
            return random.choice(start_outputs)


# In[ ]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[ ]:


from sklearn.metrics.pairwise import cosine_similarity


# In[ ]:


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
    if(req_tfidf==0):
        gollum_output=gollum_output+"YOU SHALL NOT PASS. Sméagol wants you to rephrase"
        return gollum_output
    else:
        gollum_output = gollum_output+sent_precious[idx]
        return gollum_output


# In[ ]:


gollumpanic =["The Master is tough", "Master should be resting, Master needs to keep up his strength", "Stop asking questions you fat Hobbit"]

def last(master_input):
    splint_ring=[]
    Frodon=[]
    splint_ring=master_input.split()
    Frodon= splint_ring[len(splint_ring)-1]
    return (Frodon)


# In[ ]:


flag=True
    
print("GOLLUM: Sméagol is here to serve the Master. Ask Sméagol about the precious: introduction, prologue, the fellowship, thetwotowers. Sméagol can develop further if you say morecategoryname. Say 'precious' to stop talking to Sméagol.")

while(flag==True):
    master_input = input()
    master_input=master_input.lower()
    if(master_input!='precious'):
        if(master_input=='thanks' or master_input=='thank you' ):
            flag=False
            print("GOLLUM: Let the precious be with you")
        else:
            if(gollumanswer(master_input)!=None):
                print("GOLLUM: "+gollumanswer(master_input))
            else:
                if (question(master_input)=='?'):
                    print("GOLLUM: "+random.choice(gollumpanic))
                else:
                    print("GOLLUM: ",end="")
                    print(questofthering(master_input))
                    sent_precious.remove(master_input)
    else:
        flag=False
        print("GOLLUM: GIVE IT TO US !")

