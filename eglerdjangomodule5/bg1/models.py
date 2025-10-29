from django.db import models

# Create your models here.
class Character(models.Model):
    char_name = models.CharField(max_length=50)
    char_race = models.CharField(max_length=50)
    char_class = models.CharField(max_length=50)
    char_align = models.CharField(max_length=50)
    char_str = models.IntegerField()
    char_dex = models.IntegerField()
    char_con = models.IntegerField()
    char_wis = models.IntegerField()
    char_int = models.IntegerField()
    char_cha = models.IntegerField()
    char_desc = models.TextField(blank=True)

    def __str__(self):
        return self.char_name
