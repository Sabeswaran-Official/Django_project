from django.db import models

# Create your models here.
class Students_data(models.Model):
    full_name=models.CharField(max_length=50,null=True)
    username=models.CharField(max_length=50,null=True)
    reg_no=models.CharField(max_length=10,null=True)
    course=models.CharField(max_length=20,null=True)
    year_choices=[
        ('1st year','1st year'),
        ('2nd year','2nd year'),
        ('3rd year','3rd year'),
        ('4th year','4th year'),
    ]
    year=models.CharField(max_length=10,choices=year_choices)
    gpa=models.IntegerField(default=0)
    gmail_id=models.CharField(max_length=20,null=True)
    photo=models.ImageField(null=True,upload_to='media/')
    

    # def __str__(self):
    #     return self.id
    def __str__(self):
        return self.username

