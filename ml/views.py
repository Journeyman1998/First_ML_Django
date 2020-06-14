from django.shortcuts import render


# Create your views here.

species = ['Bream', 'Parkki', 'Perch', 'Pike',  'Roach', 'Smelt', 'Whitefish']

def index(request):
    return render(request, 'index.html', {'species': species, 'result': None})

def predict(request):
    s_list = []
    s_list.append(float(request.POST['vertical']))
    s_list.append(float(request.POST['diagonal']))
    s_list.append(float(request.POST['cross']))
    s_list.append(float(request.POST['height']))
    s_list.append(float(request.POST['width']))

    s = request.POST['species']

    for i in species:
        to_app = 1 if s == i else 0
        s_list.append(to_app)

    y_pred = models.predict(s_list)
    
    return render(request, 'index.html', {'species': species, 'result': y_pred})