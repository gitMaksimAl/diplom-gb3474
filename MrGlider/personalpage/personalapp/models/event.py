from uuid import uuid4
from datetime import datetime
from typing import Optional

from django.db import models
from .user import User


class Color(models.Model):
    """
    Attributes
    __________
        foreground | background : str
            color code in hex 000000-FFFFFF
    """
    color_id: Optional[str] = models.CharField(max_length=32, default=uuid4().hex, unique=True)
    foreground: str = models.CharField(max_length=6, default='000000')
    background: str = models.CharField(max_length=6, default='FFFFFF')


class EventDate(models.Model):
    date: str = models.DateField()
    datetime: datetime = models.DateField()
    timezone: Optional[str] = models.CharField(max_length=255, default='Europe/Moscow')


class Event(models.Model):
    """
    Event model based on Google calendar.event model. Some fields can be omitted

    ...

    Attributes
    __________
        event_id : str
            base32hex string
        creator | organizer : int
            user primary key(for Google Profile ID use user.email)
        event_type :str
            from Google Calendar can be one of
            ['default', 'outOfOffice', 'workingLocation']
    """
    event_id: Optional[str] = models.CharField(max_length=32, default=uuid4().hex, unique=True)
    status: Optional[str] = models.CharField(choices=[
        ('confirmed', 'confirmed'),
        ('tentative', 'tentative'),
        ('canceled', 'canceled'),
    ], max_length=9, default='tentative')
    html_link: Optional[str] = models.TextField(default='')
    created: Optional[datetime] = models.DateTimeField(auto_now_add=True)
    updated: datetime = models.DateTimeField(default=created)
    summary: str = models.CharField(max_length=255)
    description: Optional[str] = models.TextField(default='')
    color_id: str = models.ForeignKey(to=Color, to_field='color_id', on_delete=models.CASCADE)
    creator: int = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='event_creator')
    organizer: Optional[int] = models.ForeignKey(
        to=User, default=creator,
        on_delete=models.SET,
        related_name='event_organizer')
    start: datetime = models.ForeignKey(
        to=EventDate,
        on_delete=models.PROTECT,
        related_name='event_start'
    )
    end: Optional[datetime] = models.ForeignKey(
        to=EventDate,
        on_delete=models.PROTECT,
        related_name='event_end'
    )
    event_type: Optional[str] = models.CharField(choices=[
        ('default', 'default'),
        ('outOfOffice', 'outOfOffice'),
        ('workingLocation', 'workingLocation'),
    ],max_length=15, default='default')


class EventBase(models.Model):
    event_id: str = models.ForeignKey(
        to=Event,
        to_field='event_id',
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
    ], max_length=11, default='needsAction')


class Attachment(EventBase):
    """
    Attributes
    __________
        mime_type : str
            https://www.iana.org/assignments/media-types/media-types.xhtml
        file_id : str
            GoogleDrive Id
    """
    file_url: str = models.TextField()
    title: str = models.CharField(max_length=25)
    mime_type: Optional[str] = models.TextField(default='')
    icon_link: Optional[str] = models.TextField(default='')
    file_id: Optional[str] = models.TextField()


class RecurrenceRule(EventBase):
    """
    Attributes
    __________
        by_month : str
            example '1,...12'
        by_day : str
            example '1234567'
    """
    freq: str = models.CharField(choices=[
        ('daily', 'DAILY'),
        ('weekly', 'WEEKLY'),
        ('monthly', 'MONTHLY'),
        ('yearly', 'YEARLY'),
    ], max_length=7)
    interval: int = models.IntegerField(default=0)
    by_month: str = models.CharField(max_length=24, default='')
    by_day: str = models.CharField(max_length=7, default='')
    until: datetime = models.DateTimeField()
    count: int = models.IntegerField(default=0)


class Recurrence(EventBase):
    """
    Rules and dates for recurring events

    ...

    Attributes
    __________
        ex_date : datetime
            exclude date
        r_date : datetime
            recurrence date
    Note
    ____
        Some fields can be omitted.
        https://datatracker.ietf.org/doc/html/rfc5545#section-3.8.5
    """
    ex_date: Optional[datetime] = models.DateTimeField(default=None)
    d_start: Optional[datetime] = models.DateTimeField(default=None)
    r_date: Optional[datetime] = models.DateTimeField(default=None)
    r_rule: int = models.ForeignKey(to=RecurrenceRule, on_delete=models.DO_NOTHING)
