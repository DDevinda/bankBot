import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BotuiComponent } from './pages/botui/botui.component';

const routes: Routes = [
  { path: 'bot', component: BotuiComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
