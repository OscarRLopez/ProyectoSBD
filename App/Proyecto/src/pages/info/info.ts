import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

/**
 * Generated class for the InfoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-info',
  templateUrl: 'info.html',
})
export class InfoPage {
  oferta = {};
  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.oferta =this.navParams.get('oferta');
    console.log(JSON.stringify(this.oferta));
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad InfoPage');
  }

}
