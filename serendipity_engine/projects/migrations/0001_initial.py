# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('office_location', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding M2M table for field units on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_units')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('unit', models.ForeignKey(orm[u'units.unit'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'unit_id'])

        # Adding M2M table for field contributors on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_contributors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('contributor', models.ForeignKey(orm[u'units.contributor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'contributor_id'])

        # Adding M2M table for field elements on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_elements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('element', models.ForeignKey(orm[u'elements.element'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'element_id'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Removing M2M table for field units on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_units'))

        # Removing M2M table for field contributors on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_contributors'))

        # Removing M2M table for field elements on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_elements'))


    models = {
        u'elements.element': {
            'Meta': {'object_name': 'Element'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['units.Contributor']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'elements': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['elements.Element']", 'symmetrical': 'False', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'office_location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'units': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': u"orm['units.Unit']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'units.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'units.unit': {
            'Meta': {'object_name': 'Unit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']