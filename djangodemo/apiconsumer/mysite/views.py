from django.shortcuts import render
import requests
API_KEY = 'pub_700191624575f42aa515ba0d0691caeb77cc2'
# Create your views here.


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsdata.io/api/1/sources?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['results']
    elif category:
        url = f'https://newsdata.io/api/1/latest?country=us&category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['results']
    else:
    	url = f'https://newsdata.io/api/1/latest?country=us&apiKey={API_KEY}'
    	response = requests.get(url)
    	data = response.json()
    	articles = data['results']




    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)
