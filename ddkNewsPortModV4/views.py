from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'news_list.html')


def news(request):
    return render(request, 'news_list.html')


@staff_member_required
def admin_page(request):
    return render(request, 'admin_page.html')
