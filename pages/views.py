from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def admin_only_page(request):
    return render(request, 'pages/admin_page.html')

def page1(request):
    return render(request, 'pages/pageCSS.html')

@login_required
def bootstrap_template(request):
    return render(request, 'pages/bootstrap_template.html', {'user': request.user})
