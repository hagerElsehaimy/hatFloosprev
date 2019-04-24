from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from . import form


def get_user_info(request, id):
    user = models.User.objects.get(id=id)
    if request.method == 'GET':
        user_form = form.UserProfileForm(
            initial={'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email,
                     'password': user.password, 'date': user.DOB, 'country': user.country, 'phone': user.phone})
    else:
        pass

    return render(request, 'user/profile.html', {"form": user_form})
