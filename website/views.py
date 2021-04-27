from django.views import View
from django.shortcuts import render


# Create your views here.
class IndexView(View):
    template_name = 'website/templates/index.html'
    user = None
    context = {}

    def dispatch(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            self.user = request.user
        self.context = {'user': self.user}

        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
