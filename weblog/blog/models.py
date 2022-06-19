from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    catename = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.catename

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class Tags(models.Model):
    tagname = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.tagname

class Articles(models.Model):
    title = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='类别')
    tags = models.ManyToManyField(Tags, on_delete=models.DO_NOTHING, verbose_name='标签')
    summary = models.TextField(blank=True, max_length=255)
    content = models.TextField()
    