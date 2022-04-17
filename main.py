import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as font

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = Tk()
root.title(180*" " + "OVER DRIVE - DETAILING")
root.geometry("1300x700")
style = ttk.Style(root)
style.theme_use("classic")


def on_resize(event):
    # resize the background image to the size of label
    image = bgimg.resize((event.width, event.height), Image.Resampling.LANCZOS)
    # update the image of the label
    bk_image.image = ImageTk.PhotoImage(image)
    bk_image.config(image=bk_image.image)


bgimg = Image.open('background.jpg')
bk_image = ttk.Label(root)
bk_image.place(x=0, y=0, relwidth=1, relheight=1)
bk_image.bind('<Configure>', on_resize)


def new_customer():
    global l2new_customer
    global l4new_customer
    global l6new_customer
    global text
    new_customer_window = Toplevel()
    new_customer_window.title("NUEVO CLIENTE")
    new_customer_window.geometry("385x450")
    new_customer_window.config(bg='#FFFAF0')
    bgimg = Image.open('logo2.png')
    bk_image = ttk.Label(new_customer_window)
    bk_image.place(x=0, y=0)
    bk_image.image = ImageTk.PhotoImage(bgimg)
    bk_image.config(image=bk_image.image)
    l1new_customer = ttk.Label(new_customer_window, text="Nombre: ")
    l1new_customer.grid(row=0, column=0, padx=6)
    l2new_customer = ttk.Entry(new_customer_window, width=43)
    l2new_customer.grid(row=0, column=1, pady=3)
    l3new_customer = ttk.Label(new_customer_window, text="Telefono: ")
    l3new_customer.grid(row=1, column=0, padx=6)
    l4new_customer = ttk.Entry(new_customer_window, width=43)
    l4new_customer.grid(row=1, column=1, pady=3)
    l5new_customer = ttk.Label(new_customer_window, text="Email: ")
    l5new_customer.grid(row=2, column=0, padx=6, ipadx=7)
    l6new_customer = ttk.Entry(new_customer_window, width=43)
    l6new_customer.grid(row=2, column=1, pady=3)
    l7new_customer = ttk.Label(new_customer_window, text="Apuntes: ")
    l7new_customer.grid(row=3, column=0, padx=6)
    text = Text(new_customer_window, height=3, width=33)
    text.grid(row=3, column=1, pady=3)
    bt_confirm_new_customer = ttk.Button(new_customer_window, text="Ok", command=id_new_customer)
    bt_confirm_new_customer.grid(row=4, column=1, columnspan=2, sticky="ew")


def id_new_customer():
    new_customer_add_confirm = Toplevel()
    new_customer_add_confirm.title("NUEVO CLIENTE AGREGADO")
    new_customer_add_confirm.geometry("385x450")
    new_customer_add_confirm.config(bg='#FFFAF0')
    global last_add_id
    bgimg = Image.open('logo2.png')
    bk_image = ttk.Label(new_customer_add_confirm)
    bk_image.place(x=0, y=0)
    bk_image.image = ImageTk.PhotoImage(bgimg)
    bk_image.config(image=bk_image.image)
    conn = sqlite3.connect("Customers.db")
    cursor = conn.cursor()
    insert_customer = [l2new_customer.get(), l4new_customer.get(), l6new_customer.get(), text.get("1.0", 'end')]
    cursor.execute("INSERT INTO customer VALUES (?, ?, ?, ?) ", insert_customer)
    last_add_id = cursor.lastrowid
    conn.commit()
    conn.close()
    customer_confirm = ttk.Label(new_customer_add_confirm, text="Cliente añadido con éxito!", font=("Arial", 20))
    customer_confirm.grid(row=0, column=3, pady=6, ipadx=32, sticky='ew')
    l1new_customer_confirm = ttk.Label(new_customer_add_confirm, text="Nombre: " + l2new_customer.get(),
                                       font=("Arial", 16))
    l1new_customer_confirm.grid(row=1, column=3, pady=6, ipadx=32, sticky='ew')
    l2new_customer_confirm = ttk.Label(new_customer_add_confirm, text="Telefono: " + l4new_customer.get(),
                                       font=("Arial", 20))
    l2new_customer_confirm.grid(row=2, column=3, pady=6, ipadx=32, sticky='ew')
    l3new_customer_confirm = ttk.Label(new_customer_add_confirm, text="Email: " + l6new_customer.get(),
                                       font=("Arial", 16))
    l3new_customer_confirm.grid(row=3, column=3, pady=6, ipadx=32, sticky='ew')
    l4new_customer_confirm = ttk.Label(new_customer_add_confirm, text="Apuntes: " + text.get("1.0", 'end'),
                                       font=("Arial", 14))
    l4new_customer_confirm.grid(row=4, column=3, pady=6, ipadx=32, sticky='ew')
    l5new_customer_confirm = ttk.Label(new_customer_add_confirm, text="Codigo del cliente: " + str(last_add_id),
                                       font=("Arial", 20))
    l5new_customer_confirm.grid(row=5, column=3, pady=6, ipadx=32, sticky='ew')
    bt_linking_service = ttk.Button(new_customer_add_confirm, text="ANADIR SERVICIO", command=linking_customer_service)
    bt_linking_service.grid(row=9, column=3, pady=65, ipadx=32, sticky='ew')


