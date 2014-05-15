from django.db import models


class CoreModel(models.Model):
    is_active = models.BooleanField('Active', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DreamManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Dream(CoreModel):
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


class Plan(CoreModel):
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

    objects = TaskManager()

    def __unicode__(self):
        return self.title


class IdeaManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Idea(CoreModel):
    plan = models.ForeignKey(Plan, verbose_name='Plan', related_name='ideas')
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', blank=True, null=True)

    objects = IdeaManager()

    def __unicode__(self):
        return self.title
