# for returning direct text(line 9)
from django.http import HttpResponse

# for importing templates file
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hi')
    return render(request, 'home.html', {'one': "onn"})

# inside this string we won't be passing whole html code . Hence , we use templates
# after creating templates we need to update name of folder in DIR under templates under settings.py


# def merc(Request):
    # return HttpResponse("merc")

def count(request):

    # request object can get info about what be typed in textbox with help of url parameyers after ?
    fultext = request.GET['fulltext']
    print(fultext)  # printed in cmd
    woedtext = fultext.split()
    return render(request, 'count.html', {'ftext': fultext, 'count': len(woedtext)})
