from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from teams.models import teams


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, identification, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(identification, email, user_name, first_name, password, **other_fields)

    def create_user(self, identification, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(identification=identification, email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class customUser(AbstractBaseUser, PermissionsMixin):
    identification = models.IntegerField(unique=True, primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(auto_now=True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    team_id = models.ManyToManyField(teams, through='team_user')

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'identification']

    def __str__(self):
        return self.user_name

    class Meta:
        permissions = [
            ('can_create', _('Create Permission')),
            ('can_update', _('Update Permission')),
        ]


class team_user(models.Model):
    id_team = models.ForeignKey(teams, on_delete=models.CASCADE, blank=True, null=True)
    id_User = models.ForeignKey(customUser, on_delete=models.CASCADE, blank=True, null=True)
    date_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.id_User_id) + '  Time: ' + str(self.date_time)
