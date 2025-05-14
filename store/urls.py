from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view()), 
    path('products/<int:pk>/', views.ProductDetails.as_view()),
    path('collection/', views.collection_list), 
    path('collection/<int:pk>/', views.collection_detail)
]
# model (data) that is written in python. 
# serializer converts the data into python dictionaries  ex. name , surname, etc.. dict = {"name": rijan}
# JSONrender.render(dict) converts into JSON data.
# django for backend and react for frontend. django --> python , react --> js . JSON connects differnt languages.
# python dict can be converted into JSON as well as js code also can be converted into JSON. 
