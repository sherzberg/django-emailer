# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'EmailList.query_sql'
        db.delete_column('emailer_emaillist', 'query_sql')

        # Deleting field 'EmailList.raw_emails'
        db.delete_column('emailer_emaillist', 'raw_emails')

        # Adding field 'EmailList.data_raw_emails'
        db.add_column('emailer_emaillist', 'data_raw_emails', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'EmailList.data_query_sql'
        db.add_column('emailer_emaillist', 'data_query_sql', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Removing M2M table for field site_users on 'EmailList'
        db.delete_table('emailer_emaillist_site_users')

        # Adding M2M table for field data_site_users on 'EmailList'
        db.create_table('emailer_emaillist_data_site_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('emaillist', models.ForeignKey(orm['emailer.emaillist'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('emailer_emaillist_data_site_users', ['emaillist_id', 'user_id'])


    def backwards(self, orm):
        
        # Adding field 'EmailList.query_sql'
        db.add_column('emailer_emaillist', 'query_sql', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'EmailList.raw_emails'
        db.add_column('emailer_emaillist', 'raw_emails', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Deleting field 'EmailList.data_raw_emails'
        db.delete_column('emailer_emaillist', 'data_raw_emails')

        # Deleting field 'EmailList.data_query_sql'
        db.delete_column('emailer_emaillist', 'data_query_sql')

        # Adding M2M table for field site_users on 'EmailList'
        db.create_table('emailer_emaillist_site_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('emaillist', models.ForeignKey(orm['emailer.emaillist'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('emailer_emaillist_site_users', ['emaillist_id', 'user_id'])

        # Removing M2M table for field data_site_users on 'EmailList'
        db.delete_table('emailer_emaillist_data_site_users')


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
            'id': ('django.db.models.fields.CharField', [], {'default': "'9a2634c8-ba4f-483d-a9ec-bd3322220533'", 'max_length': '36', 'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.CharField', [], {'default': "'8a5d04d2-6828-49ff-b42b-59b1a8c73376'", 'max_length': '36', 'primary_key': 'True'}),
            'lists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emailer.EmailList']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'send_after': ('django.db.models.fields.DateTimeField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'emailer.emaillist': {
            'Meta': {'ordering': "['date_created']", 'object_name': 'EmailList'},
            'data_query_sql': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'data_raw_emails': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'data_site_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'ffe55fb4-b11a-4cd2-ac20-07b8f0c18a45'", 'max_length': '36', 'primary_key': 'True'}),
            'is_oneoff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'emailer.emailtemplate': {
            'Meta': {'object_name': 'EmailTemplate'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'082baf20-0196-48ce-8238-10b770d53dc0'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['emailer']
