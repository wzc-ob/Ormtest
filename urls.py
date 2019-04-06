"""ormtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ormtest import view, test, csvtest, classview, listview

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('test/', view.hello),
                  path('ptest/', test.test),
                  path('pptest', test.profile),
                  path('csvtest/', csvtest.csv_view),
                  path('classview/', classview.BookDetailView.as_view(), name='detail'),
                  path('class/', classview.abc),
                  path('listview/', listview.ScoreListView.as_view(), name='list'),
                  path('add/', listview.add),
                  path(r'test2/<score_id>/', listview.edit, name='test'),
                  path('delete/<score_id>/', listview.delete, name='delete'),
                  path('form/', view.IndexView.as_view(), name='form'),
                  path('modelform/', view.ModelView.as_view(), name='modelform'),
                  # path('imagetest/',view.ImageView),
                  path('image/', include('ImageTest.urls',namespace= 'img'))


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
