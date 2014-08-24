# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'api_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='member_info', unique=True, to=orm['auth.User'])),
            ('profile_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('paid', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('presenter', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('honorary', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Member'])

        # Adding M2M table for field projects on 'Member'
        m2m_table_name = db.shorten_name(u'api_member_projects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'api.member'], null=False)),
            ('project', models.ForeignKey(orm[u'api.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'project_id'])

        # Adding M2M table for field skills on 'Member'
        m2m_table_name = db.shorten_name(u'api_member_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'api.member'], null=False)),
            ('skill', models.ForeignKey(orm[u'api.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'skill_id'])

        # Adding model 'Skill'
        db.create_table(u'api_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'api', ['Skill'])

        # Adding model 'Project'
        db.create_table(u'api_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_started', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('date_completed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('competition', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Project'])

        # Adding model 'HackNight'
        db.create_table(u'api_hacknight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('presenter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='presentations', to=orm['api.Member'])),
        ))
        db.send_create_signal(u'api', ['HackNight'])

        # Adding M2M table for field tags on 'HackNight'
        m2m_table_name = db.shorten_name(u'api_hacknight_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hacknight', models.ForeignKey(orm[u'api.hacknight'], null=False)),
            ('tag', models.ForeignKey(orm[u'api.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hacknight_id', 'tag_id'])

        # Adding model 'Tag'
        db.create_table(u'api_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'api', ['Tag'])

        # Adding model 'HackNightResource'
        db.create_table(u'api_hacknightresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('presentation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resources', to=orm['api.HackNight'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('uploader', self.gf('django.db.models.fields.related.ForeignKey')(related_name='uploads', to=orm['api.Member'])),
        ))
        db.send_create_signal(u'api', ['HackNightResource'])

        # Adding model 'Announcement'
        db.create_table(u'api_announcement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('long_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='announcements', to=orm['api.Member'])),
        ))
        db.send_create_signal(u'api', ['Announcement'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'api_member')

        # Removing M2M table for field projects on 'Member'
        db.delete_table(db.shorten_name(u'api_member_projects'))

        # Removing M2M table for field skills on 'Member'
        db.delete_table(db.shorten_name(u'api_member_skills'))

        # Deleting model 'Skill'
        db.delete_table(u'api_skill')

        # Deleting model 'Project'
        db.delete_table(u'api_project')

        # Deleting model 'HackNight'
        db.delete_table(u'api_hacknight')

        # Removing M2M table for field tags on 'HackNight'
        db.delete_table(db.shorten_name(u'api_hacknight_tags'))

        # Deleting model 'Tag'
        db.delete_table(u'api_tag')

        # Deleting model 'HackNightResource'
        db.delete_table(u'api_hacknightresource')

        # Deleting model 'Announcement'
        db.delete_table(u'api_announcement')


    models = {
        u'api.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'announcements'", 'to': u"orm['api.Member']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'api.hacknight': {
            'Meta': {'object_name': 'HackNight'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presenter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'presentations'", 'to': u"orm['api.Member']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'presentations'", 'symmetrical': 'False', 'to': u"orm['api.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.hacknightresource': {
            'Meta': {'object_name': 'HackNightResource'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resources'", 'to': u"orm['api.HackNight']"}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uploads'", 'to': u"orm['api.Member']"})
        },
        u'api.member': {
            'Meta': {'object_name': 'Member'},
            'honorary': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'presenter': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'profile_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Project']", 'symmetrical': 'False'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Skill']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'member_info'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'api.project': {
            'Meta': {'object_name': 'Project'},
            'competition': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'date_completed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'api.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['api']