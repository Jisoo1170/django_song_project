from django.db import models

class store(models.Model):
    TYPE1 = (
        ('1', '멜론'),
        ('2', '벅스'),
        ('3', '지니')
    )
    name = models.CharField(max_length=100)
    delay = models.IntegerField()
    site = models.CharField(max_length=1 ,choices=TYPE1)
    def __str__(self):
        return self.name

class song(models.Model):
    store = models.ForeignKey(store)
    order_time = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)
    message = models.CharField(max_length=200, null=True)
    played = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title