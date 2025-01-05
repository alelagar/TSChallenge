Decisiones y Aclaraciones

Para el Challenge de Angular:

Opté por añadir una barra de búsqueda con un dropdown a continuación, que contuviera los 3 datos por los cuales podemos filtrar. En filtrado se realiza comparando la cadena de caracteres ingresada por el usuario con el título, autor o categoría, si la cadena se encuentra en alguna parte, la fila de la tabla se seguirá mostrando, es decir, escribir ‘Intro’ eliminará los dos libros de Algorithmic Trading, pero escribir ‘Algorithm’ no elimina nada ya que los tres tienen esa cadena en alguna parte del título. Tampoco hay distinciones entre mayúsculas y minúsculas.

En primera instancia el filtro viene por defecto en Title, ya que es el primer dato que se ve cuando se mira la tabla.

Para el Challenge de Django:

La solicitud es, dado un nombre y una categoría implementar un remove de la categoría.  
El remove está implementado y es accesible, ahora, se da el caso de que existe más de un libro con el mismo nombre, pero diferente autor. Para esto decidí implementar diferentes métodos remove que me permitan discernir.   
En primera instancia implemente otro, pero que ahora también solicite autor, el método es funcional y está probado.  
Por último, implemente un método que elimina la categoría en base al id del libro y la categoría, este me parece el más óptimo ya que id es un dato que no se presta a confusiones, es único.

Otro problema que surgió fue que en la DB, en la tabla de categorías, la categoría Technology estaba repetida, entonces en algunas consultas, cuando trataba de trabajar con esa categoría retornaba múltiples objetos, impidiendo removerla o añadirla como categoría de un libro.  
La opción que tomé fue dejar un único Technology en la tabla Category de la DB y con eso se solucionaron los problemas.

También añadí métodos add-category, pero que fueron usados solo para volver a añadir las categorías eliminadas al momento de testear. En el archivo tests.py quedan los comandos que use para testear junto con las consultas que use para revisar la tabla conflictiva de la DB.

Para el Challenge opcional:

Añadí botones con el símbolo X a continuación de la columna de categorías, al presionar la X la categoría es eliminada utilizando el método remove que elimina por id y categoría, ya que me parecía más eficiente que el de Title-Author-Category e identifica unívocamente el dato a remover a diferencia del Title-Category.  
Contemple la opción de crear un botón que despliegue las categorías junto con su x, similar a lo que se hace con los filtros, llegue a implementarlo, pero por cuestiones estéticas preferí la opción que quedó en la entrega.

