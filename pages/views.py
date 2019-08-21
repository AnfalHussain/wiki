from django.shortcuts import render
from .models import Page


def list_view(request):
    context = {
        "page_list": Page.objects.all(),
    }
    return render(request, 'list.html', context)

def detail_view(request, page_id):
    context = {
        "page_detail": Page.objects.get(id=page_id),
    }
    return render(request, 'detail.html', context)
