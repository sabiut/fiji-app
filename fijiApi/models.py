from django.db import models


class Confederacy(models.Model):
    confederancy_name = models.CharField(max_length=25)


    def __str__(self):
        return self.confederancy_name


class Provinces(models.Model):
    confederancy = models.ForeignKey(Confederacy, related_name='province', null=True, default='', on_delete=models.CASCADE)
    confederancy_code = models.CharField(max_length=25)
    province_name = models.CharField(max_length=25)

    def __str__(self):
        return self.province_name


class Districts(models.Model):
    confederancy = models.ForeignKey(Confederacy, related_name='district',null=True, default='', on_delete=models.CASCADE)
    province = models.ForeignKey(Provinces,related_name='district', null=True, on_delete=models.CASCADE)
    province_code = models.CharField(max_length=25)
    district_name = models.CharField(max_length=25)

    def __str__(self):
        return self.district_name

class Villages(models.Model):
    confederancy = models.ForeignKey(Confederacy, related_name ='village',null=True, default='', on_delete=models.CASCADE)
    district = models.ForeignKey(Districts, related_name='village', null=True, on_delete=models.CASCADE)
    province = models.ForeignKey(Provinces, related_name='village', null=True, on_delete=models.CASCADE)
    district_code = models.CharField(max_length=25)
    village_name = models.CharField(max_length=25)
    acknowledgement = models.TextField(default='')

    def __str__(self):
        return self.village_name


class contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length= 25)
    email = models.CharField(max_length= 25)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name