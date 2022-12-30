from django.db import models
class HRMAN(models.Model):
    name=models.CharField(max_length=20)
    psd=models.CharField(max_length=15)
    hrid=models.IntegerField()
#
class EMP(models.Model):
     name=models.CharField(max_length=20)
     dept=models.CharField(max_length=20)
     empid = models.IntegerField()
     mob = models.IntegerField()
     psd=models.CharField(max_length=15)
     status=models.IntegerField(null=True)

#
# #
# #
# # class PENDING(models.Model):
# #     pl=models.CharField(max_length=30)
# #
# # class APPROVED(models.Model):
# #     al=models.CharField(max_length=20)
# #
# # class DECLINED(models.Model):
# #     dl=models.CharField(max_length=30)
# #
class leavreq(models.Model):
    # empid = models.ForeignKey(EMP,on_delete=models.CASCADE)
    ltype=models.CharField(max_length=30)
    ldays=models.IntegerField()
    lmsg=models.CharField(max_length=30)
    lid=models.IntegerField()




# Create your models here.
