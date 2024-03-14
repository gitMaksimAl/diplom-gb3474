import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet, Count
from django.middleware.csrf import get_token

from .models import User, Event, SocialMedia, Project, Skill, Certificate
from .forms import ContactForm
from .services import SkillEncoder, ProjectEncoder, CertificateEncoder


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
    certs = Certificate.objects.filter(user_id=user.pk).all()
    return JsonResponse(data=list(certs), safe=False, encoder=CertificateEncoder)


def all_projects(request: HttpRequest) -> JsonResponse:
    user = User.objects.filter(active=True).first()
    projects = Project.objects.filter(user_id=user.pk).all()
    return JsonResponse(data=list(projects), safe=False, encoder=ProjectEncoder)


def all_skills(request: HttpRequest) -> JsonResponse:
    user = User.objects.filter(active=True).first()
    skills = Skill.objects.filter(user_id=user.pk).all()
    return JsonResponse(data=list(skills), safe=False, encoder=SkillEncoder)


def contact(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(
                data={'form': form.as_p(), 'message': 'Thanks for contact!'}
            )
    form = ContactForm()
    context = {
        'form': form.as_p(),
        'message': 'Please fill form for contact',
        'csrfmiddlewaretoken': get_token(request)
    }
    print(context)
    return JsonResponse(data=context)
