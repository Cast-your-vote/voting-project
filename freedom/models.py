from datetime import date
from django.db import models

# Create your models here.

class Address(models.Model):
    village = models.CharField(max_length=30)
    parish = models.CharField(max_length=30)
    sub_county = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    region = models.CharField(max_length=30)

    def __str__(self):
        return self.parish

class Political_party(models.Model):
    name = models.CharField(max_length=30)
    emblem = models.ImageField(upload_to='emblem_images/')
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Voter_type(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    
    PRIVELEDGE_CHOICES = [
        ('FP', 'Fingerprint_patterns'),
        ('VC', 'Voice'),
        ('BR', 'Braille_keypad'),
    ]

    priveledges = models.CharField(max_length=2, choices=PRIVELEDGE_CHOICES)

    def __str__(self):
        return self.name

class Audio(models.Model):
    english_text = models.CharField(max_length=50)
    luganda_text = models.CharField(max_length=50)
    kiswahili_text = models.CharField(max_length=50)
    english_audio = models.FileField(upload_to='english_audio/')
    luganda_audio = models.FileField(upload_to='luganda_audio/')
    kiswahili_audio = models.FileField(upload_to='kiswahili_audio/')
    cast_voice = models.FileField(upload_to='cast_audio/')

    def __str__(self):
        return self.english_text

class Polling_station(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    image = models.ImageField(upload_to='candidate_images/')
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    political_party = models.ForeignKey(Political_party, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Voter(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(auto_now_add=True)
    nin_number = models.CharField(max_length=15)
    phone_contact = models.CharField(max_length=10)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    Voter_type = models.ForeignKey(Voter_type, on_delete=models.CASCADE)
    #fingerprint_pattern = models.ForeignKey(Fingerprints, on_delete=models.CASCADE)
    Polling_station = models.ForeignKey(Polling_station, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.first_name
    
class Fingerprints(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    right_thumb = models.BinaryField()
    right_index_finger = models.BinaryField()
    right_middle_finger = models.BinaryField()
    right_ring_finger = models.BinaryField()
    right_pinky_finger = models.BinaryField()
    left_thumb = models.BinaryField()
    left_index_finger = models.BinaryField()
    left_middle_finger = models.BinaryField()
    left_ring_finger = models.BinaryField()
    left_pinky_finger = models.BinaryField()

    def __str__(self):
        return self.right_thumb
    


    
    
    
    
    

   # class Meta:
    #    verbose_name = _("")
    #    verbose_name_plural = _("s")

   # def __str__(self):
   #     return self.name

    #def get_absolute_url(self):
    #    return reverse("_detail", kwargs={"pk": self.pk})
#)
    

