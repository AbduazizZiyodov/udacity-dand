import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { FooterComponent } from './components/footer/footer.component';
import { CoreComponent } from './components/core/core.component';

import { HttpClientModule } from '@angular/common/http';

import { ChartsModule } from 'ng2-charts';
import { AngularImageViewerModule } from 'angular-x-image-viewer';

@NgModule({
  declarations: [AppComponent, HeaderComponent, FooterComponent, CoreComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MDBBootstrapModule.forRoot(),
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    ChartsModule,
    AngularImageViewerModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
