# Generated by Django 4.2.10 on 2024-03-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0002_remove_userprofile_profile_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
    ]