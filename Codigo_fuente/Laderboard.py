from tkinter import ttk
from tkinter import *
import sqlite3

class Users:

    db_name = 'Resources\\Data_base\\Users.db'

    def run_query(self, query, parameters = ()): #Funcion para consultar base de datos
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def sourceClients(self): #Funcion para buscar los datos
        #Consult and clean data
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        #obtain data
        query = 'SELECT * FROM USUARIOS ORDER BY SCORE ASC' 
        db_rows = self.run_query(query)

        #filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[0], values = (row[1], row[2], row[4], row[5]))

    def validation(self): #Validate
        return len(self.name.get()) != 0 and len(self.lastName.get()) and len(self.CC.get()) != 0 and  len(self.email.get()) != 0

    def addClients(self): #Add clients from app
        if self.validation():
            query = 'INSERT INTO clientes VALUES(?,?,?,?,?,?)'
            parameters = (self.CC.get(), self.name.get(), self.lastName.get(), self.phone.get(), self.cellphone.get(), self.email.get())
            self.run_query(query,parameters)
            self.messagge.config(fg = 'green')
            self.messagge['text'] = 'Cliente {} agregado Satisfactoriamente'.format(self.name.get())
            self.name.delete(0,END)
            self.lastName.delete(0,END)
            self.CC.delete(0,END)
            self.phone.delete(0,END)
            self.cellphone.delete(0,END)
            self.email.delete(0,END)
        else:
            self.messagge['text'] = 'Nombres, apellidos, CC/NIT y el correo son requeridos.'
        self.sourceClients()

    def deleteClient(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.messagge['text'] = 'Por favor seleccione un cliente.'
            return
        self.messagge['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM clientes WHERE nombres = ?'
        self.run_query(query, (name, ))
        self.messagge['text'] = 'Cliente {} eliminado satisfactoriamente.'.format(name)
        self.sourceClients()

    def editClient(self):
        self.messagge['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.messagge['text'] = 'Por favor seleccione un cliente.'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_data = self.tree.item(self.tree.selection())['values']
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar Cliente'

        #Old name
        Label(self.edit_wind, text = 'Nombre Antiguo: ', pady = 10).grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)

        #New name
        Label(self.edit_wind, text = 'Nombre Nuevo: ', pady = 10).grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        #Old last Name
        Label(self.edit_wind, text = 'Apellido Antiguo: ', pady = 10).grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_data[0]), state = 'readonly').grid(row = 2, column = 2)

        #New last name
        Label(self.edit_wind, text = 'Apellido Nuevo: ', pady = 10).grid(row = 3, column = 1)
        new_lastname = Entry(self.edit_wind)
        new_lastname.grid(row = 3, column = 2)

        #Old CC/NIT
        Label(self.edit_wind, text = 'CC/NIT Antiguo: ', pady = 10).grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_data[1]), state = 'readonly').grid(row = 4, column = 2)

        #New CC/NIT
        Label(self.edit_wind, text = 'CC/NIT Nuevo: ', pady = 10).grid(row = 5, column = 1)
        new_CC = Entry(self.edit_wind)
        new_CC.grid(row = 5, column = 2)

        #Old phone
        Label(self.edit_wind, text = 'Teléfono Antiguo: ', pady = 10).grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_data[2]), state = 'readonly').grid(row = 6, column = 2)

        #New phone
        Label(self.edit_wind, text = 'Teléfono Nuevo: ', pady = 10).grid(row = 7, column = 1)
        new_phone = Entry(self.edit_wind)
        new_phone.grid(row = 7, column = 2)

        #Old cellphone
        Label(self.edit_wind, text = 'Celular Antiguo: ', pady = 10).grid(row = 8, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_data[3]), state = 'readonly').grid(row = 8, column = 2)

        #New cellphone
        Label(self.edit_wind, text = 'Celular Nuevo: ', pady = 10).grid(row = 9, column = 1)
        new_cellphone = Entry(self.edit_wind)
        new_cellphone.grid(row = 9, column = 2)

        #Old email
        Label(self.edit_wind, text = 'Correo Antiguo: ', pady = 10).grid(row = 10, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_data[4]), state = 'readonly').grid(row = 10, column = 2)

        #New email
        Label(self.edit_wind, text = 'Correo Nuevo: ', pady = 10).grid(row = 11, column = 1)
        new_email = Entry(self.edit_wind)
        new_email.grid(row = 11, column = 2)

        #Edit button
        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.updateClients(new_name.get(), name, new_lastname.get(), new_phone.get(), new_cellphone.get(), new_email.get(), new_CC.get(), old_data)).grid(row = 12, column = 2, sticky = W)

    def updateClients(self, new_name, name, new_lastname, new_phone, new_cellphone, new_email, new_CC, old_data):
        query = '''
            UPDATE clientes SET cc = ?, 
            nombres = ?, 
            apellidos = ?, 
            telefono = ?, 
            celular = ?, 
            correo = ? WHERE 
            cc = ? 
        '''

        parameters = (
            new_CC, 
            new_name, 
            new_lastname, 
            new_phone, 
            new_cellphone, 
            new_email, 
            old_data[1]
        )
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.messagge['text'] = 'Cliente {} actualizado satisfactoriamente'.format(name)
        self.sourceClients()


        
    def __init__(self, window):
        # Abrir 
        self.wind = window
        self.wind.title('Laderboard')
        self.wind.config(bg = '#000')

        # Table
        self.tree = ttk.Treeview(height = 10)
        self.tree['columns']=('#1', "#2", "#3", "#4")
        self.tree.grid(row = 9, column = 0, columnspan = 2)
        self.tree.column("#0", width=130, minwidth=100)
        self.tree.column("#1", width=130, minwidth=100)
        self.tree.column("#2", width=100, minwidth=100)
        self.tree.column("#3", width=100, minwidth=100)
        self.tree.column("#4", width=100, minwidth=100)
        self.tree.heading('#0', text = 'Nickname', anchor = CENTER)
        self.tree.heading('#1', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#2', text = 'Email', anchor = CENTER)
        self.tree.heading('#3', text = 'Victories', anchor = CENTER)
        self.tree.heading('#4', text = 'Score', anchor = CENTER)

        #Edit and Delete Buttons
        ttk.Button(text = 'EDITAR', command = self.editClient).grid(row = 10, column = 1, sticky = W + E)
        ttk.Button(text = 'BORRAR', command = self.deleteClient).grid(row = 10, column = 0, sticky = W + E)

        self.sourceClients()

if __name__ == '__main__':
    window = Tk()
    application = Users(window)
    window.mainloop()