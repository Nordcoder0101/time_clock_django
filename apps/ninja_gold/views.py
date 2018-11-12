from django.shortcuts import render, redirect
from random import randint


def index(request):
    
    gold_count = request.GET.get('gold_count') 
    isMessage = request.GET.get('gold_count')
    
    request.GET.get('isMessage', '')

    if not isMessage:
        request.session['activitiesLog'] = []

  
    if not gold_count:
        request.session['gold_counter'] = 0

    print(request.session['activitiesLog'])
    print(isMessage)

    # return render(request, 'random_word/index.html')
    return render(request,'ninja_gold/index.html')


def change_gold(request):
    if request.method == "POST":
        location = request.POST["location"]
    
    request.session['did_win'] = True

    if location == 'farm':
        
        farmGold = randint(10, 20)
        farmGoldMessage = f'<p class = "win"> You gained {farmGold} amount of gold </p>'
        request.session['gold_counter'] += farmGold 
        request.session['activitiesLog'].append(farmGoldMessage)
        print(request.session['activitiesLog'])
        

    elif location == 'cave':
        
        caveGold = randint(5, 10)
        caveGoldMessage = f'<p class = "win"> You gained {caveGold} gold </p>'
        request.session['gold_counter'] += caveGold
        request.session['activitiesLog'].append(caveGoldMessage)

    elif location == 'house':
        
        houseGold = randint(2, 5)
        houseGoldMessage = f'<p class = "win"> You gained {houseGold} gold </p>'
        request.session['activitiesLog'].append(houseGoldMessage)
        
        

    elif location == 'casino':
        casinoGold = randint(-50,50)
        # casinoGainGoldMessage = f' You gained {casinoGold}  of gold'
        casinoGainGoldMessage = f'<p class = "win"> You gained {casinoGold}  of gold </p>'
        casinoLoseGoldMessage = f'<p class = "loss"> You lost {casinoGold *-1}  of gold </p>'
        request.session['gold_counter'] += casinoGold
        if casinoGold >= 0:
            request.session['activitiesLog'].append(casinoGainGoldMessage)
            request.session['did_win'] = False
        else:
            request.session['activitiesLog'].append(casinoLoseGoldMessage)
            
    if len(request.session['activitiesLog']) > 0:
        isMessage = 'True'
      
        

       
    gold_count = request.session['gold_counter']
        
    return redirect("/ninja_gold/?gold_count={}&isMessage={}".format(gold_count, isMessage))    



