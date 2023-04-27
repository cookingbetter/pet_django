"""own URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# from app.views import add_post, add_receipt, index, add_new_element
from app.views import add_post, index, favorites, checkout, purchases, item, subscribe, mysubs
from app.views import CustomLoginView, CustomLogoutView, signup, change_password

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


# вроде бы работает


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('change_password/', change_password, name='change_password'),
    path('', index, name='receipts'),
    path('add_post/', add_post, name='add_post'),
    path('favorites/', favorites, name='favorites'),
    path('checkout/<int:receipt_id>', checkout, name='checkout'),
    path('purchases/', purchases, name='purchases'),
    path('item/<int:receipt_id>', item, name='item'),
    path('subscribe/<int:receipt_id>', subscribe, name='subscribe'),
    path('mysubs/', mysubs, name='mysubs')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns