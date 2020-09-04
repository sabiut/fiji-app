from django.db import models

class Confederacy(models.Model):
    confederancy_name = models.CharField(max_length=25)

    def __str__(self):
        return self.confederancy_name


class Provinces(models.Model):
    confederancy = models.ForeignKey(Confederacy, null=True, default='',on_delete=models.CASCADE)
    confederancy_code = models.CharField(max_length= 25)
    province_name = models.CharField(max_length= 25)

    def __str__(self):
        return self.province_name

class Districts(models.Model):
    province = models.ForeignKey(Provinces, null=True, on_delete=models.CASCADE)
    province_code = models.CharField(max_length=25)
    district_name = models.CharField(max_length= 25)

    def __str__(self):
        return self.district_name

class Villages(models.Model):
    district = models.ForeignKey(Districts, null=True, on_delete=models.CASCADE)
    district_code = models.CharField(max_length=25)
    village_name = models.CharField(max_length=25)
    acknowledgement = models.TextField(default='')

    def __str__(self):
        return self.village_name

