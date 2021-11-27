import csv

from django.core.management.base import BaseCommand
from django.db import transaction

from users.models import AppUser, BalanceHistory, REFERRAL_BONUS


class Command(BaseCommand):
    help = 'Import users from csv'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    @transaction.atomic
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                user = AppUser.objects.create(
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    referrer_email=row[4],
                    balance=row[5],
                )
                if referrer := user.get_referrer:
                    referrer.add_points(REFERRAL_BONUS)
                    BalanceHistory.objects.create(
                        amount=REFERRAL_BONUS,
                        user=referrer,
                        event_type=3,  # referral
                        extra_info=f'Referred {user}'
                    )
