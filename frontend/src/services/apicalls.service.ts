import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { HttpHeaders } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApicallsService {

  baseUrl = ' http://localhost:5005/webhooks/rest/webhook';
  // http: any;
  // headers: any;
  // options: any;

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };

  constructor( private httpClient: HttpClient) { }

  sendMessage = messsagePayload => {
    return this.httpClient.post(this.baseUrl, messsagePayload, this.httpOptions).pipe(map((res) => res));
  }


}
