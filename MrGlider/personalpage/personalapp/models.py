from uuid import uuid4
from datetime import datetime
from typing import Optional

from django.db import models
from django.utils import timezone


class User(models.Model):
    """
    Fields
        time_zone default='Europe/Moscow'
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    """
    email: str = models.EmailField(unique=True)
    firstname: str = models.CharField(max_length=255)
    lastname: Optional[str] = models.CharField(max_length=255, default="")
    time_zone: Optional[str] = models.CharField(max_length=255, default="Europe/Moscow")
    username: str = models.CharField(max_length=12)


class Color(models.Model):
    color_id: str = models.CharField(max_length=32, default=uuid4().hex)
    foreground: str = models.CharField(max_length=6, default='000000')
    background: str = models.CharField(max_length=6, default='FFFFFF')


class EventDate(models.Model):
    date: str = models.DateField()
    datetime: datetime = models.DateField()
    timezone: Optional[str] = models.CharField(max_length=255, default='Europe/Moscow')


class Event(models.Model):
    """
    Fields
        event_id base32hex string
        creator Google Profile ID
        organizer Google Profile ID
        event_type from Google Calendar
            ['default', 'outOfOffice', 'workingLocation']
    """
    event_id: Optional[str] = models.CharField(max_length=32, default=uuid4().hex)
    status: Optional[str] = models.CharField(choices=[
        ('confirmed', 'confirmed'),
        ('tentative', 'tentative'),
        ('canceled', 'canceled'),
    ], default='tentative')
    html_link: Optional[str] = models.TextField(default='')
    created: Optional[datetime] = models.DateTimeField(auto_now_add=True)
    updated: datetime = models.DateTimeField(default=created)
    summary: str = models.CharField(max_length=255)
    description: Optional[str] = models.TextField(default='')
    color_id: str = models.ForeignKey(to=Color.color_id, on_delete=models.CASCADE)
    creator: str = models.ForeignKey(to=User, on_delete=models.CASCADE)
    organizer: Optional[int] = models.ForeignKey(to=User, default=creator, on_delete=models.SET)
    start: datetime = models.ForeignKey(to=EventDate, on_delete=models.PROTECT)
    end: Optional[datetime] = models.ForeignKey(to=EventDate, on_delete=models.PROTECT)
    event_type: Optional[str] = models.CharField(choices=[
        ('default', 'default'),
        ('outOfOffice', 'outOfOffice'),
        ('workingLocation', 'workingLocation'),
    ], default='default')


class EventBase(models.Model):
    event_id: str = models.ForeignKey(
        to=Event.event_id,
        on_delete=models.CASCADE
    )


class Attendee(EventBase):
    display_name: str = models.CharField(max_length=12)
    email: Optional[str] = models.EmailField(default='')
    organizer: Optional[bool] = models.BooleanField(default=False)
    response_status: Optional[str] = models.CharField(choices=[
        ('needsAction', 'needsAction'),
        ('declined', 'declined'),
        ('tentative', 'tentative'),
        ('accepted', 'accepted'),
    ], default='needsAction')


class Attachment(EventBase):
    """
    Fields
        mime_type https://www.iana.org/assignments/media-types/media-types.xhtml
        file_id GoogleDrive Id
    """
    file_url: str = models.TextField()
    title: str = models.CharField(max_length=25)
    mime_type: Optional[str] = models.TextField(default='')
    icon_link: Optional[str] = models.TextField(default='')
    file_id: Optional[str] = models.TextField()


class RecurrenceRule(EventBase):
    """
    Fields
        by_month example '1,...12'
        by_day example '1234567'
    """
    freq: str = models.CharField(choices=[
        ('daily', 'DAILY'),
        ('weekly', 'WEEKLY'),
        ('monthly', 'MONTHLY'),
        ('yearly', 'YEARLY'),
    ])
    interval: int = models.IntegerField(default=0)
    by_month: str = models.CharField(max_length=24, default='')
    by_day: str = models.CharField(max_length=7, defautl='')
    until: datetime = models.DateTimeField()
    count: int = models.IntegerField(default=0)


class Recurrence(EventBase):
    """
    Rules and dates for recurring events.
    Fields
        ex_date exclude date
        r_date recurrence date
    NOTE:
        Some fields can be omitted.
    https://datatracker.ietf.org/doc/html/rfc5545#section-3.8.5
    """
    ex_date: Optional[datetime] = models.DateTimeField(default=None)
    d_start: Optional[datetime] = models.DateTimeField(default=None)
    r_date: Optional[datetime] = models.DateTimeField(default=None)
    r_rule: int = models.ForeignKey(to=RecurrenceRule, on_delete=models.DO_NOTHING)
