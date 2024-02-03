from sqlalchemy.orm import as_declarative, declared_attr
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey, Float, BOOLEAN
from pydantic import EmailStr
from datetime import datetime
from enum import Enum
from typing import Optional


class Status(Enum):

    confirmed = 1
    tentative = 2
    canceled = 3


class AttendeeStatus(Status):

    need_action = 4


@as_declarative()
class Base:

    __name__: str

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


class Event(Base):

    id: Optional[str] = Column(String(32), nullable=False, primary_key=True)
    status: Optional[Enum(Status)] = Column(Enum(Status), default=Status.confirmed)
    html_link: str = Column(String, default="")
    created: datetime = Column(DATETIME, nullable=False)
    updated: datetime = Column(DATETIME)
    summary: str = Column(String(12), default="")
    description: str = Column(String, default="")
    color_id: str = Column(String, default="")
    creator: Optional[int] = Column(Integer, nullable=False) # Google Profile ID
    organizer: Optional[int] = Column(Integer, default=None) # Google Profile ID
    start: datetime = Column(DATETIME)
    end: Optional[datetime] = Column(DATETIME, default=None)
    ical_uid: Optional[str] = Column(String(60))
    event_type: Optional[str] = Column(String, default="default")


class EventBase(Base):

    event_id: str = Column(
        String(32),
        ForeignKey(f"{Event.__tablename__}.id")
    )


class Attendee(EventBase):

    display_name: str = Column(String, nullable=False)
    email: Optional[EmailStr] = Column(EmailStr, default="")
    organizer: Optional[bool] = Column(BOOLEAN, default=False)
    response_status: Optional[Enum(AttendeeStatus)] = Column(
        Enum(AttendeeStatus),
        default=AttendeeStatus.need_action
    )


class Attachment(EventBase):

    file_url: str = Column(String, default="")
    title: str = Column(String(12), default="")
    mime_type: Optional[str] = Column(String(255), default="")
    icon_link: Optional[str] = Column(String, default="")
    file_id: Optional[str] = Column(String, default="") # GoogleDrive Id


class User(Base):

    id: int = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        default=None
    )
    email: Optional[EmailStr] = Column(EmailStr, default="")
    firstname: str = Column(String)
    lastname: Optional[str] = Column(String, default="")
    timeZone: Optional[str] = Column(String, default="")
    username: str = Column(String)


class Recurrence(EventBase):

    ex_date: Optional[datetime] = Column(DATETIME, default=None)
    r_date: Optional[datetime] = Column(DATETIME, default=None)
    r_rule: Optional[...]
