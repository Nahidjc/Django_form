from django.db import models

class Musician(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name+" "+self.last_name
class Album(models.Model):
    Artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    relase_date = models.DateField()
    rating = (
    (1,"worst"),
    (2,"bad"),
    (3,"Good"),
    (4,"Excelent"),
    )
    num_stars = models.IntegerField(choices=rating)
    class Meta:
        db_table = "Album"
