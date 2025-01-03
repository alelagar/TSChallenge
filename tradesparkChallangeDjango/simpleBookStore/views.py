from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView #util para el delete
from .models import Author, Category, Book
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Código para el Challenge Django
class RemoveCategoryFromBookView(APIView):
    def delete(self, request, book_title, category_name):
        try:
            # trato de obtener book y category
            #si tengo más de un book con el mismo nombre, informo error, hay que usar el otro método
            books = Book.objects.filter(title=book_title)
            if books.count() > 1:
                return Response({"error": f"Multiple books found with the title '{book_title}'.Please specify the author."}, status=status.HTTP_400_BAD_REQUEST)
            
            book = books.first()
            category = Category.objects.get(name=category_name)
            if category in book.categories.all():
                book.categories.remove(category)
                return Response({"message": f"Category '{category_name}'removed from book '{book_title}'."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": f"Category '{category_name}' is not associated with book '{book_title}'."}, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        

class RemoveCategoryFromBookWithAuthorView(RemoveCategoryFromBookView):
    def delete(self, request, book_title, author_name, category_name):
        try:
            # Busco el autor
            author = Author.objects.get(name=author_name)

            # Busco el libro por título y autor
            book = Book.objects.get(title=book_title, author=author)
            category = Category.objects.get(name=category_name)

            # Eliminar la categoría si está asociada
            if category in book.categories.all():
                book.categories.remove(category)
                return Response({"message": f"Category '{category_name}' removed from book '{book_title}' by {author_name}."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": f"Category '{category_name}' is not associated with book '{book_title}'."}, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response({"error": "Author not found."}, status=status.HTTP_404_NOT_FOUND)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        


#Add solo para poder hacer pruebas con los deletes
class AddCategoryToBookView(APIView):
    def post(self, request, book_title, category_name):
        try:
            # Buscar el libro por el título
            book = Book.objects.get(title=book_title)

            # Buscar la categoría por el nombre
            category = Category.objects.get(name=category_name)

            # Verificar si la categoría ya está asociada al libro
            if category in book.categories.all():
                return Response({"message": f"Category '{category_name}' is already associated with book '{book_title}'."}, status=status.HTTP_200_OK)
            
            # Asociar la categoría al libro
            book.categories.add(category)
            return Response({"message": f"Category '{category_name}' added to book '{book_title}'."}, status=status.HTTP_201_CREATED)

        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)