def linking_customer_service():
    global services_parameter
    global prices_parameter
    global text_servicio
    customer_service = Toplevel()
    customer_service.title("AGREGANDO SERVICIO")
    customer_service.geometry("385x450")
    customer_service.config(bg='#FFFAF0')
    bgimg = Image.open('logo2.png')
    bk_image = ttk.Label(customer_service)
    bk_image.place(x=0, y=0)
    bk_image.image = ImageTk.PhotoImage(bgimg)
    bk_image.config(image=bk_image.image)
    conn = sqlite3.connect("All_services.db")
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid  FROM all_service")
    records = cursor.fetchall()
    services_names = []
    prices = []
    service_id = []
    for c in range(0, len(records)):
        services_names.append(records[c][0])
        prices.append(records[c][1])
    services_names.append("Otros")
    prices.append("Otros")
    l1new_customer_service = ttk.Label(customer_service, text=l2new_customer.get(), font=("Arial", 16))
    l1new_customer_service.grid(row=1, column=1, pady=6, ipadx=32, sticky='ew')
    l2new_customer_confirm = ttk.Label(customer_service, text=str(last_add_id), font=("Arial", 20))
    l2new_customer_confirm.grid(row=2, column=1, pady=6, ipadx=32, sticky='ew')
    services_parameter = StringVar()
    prices_parameter = StringVar()
    l1services_parameter = ttk.Label(customer_service, text="Servicio")
    l1services_parameter.grid(row=3, column=1, columnspan=2, padx=5, pady=3, ipady=4, sticky="ew")
    drop = ttk.OptionMenu(customer_service, services_parameter, services_names[-1], *services_names)
    drop.grid(row=3, column=2, columnspan=2, padx=5, pady=6, sticky="ew")
    l1prices_parameter = ttk.Label(customer_service, text="Prices")
    l1prices_parameter.grid(row=4, column=1, columnspan=2, padx=5, pady=3, ipady=4, sticky="ew")
    drop = ttk.OptionMenu(customer_service, prices_parameter, prices[-1], *prices)
    drop.grid(row=4, column=2, columnspan=2, padx=5, pady=6, sticky="ew")
    l7new_customer = ttk.Label(customer_service, text="Apuntes: ")
    l7new_customer.grid(row=5, column=1, padx=6)
    text_servicio = Text(customer_service, height=3, width=33)
    text_servicio.grid(row=6, column=2)
    bt_linking_service_customer = ttk.Button(customer_service, text="Agregar", command=linking_customer_service_database)
    bt_linking_service_customer.grid(row=8, column=0, columnspan=2, padx=5, pady=3, ipady=2, ipadx=27, sticky="ew")

    conn.commit()
    conn.close()


def linking_customer_service_database():
    conn = sqlite3.connect("Services.db")
    cursor = conn.cursor()
    insert_customer_service = [l2new_customer.get(), last_add_id, services_parameter.get(),prices_parameter.get(),
                               text_servicio.get("1.0", 'end')]
    cursor.execute("INSERT INTO customer VALUES (?, ?, ?, ?, ?) ", insert_customer_service)
    conn.commit()
    conn.close()
    return


