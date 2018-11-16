from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    data = request.GET['countreply']
    word_list1 = data.split()
    word_list1_length = len(word_list1)

    worddictionary = {}

    for word in word_list1:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorted_list = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'textreply':data, 'wordcount':word_list1_length, 'word_dict1':sorted_list})


def about(request):
    return render(request, 'about.html')
