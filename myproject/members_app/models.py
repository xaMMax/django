from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.name


class MemberData(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    text = models.TextField(max_length=600, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.member.name}, {self.pub_date}'
