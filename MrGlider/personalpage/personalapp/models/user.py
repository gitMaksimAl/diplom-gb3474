import datetime
from typing import Optional

from django.db import models


class User(models.Model):
    """
    User model by default is not active

    ...

    Attributes
    __________
        email : str
            must be Google Mail to access Google Calendar events
        time_zone : str
            default='Europe/Moscow' see available on
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        user_name : str
            display name
    """
    email: str = models.EmailField(unique=True)
    first_name: str = models.CharField(max_length=255)
    last_name: Optional[str] = models.CharField(max_length=255, default=None)
    time_zone: Optional[str] = models.CharField(max_length=255, default="Europe/Moscow")
    user_name: str = models.CharField(max_length=12)
    biography: str = models.TextField()
    spec: str = models.CharField(max_length=255, default=None)
    active: bool = models.BooleanField(default=False)


class UserBase(models.Model):
    user_id: int = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class SocialMedia(UserBase):
    name: str = models.CharField(max_length=12)
    link: str = models.CharField(max_length=255)


class Skill(UserBase):
    name: str = models.CharField(max_length=12)
    title: str = models.CharField(max_length=255)
    description: str = models.TextField()


class Certificate(UserBase):
    publisher: str = models.CharField(max_length=255)
    title: str = models.CharField(max_length=255)
    date: Optional[datetime.date] = models.DateField(default=None)
    link: Optional[str] = models.CharField(max_length=255, default=None)


class Project(UserBase):
    name: str = models.CharField(max_length=25)
    task: str = models.CharField(max_length=255)
    description: Optional[str] = models.TextField(default=None)
    status: str = models.CharField(
        choices=[
            ('onTrack', 'On Track'),
            ('onHold', 'On Hold'),
            ('done', 'Done'),
            ('ready', 'Ready'),
            ('offTrack', 'Off Track'),
            ('blocked', 'Blocked')
        ], max_length=8, default='onTrack'
    )
    website: Optional[str] = models.CharField(max_length=255, default=None)
    role: str = models.CharField(
        choices=[
            ('contributor', 'contributor'),
            ('executor', 'executor'),
            ('customer', 'customer'),
            ('sponsor', 'sponsor'),
        ], max_length=11, default='contributor'
    )


class Contact(models.Model):
    email: str = models.EmailField()
    subject: str = models.CharField(max_length=255)
    message: str = models.TextField()
