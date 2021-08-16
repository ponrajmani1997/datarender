from django.shortcuts import render

# Create your views here.
def IPL(request):
    return render(request,'csk.html',context={'team':'CSK','result':'won 3 Trophies','opponent':'ready to beat Mumbai'})