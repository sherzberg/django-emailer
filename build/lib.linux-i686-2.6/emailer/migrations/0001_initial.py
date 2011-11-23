# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EmailTemplate'
        db.create_table('emailer_emailtemplate', (
            ('id', self.gf('django.db.models.fields.CharField')(default='65792b55-240e-4c80-9126-b650a7c51136', max_length=36, primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('emailer', ['EmailTemplate'])

        # Adding model 'EmailList'
        db.create_table('emailer_emaillist', (
            ('id', self.gf('django.db.models.fields.CharField')(default='f70bf28d-8f29-46dd-ac15-fda3692031eb', max_length=36, primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('emailer', ['EmailList'])

        # Adding model 'EmailBlast'
        db.create_table('emailer_emailblast', (
            ('id', self.gf('django.db.models.fields.CharField')(default='4938f5b0-b959-47a7-a2fe-c32713b9af77', max_length=36, primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('send_after', self.gf('django.db.models.fields.DateTimeField')()),
            ('from_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('emailer', ['EmailBlast'])

        # Adding model 'Email'
        db.create_table('emailer_email', (
            ('id', self.gf('django.db.models.fields.CharField')(default='e69926a6-5aca-4c96-a482-df304adc9f54', max_length=36, primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('email_blast', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emailer.EmailBlast'])),
            ('to_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('merge_data', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('opened', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('emailer', ['Email'])


    def backwards(self, orm):
        
        # Deleting model 'EmailTemplate'
        db.delete_table('emailer_emailtemplate')

        # Deleting model 'EmailList'
        db.delete_table('emailer_emaillist')

        # Deleting model 'EmailBlast'
        db.delete_table('emailer_emailblast')

        # Deleting model 'Email'
        db.delete_table('emailer_email')


    models = {
        'emailer.email': {
            'Meta': {'ordering': "['date_created']", 'object_name': 'Email'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_blast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emailer.EmailBlast']"}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'37ebacce-ec19-410c-bf79-8a7c87f80d5d'", 'max_length': '36', 'primary_key': 'True'}),
            'merge_data': ('django.db.models.fields.TextField', [], {}),
            'opened': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        },
        'emailer.emailblast': {
            'Meta': {'ordering': "['date_created']", 'object_name': 'EmailBlast'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'724f2e29-7df5-4f17-8a99-b1fa80251ab5'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'send_after': ('django.db.models.fields.DateTimeField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'emailer.emaillist': {
            'Meta': {'ordering': "['date_created']", 'object_name': 'EmailList'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'764d68ef-c44a-4288-bbdf-f9d08b433791'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'emailer.emailtemplate': {
            'Meta': {'object_name': 'EmailTemplate'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'4d317b84-e206-4c55-b9b3-bd27eb8bc98b'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        }
    }

    complete_apps = ['emailer']
