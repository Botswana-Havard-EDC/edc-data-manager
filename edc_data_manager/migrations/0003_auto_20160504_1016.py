# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 10:16
from __future__ import unicode_literals

from django.db import migrations
import django_crypto_fields.fields.encrypted_text_field


class Migration(migrations.Migration):

    dependencies = [
        ('edc_data_manager', '0002_auto_20160504_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionitem',
            name='comment',
            field=django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(help_text=' (Encryption: AES local) (Encryption: AES local) (Encryption: AES local)'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(help_text=' (Encryption: AES local) (Encryption: AES local) (Encryption: AES local)'),
        ),
    ]