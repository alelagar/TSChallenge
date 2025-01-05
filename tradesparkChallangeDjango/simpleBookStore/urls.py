from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, BookViewSet, RemoveCategoryFromBookView, RemoveCategoryFromBookWithAuthorView, AddCategoryToBookView, AddCategoryToBookIdView, RemoveCategoryFromBookWithIdView
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

    path('remove-category-id/<int:book_id>/<str:category_name>/', RemoveCategoryFromBookWithIdView.as_view(), name='remove-category-with-id'),
    # Remove con id y categoria

    # Adds para volver a cargar despues de testear el remove
    path('add-category/<str:book_title>/<str:author_name>/<str:category_name>/', AddCategoryToBookView.as_view(), name='add-category'),
   
    path('add-category-id/<int:book_id>/<str:category_name>/', AddCategoryToBookIdView.as_view(), name='add-category-id'),
]




