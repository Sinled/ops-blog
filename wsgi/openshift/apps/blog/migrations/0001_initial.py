# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostType'
        db.create_table(u'blog_posttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'blog', ['PostType'])

        # Adding model 'Blog'
        db.create_table(u'blog_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.PostType'], null=True, blank=True)),
            ('post_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('post_text', self.gf('django.db.models.fields.TextField')()),
            ('post_illustration', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Blog'])


    def backwards(self, orm):
        # Deleting model 'PostType'
        db.delete_table(u'blog_posttype')

        # Deleting model 'Blog'
        db.delete_table(u'blog_blog')


    models = {
        u'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post_text': ('django.db.models.fields.TextField', [], {}),
            'post_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.PostType']", 'null': 'True', 'blank': 'True'})
        },
        u'blog.posttype': {
            'Meta': {'object_name': 'PostType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['blog']