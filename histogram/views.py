from django.shortcuts import render
from django.http import HttpResponse
from assigment.settings import BASE_DIR
import os


def hcount(request,filename):
	try:
		path= os.path.join(BASE_DIR,"static","templates",filename)
		path2 = open(path)
		dictionary={}
		for word in path2.read().split(" "):
			if word in dictionary:
				dictionary[word] += 1
			else:
				dictionary[word] = 1
		output = "Name: %s <br> Words: <br>" % filename
		for g in dictionary:
			output += "%s: %d <br>"%(g,dictionary[g])
		return HttpResponse(output)
	except:
		return HttpResponse("There is no file named as %s" %filename)

