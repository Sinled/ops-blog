# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteUsers'
        db.create_table(u'blog_siteusers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True)),
            ('github', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['SiteUsers'])

        # Adding field 'Blog.post_author'
        db.add_column(u'blog_blog', 'post_author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.SiteUsers'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SiteUsers'
        db.delete_table(u'blog_siteusers')

        # Deleting field 'Blog.post_author'
        db.delete_column(u'blog_blog', 'post_author_id')


    models = {
        u'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.SiteUsers']", 'null': 'True', 'blank': 'True'}),
            'post_illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post_text': ('django.db.models.fields.TextField', [], {}),
            'post_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.PostType']", 'null': 'True', 'blank': 'True'})
        },
        u'blog.posttype': {
            'Meta': {'object_name': 'PostType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'blog.siteusers': {
            'Meta': {'object_name': 'SiteUsers'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']