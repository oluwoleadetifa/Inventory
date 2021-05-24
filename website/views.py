from django.views import View
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.

class IndexView(View):
    template_name = 'index.html'
    user = None
    context = {}

    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            self.user = request.user
        self.context = {'user': self.user}

        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class EventView(View):
    template_name = 'events.html'
    user = None
    context = {}

    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            self.user = request.user
        self.context = {'user': self.user}

        return super(EventView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    @xframe_options_exempt
    def ok_to_load_in_a_frame(self, request):
        return HttpResponse("This page is safe to load in a frame on any site.")


class AddEvent(View):
    template_name = 'add_event.html'
    user = None
    context = {}

    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            self.user = request.user
        self.context = {'user': self.user}

        return super(AddEvent, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render_to_string(request, self.template_name, self.context)

    @xframe_options_exempt
    def ok_to_load_in_a_frame(self, request):
        return HttpResponse("This page is safe to load in a frame on any site.")
