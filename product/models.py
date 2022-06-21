from django.db import models
from user.models import UserModel
from datetime import datetime

class ProductModel(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=100)
    desc = models.TextField("내용")
    thumnail = models.ImageField("썸네일", upload_to='product/thumnail/', blank=True)
    created_at = models.DateTimeField("등록일", auto_now_add=True)
    updated_at = models.DateTimeField("업데이트",auto_now=True)
    exposure_start = models.DateTimeField("게시 시간", default=datetime.now)
    exposure_end = models.DateTimeField("게시 종료", default=datetime.now)

    def __str__(self):
        return self.title