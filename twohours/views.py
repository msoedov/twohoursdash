from django.shortcuts import resolve_url
from django.views.generic import ListView, UpdateView, DetailView
from separated.views import CsvView
from .models import User
from .templatetags.th_tags import eligible, bizz


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User

    def get_success_url(self):
        return resolve_url('twohours:user_details', pk=self.object.pk)


class UserListView(ListView):
    model = User


class UserCsvList(CsvView):
    model = User
    columns = [
        ('username', 'Username'),
        ('birthday', 'Birthday'),
        (lambda m: eligible(m.birthday), 'Eligible'),
        ('random', 'Random'),
        (lambda m: bizz(m.random), 'BizzFizz'),
    ]

user_details = UserDetailView.as_view()
user_update = UserUpdateView.as_view()
user_list = UserListView.as_view()
user_csv = UserCsvList.as_view()
