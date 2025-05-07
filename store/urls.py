from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list), 
    path('products/<int:id>/', views.product_details)
]
# model (data) that is written in python. 
# serializer converts the data into python dictionaries  ex. name , surname, etc.. dict = {"name": rijan}
# JSONrender.render(dict) converts into JSON data.
# django for backend and react for frontend. django --> python , react --> js . JSON connects differnt languages.
# python dict can be converted into JSON as well as js code also can be converted into JSON. 
