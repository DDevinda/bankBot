import { Component, OnInit } from '@angular/core';
import { ApicallsService } from 'src/services/apicalls.service';

@Component({
  selector: 'app-botui',
  templateUrl: './botui.component.html',
  styleUrls: ['./botui.component.css']
})
export class BotuiComponent implements OnInit {

  constructor(private apiCallsService: ApicallsService) { }

  currentChat;
  userMessageArray = [];
  messagePayload = {
    sender: 'default',
    message: 'hi'
  };

  ngOnInit() {

    // this.apiCallsService.sendMessage(this.messagePayload).subscribe(resp => console.log(resp));
  }

  sendMessage = () => {
    this.messagePayload.message = this.currentChat;
    this.userMessageArray.push(this.currentChat);
    console.log(this.userMessageArray);
    this.apiCallsService.sendMessage(this.messagePayload).subscribe(res => {
      console.log(res[0].text);
      this.userMessageArray.push(res[0].text);
    } );
    this.currentChat = null;
  }

}
