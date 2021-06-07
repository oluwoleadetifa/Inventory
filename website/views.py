import copy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import messages

from .forms import *


# Create your views here.


def IndexView(request):
    form = AuthenticationForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('website:website.event')
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request=request, template_name="index.html", context={"form": form})


def logoutUser(request):
    logout(request)
    return redirect('website:website.index')


class EventView(View):
    template_name = 'events.html'
    user = None
    context = {}
    data = {}

    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            self.user = request.user
        self.context = {'user': self.user}
        self.data = {'status': 400}

        return super(EventView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        event_form = EventForm(initial={'created_by': self.user})
        event_form.fields['assigned_to'].queryset = models.User.objects.exclude(id=self.user.id)
        self.context.update({
            'inventory_form': InventoryForm(),
            'event_form': event_form,
            'item_form': ItemForm()
        })
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        # the different forms data will be submitted to
        post_data = copy.deepcopy(request.POST)
        item_form = ItemForm(post_data)
        # To be done if form is valid
        if item_form.is_valid():
            item = item_form.save()
            post_data['item'] = item
            post_data['created_by'] = self.user
            event_form = EventForm(post_data)
            if event_form.is_valid():
                event = event_form.save()
                post_data['event'] = event
                inventory_form = InventoryForm(post_data)
                if inventory_form.is_valid():
                    inventory = inventory_form.save()
                    self.data['status'] = 200
                else:
                    message = ""
                    for key, value in inventory_form.errors.items():
                        message += f"{key}: {value[0]}/n"
                    self.data['details'] = message
            else:
                message = ""
                for key, value in event_form.errors.items():
                    message += f"{key}: {value[0]}/n"
                self.data['details'] = message
        else:
            message = ""
            for key, value in item_form.errors.items():
                message += f"{key}: {value[0]}/n"
            self.data['details'] = message

        return JsonResponse(self.data, safe=False, status=self.data['status'])

    @xframe_options_exempt
    def ok_to_load_in_a_frame(self, request):
        return HttpResponse("This page is safe to load in a frame on any site.")
