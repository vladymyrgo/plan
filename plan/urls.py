from django.conf.urls import patterns, include, url
from django.contrib import admin

from dream.views import (
    DreamListView, DreamCreateView, DreamEditView,
    PlanListView, PlanCreateView, PlanEditView,
    TaskListView, TaskCreateView, TaskEditView,
    IdeaListView, IdeaCreateView, IdeaEditView
)

admin.autodiscover()

dream_patterns = patterns('',
    # noqa
    url(r'^$', DreamListView.as_view(), name='list'),
    # url(r'^dreams/(?P<dream_filter>active|possible|reserve|staffed|finished|managed)/$',
    #     DreamListView.as_view(),
    #     name='list'),
    url(r'^dreams/new/$',
        DreamCreateView.as_view(),
        name='new'),
    url(r'^dreams/(?P<slug>[-_\w]+)/$',
        DreamEditView.as_view(),
        name='edit'),
)

plan_patterns = patterns('',
    # noqa
    url(r'^dreams/(?P<dream_slug>[-_\w]+)/plans/$',
        PlanListView.as_view(),
        name='list'),
    url(r'^dreams/(?P<dream_slug>[-_\w]+)/plans/new/$',
        PlanCreateView.as_view(),
        name='new'),
    url(r'^dreams/(?P<dream_slug>[-_\w]+)/plans/(?P<slug>[-_\w]+)/$',
        PlanEditView.as_view(),
        name='edit'),
)

task_patterns = patterns('',
    # noqa
    url(r'^tasks/$',
        TaskListView.as_view(),
        name='list'),
    url(r'^dreams/(?P<dream_slug>[-_\w]+)/plans/(?P<plan_slug>[-_\w]+)/tasks/new/$',
        TaskCreateView.as_view(),
        name='new'),
    url(r'^dreams/(?P<dream_slug>[-_\w]+)/plans/(?P<plan_slug>[-_\w]+)/tasks/(?P<pk>\d+)/$',
        TaskEditView.as_view(),
        name='edit'),
)

idea_patterns = patterns('',
    # noqa
    url(r'^ideas/new/$',
        IdeaCreateView.as_view(),
        name='new'),
    url(r'^dreams/(?P<dream_slug>[-_\w]+)/ideas/$',
        IdeaListView.as_view(),
        name='list_for_dream'),
    # url(r'^dreams/(?P<dream_slug>[-_\w]+)/ideas/new/$',
    #     IdeaCreateView.as_view(),
    #     name='new_for_dream'),
    url(r'^dreams/(?P<dream_slug>[-_\w]+)/plans/(?P<plan_slug>[-_\w]+)/ideas/$',
        IdeaListView.as_view(),
        name='list_for_plan'),
    # url(r'^dreams/(?P<dream_slug>[-_\w]+)/plans/(?P<plan_slug>[-_\w]+)/ideas/new/$',
    #     IdeaCreateView.as_view(),
    #     name='new_for_plan'),
    url(r'^ideas/(?P<pk>\d+)/$',
        IdeaEditView.as_view(),
        name='edit'),
)

urlpatterns = patterns('',
    # noqa
    url(r'^', include(dream_patterns, namespace='dream')),
    url(r'^', include(plan_patterns, namespace='plan')),
    url(r'^', include(task_patterns, namespace='task')),
    url(r'^', include(idea_patterns, namespace='idea')),
    url(r'^admin/', include(admin.site.urls)),
)
