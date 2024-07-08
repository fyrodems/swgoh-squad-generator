import { Component, OnInit } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  users: any[] = [];
  title = 'app';

  constructor(private userService: UserService) {}

  ngOnInit() {
    this.userService.getUsers().subscribe((data) => {
      this.users = data;
    });
  }

  addUser(name: string, email: string) {
    const newUser = { name, email };
    this.userService.addUser(newUser).subscribe((user) => {
      this.users.push(user);
    });
  }
}