def search_customer():
    global search_parameter
    global l2search_customer
    search_customer_window = Toplevel()
    search_customer_window.title("BUSCADOR DE CLIENTES")
    search_customer_window.geometry("385x450")
    search_customer_window.config(bg='#FFFAF0')
    bgimg = Image.open('logo2.png')
    bk_image = ttk.Label(search_customer_window)
    bk_image.place(x=0, y=0)
    bk_image.image = ImageTk.PhotoImage(bgimg)
    bk_image.config(image=bk_image.image)
    parameter = ['ID', 'NOMBRE', 'EMAIL', 'TELEFONO']
    search_parameter = StringVar()
    l1search_customer = ttk.Label(search_customer_window, text="Parametro de busqueda")
    l1search_customer.grid(row=0, column=1, columnspan=2, padx=5, pady=3, ipady=4, sticky="e")
    drop = ttk.OptionMenu(search_customer_window, search_parameter, parameter[0], *parameter)
    drop.grid(row=0, column=3, columnspan=2, padx=5, pady=3, sticky="ew")
    l2search_customer = ttk.Entry(search_customer_window, width=40)
    l2search_customer.grid(row=2, column=4, pady=3)
    bt_search_customer_parameter = ttk.Button(search_customer_window, text="Buscar", command=search_customer_parameter)
    bt_search_customer_parameter.grid(row=2, column=0, columnspan=2, padx=5, pady=3, ipady=2, ipadx=27, sticky="e")


def search_customer_parameter():
    link_service_window = Toplevel()
    link_service_window.title("AGREGAR SERVICIO")
    link_service_window.geometry("385x450")
    link_service_window.config(bg='#FFFAF0')
    if str(search_parameter.get()) == "ID":
        print("id selecionado")
        #INSERT SEARCH DONE BY ID
    elif str(search_parameter.get()) == "NOMBRE":
        # INSERT SEARCH DONE BY NAME
        print("NOME selecionado")
    elif str(search_parameter.get()) == "EMAIL":
        # INSERT SEARCH DONE BY EMAIL
        print("EMAIL selecionado")
    elif str(search_parameter.get()) == "TELEFONO":
        # INSERT SEARCH DONE BY TELEFONO
        print("TELEFONO selecionado")
    return


def update_customer():
    return


def delete_customer():
    return


def export_customer():
    return


def export_service():
    return


def export_all():
    return


def new_service():
    global l2new_service
    global l4new_service
    new_service_window = Toplevel()
    new_service_window.title("NUEVO CLIENTE")
    new_service_window.geometry("385x450")
    new_service_window.config(bg='#FFFAF0')
    bgimg = Image.open('logo2.png')
    bk_image = ttk.Label(new_service_window)
    bk_image.place(x=0, y=0)
    bk_image.image = ImageTk.PhotoImage(bgimg)
    bk_image.config(image=bk_image.image)
    l1new_service= ttk.Label(new_service_window, text="Servicio: ")
    l1new_service.grid(row=0, column=0, padx=6)
    l2new_service = ttk.Entry(new_service_window, width=43)
    l2new_service.grid(row=0, column=1, pady=3)
    l3new_service = ttk.Label(new_service_window, text="Precio: ")
    l3new_service.grid(row=1, column=0, padx=6)
    l4new_service = ttk.Entry(new_service_window, width=43)
    l4new_service.grid(row=1, column=1, pady=3)
    bt_add_service = ttk.Button(new_service_window, text="Anadir servicio", command=adding_new_service)
    bt_add_service.grid(row=2, column=0, columnspan=2)


def adding_new_service():
    conn = sqlite3.connect("All_services.db")
    cursor = conn.cursor()
    insert_service = [l2new_service.get(), l4new_service.get()]
    cursor.execute("INSERT INTO all_service VALUES (?, ?) ", insert_service)
    conn.commit()
    conn.close()


def update_service():
    return


def all_service():
    conn = sqlite3.connect("All_services.db")
    cursor = conn.cursor()
    show_all_services = Toplevel()
    show_all_services.title("All Services")
    show_all_services.geometry("385x450")
    show_all_services.config(bg='#FFFAF0')
    cursor.execute("SELECT *, oid  FROM all_service")
    records = cursor.fetchall()
    services_names = []
    prices = []
    service_id = []
    for c in range(0, len(records)):
        services_names.append(records[c][0])
        prices.append(records[c][1])
        service_id.append(records[c][2])
    new_dict = dict(zip(services_names, prices))
    c = 2
    for key, value in new_dict.items():
        query_label1 = ttk.Label(show_all_services, text=f"Servicio: {key} | Precio: {value} Euros")
        query_label1.grid(row=c, column=0, columnspan=2, pady=3, sticky="ew")
        c += 1
    conn.commit()
    conn.close()


def delete_service():
    return


