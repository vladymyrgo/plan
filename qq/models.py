from django.db import models

from dream.models import CoreModel


class QuestionManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Question(CoreModel):
    parent_answer = models.OneToOneField('Answer', verbose_name='Parent answer', related_name='child_question', blank=True, null=True)
    body = models.CharField('Body', max_length=255)

    objects = QuestionManager()

    def __unicode__(self):
        return self.body


class AnswerManager(models.Manager):
    def actual_list(self):
        return self.get_queryset().filter(is_active=True)


class Answer(CoreModel):
    question = models.ForeignKey(Question, verbose_name='Question', related_name='answers')
    body = models.CharField('Body', max_length=255)

    objects = AnswerManager()

    def __unicode__(self):
        return self.body
