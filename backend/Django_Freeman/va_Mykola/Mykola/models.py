from django.db import models


class Users(models.Model):
    person_email = models.EmailField(max_length=250)
    person_password = models.CharField(max_length=30, default='')

    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    telegram_id = models.CharField(max_length=100, blank=True)

    counter_login = models.IntegerField(default=0)
    data_reg = models.DateField(auto_now_add=True)
    lust_login = models.DateField(auto_now=True)

    def __str__(self):
        return self.telegram_id

    # class Meta:
    #     verbose_name = "Mykola's users"
    #     verbose_name_plural = "Mykola's users"
    #     ordering = ['data_reg']


class Features(models.Model):
    features_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.features_name
