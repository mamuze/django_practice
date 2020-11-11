from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')


#user,body, created_at.. 얘네는 내가 코딩할 때 쓰는 변수! (테이블에 있는 이름들은 장고가 알아서 만들어서 쓴다!)
# >> 여기서 user는 post.user 이다. 
#여기서 User는 가져오고자 하는 것이다

#related_name -> user.liked_posts 
# #하나를 적을 때 반대편에서는 어떻게 사용될지 같이 정의한 것 

    def __str__(self):
        # return f'{self.author} :{self.body}'
        if self.user:
            return f'{self.user.get_username()} : {self.body}'

        return f'{self.body}'

