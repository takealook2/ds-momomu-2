from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "board/", blank=True, null=True)
    #오류나면 "board/"이부분 수정해보기 ->boardapp/으로??

    def __str__(self):
        return self.title #제목으로 보이게
    
    def summary(self):
        return self.body[:100]

#댓글 관련 모델
class Comment(models.Model):
    post = models.ForeignKey(Board, related_name='comments', on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20) 
    comment_text=models.TextField() 
    created_at=models.DateTimeField(default=timezone.now) #장고에서 기본으로 제공됨 
    # 들어갈 내용들 : 댓글 작성자, 댓글 내용, 댓글 작성 시간

    def approve(self):
        self.save()

    def __str__(self): 
        return self.comment_text