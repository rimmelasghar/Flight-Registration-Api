# Generated by Django 4.1 on 2022-09-03 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('available_seats', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('num', models.CharField(max_length=30, unique=True)),
                ('departure', models.CharField(max_length=100)),
                ('arrival', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('duration', models.CharField(max_length=30)),
                ('seats', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketid', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('A', 'Active'), ('NA', 'Non-Active')], max_length=30)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bohatsasta.details')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='bohatsasta.flight'),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30)),
                ('card_type', models.CharField(choices=[('mc', 'MASTER CARD'), ('vc', 'VISA CARD')], max_length=3)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
