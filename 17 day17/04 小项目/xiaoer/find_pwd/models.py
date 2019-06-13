from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    realname = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    channel = models.CharField(max_length=4)
    phone = models.CharField(max_length=32)
    sex = models.TextField()  # This field type is a guess.
    province_id = models.PositiveIntegerField()
    city_id = models.PositiveIntegerField()
    head_url = models.CharField(max_length=125)
    login_secret = models.CharField(max_length=8)
    money = models.FloatField()
    creator = models.PositiveIntegerField()
    creation = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'account'
