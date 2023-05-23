from django.db import models

# Create your models here.
class Languaje(models.Model):
    OPTIONS=(
        ('Es','Español'),
        ('En','Inglés'),
    )
    language=models.CharField(choices=OPTIONS,max_length=100)
    class Meta:
        abstract = True
    
class TimePeriod(models.Model):
    started=models.DateField()
    # If it's null it's because I'm working on it. (input_formats=['%d/%m/%Y'])
    ended=models.DateField(null=True,blank=True)
    class Meta:
        abstract = True
        verbose_name='Time Period'
        verbose_name_plural = 'Time Period'

class Skills(Languaje):
    title=models.CharField(max_length=100)
    logo=models.FileField(upload_to='skills/logos')
    description=models.CharField(max_length=225,null=True,blank=True)
    is_soft_skill=models.BooleanField(default=False)
    learning=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Skill'
        verbose_name_plural = 'Skills'

class ProjectsImages(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='proyects')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Project Image'
        verbose_name_plural = 'Projects Images'

class Projects(Languaje,TimePeriod):
    title=models.CharField(max_length=100)
    description=models.TextField()
    images = models.ManyToManyField(ProjectsImages,blank=True)
    logo=models.FileField(upload_to='proyects/logos',blank=True,null=True)
    technologies=models.ManyToManyField(Skills,blank=True)
    # Some projects were developed in two differents repos:
    url_back=models.CharField(max_length=225,null=True,blank=True)
    url_front=models.CharField(max_length=225,null=True,blank=True)
    url_deploy=models.CharField(max_length=225,null=True,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Project'
        verbose_name_plural = 'Projects'

class Education(Languaje,TimePeriod):
    degree=models.CharField(max_length=225)
    description=models.TextField()
    image=models.FileField(upload_to='education',null=True,blank=True)
    
    def __str__(self):
        return self.degree

    class Meta:
        verbose_name='Education'
        verbose_name_plural = 'Educations'
        

class JobExperience(Languaje,TimePeriod):
    company=models.CharField(max_length=225)
    logo=models.ImageField(upload_to='companies',blank=True,null=True)
    position=models.CharField(max_length=225)
    description=models.TextField(blank=True,null=True)
    technologies=models.ManyToManyField(Skills)
    def __str__(self):
        return '{}  {}'.format(self.company,self.position)
    class Meta:
        verbose_name='Job Experience'
        verbose_name_plural = 'Job Experiences'
