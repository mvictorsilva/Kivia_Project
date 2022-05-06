from verification_email import SendEmail
###Import DataBase
import mysql.connector


class DataBase(SendEmail):
    def connect_db(self):
        self.connect = mysql.connector.connect(
            host = 'localhost',
            database = 'projeto_kivia_testes',
            user = 'root'
        )
        self.cursor = self.connect.cursor()

    def disconnect_db(self):
        self.connect.close()

    def variables_cadastre(self):
        self.name = self.nameEntry.text()
        self.surname = self.surnameEntry.text()
        self.email = self.emailEntry.text()
        self.password = self.passwordEntry.text()

    def variables_login(self):
        self.email_login = self.emailEntry_login.text()
        self.password_login = self.passwordEntry_login_frame.text()

    def clear_entrys_cadastre(self):
        self.nameEntry.clear()
        self.surnameEntry.clear()
        self.emailEntry.clear()
        self.passwordEntry.clear()

    def clear_entrys_login(self):
        self.emailEntry_login.clear()
        self.passwordEntry_login_frame.clear()

    def create_user(self):
        self.connect_db()
        self.variables_cadastre()

        if self.name == '':
            print('escreva alguma coisa')

        elif self.surname == '':
            print('escreva alguma coisa')

        elif self.email == '':
            print('escreva alguma coisa')

        elif self.password == '':
            print('escreva alguma coisa')

        else:

            self.cursor.execute("""
                insert into clientes(nome_cliente, sobrenome_cliente, email, senha)
                values(%s, %s, %s, %s)
            """,
            (
                self.name,
                self.surname,
                self.email,
                self.password
            ))

            self.send_mail()
            self.clear_entrys_cadastre()
            self.connect.commit()
        self.disconnect_db()

    def confirmation_user(self):
        self.connect_db()
        self.variables_login()

        if self.email_login == '':
            print('user and password incorrect')
            self.clear_entrys_login()
        elif self.password_login == '':
            print('user and password incorrect')
            self.clear_entrys_login()
        else:
        
            self.cursor.execute(f"""
                select senha from clientes where email = '{self.email_login}'
            """)
            self.passaword_db = self.cursor.fetchall()

            if self.password_login == self.passaword_db[0][0]:
                print('cadastro')
            else:
                print('no user')

            self.clear_entrys_login()
            self.connect.commit()
        self.disconnect_db()
