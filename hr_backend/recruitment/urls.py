from django.urls import path
from .views import JobPostListCreateView, ApplicationListCreateView, JobPostDetailView, ApplicationDetailView

urlpatterns = [
    path('job-posts/', JobPostListCreateView.as_view(), name='job-post-list-create'),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('job-posts/<int:pk>/', JobPostDetailView.as_view(), name='job-post-detail'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
]
