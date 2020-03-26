from django.db import models

# Create your models here.


class Allmoney(models.Model):

    time = models.DateTimeField('时间', auto_now=True, auto_now_add=False)
    money = models.FloatField('金额', default=0)

    class Meta:
        verbose_name = "所有money"
        # verbose_name_plural = "们"

    def __str__(self):
        return str(self.time)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Detailmoney(models.Model):

    allmoney = models.ForeignKey(
        Allmoney, verbose_name='对应总额', on_delete=models.CASCADE)
    jingdong = models.FloatField('京东', default=0)
    zhifubao = models.FloatField('支付宝', default=0)
    qita = models.FloatField('其他', default=0)
    huabei = models.FloatField('花呗', default=0)
    baitiao = models.FloatField('白条', default=0)

    class Meta:
        verbose_name = '明细'
        # verbose_name_plural = _("s")

    def __str__(self):
        return str(self.allmoney)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
