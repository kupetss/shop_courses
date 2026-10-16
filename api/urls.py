from django.urls import path, include
from api.models import CategoryResource, CourseRosource
from tastypie.api import Api

api = Api(api_name='v1')
api.register(CourseRosource())
api.register(CategoryResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
