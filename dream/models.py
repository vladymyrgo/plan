from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.core.urlresolvers import reverse
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

    qq = models.TextField('QQ', blank=True, null=True)
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)
    completion_date = models.DateField('Completion date', blank=True, null=True)
    rating = models.IntegerField('Rating', blank=True, null=True)

    objects = DreamManager()

    class Meta:
        ordering = ('-rating',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dream:edit', args=(self.slug,))

    def get_create_plan_url(self):
        return reverse('plan:new', args=(self.slug,))


class PlanManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Plan(SlugModelMixin, CoreModel):
    SLUG_SOURCE = 'title'

    dream = models.ForeignKey(Dream, verbose_name='Dream', related_name='plans')
    qq = models.TextField('QQ', blank=True, null=True)
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)
    rating = models.IntegerField('Rating', blank=True, null=True)

    objects = PlanManager()

    class Meta:
        ordering = ('-rating',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('plan:edit', args=(self.dream.slug, self.slug,))

    def get_create_task_url(self):
        return reverse('task:new', args=(self.dream.slug, self.slug,))


class TaskManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)

    def to_do_list(self):
        return self.actual_list().filter(is_done=False)


class Task(CoreModel):
    plan = models.ForeignKey(Plan, verbose_name='Plan', related_name='tasks', blank=True, null=True)
    # parent_task = models.ForeignKey('self', limit_choices_to={'parent_task': None}, verbose_name='Parent_task', related_name='child_tasks', blank=True, null=True)
    qq = models.TextField('QQ', blank=True, null=True)
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)
    start_date = models.DateField('Start date', blank=True, null=True)
    end_date = models.DateField('End date', blank=True, null=True)
    is_done = models.BooleanField('Done', default=False)

    objects = TaskManager()

    class Meta:
        ordering = ('start_date',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task:edit', args=(self.plan.dream.slug, self.plan.slug, self.id,))


class IdeaManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Idea(CoreModel):
    dream = models.ForeignKey(Dream, verbose_name='Dream', related_name='ideas', blank=True, null=True)
    plan = models.ForeignKey(Plan, verbose_name='Plan', related_name='ideas', blank=True, null=True)
    qq = models.TextField('QQ', blank=True, null=True)
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)

    objects = IdeaManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('idea:edit', args=(self.id,))
