/**
 * Pipe personalizado para filtrar una lista de libros segun un criterio de busqueda.
 * 
 * Este pipe permite realizar busquedas dinámicas en un array de libros con base en el texto ingresado
 * y el tipo de filtro seleccionado (titulo, autor o categorias).
 */
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'bookFilter'  //Nombre que uso en HTML
})
export class BookFilterPipe implements PipeTransform {

    /**
   * Metodo transform que aplica el filtro a la lista de libros.
   * 
   * books - Libros a filtrar.
   * searchText - Texto ingresado por el usuario.
   * filterBy - Criterio de filtro
   * return: lista filtrada de libros que coinciden con el criterio de búsqueda.
   */
  transform(books: any[], searchText: string, filterBy: 'title' | 'author' | 'categories'): any[]{
    if (!books || !searchText || !filterBy) {
      return books;
    }

    searchText = searchText.toLocaleLowerCase();

    // Filtra los libros segun el tipo de filtro seleccionado
    return books.filter(book => {
      console.log('Book Categories:', book.categories);
      if (filterBy === 'title') {
        return book.title?.toLowerCase().includes(searchText);
      } else if (filterBy === 'author') {
        return book.author?.name?.toLowerCase().includes(searchText);
      } else if (filterBy === 'categories') {
        return book.categories?.some((category: any) =>
          category.name.toLowerCase().includes(searchText)
        );
      }
      return false;
    });
  }
}