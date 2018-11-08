from django.shortcuts import render, redirect
import string
import random


def index(request):
  # if not request.session['times_clicked']: 
  #   request.session['times_clicked'] = 0  
  return render(request, 'random_word/index.html')

def generate_word(request):
    if request.method == "POST":
      print('clicked')
      request.session['random_word'] = ''

      if not request.session['times_clicked']:
          request.session['times_clicked'] = 0
      
      request.session['times_clicked'] += 1
      

      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      number_of_letters = random.randint(3,10)
      for i in range(0, number_of_letters, 1):
          random_letter = random.choice(alphabet)
          request.session['random_word'] += random_letter
      context = {
        'random_word': request.session['random_word'],
        'times_clicked': request.session['times_clicked']
      }
      return redirect('/random_word', context)

def reset(request):
    if request.method == "POST":
         request.session['random_word'] = ''
         request.session['times_clicked'] = 0
    return redirect('/random_word')