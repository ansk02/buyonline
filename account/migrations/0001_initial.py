# Generated by Django 3.2.4 on 2021-06-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=200, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=200, verbose_name='Nom')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name="Nom d'd'utilisateur")),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=60, verbose_name='Téléphone')),
                ('city', models.CharField(max_length=60, verbose_name='Ville')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Compte crée')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Dernière connexion')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin ?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff ?')),
                ('is_active', models.BooleanField(default=False, verbose_name='Actif ?')),
                ('is_superadmin', models.BooleanField(default=False, verbose_name='Super Admin ?')),
            ],
            options={
                'verbose_name': 'Compte',
                'verbose_name_plural': 'Comptes',
            },
        ),
    ]
