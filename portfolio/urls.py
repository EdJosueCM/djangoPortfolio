from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfol import views
from course.views import signin, courses, signout, signup, course_List, course_create, course_update, course_delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("blog/", include("blog.urls")),
    path("signup/", signup, name="signup"),
    path("courses/", course_List, name="courses"),
    path("course_create/", course_create, name="courses_create"),
    path("course_update/<int:id>/", course_update, name="course_update"),
    path("course_delete/<int:id>/", course_delete, name="course_delete"),
    path("logout/", signout, name="logout"),
    path("signin/", signin, name="signin"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
