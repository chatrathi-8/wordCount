from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'homepage.html')
def welcome(request):
	return HttpResponse("Hamaya")
def count(request):
	fulltext = request.GET["fulltext"]
	wordList = fulltext.split()
	wordDic = {}
	for word in wordList:
		if word in wordDic:
			wordDic[word] +=1

		else:
			wordDic[word] =1
	sortedName = sorted(wordDic.items(), key=operator.itemgetter(1), reverse=True)

	return render(request,"count.html", {'fulltext':fulltext, 'count':len(wordList), 'sortedName':sortedName})
def about(request):
	return render(request, "about.html")