from django.db import models

# 在这里创建模型 Create your models here. 

class Topic(models):
    """ 用户学习的主题 """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=Ture)

    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.text