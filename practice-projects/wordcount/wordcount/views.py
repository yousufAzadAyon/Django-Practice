from django.http import HttpResponse
from django.shortcuts import render 
import operator

def home(request):
    return render(request,"index.html")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordcount = {}
    for i in wordlist:
        if i in wordcount:
            wordcount[i] += 1

        else:
            wordcount[i] = 1

    sortedword = sorted(wordcount.items(), reverse=True, key=operator.itemgetter(1))

    return render(request, "count.html", {'fulltext':fulltext, 'count':len(wordlist), 'sortedword':sortedword})


def about(request):
    return render(request, "about.html")