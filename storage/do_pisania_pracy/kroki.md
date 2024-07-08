# Tworzenie aplikacji: Angular, .NET, PostgreSQL

## Krok 1: Zainstalowanie narzędzi

1. **Node.js i npm**:
   - Pobierz i zainstaluj Node.js z [oficjalnej strony](https://nodejs.org/). npm (Node Package Manager) zostanie zainstalowany razem z Node.js.

2. **Angular CLI**:
   - Otwórz terminal lub wiersz poleceń i zainstaluj Angular CLI globalnie:
     ```bash
     npm install -g @angular/cli
     ```

3. **.NET SDK**:
   - Pobierz i zainstaluj .NET SDK z [oficjalnej strony](https://dotnet.microsoft.com/download).

4. **PostgreSQL**:
   - Pobierz i zainstaluj PostgreSQL z [oficjalnej strony](https://www.postgresql.org/download/).
   (port: 5432, haslo: 2710)

## Krok 2: Tworzenie aplikacji w Angularze

1. **Tworzenie nowej aplikacji Angular**:
   - W terminalu uruchom:
     ```bash
     ng new my-angular-app
     cd my-angular-app
     ```

2. **Uruchomienie serwera deweloperskiego**:
   - W terminalu, będąc w katalogu projektu, uruchom:
     ```bash
     ng serve
     ```
   - Aplikacja powinna być dostępna pod adresem `http://localhost:4200`.

## Krok 3: Tworzenie aplikacji w .NET

1. **Tworzenie nowej aplikacji .NET Web API**:
   - Otwórz terminal i uruchom:
     ```bash
     dotnet new webapi -o MyApi
     cd MyApi
     ```

2. **Uruchomienie serwera deweloperskiego**:
   - W terminalu, będąc w katalogu projektu, uruchom:
     ```bash
     dotnet run
     ```
   - API powinno być dostępne pod adresem `https://localhost:5001`.

## Krok 4: Konfiguracja PostgreSQL

1. **Utworzenie bazy danych**:
   - Otwórz psql (konsola PostgreSQL) i utwórz nową bazę danych:
     ```sql
     CREATE DATABASE my_database;
     ```

2. **Utworzenie tabeli**:
   - W terminalu psql, wybierz nowo utworzoną bazę danych i utwórz przykładową tabelę:
     ```sql
     \c my_database
     CREATE TABLE Users (
         Id SERIAL PRIMARY KEY,
         Name VARCHAR(100),
         Email VARCHAR(100)
     );
     ```

## Krok 5: Połączenie .NET z PostgreSQL

1. **Dodanie pakietów NuGet**:
   - W katalogu projektu .NET, uruchom:
     ```bash
     dotnet add package Npgsql.EntityFrameworkCore.PostgreSQL
     dotnet add package Microsoft.EntityFrameworkCore.Design
     ```

2. **Konfiguracja bazy danych w `appsettings.json`**:
   - Dodaj ustawienia połączenia do PostgreSQL w pliku `appsettings.json`:
     ```json
     "ConnectionStrings": {
         "DefaultConnection": "Host=localhost;Database=my_database;Username=your_username;Password=your_password"
     }
     ```

3. **Konfiguracja kontekstu bazy danych**:
   - Utwórz klasę `ApplicationDbContext` w katalogu `Data`:
     ```csharp
     using Microsoft.EntityFrameworkCore;

     public class ApplicationDbContext : DbContext
     {
         public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
             : base(options)
         {
         }

         public DbSet<User> Users { get; set; }
     }

     public class User
     {
         public int Id { get; set; }
         public string Name { get; set; }
         public string Email { get; set; }
     }
     ```

4. **Rejestracja kontekstu w `Startup.cs`**:
   - Dodaj w metodzie `ConfigureServices`:
     ```csharp
     services.AddDbContext<ApplicationDbContext>(options =>
         options.UseNpgsql(Configuration.GetConnectionString("DefaultConnection")));
     ```

## Krok 6: Połączenie Angular z .NET API

1. **Serwis Angular do komunikacji z API**:
   - Utwórz serwis w Angularze:
     ```bash
     ng generate service user
     ```
   - W pliku `user.service.ts`, dodaj:
     ```typescript
     import { Injectable } from '@angular/core';
     import { HttpClient } from '@angular/common/http';
     import { Observable } from 'rxjs';

     @Injectable({
       providedIn: 'root'
     })
     export class UserService {

       private apiUrl = 'https://localhost:5001/api/users';

       constructor(private http: HttpClient) { }

       getUsers(): Observable<any> {
         return this.http.get(this.apiUrl);
       }

       addUser(user: any): Observable<any> {
         return this.http.post(this.apiUrl, user);
       }
     }
     ```

2. **Korzystanie z serwisu w komponencie Angular**:
   - W komponencie, na przykład `app.component.ts`, dodaj:
     ```typescript
     import { Component, OnInit } from '@angular/core';
     import { UserService } from './user.service';

     @Component({
       selector: 'app-root',
       templateUrl: './app.component.html',
       styleUrls: ['./app.component.css']
     })
     export class AppComponent implements OnInit {

       users: any[] = [];

       constructor(private userService: UserService) { }

       ngOnInit() {
         this.userService.getUsers().subscribe(data => {
           this.users = data;
         });
       }

       addUser(name: string, email: string) {
         const newUser = { name, email };
         this.userService.addUser(newUser).subscribe(user => {
           this.users.push(user);
         });
       }
     }
     ```

To jest podstawowy szkielet aplikacji. Dalsze kroki będą obejmować:
- Rozszerzenie modelu danych.
- Walidacja formularzy w Angularze.
- Obsługa autoryzacji i uwierzytelniania.
- Pisanie testów jednostkowych.

Jeśli potrzebujesz więcej szczegółów na temat konkretnych kroków, chętnie pomogę!
