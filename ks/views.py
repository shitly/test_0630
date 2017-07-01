from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, "ks/index.html", {
        "l1": [i for i in range(60)],
        "l2": [i for i in range(30)],
    })
