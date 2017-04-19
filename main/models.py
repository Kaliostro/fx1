from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title;
		
class Trade(models.Model):
#	class Meta:
#		db_table='trade'
	trade_currency = models.CharField(max_length=10)
	trade_date_signal = models.DateTimeField()
	trade_trend = models.CharField(max_length=6)
	trade_price_open = models.FloatField()
	trade_sl = models.FloatField()
	trade_tp = models.FloatField()
	trade_price_close = models.FloatField()
	trade_date_close = models.DateTimeField()
	trade_result = models.IntegerField()