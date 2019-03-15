from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from groups.models import Group, GroupMember

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    models = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

