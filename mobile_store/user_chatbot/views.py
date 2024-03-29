from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from user_panel.models import *
from django.contrib.auth.models import User

# Create your views here.
from user_panel. utils import cartData, cookieCart, guestOrder



import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
from tensorflow.python.framework import ops
import random
import json
import pickle
import numpy as np

modelll = None

def load():
    global modelll
    if modelll is None:
        with open('static/mobilee.pkl', 'rb') as f:
            modelll = pickle.load(f)


with open("static/intents.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

import os

if os.path.exists("model.tflearn.meta"):
    model.load("model.tflearn")
else:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")   



def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def chatss(um):
    while True:
        inp = um
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        
        ss = random.choice(responses)
        return ss
        break



def contact(request):
    if request.user.is_authenticated:
        user_name = request.user.username          
        chat = Chat.objects.filter(user_name=user_name) 
        data = cartData(request)

        cartItems = data['cartItems']
        order = data['order']
        items = data['items']

        products = Product.objects.all()
        context = {}
        context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'Chat':chat,
         }
        return render(request, 'user_panel/contact.html', context)     

    else: 
        data = cartData(request)

        cartItems = data['cartItems']
        order = data['order']
        items = data['items']

        products = Product.objects.all()
        context = {}
        context = {
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
         }
        return render(request, 'user_panel/login.html', context)   

def chat_contact(request):
    user_name = request.user.username    
    print(request.method)
    if request.is_ajax():
        um = request.POST.get('user_messages', None)
        cm = chatss(um)
        if um and cm:
            data  = Chat(user_name=user_name, user_message=um, chatbot_message=cm)
            data.save()
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON
                     
    chat = Chat.objects.filter(user_name=user_name) 
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {}
    context = {
    'products': products,
    'items': items,
    'order': order,
    'cartItems': cartItems,
    'Chat':chat,
         }
    return render(request, 'user_panel/contact.html', context)


def price_prediction(request):
    if request.method == "POST":
        load()
        modell = request.POST['modell']
        ram = request.POST['ram']
        rom = request.POST['rom']
        cammera = request.POST['cammera']
        print(ram, rom, cammera)
        ram = int(ram)
        rom = int(rom)
        cammera = int(cammera)
        prediction = modelll.predict([[cammera, rom, ram]])
        data = cartData(request)

        cartItems = data['cartItems']
        order = data['order']
        items = data['items']

        products = Product.objects.all()
        context = {
        'prediction': prediction,
        'products': products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'cammera':cammera,
        'ram': ram,
        'rom':rom,
        'model': modell,
        }
        return render(request,  'user_panel/prediction.html', context) 
      


            