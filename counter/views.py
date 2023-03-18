from django.shortcuts import render

#c2e6WmoS/f7gnmiNNGcHFQ==Tgud3e6GqWLV83zk


def home(request):
    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']   #input bar's name = query; this gets the text in the input bar
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers = {'X-Api-Key': 'c2e6WmoS/f7gnmiNNGcHFQ==Tgud3e6GqWLV83zk'}) # to fetch the request from api

        try:
            api = json.loads(api_request.content) #json.loads -> used to parse json data to python
            print(api_request.content)
        except Exception as e:
            api = "OOPS! There was an error"
            print(e)
        return render(request, 'home.html',{'api':api})
    
    else:
        return render(request, 'home.html',{'query':'Enter a valid dish'})
