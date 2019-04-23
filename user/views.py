from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from . import form


def get_user_info(request, id):
    user = {"user": models.User.objects.get(id=id)}
    userr = models.User.objects.get(id=id)
    user_form = form.UserProfileForm(initial={'first_name':userr.first_name,'last_name': userr.last_name,'Email': userr.email})

    return render(request, 'user/profile.html', {"user": user, "form": user_form})
