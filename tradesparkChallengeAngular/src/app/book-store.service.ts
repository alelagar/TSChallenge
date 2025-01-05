import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookStoreService {

  constructor(private client: HttpClient) { }

  getBooks() {
    return this.client.get('http://localhost:8000/bookStore/books/')
  }

  //URL de remove con id y categoria
  removeCategory(bookId: string, categoryName: string): Observable<any> {
    const url = `http://localhost:8000/bookStore/remove-category-id/${encodeURIComponent(bookId)}/${encodeURIComponent(categoryName)}/`;
    return this.client.delete(url);
  }

}
