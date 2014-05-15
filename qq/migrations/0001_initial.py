# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'qq_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('parent_answer', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='child_question', unique=True, null=True, to=orm['qq.Answer'])),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'qq', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'qq_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['qq.Question'])),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'qq', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'qq_question')

        # Deleting model 'Answer'
        db.delete_table(u'qq_answer')


    models = {
        u'qq.answer': {
            'Meta': {'object_name': 'Answer'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['qq.Question']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'qq.question': {
            'Meta': {'object_name': 'Question'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'parent_answer': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'child_question'", 'unique': 'True', 'null': 'True', 'to': u"orm['qq.Answer']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['qq']