def customer():
    insert_window = Toplevel()
    insert_window.title("CLIENTES")
    insert_window.geometry("270x450")
    insert_window.config(bg='#FFFAF0')
    bt_insert_customer = ttk.Button(insert_window, text="Nuevo Cliente", command=new_customer)
    bt_insert_customer.grid(row=1, column=2, columnspan=3, padx=30, pady=15, ipadx=50, ipady=20)

    bt_update_customer = ttk.Button(insert_window, text="Actualizar Cliente", command=update_customer)
    bt_update_customer.grid(row=4, column=2, columnspan=3, padx=30, pady=15, ipadx=40, ipady=20)

    bt_search_customer = ttk.Button(insert_window, text="Buscar Cliente", command=search_customer)
    bt_search_customer.grid(row=7, column=2, columnspan=3, padx=30, pady=15, ipadx=50, ipady=20)

    bt_search_customer = ttk.Button(insert_window, text="Borrar Cliente", command=delete_customer)
    bt_search_customer.grid(row=10, column=2, columnspan=3, padx=30, pady=15, ipadx=50, ipady=20)

    return


def services():
    insert_window_services = Toplevel()
    insert_window_services.title("SERVICIOS")
    insert_window_services.geometry("270x450")
    insert_window_services.config(bg='#FFFAF0')
    bt_new_service = ttk.Button(insert_window_services, text="Anadir Servicio", command=new_service)
    bt_new_service.grid(row=1, column=2, columnspan=3, padx=30, pady=15, ipadx=32, ipady=20)

    bt_update_service = ttk.Button(insert_window_services, text="Actualizar Servicio", command=update_service)
    bt_update_service.grid(row=4, column=2, columnspan=3, padx=30, pady=15, ipadx=25, ipady=20)

    bt_all_service = ttk.Button(insert_window_services, text="Todos Servicios", command=all_service)
    bt_all_service.grid(row=7, column=2, columnspan=3, padx=30, pady=15, ipadx=32, ipady=20)

    bt_search_customer = ttk.Button(insert_window_services, text="Borrar servicio", command=delete_service)
    bt_search_customer.grid(row=10, column=2, columnspan=3, padx=30, pady=15, ipadx=36, ipady=20)
    return


def exports():
    insert_window_export = Toplevel()
    insert_window_export.title("INFORMES")
    insert_window_export.geometry("270x450")
    insert_window_export.config(bg='#FFFAF0')
    bt_export_customer = ttk.Button(insert_window_export, text="Exportar lista de Clientes", command=export_customer)
    bt_export_customer.grid(row=1, column=2, columnspan=3, padx=30, pady=15, ipadx=23, ipady=20)

    bt_export_services = ttk.Button(insert_window_export, text="Exportar lista de Servicios", command=export_service)
    bt_export_services.grid(row=4, column=2, columnspan=3, padx=30, pady=15, ipadx=20, ipady=20)

    bt_export_all = ttk.Button(insert_window_export, text="Informe General", command=export_all)
    bt_export_all.grid(row=7, column=2, columnspan=3, padx=30, pady=15, ipadx=43, ipady=20)
    date_insert = ttk.Label(insert_window_export, text="Data inicial -> ")
    date_insert.grid(row=8, column=2, ipadx=6)
    date_inserte_initial = ttk.Entry(insert_window_export, width=15)
    date_inserte_initial.grid(row=8, column=3)
    date_insert2 = ttk.Label(insert_window_export, text="Data final -> ")
    date_insert2.grid(row=9, column=2, ipadx=10)
    date_inserte_final = ttk.Entry(insert_window_export, width=15)
    date_inserte_final.grid(row=9, column=3)
    return


def agenda():
    insert_window_agenda = Toplevel()
    insert_window_agenda.title("AGENDA")
    insert_window_agenda.geometry("270x450")
    insert_window_agenda.config(bg='#FFFAF0')
    return


def gastos():
    insert_window_gastos = Toplevel()
    insert_window_gastos.title("GASTOS")
    insert_window_gastos.geometry("270x450")
    insert_window_gastos.config(bg='#FFFAF0')
    return


bt_customer = ttk.Button(root, text="Clientes", command=customer)
bt_customer.grid(row=1, column=2, columnspan=3, padx=30, pady=30, ipadx=49, ipady=20)

bt_insert_service = ttk.Button(root, text="Servicios", command=services)
bt_insert_service.grid(row=1, column=5, columnspan=3, padx=30, pady=30, ipadx=50, ipady=20)

bt_exports = ttk.Button(root, text="Informes", command=exports)
bt_exports.grid(row=1, column=8, columnspan=3, padx=30, pady=30, ipadx=50, ipady=20)

bt_agenda = ttk.Button(root, text="Agenda", command=agenda)
bt_agenda.grid(row=1, column=11, columnspan=3, padx=30, pady=30, ipadx=54, ipady=20)

bt_gastos = ttk.Button(root, text="Gastos", command=gastos)
bt_gastos.grid(row=1, column=14, columnspan=3, padx=30, pady=30, ipadx=54, ipady=20)

root.mainloop()
































