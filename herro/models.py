from django.db import models
from herro_project.settings import AUTH_USER_MODEL

class Exercice(models.Model):
    nom = models.CharField(max_length=150)
    
    UNITE_CHOIX = [
        ("kg", "kg"),
        ("km/h", "km/h"),
    ]
    unité = models.CharField(max_length=10,choices=UNITE_CHOIX,default=UNITE_CHOIX[0])
    
    description = models.TextField(blank=True)
    Image = models.ImageField(upload_to="Exercices_img",blank=True,null=True)
    
    def __str__(self):
        return self.nom
    
class Perf(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)
    perf_value = models.FloatField(default=0.0)
    public = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.exercice.nom} ({self.perf_value} {self.exercice.unité})"
    
class All_Perf(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    perfs = models.ManyToManyField(Perf)
    
    def __str__(self):
        return f"{self.user.username} - PERFS"
    




