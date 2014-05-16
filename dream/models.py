from django.db import models
from django_extensions.db.fields import AutoSlugField
from pytils.translit import translify


class SlugModelMixin(models.Model):
    slug = AutoSlugField(populate_from='slug_translit', db_index=True)

    @property
    def slug_translit(self):
        return translify(getattr(self, self.SLUG_SOURCE))

    class Meta:
        abstract = True


class CoreModel(models.Model):
    is_active = models.BooleanField('Active', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DreamManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Dream(SlugModelMixin, CoreModel):
    SLUG_SOURCE = 'title'

    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)
    completion_date = models.DateTimeField('Completion date', blank=True, null=True)
    rating = models.IntegerField('Rating', blank=True, null=True)

    objects = DreamManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-rating',)


class PlanManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Plan(SlugModelMixin, CoreModel):
    SLUG_SOURCE = 'title'

    dream = models.ForeignKey(Dream, verbose_name='Dream', related_name='plans')
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)
    rating = models.IntegerField('Rating', blank=True, null=True)

    objects = PlanManager()

    def __unicode__(self):
        return self.title


class TaskManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Task(CoreModel):
    plan = models.ForeignKey(Plan, verbose_name='Plan', related_name='tasks')
    parent_task = models.ForeignKey('self', limit_choices_to={'parent_task': None}, verbose_name='Parent_task', related_name='child_tasks', blank=True, null=True)
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)
    start_date = models.DateTimeField('Start date', blank=True, null=True)
    end_date = models.DateTimeField('End date', blank=True, null=True)
    is_done = models.BooleanField('Done', default=False)

    objects = TaskManager()

    def __unicode__(self):
        return self.title


class IdeaManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Idea(CoreModel):
    dream = models.ForeignKey(Dream, verbose_name='Dream', related_name='ideas', blank=True, null=True)
    plan = models.ForeignKey(Plan, verbose_name='Plan', related_name='ideas', blank=True, null=True)
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)

    objects = IdeaManager()

    def __unicode__(self):
        return self.title
