from django.db import models

# Create your models here.
class VoterModel(models.Model):
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    dob=models.DateField()
    address=models.TextField()
    voter_id_number=models.CharField(max_length=20,unique=True)
    photo=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name