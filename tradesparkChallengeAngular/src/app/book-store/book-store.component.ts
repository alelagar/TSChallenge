import { Component, OnInit } from '@angular/core';
import { BookStoreService } from '../book-store.service';

@Component({
  selector: 'app-book-store',
  templateUrl: './book-store.component.html',
  styleUrls: ['./book-store.component.css']
})
export class BookStoreComponent implements OnInit {

  books: any[] = [];
  searchText: string = '';  // Variable para el texto de búsqueda
  filterBy: 'title' | 'author' | 'categories';  // Variable para el filtro

  constructor(private bookStoreService: BookStoreService) { }

  ngOnInit(): void {
    this.bookStoreService.getBooks().subscribe((data: any[]) => {
      console.log('Datos recibidos desde el servicio:', data);
      this.books = data; 
    })
  }

  categoriesToString(categories: any[]): string {
    let categoriesString = "";
    categories.forEach((category, index) => {
      categoriesString += category.name;
      if (index < categories.length - 1) {
        categoriesString += ", ";
      }
    });
    return categoriesString;
  }


  removeCategory(book: any, categoryName: string): void {
    this.bookStoreService.removeCategory(book['id'], categoryName).subscribe(
      response => {
        console.log('Category removed:', response);
        // Actualiza la lista local de libros tras la eliminación
        book.categories = book.categories.filter((cat: any) => cat.name !== categoryName);
      },
      error => {
        console.error('Error removing category:', error);
      }
    );
  }

}
