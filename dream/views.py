from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .utils import get_object_or_None

from .models import Dream, Plan, Task, Idea


class DreamMixin(object):
    def get_context_data(self, **kwargs):
        context = super(DreamMixin, self).get_context_data(**kwargs)
        context['dream'] = get_object_or_None(Dream.objects.actual_list(), slug=self.kwargs['dream_slug'])
        return context


class PlanMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PlanMixin, self).get_context_data(**kwargs)
        context['plan'] = get_object_or_None(Plan.objects.actual_list(), slug=self.kwargs['plan_slug'])
        return context


class DreamCreateView(CreateView):
    model = Dream
    template_name_suffix = '_new_form'


class DreamEditView(UpdateView):
    model = Dream
    template_name_suffix = '_edit_form'


class DreamListView(ListView):
    model = Dream


class PlanCreateView(DreamMixin, CreateView):
    model = Plan
    template_name_suffix = '_new_form'


class PlanEditView(DreamMixin, UpdateView):
    model = Plan
    template_name_suffix = '_edit_form'


class PlanListView(DreamMixin, ListView):
    model = Plan


class TaskCreateView(PlanMixin, CreateView):
    model = Task
    template_name_suffix = '_new_form'


class TaskEditView(PlanMixin, UpdateView):
    model = Task
    template_name_suffix = '_edit_form'


class TaskListView(PlanMixin, ListView):
    model = Task


class IdeaCreateView(DreamMixin, PlanMixin, CreateView):
    model = Idea
    template_name_suffix = '_new_form'


class IdeaEditView(DreamMixin, PlanMixin, UpdateView):
    model = Idea
    template_name_suffix = '_edit_form'


class IdeaListView(DreamMixin, PlanMixin, ListView):
    model = Idea
