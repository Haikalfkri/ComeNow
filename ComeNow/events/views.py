from django.shortcuts import render

# Create your views here.
def EventView(request):
    return render(request, "events/events.html")


def DetailPage(request):
    return render(request, "events/detailPage.html")