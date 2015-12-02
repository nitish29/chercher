import urllib.request
import urllib.parse
import json
from django.http import HttpResponse

def search(request):
	
	try:
		
		errors = []

		search_context = request.GET['q']
		search_context = search_context.strip()
		formatted_string = search_context.replace(",", " ")
		formatted_string = ' '.join(formatted_string.split())
		data = urllib.parse.urlencode({'q': formatted_string, 'wt': 'json', 'indent': 'true'})
		data = data.encode('utf-8')
		#req = urllib.request.urlopen('http://52.34.128.215:8983/solr/recipeally/select', data)
		#content = req.read()
		#reply = json.loads(content.decode())





	except:
		errors.append('Error Completing request')

	if not errors:
		response = HttpResponse(json.dumps({'status': 'success'}),
		content_type='application/json')
	else:
		response = HttpResponse(json.dumps({'status': 'failure','errors': errors}),
		content_type='application/json')

	return response