# Generated by Django 2.0.6 on 2018-06-27 11:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imported_file', models.FileField(unique=True, upload_to='')),
                ('as_of', models.DateField(default=django.utils.timezone.now)),
                ('description', models.CharField(default='n/a', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReconciliationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recon_msg', models.CharField(default='n/a', max_length=100)),
                ('file_1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recon_file_1', to='core.FileModel')),
                ('file_2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recon_file_2', to='core.FileModel')),
            ],
        ),
    ]
