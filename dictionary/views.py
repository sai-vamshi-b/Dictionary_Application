from django.shortcuts import render

# for API
import requests

def home_view(request):
    return render(request, 'dictionary/index.html')

def search_view(request):
    word = request.GET.get('search').lower()
    data = requests.get('https://api.dictionaryapi.dev/api/v1/entries/en/' + word)
    full_data = data.json()
    context = {
            'word': word,
            'full_data':full_data,
        }
    return render(request, 'dictionary/search.html', context)
