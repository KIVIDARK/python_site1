import os

from django.http import HttpResponse


def hello(request):
    return HttpResponse(u'Hello World!')


from django.http import Http404
from datetime import *


def dtime(request, offset):
    try:
        offset = int(offset)
        dt = datetime.now() + timedelta(hours=offset)
        result = HttpResponse(u'<html><body>%s</body></html>' % dt)
        return result
    except ValueError:
        raise Http404


from django.shortcuts import render


def templ(request, arg):
    localarg = 'in templ'
    context = {'context_arg': arg, 'templ_arg': localarg, 'incontext': ['1 arg', '2 arg']}

    return render(request, 'templ.html', context)


def index(request, name, arg='0_10'):
    main_title = 'Читалка анлайн!'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(os.path.join(BASE_DIR, 'templates/' + str(name) + '.txt'))
    spis = []
    textlen = len(file.readlines())
    alfa = 0
    if textlen <= 100:
        alfa = 5
    elif 100 < textlen <= 500:
        alfa = 10
    elif 500 < textlen <= 1000:
        alfa = 20
    elif textlen > 1000:
        alfa = 50
    spis += list([str(x) + '_' + str((x + alfa - 1)) for x in range(textlen) if x % alfa == 0])
    file = open(os.path.join(BASE_DIR, 'templates/' + str(name) + '.txt'))
    text = file.readlines()[int(arg.split(sep='_')[0]): int(arg.split(sep='_')[1])]
    file.close()
    text_title = (str(arg.split(sep='_')[0]) + ' - ' + str(arg.split(sep='_')[1]))
    context = {'spis': spis, 'main_title': main_title, 'first_text': text, 'text_title': text_title,
               'book': name}

    return render(request, 'index.html', context)
