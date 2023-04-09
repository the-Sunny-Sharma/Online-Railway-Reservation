from django.utils.timezone import now
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    comment=models.TextField()
    date=models.DateField()
    def __str__(self):
            return self.name
        
class BookTicket(models.Model):
      username=models.CharField(max_length=50,default="")
      pnr_number=models.IntegerField(primary_key=True)
      trainNumber=models.CharField(max_length=20)
      pass1name=models.CharField(max_length=100)
      pass1age=models.CharField(max_length=10)
      pass1berth_opt=models.CharField(max_length=100,default='SL')
      pass2name=models.CharField(max_length=100,blank=True, null=True)
      pass2age=models.CharField(max_length=10,blank=True,null=True)
      pass2berth_opt=models.CharField(max_length=100,blank=True,null=True)
      pass3name=models.CharField(max_length=100,blank=True,null=True)
      pass3age=models.CharField(max_length=10,blank=True,null=True)
      pass3berth_opt=models.CharField(max_length=100,blank=True,null=True)
      source=models.CharField(max_length=30,blank=True,null=True)
      destination=models.CharField(max_length=30,blank=True,null=True)
      dateJourney=models.DateField(default=now, editable=True)
      def __str__(self):
            return str(self.pnr_number)

class Register(models.Model):
      fname=models.CharField(max_length=20)
      mname=models.CharField(max_length=20)
      lname=models.CharField(max_length=20)
      mail=models.CharField(max_length=50,unique=True)
      dob=models.DateField()
      phone=models.CharField(max_length=15)
      username=models.CharField(max_length=50,primary_key=True)
      password=models.CharField(max_length=50)
      def __str__(self):
            return self.username

class Chart(models.Model):
      train_no=models.IntegerField()
      train_name=models.CharField(max_length=100)
      train_source=models.CharField(max_length=100)
      train_dest=models.CharField(max_length=100)
      train_departure=models.CharField(max_length=100)
      train_arrival=models.CharField(max_length=100)
      run_d=models.TextField()

      def __str__(self):
            return self.train_name

