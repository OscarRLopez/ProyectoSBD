import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';
import { InfoPage } from '../info/info';
import { BuscarPage } from '../buscar/buscar';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  ofertas = [];
  infoPage = InfoPage;
  buscarPage = BuscarPage;

  constructor(public navCtrl: NavController, public http: HttpClient) {
    this.http.get('v1/api/v1/agenda')
    .subscribe( data => {
      //console.log(JSON.stringify(data));
      this.ofertas = data['0'];
      console.log(JSON.stringify(this.ofertas));
    }, error => {
      console.log(JSON.stringify(error));
    });
  }

  info (oferta){
    console.log('click');
    this.navCtrl.push(this.infoPage, {oferta: oferta});
  }

  search(){
    console.log('search');
    this.navCtrl.push(this.buscarPage, {ofertas: this.ofertas});
  }

}
