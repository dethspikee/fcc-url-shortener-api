from validator_collection import checkers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages

from .forms import UrlForm
from .models import Url
# Create your views here.



class Index(View):
    template_name = 'index.html'
    form_class = UrlForm

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                'form': self.form_class()
            }
        )


class UrlShortener(View):
    def get(self, request, id):
        obj = Url.objects.get(id=int(id))
        link = obj.original_url
        return HttpResponseRedirect(link)

class UrlCreate(View):
    form_class = UrlForm

    def get(self, request):
        return redirect('/')

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            url = bound_form.cleaned_data['url']
            if checkers.is_url(url):
                # check if obj already exists in database if so return json with detail
                if Url.objects.filter(original_url=url).exists():
                    obj = Url.objects.get(original_url=url)
                    return JsonResponse({
                        "original_url": obj.original_url,
                        "short_url": obj.id
                    })
                # if doesnt exist create new obj and return json
                else:
                    obj = Url.objects.create(original_url=url)
                    return JsonResponse({
                        'original_url': obj.original_url,
                        'short_url': obj.id,
                    })
            else:
                return JsonResponse({
                    'error': 'invalid URL'
                })
        else:
            return redirect('/')