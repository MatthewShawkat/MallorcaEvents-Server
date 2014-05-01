# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'events_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'events', ['Category'])

        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('adult_price', self.gf('django.db.models.fields.DecimalField')(max_digits=9999, decimal_places=2)),
            ('child_price', self.gf('django.db.models.fields.DecimalField')(max_digits=9999, decimal_places=2)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Category'])),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Adding model 'Photo'
        db.create_table(u'events_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
        ))
        db.send_create_signal(u'events', ['Photo'])

        # Adding model 'Promotion'
        db.create_table(u'events_promotion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(max_digits=100, decimal_places=2)),
        ))
        db.send_create_signal(u'events', ['Promotion'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'events_category')

        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Deleting model 'Photo'
        db.delete_table(u'events_photo')

        # Deleting model 'Promotion'
        db.delete_table(u'events_promotion')


    models = {
        u'events.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'adult_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9999', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Category']"}),
            'child_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9999', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'events.photo': {
            'Meta': {'object_name': 'Photo'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'events.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'max_digits': '100', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['events']