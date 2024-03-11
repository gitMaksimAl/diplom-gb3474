from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from .models import User, Event, SocialMedia, Project, Skill, Certificate


def home(request: HttpRequest) -> HttpResponse:
    user = User.objects.filter(active=True).first()
    social_media = SocialMedia.objects.filter(user_id=user.pk).all()
    return render(
        request,
        'personalapp/main.html',
        context={'user': user, 'social_media': social_media}
    )


def all_events(request: HttpRequest) -> JsonResponse:
    user = User.objects.filter(active=True).first()
    events = Event.objects.filter(creator=user.pk).all()
    return JsonResponse(data={'events': events})


def all_certificates(request: HttpRequest) -> JsonResponse:
    user = User.objects.filter(active=True).first()
    query = Certificate.objects.filter(user_id=user.pk).all().query
    query.group_by = ['publisher']
    certs = QuerySet(query=query, model=Certificate)
    return JsonResponse(data={'certificates': certs})


def all_projects(request: HttpRequest) -> JsonResponse:
    user = User.objects.filter(active=True).first()
    projects = Project.objects.filter(user_id=user.pk).all()
    return JsonResponse(data={'projects': projects})


def all_skills(request: HttpRequest) -> JsonResponse:
    user = User.objects.filter(active=True).first()
    query = Skill.objects.filter(user_id=user.pk).all().query
    query.group_by = ['name']
    skills = QuerySet(query=query, model=Skill)
    return JsonResponse(data={'skills': skills})
