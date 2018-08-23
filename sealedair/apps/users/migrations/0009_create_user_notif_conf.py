from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
import django.contrib.postgres.fields
from django.db import migrations, models


def create_user_notifications(apps, schema_editor):

    User = apps.get_model("auth", "User")
    UserNofiConfig = apps.get_model(
        'sealedair_notifications', 'UserNotificationsConfig')
    db_alias = schema_editor.connection.alias

    for u in User.objects.using(db_alias).all():
        try:
            user_notif = u.notifications_config
        except ObjectDoesNotExist:
            new_user_notif = UserNofiConfig.objects.create(user=u)


def do_nothing(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('sealedair_users', '0008_auto_20180730_0559'),
    ]

    operations = [
        migrations.RunPython(create_user_notifications, do_nothing),
    ]
