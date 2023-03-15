import uuid

from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse


class Province(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class PromotionApplicant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='')
    reg_number = models.CharField(max_length=100)
    nat_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    application_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class PromotionWeeklyDraw(models.Model):
    weekly_winner = models.ForeignKey(PromotionApplicant, on_delete=models.CASCADE)
    draw_number = models.IntegerField(default=0, null=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    notified = models.BooleanField(default=False)
    notified_on = models.DateField()
    price_claimed = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.weekly_winner.first_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class GrandPriceDraw(models.Model):
    weekly_winner = models.ForeignKey(PromotionApplicant, on_delete=models.CASCADE)
    draw_number = models.IntegerField(default=0, null=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    notified = models.BooleanField(default=False)
    notified_on = models.DateField()
    price_claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.weekly_winner.first_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class vlicDb(models.Model):
    Regno = models.CharField(max_length=100, null=False)
    Status = models.CharField(max_length=100,null=False)
    Penalties = models.IntegerField(default=0)
    Arrears = models.IntegerField(default=0)
    DateLicensed = models.DateField(null=False)
    ExpiryDate = models.DateField(null=False)
    dateCaptured = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Regno

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class LicenseDb(models.Model):
    EXPIRED = models.CharField(max_length=100, null=True)
    REGISTRATION_NO = models.CharField(max_length=100, null=False)
    LICENSE_STATUS = models.CharField(max_length=100,null=False)
    PENALTY_AMOUNT = models.IntegerField(default=0)
    ARREAR_AMOUNT = models.IntegerField(default=0)
    LAST_LICENSING_TRANSACTION = models.DateTimeField(null=False)
    BLACKLISTED = models.CharField(max_length=100)
    LICENCE_EXPIRY_DATE = models.DateTimeField(null=False)
    Date_Captured = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.REGISTRATION_NO

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
