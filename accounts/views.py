from django.shortcuts import render
from django.views import View


def register(request):
    pass


def login(request):
    pass


class Project(View):
    # all these views are protected
    # form based views

    def get(self):
        # returns a specific project with the ID
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
