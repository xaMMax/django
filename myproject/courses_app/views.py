from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
# @login_required(login_url='/admin')
def courses_page(request):

    return render(request, 'courses.html')
