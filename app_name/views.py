from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response

from forms import NewBetaUserForm
from models import BetaUser

def signup_view(request):
    if request.method == 'POST':
        form = NewBetaUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Hooray! A new email address is collected!
            b = BetaUser(name=data['name'], email=data['email'])
            b.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = NewBetaUserForm()

    return render(request, 'index.html', {'form' : form, 'noun': "sample Bootstrap form "})

def null_view(request):
    return HttpResponse("This doesn't do anything")