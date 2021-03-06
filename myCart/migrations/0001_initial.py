# Generated by Django 2.2.4 on 2019-09-22 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cook', '0006_auto_20190922_0904'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cook.Food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
