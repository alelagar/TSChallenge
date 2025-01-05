from django.test import TestCase

# Create your tests here.


# Problemas con technology:
#    Tanto para eliminar como para agregar esta categoria tenia dificultades
#    comprobe en db y resulto estar repetida, por eso en varias consultas
#    me retornaba multiple object
#
#    Consultas:
#       docker exec -it tradesparkchallange-django-1 bash
#
#       python manage.py shell
#       from simpleBookStore.models import Category
#       Category.objects.all()
#
#       Me retorno:
#       <QuerySet [<Category: Technology>, <Category: Technology>, <Category: Software>, <Category: Algorithms>]>
#
#       La opción que tomé fue la de dejar solo un Technology.
#       >>> category_to_delete = Category.objects.get(id=1)
#       >>> category_to_delete.delete()


#Comandos para Testing de BackEnd

#Curl que Elimina con nombre y categoria: 
#       curl -X DELETE http://localhost:8000/bookStore/remove-category/Introduction%20to%20algorithms/Software/
#   Para eliminar categorias de Algorithmic Trading necesito mas info, ya que hay 2 nombres iguales
#   Puedo usar id como abajo, o hay una tercera opcion con Title, Author y Category
#   curl -X DELETE http://localhost:8000/bookStore/remove-category/Algorithmic%20Trading/TradeSparkSrl/Software/

#Curl que elimina con id
#       curl -X DELETE http://localhost:8000/bookStore/remove-category-id/1/Technology/
#       Otras categorias: Software, Algorithms
#       Ids: 1, 2 y 3.

#Curl que Añade categoria con id 
#       curl -X POST http://localhost:8000/bookStore/add-category-id/1/Technology/
#       Otras categorias: Software, Algorithms
#       Ids: 1, 2 y 3.