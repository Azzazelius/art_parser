from django.shortcuts import render


def index(request):
    data = {
        'title_key': 'Главная страница',  # в словаре данные, которые передаются в темплейт
        'values': [123, 'hi!', 'bla-bla']
    }

    return render(request, 'testApp/index.html', data)


def about(request):
    return render(request, 'testApp/about.html')
