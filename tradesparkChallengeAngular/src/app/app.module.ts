import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BookStoreComponent } from './book-store/book-store.component';
import { MainPageComponent } from './main-page/main-page.component';
import { BookFilterPipe } from './pipes/book-filter.pipe';



@NgModule({
  declarations: [
    AppComponent,
    BookStoreComponent,
    MainPageComponent,
    BookFilterPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
