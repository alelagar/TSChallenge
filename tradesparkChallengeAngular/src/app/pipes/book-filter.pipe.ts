import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'bookFilter'
})
export class BookFilterPipe implements PipeTransform {

  transform(books: any[], searchText: string, filterBy: 'title' | 'author' | 'categories'): any[]{
    if (!books || !searchText || !filterBy) {
      return books;
    }

    searchText = searchText.toLocaleLowerCase();


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