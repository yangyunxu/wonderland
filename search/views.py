from django.shortcuts import render

# Create your views here.
def theBestWonders(request):
    return render(request, 'search/thebestwonders.html')

def searchResult(request):
    # return render(request, 'search/searchpage.html', context=context_dict)
    return render(request, 'search/searchpage.html')

