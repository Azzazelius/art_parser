from django.shortcuts import render


def index(request):
    return render(request, 'testApp/index.html', {'title': 'Главная страница'})  # в словаре данные, которые
    # передаются в темплейт


def about(request):
    return render(request, 'testApp/about.html')
