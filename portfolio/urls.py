from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfol import views
from course.views import signin, signout, signup, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("blog/", include("blog.urls")),
    path("signup/", signup, name="signup"),
    path("courses/", CourseListView.as_view(), name="courses"),
    path("course_create/", CourseCreateView.as_view(), name="courses_create"),
    path("course_update/<int:pk>/", CourseUpdateView.as_view(), name="course_update"),
    path("course_delete/<int:pk>/", CourseDeleteView.as_view(), name="course_delete"),
    # path("courses/", course_List, name="courses"),
    # path("course_create/", course_create, name="courses_create"),
    # path("course_update/<int:id>/", course_update, name="course_update"),
    # path("course_delete/<int:id>/", course_delete, name="course_delete"),
    path("logout/", signout, name="logout"),
    path("signin/", signin, name="signin"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
