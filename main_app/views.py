from django.shortcuts import render, redirect
from .models import SlugTable
from django.http import JsonResponse, HttpResponse
# Create your views here.


def mainAppPage(request):
    return render(request, 'main_app/mainApp.html')


def urlShorten(request):
    if request.method == 'GET' and request.is_ajax() == True:
        SlugTable.objects.create(
            slug=request.GET['slug'], url=request.GET['url'])
        data = {
            'name': request.GET['slug']
        }
        return JsonResponse(data)
    else:
        return HttpResponse(status=404)


def slugQuery(request):
    if request.method == 'GET' and request.is_ajax() == True:
        slug = request.GET['slug']
        try:
            SlugTable.objects.get(slug__exact=slug)
            data = {
                'valid_slug': False
            }
            return JsonResponse(data)
        except SlugTable.DoesNotExist:
            if slug == '':
                data = {
                    'valid_slug': False
                }
            else:
                data = {
                    'valid_slug': True
                }
            return JsonResponse(data)
    else:
        return HttpResponse(status=404)


def urlRedirect(request, slug):
    try:
        site = SlugTable.objects.get(slug__exact=slug)
        goto = site.url
        return redirect(goto)
    except SlugTable.DoesNotExist:
        return redirect('../')
