from rest_framework import serializers
from .models import Education,JobExperience,Projects,Skills,ProjectsImages,Languaje


class ProjectsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectsImages
        fields= '__all__'


class EducationSerializer(serializers.ModelSerializer):
    started=serializers.DateField(format='%d/%m/%Y')
    ended=serializers.DateField(format='%d/%m/%Y')
    class Meta:
        model = Education
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skills
        fields = '__all__'

class JobExperienceSerializer(serializers.ModelSerializer):
    started=serializers.DateField(format='%d/%m/%Y')
    ended=serializers.DateField(format='%d/%m/%Y')
    technologies=SkillSerializer(many=True)
    class Meta:
        model = JobExperience
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    started=serializers.DateField(format='%d/%m/%Y')
    ended=serializers.DateField(format='%d/%m/%Y')
    technologies=SkillSerializer(many=True)
    images=ProjectsImagesSerializer(many=True)
    class Meta:
        model = Projects
        fields = '__all__'