from typing import Optional

from django.db import models


class User(models.Model):
    """
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
    last_name: Optional[str] = models.CharField(max_length=255, default="")
    time_zone: Optional[str] = models.CharField(max_length=255, default="Europe/Moscow")
    user_name: str = models.CharField(max_length=12)
