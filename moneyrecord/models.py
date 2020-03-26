from django.db import models

# Create your models here.
class Allmoney(models.Model):

    time=models.DateField(_("时间"), auto_now=True, auto_now_add=False)
    money=models.FloatField(_("金额"))

    class Meta:
        verbose_name = _("所有money")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.money

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
