import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { InfoPage } from '../info/info';

/**
 * Generated class for the BuscarPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-buscar',
  templateUrl: 'buscar.html',
})
export class BuscarPage {
  lista = [];
  ofertas = [];

  infoPage = InfoPage;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.lista = this.navParams.get('ofertas');
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad BuscarPage');
  }

  getItems(ev: any) {
    console.log(ev.target.value);
    let busqueda = ev.target.value.toLowerCase();

    this.ofertas = this.lista.filter(oferta => {
      return oferta.profesor.toLowerCase().includes(busqueda) + oferta.materia.toLowerCase().includes(busqueda) + oferta.nrc.toLowerCase().includes(busqueda) + oferta.clave.toLowerCase().includes(busqueda)
    });
    console.log(JSON.stringify(this.ofertas));
  }

  info(oferta){
    this.navCtrl.push(this.infoPage, {oferta: oferta});
  }

}
