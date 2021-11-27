# Generated by Django 2.2 on 2021-11-27 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('balance', models.IntegerField(default=0, verbose_name='Balance')),
                ('referrer_email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Referrer')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='BalanceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('event_type', models.IntegerField(choices=[(0, 'reservation'), (1, 'contest'), (2, 'promo_code'), (3, 'referral'), (4, 'other')], verbose_name='Event')),
                ('extra_info', models.TextField(blank=True, null=True, verbose_name='Extra info')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.AppUser', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Balance history',
                'verbose_name_plural': 'Balance histories',
            },
        ),
    ]