from django.shortcuts import render



def homepage(request):
     
     return render(request, 'index.html' )


def project_info(request):
    
    return render(request, 'project_info.html')


def promise(request):
    
    return render(request, 'promise.html')    
     
     
def developers_section(request):
     
     return render(request, 'for_devs.html')