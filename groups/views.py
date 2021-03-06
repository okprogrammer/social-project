from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixixin,
                                        PermissionRequiredMixin)

from django.core.urlresolvers import reverse
from django.views import generic

from groups.models import Group,GroupMember

class CreateGroup(LoginRequiredMixixin,generic.CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group