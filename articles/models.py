from django.db import models
from django.db import models


from django.db import models

from django.conf import settings
from django.db.models.fields import DateField
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name="Başlık")
    body = models.TextField(verbose_name="Metin")
    date = models.DateField(auto_now_add=True, verbose_name="Tarih")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Yazar")



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
# Create your models here.
