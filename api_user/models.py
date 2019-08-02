from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUser(AbstractUser):
    is_parent = models.BooleanField(
        _('is parent'),
        default=False,
        help_text=(
            'Designates whether this user should assign tasks'
            'In ParentMode is const (api.models.parent_mode = True); in StudentMode changing periodically'
        )
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.username
