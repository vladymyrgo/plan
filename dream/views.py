from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .utils import get_object_or_None

from .forms import DreamForm, TaskForm

from .models import Dream, Plan, Task, Idea


class DreamMixin(object):
    def get_context_data(self, **kwargs):
        context = super(DreamMixin, self).get_context_data(**kwargs)
        context['dream'] = get_object_or_None(Dream.objects.actual_list(), slug=self.kwargs.get('dream_slug'))
        return context


class PlanMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PlanMixin, self).get_context_data(**kwargs)
        context['plan'] = get_object_or_None(Plan.objects.actual_list(), slug=self.kwargs.get('plan_slug'))
        return context


class DreamCreateView(CreateView):
    model = Dream
    form_class = DreamForm
    template_name_suffix = '_new_form'


class DreamEditView(UpdateView):
    model = Dream
    form_class = DreamForm
    template_name_suffix = '_edit_form'


class DreamListView(ListView):
    model = Dream
    queryset = Dream.objects.actual_list()


class PlanCreateView(DreamMixin, CreateView):
    model = Plan
    template_name_suffix = '_new_form'


class PlanEditView(DreamMixin, UpdateView):
    model = Plan
    template_name_suffix = '_edit_form'


class PlanListView(DreamMixin, ListView):
    model = Plan
    queryset = Plan.objects.actual_list()


class TaskCreateView(DreamMixin, PlanMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name_suffix = '_new_form'


class TaskEditView(DreamMixin, PlanMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name_suffix = '_edit_form'


class TaskToDoListView(DreamMixin, PlanMixin, ListView):
    model = Task
    queryset = Task.objects.to_do_list()

    def get_context_data(self, **kwargs):
        context = super(TaskToDoListView, self).get_context_data(**kwargs)
        context['tasks_with_plan'] = Task.objects.with_plan_list()
        context['tasks_without_plan'] = Task.objects.without_plan_list()
        return context


class TaskPurchasesListView(DreamMixin, PlanMixin, ListView):
    model = Task
    template_name = 'dream/task_purchase_list.html'
    queryset = Task.objects.purchase_list()


class IdeaCreateView(DreamMixin, PlanMixin, CreateView):
    model = Idea
    template_name_suffix = '_new_form'


class IdeaEditView(DreamMixin, PlanMixin, UpdateView):
    model = Idea
    template_name_suffix = '_edit_form'

    def get_context_data(self, **kwargs):
        context = super(IdeaEditView, self).get_context_data(**kwargs)
        context['dream'] = self.object.dream
        context['plan'] = self.object.plan
        return context


class IdeaListView(DreamMixin, PlanMixin, ListView):
    model = Idea
    queryset = Idea.objects.actual_list()
