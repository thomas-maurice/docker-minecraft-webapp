from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from minecraft.forms import UserForm

class ListUsers(ListView):
    model = User
    template_name = "user/user_list.html"
    paginate_by = 10
    queryset = User.objects.filter()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListUsers, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListUsers, self).get_context_data(**kwargs)
        return context

class ShowUser(DetailView):
    model = User
    template_name = "user/user.html"
    context_object_name = "u"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShowUser, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])

    def get_object(self):
        return super(ShowUser, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(ShowUser, self).get_context_data(**kwargs)
        return context

class UpdateUser(UpdateView):
    model = User
    template_name = "user/user_update_form.html"
    form_class = UserForm
    context_object_name = "u"

    def get_success_url(self):
        return reverse_lazy('show_user', kwargs={"pk":self.kwargs['pk']})

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.kwargs['pk'])

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateUser, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        #form.instance.author = self.request.user
        self.object.set_password(form.instance.password)
        return super(UpdateUser, self).form_valid(form)

class DeleteUser(DeleteView):
    model = User
    template_name = "user/user_delete_form.html"
    success_url = reverse_lazy('list_user')
    context_object_name = "u"

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteUser, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.kwargs['pk'])

class CreateUser(CreateView):
    model = User
    template_name = "user/user_create_form.html"
    form_class = UserForm
    success_url = reverse_lazy("list_user")
    context_object_name = "u"

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateUser, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        self.object.set_password(self.object.password)
        self.object.save()
        return reverse_lazy('show_user', kwargs={"pk":self.object.id})

    def form_valid(self, form):
        return super(CreateUser, self).form_valid(form)
