# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'EmailList.query_sql'
        db.add_column('emailer_emaillist', 'query_sql', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding M2M table for field site_users on 'EmailList'
        db.create_table('emailer_emaillist_site_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('emaillist', models.ForeignKey(orm['emailer.emaillist'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('emailer_emaillist_site_users', ['emaillist_id', 'user_id'])


    def backwards(self, orm):
        
        # Deleting field 'EmailList.query_sql'
        db.delete_column('emailer_emaillist', 'query_sql')

        # Removing M2M table for field site_users on 'EmailList'
        db.delete_table('emailer_emaillist_site_users')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'emailer.email': {
            'Meta': {'ordering': "['date_created']", 'object_name': 'Email'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_blast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emailer.EmailBlast']"}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'58d53282-4c8c-4ba8-82dc-2f5af1afab48'", 'max_length': '36', 'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.CharField', [], {'default': "'fff405cf-58e6-4b01-b803-99b958076258'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'send_after': ('django.db.models.fields.DateTimeField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'emailer.emaillist': {
            'Meta': {'ordering': "['date_created']", 'object_name': 'EmailList'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'4137e684-e415-42ec-8266-1430fd5440ab'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'query_sql': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'site_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'emailer.emailtemplate': {
            'Meta': {'object_name': 'EmailTemplate'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'8e6437a8-3dfd-4c14-be21-c246d71da579'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['emailer']
