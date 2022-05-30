from django.db import models

# Create your models here.
class AccountsInstitution(models.Model):
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING, primary_key=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    name_organisation = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    license_file = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'accounts_institution'


class AccountsLocum(models.Model):
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING, primary_key=True)
    profile_image = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    about_me = models.TextField()
    service = models.CharField(max_length=255, blank=True, null=True)
    cv_file = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'accounts_locum'


class AccountsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_locum = models.BooleanField()
    is_institution = models.BooleanField()
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'accounts_user'