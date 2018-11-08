from django.shortcuts import render

from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print(f"****************{context['time']}")
    return render(request,'show_time/index.html', context)
