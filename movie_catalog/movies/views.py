from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import Resolver404



def index(request: HttpRequest):
    return HttpResponse('Index HTML')


def categories(request: HttpRequest, category_id: int):
    print(request)
    print(category_id)
    return HttpResponse(category_id)


def page_not_found(request: HttpRequest, exception: Resolver404):
    return HttpResponseNotFound('<h1>Такой страницы нет!</h1>')