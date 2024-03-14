from django.core.serializers.json import DjangoJSONEncoder

from .models import Skill, Certificate, Project


class SkillEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Skill):
            return {
                'name': o.name,
                'title': o.title,
                'description': o.description
            }
        return super().default(o)


class CertificateEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Certificate):
            return {
                'publisher': o.publisher,
                'title': o.title
            }
        return super().default(o)


class ProjectEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Project):
            return {
                'name': o.name,
                'task': o.task,
                'website': o.website
            }
        return super().default(o)
