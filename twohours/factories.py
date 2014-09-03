import factory

from django.contrib.auth.hashers import make_password
from django.contrib.webdesign import lorem_ipsum
from django.utils.timezone import now
from .models import User


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User

    @factory.lazy_attribute
    def password(self):
        return make_password('qwerty')

    @factory.sequence
    def username(n):
        return '{0}_{1}'.format(lorem_ipsum.words(1, False), n)

    @factory.lazy_attribute_sequence
    def email(self, n):
        return '{}@example.com'.format(self.username, n)

    @factory.lazy_attribute
    def first_name(self):
        return lorem_ipsum.words(1, False).capitalize()

    @factory.lazy_attribute
    def last_name(self):
        return lorem_ipsum.words(1, False).capitalize()

    @factory.lazy_attribute
    def birthday(self):
        return now()
