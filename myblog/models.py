from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #게시자 변수
    title = models.CharField(max_length =200) #제목
    text = models.TextField() #본문
    created_date = models.DateTimeField(default = timezone.now) #작성 시간
    published_date = models.DateTimeField(blank = True, null= True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title