from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import vpn, profile
from .forms import UserForm


def index(request, vpnid):
    vpns = vpn.objects.all()
    totalprofilevpnsconnections = 0
    totalvpns = 0
    onlinevpns = 0
    for vpnobject in vpns:
        totalprofilevpnsconnections += vpnobject.profiles.count()
        totalvpns += 1
        if vpnobject.status != 'grey':
            onlinevpns += 1
    if vpnid is None:
        vpnid = vpns.first().id
    currentvpn = vpn.objects.get(pk=vpnid)
    profiles = profile.objects.all()
    form = UserForm()
    if (request.method == 'POST'):
        userForm = UserForm(request.POST)
        userFormId = userForm.data.get('id')
        user = User.objects.get(pk=userFormId)
        userForm = UserForm(request.POST, instance=user)
        if userForm.is_valid():
            userForm.save()
            return render(request, 'index.html', {'vpns': vpns,
                                                  'profiles': profiles,
                                                  'currentvpn': currentvpn,
                                                  'totalprofilevpnsconnections': totalprofilevpnsconnections,
                                                  'onlinevpns': onlinevpns,
                                                  'totalvpns': totalvpns,
                                                  'form': form})
    return render(request, 'index.html', {'vpns': vpns,
                                          'profiles': profiles,
                                          'currentvpn': currentvpn,
                                          'totalprofilevpnsconnections': totalprofilevpnsconnections,
                                          'onlinevpns': onlinevpns,
                                          'totalvpns': totalvpns,
                                          'form': form})