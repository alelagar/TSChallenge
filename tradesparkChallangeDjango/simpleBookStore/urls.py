from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, BookViewSet, RemoveCategoryFromBookView, RemoveCategoryFromBookWithAuthorView, AddCategoryToBookView
#Importe la vista nueva

router = DefaultRouter()

router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('remove-category/<str:book_title>/<str:category_name>/', RemoveCategoryFromBookView.as_view(), name='remove-category'),
    #Endpoint para probar el delete de categorias básico

    path('remove-category/<str:book_title>/<str:author_name>/<str:category_name>/', RemoveCategoryFromBookWithAuthorView.as_view(), name='remove-category-with-author'),
    #Caso de titulo repetido, añadimos autor

    path('add-category/<str:book_title>/<str:author_name>/<str:category_name>/', AddCategoryToBookView.as_view(), name='add-category'),
]


#Curl de testeo: curl -X DELETE http://localhost:8000/bookStore/remove-category/Introduction%20to%20algorithms/Software/

