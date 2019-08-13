from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


def home(request):
    return render(request,'home.html')

@api_view(['Get'])
def search_doingfunc(request):
    
    word=request.query_params.get('word',None)
    if word is None:
        return Response("Need url with query parama word ",status=400)
    """
    write your logic here
    word variable is search word it is in string obj

    """



    yourresult="workingfine"
    return Response(yourresult)