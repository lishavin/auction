from django.db import models
from django.core.validators import RegexValidator #전화번호 유효성 검사

class item(models.Model):
    phoneNumberRegex = RegexValidator(regex = r'^([0-9]{3})-?([0-9]{3})-?([0-9]{4})$') #000-000-0000 형태로
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 10, null=True) #unique=True 할 필요? 
    name = models.CharField(max_length=20) 
    email = models.EmailField(max_length=70)
    min_bid = models.IntegerField(blank=True, null=True) #입찰시작가
    info = models.CharField(max_length=200, blank=True) #글자수 제한할건지?
    create_time = models.DateTimeField(auto_now_add=True) #타이머 기능 때문에 일단 만들어놓음
    image = models.ImageField(upload_to='', blank=True, null=True) #static 파일 만들기


    def __str__(self):
        return self.name

