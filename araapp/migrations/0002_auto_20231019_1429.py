# Generated by Django 3.2.22 on 2023-10-19 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('araapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer_info',
            name='cate1',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='influencer_info',
            name='cate2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='influencer_info',
            name='cate3',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='influencer_info',
            name='local',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
