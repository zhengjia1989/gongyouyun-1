# Generated by Django 2.2.6 on 2020-04-10 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20200403_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testrecord',
            options={'ordering': ['id'], 'verbose_name': '考试记录', 'verbose_name_plural': '考试记录'},
        ),
    ]