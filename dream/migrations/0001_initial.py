# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dream'
        db.create_table(u'dream_dream', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('completion_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dream', ['Dream'])

        # Adding model 'Plan'
        db.create_table(u'dream_plan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dream', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plans', to=orm['dream.Dream'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dream', ['Plan'])

        # Adding model 'Task'
        db.create_table(u'dream_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', to=orm['dream.Plan'])),
            ('parent_task', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_tasks', null=True, to=orm['dream.Task'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_done', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'dream', ['Task'])

        # Adding model 'Idea'
        db.create_table(u'dream_idea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dream', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ideas', null=True, to=orm['dream.Dream'])),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ideas', null=True, to=orm['dream.Plan'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dream', ['Idea'])


    def backwards(self, orm):
        # Deleting model 'Dream'
        db.delete_table(u'dream_dream')

        # Deleting model 'Plan'
        db.delete_table(u'dream_plan')

        # Deleting model 'Task'
        db.delete_table(u'dream_task')

        # Deleting model 'Idea'
        db.delete_table(u'dream_idea')


    models = {
        u'dream.dream': {
            'Meta': {'ordering': "('-rating',)", 'object_name': 'Dream'},
            'completion_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'dream.idea': {
            'Meta': {'object_name': 'Idea'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dream': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ideas'", 'null': 'True', 'to': u"orm['dream.Dream']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ideas'", 'null': 'True', 'to': u"orm['dream.Plan']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'dream.plan': {
            'Meta': {'object_name': 'Plan'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dream': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plans'", 'to': u"orm['dream.Dream']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'dream.task': {
            'Meta': {'object_name': 'Task'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent_task': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_tasks'", 'null': 'True', 'to': u"orm['dream.Task']"}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': u"orm['dream.Plan']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dream']