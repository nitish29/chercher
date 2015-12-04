import urllib.request
import urllib.parse
import json
from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
import pdb

def search(request):
	
	try:
		
		pdb.set_trace()
		errors = []

		search_context = request.GET['q']
		search_context = search_context.strip()
		formatted_string = search_context.replace(",", " ")
		formatted_string = ' '.join(formatted_string.split())
		formatted_string = 'text_en:' + formatted_string
		data = urllib.parse.urlencode({'q': formatted_string, 'wt': 'json', 'indent': 'true'})
		data = data.encode('utf-8')
		req = urllib.request.urlopen('http://uakk04319339.archit017.koding.io:8983/solr/project1/select', data)
		#req = urllib.request.urlopen('http://uakk04319339.archit017.koding.io:8983/solr/project1/select?q=text_en%3Afootball&wt=json&indent=true')
		content = req.read()
		decoded_json_content = json.loads(content.decode())
		#print(decoded_json_content)
		json_response = decoded_json_content["response"]
		feed_data = json_response["docs"]
		#suggestions=getSuggestions()
		

		context = { "data" : feed_data }
		

	except:
		errors.append('Error Completing request')

	if not errors:
		return render(request, "search.html", context)
	else:
		context = { "errors" : errors }
		return render(request, "search.html", context)

	
	#return render(request, "search.html", search_context)
def getSuggestions(request):
	#pdb.set_trace()
	search_context = request.GET['s']
	search_context = search_context.strip()
	formatted_string = search_context.replace(",", " ")
	formatted_string = ' '.join(formatted_string.split())
	request_params = urllib.parse.urlencode({'q': formatted_string, 'wt': 'json', 'indent': 'true'})
	request_params = request_params.encode('utf-8')
	suggestion_fetch_request=urllib.request.urlopen('http://uakk04319339.archit017.koding.io:8983/solr/project1/suggest', request_params)
	raw_json=suggestion_fetch_request.read()
	decoded_json_content = json.loads(raw_json.decode())
	suggestions_list= decoded_json_content['spellcheck']['suggestions'][1]['suggestion']
	output='<ul id="live-search-results" class="clearfix">'
	for i in suggestions_list:
		output=output+'<li id="'+i+'" class="search-result faq" onclick="displaySuggestion(this.id)">'+i+'</li>'
	output=output+'</ul>'
	#return render("suggestions.html")
	return HttpResponse(output)

def getAuto():
	pdb.set_trace()
	return render("suggestions.html")