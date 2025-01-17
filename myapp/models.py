from django.db import models

# Create your models here.
STATE_CHOICE = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat')
)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE ,max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileimg',blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)
