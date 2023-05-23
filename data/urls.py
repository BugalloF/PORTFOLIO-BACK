from django.urls import path
from .views import EducationListCreateView,SkillsListCreateView,JobExperienceListCreateView,ProjectListCreateView

urlpatterns = [
    path('education/', EducationListCreateView.as_view(), name='education_list'),
    path('skills/', SkillsListCreateView.as_view(), name='skills_list'),
    path('jobexperience/', JobExperienceListCreateView.as_view(), name='jobs_list'),
    path('project/', ProjectListCreateView.as_view(), name='projects_list'),

]
