import logging

from django.db import models
from django.utils.translation import gettext as _

logger = logging.getLogger(__name__)

REFERRAL_BONUS = 20


class AppUser(models.Model):
    first_name = models.CharField(_('First name'), max_length=100)
    last_name = models.CharField(_('Last name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=100)
    balance = models.IntegerField(_('Balance'), default=0)
    referrer_email = models.EmailField(_('Referrer'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def get_referrer(self):
        qs = AppUser.objects.filter(email=self.referrer_email)
        if count := qs.count() > 1:
            logger.warning('Unexpected number of referrers %s', count)
        return qs.first()

    def add_points(self, amount):
        self.balance += amount
        self.save()


class BalanceHistory(models.Model):
    TYPES = (
        (0, 'reservation'),
        (1, 'contest'),
        (2, 'promo_code'),
        (3, 'referral'),
        (4, 'other'),
    )
    user = models.ForeignKey(AppUser, verbose_name=_('User'), on_delete=models.CASCADE)
    amount = models.IntegerField(_('Amount'))
    event_type = models.IntegerField(_('Event'), choices=TYPES)
    extra_info = models.TextField(_('Extra info'), null=True, blank=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('Balance history')
        verbose_name_plural = _('Balance histories')

    def __str__(self):
        return f'{self.user} {self.amount}'
