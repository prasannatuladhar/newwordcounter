
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    textarea = request.GET['textarea']
    wordlist = textarea.split()
    words = {}
    for word in wordlist:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    return render(request,'counter.html', {'counter':len(wordlist),'textarea':textarea,'words':words.items()})


