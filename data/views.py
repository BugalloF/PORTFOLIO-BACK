from rest_framework import generics
from .models import Education,JobExperience,Projects,Skills
from .serializers import EducationSerializer,SkillSerializer,JobExperienceSerializer,ProjectSerializer
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError


class EducationListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        language = self.request.query_params.get('lan','Es')
        if language is None:
            raise ValidationError('lan query required')
        language = language.capitalize()
        accepted_lan = ['Es','En']
        if language not in accepted_lan:
            raise ValueError('Language not supported.')
        queryset = Education.objects.filter(language=language)
        return queryset

    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_queryset = EducationSerializer(queryset, many=True)
        return JsonResponse(serialized_queryset.data, safe=False)

class SkillsListCreateView(generics.ListCreateAPIView):
    def get_queryset(self): 
        language = self.request.query_params.get('lan','Es')
        if language is None:
            raise ValidationError('lan query required')
        language = language.capitalize()
        accepted_lan = ['Es','En']
        if language not in accepted_lan:
            raise ValueError('Language not supported.')
        queryset = Skills.objects.filter(language=language)
        return queryset

    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_queryset = SkillSerializer(queryset, many=True)
        return JsonResponse(serialized_queryset.data, safe=False)

class JobExperienceListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        language = self.request.query_params.get('lan','Es')
        if language is None:
            raise ValidationError('lan query required')
        language = language.capitalize()
        accepted_lan = ['Es','En']
        if language not in accepted_lan:
            raise ValueError('Language not supported.')
        queryset = JobExperience.objects.filter(language=language)
        return queryset

    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_queryset = JobExperienceSerializer(queryset, many=True)
        return JsonResponse(serialized_queryset.data, safe=False)

class ProjectListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        language = self.request.query_params.get('lan','Es')
        if language is None:
            raise ValidationError('lan query required')
        language = language.capitalize()
        accepted_lan = ['Es','En']
        if language not in accepted_lan:
            raise ValueError('Language not supported.')
        queryset = Projects.objects.filter(language=language)
        return queryset

    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_queryset = ProjectSerializer(queryset, many=True)
        return JsonResponse(serialized_queryset.data, safe=False)

