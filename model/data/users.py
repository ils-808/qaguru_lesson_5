import dataclasses
import datetime
from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'

class Hobbies(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class BaseUser:
    current_address: str
    email: str

@dataclasses.dataclass
class User(BaseUser):
    perm_address: str
    full_name:str



@dataclasses.dataclass
class Student(BaseUser):
    first_name: str
    last_name: str
    gender: Gender
    mobile_phone: str
    birthdate: datetime.date
    subject: str
    hobbies: Hobbies
    picture_path: str
    state: str
    city: str




