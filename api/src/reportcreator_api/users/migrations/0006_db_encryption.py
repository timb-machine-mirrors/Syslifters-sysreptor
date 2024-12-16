# Generated by Django 4.1.2 on 2022-10-27 17:26

from django.db import migrations, models

import reportcreator_api.users.querysets
import reportcreator_api.utils.crypto.fields


def migrate_to_encryption(apps, schema_editor):
    PentestUser = apps.get_model('users', 'PentestUser')

    users = list(PentestUser.objects.all())
    for u in users:
        u.password_new = u.password
    PentestUser.objects.bulk_update(users, ['password_new'])


def reverse_migrate_from_encryption(apps, schema_editor):
    PentestUser = apps.get_model('users', 'PentestUser')

    users = list(PentestUser.objects.all())
    for u in users:
        u.password = u.password_new
    PentestUser.objects.bulk_update(users, ['password'])


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_guest_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('expire_date', models.DateTimeField(db_index=True, verbose_name='expire date')),
                ('session_key', reportcreator_api.utils.crypto.fields.EncryptedField(base_field=models.CharField(max_length=40, verbose_name='session key'), editable=True)),
                ('session_data', reportcreator_api.utils.crypto.fields.EncryptedField(base_field=models.TextField(verbose_name='session data'), editable=True)),
                ('session_key_hash', models.BinaryField(max_length=32, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
                'abstract': False,
            },
            managers=[
                ('objects', reportcreator_api.users.querysets.SessionManager()),
            ],
        ),
        migrations.AddField(
            model_name='pentestuser',
            name='password_new',
            field=reportcreator_api.utils.crypto.fields.EncryptedField(base_field=models.CharField(max_length=128, default='', verbose_name='password'), editable=True),
            preserve_default=False,
        ),
        migrations.RunPython(code=migrate_to_encryption, reverse_code=reverse_migrate_from_encryption),
        migrations.RemoveField(
            model_name='pentestuser',
            name='password',
        ),
        migrations.RenameField(
            model_name='pentestuser',
            old_name='password_new',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='pentestuser',
            name='password',
            field=reportcreator_api.utils.crypto.fields.EncryptedField(base_field=models.CharField(max_length=128, verbose_name='password'), editable=True),
        ),
    ]
