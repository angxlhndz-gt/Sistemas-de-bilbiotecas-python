import os
import time
from colorama import Fore, Style
import datetime

lista1 = "0123456789ABCDEFGHIJKLM,"
lista2 = "$*+.~^@>-&NOPQRSTUVWXYZ/"
def cambio_color(texto):
    cx = f"{Style.BRIGHT}{Fore.GREEN}{texto}{Style.RESET_ALL}"
    return cx
def cambio_color_center(texto):
    cs = f"{Style.BRIGHT}{Fore.GREEN}{texto.center(80)}{Style.RESET_ALL}"
    return cs
def cambio_color_center_rojo(texto):
    cf = f"{Style.BRIGHT}{Fore.RED}{texto.center(80)}{Style.RESET_ALL}"
    return cf
def encriptar(texto, lista1, lista2):
    texto_encriptado = ""
    for Letra in texto:
        if lista1.find(Letra) != -1:
            pos = lista1.find(Letra)
            texto_encriptado += lista2[pos]
        else:        
            pos = lista2.find(Letra)
            texto_encriptado += lista1[pos]
    return texto_encriptado
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(cambio_color_center("********* Bienvenido biblioteca UMES ***********\n"))
    print("Por favor seleccione una opción: \n")
    print(cambio_color("1.") + " Ingresar en Modo administrador")
    print(cambio_color("2.") + " Ingresar modo Bibliotecario")
    print(cambio_color("3.") + " Salir\n")
    opcion_menu = input("Ingresar opción: ")
    if opcion_menu == "1": 
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(cambio_color_center("********* Bienvenido Administrador ***********\n"))
            print("Por favor ingresar los siguientes datos:\n ")
            user_admin = input("Ingresar Usuario: ").upper()
            pass_admin = input("Ingresar su contraseña: ").upper()
            user_admin_encript = encriptar(user_admin, lista1, lista2)
            pass_admin_encript = encriptar(pass_admin, lista1, lista2)
            archivo = open('administrador.key','r')
            administrador = archivo.readlines()
            archivo.close()
            encontrar = False
            for x in administrador:
                if x.strip() == user_admin_encript + "," + pass_admin_encript:
                    encontrar = True
            if encontrar == True:        
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cambio_color_center("Acceso Válido!!"))
                time.sleep(2)
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cambio_color_center_rojo("Acceso Denegado!!"))
                time.sleep(2)

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(cambio_color_center("********* Bienvenido de nuevo Administrador ***********\n"))
            print("Por favor seleccione una opción: \n")
            print(cambio_color("1.") + " Gestion de Usuarios")
            print(cambio_color("2.") + " Gestion de Libros")
            print(cambio_color("3.") + " Salir\n")
            opcion = input("Ingresar opción: ")
            if opcion == "1":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center("********* Bienvenido Administrador ***********\n"))
                    print(cambio_color("**Gestion de usuarios**\n"))
                    print(cambio_color("1.") + " Agregar usuario")
                    print(cambio_color("2.") + " Cambiar usuario")
                    print(cambio_color("3.") + " Eliminar usuario")
                    print(cambio_color("4.") + " Ver todos los usuarios")
                    print(cambio_color("5.") + " Salir\n")
                    opcion1 = input("Ingresar una opcion: ")
                    if opcion1 == "1":
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(cambio_color_center(("****Gestion de usuarios****\n")))
                            print(cambio_color("1.") + " Agregar Administradores")
                            print(cambio_color("2.") + " Agregar Bibliotecarios") 
                            print(cambio_color("3.") + " Salir\n") 
                            opcion2 = input("Ingresar una opcion: ")
                            if opcion2 == "1":
                                os.system('cls' if os.name == 'nt' else 'clear')
                                while True:
                                    user_new = input("Ingresar usuario: ").upper()
                                    pass_new = input("Ingresar contraseña: ").upper()
                                    user_new = encriptar(user_new, lista1, lista2)
                                    pass_new = encriptar(pass_new, lista1, lista2)
                                    archivo = open('administrador.key','a')
                                    archivo.write(user_new+","+pass_new+"\n")
                                    archivo.close()
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color("Usuario Agregado con Éxito!!"))
                                    time.sleep(1)
                                    break
                            elif opcion2 == "2":
                                os.system('cls' if os.name == 'nt' else 'clear')
                                while True:
                                    user_new = input("Ingresar usuario: ").upper()
                                    pass_new = input("Ingresar contraseña: ").upper()
                                    user_new = encriptar(user_new, lista1, lista2)
                                    pass_new = encriptar(pass_new, lista1, lista2)
                                    archivo = open('bibliotecarios.key','a')
                                    archivo.write(user_new+","+pass_new+"\n")
                                    archivo.close()
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color("Usuario Agregado con Éxito!!"))
                                    time.sleep(1)
                                    break
                            elif opcion2 == "3":
                                break
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center_rojo("Elegir una opcion válida"))
                                time.sleep(2)
                    elif opcion1 == "2":
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(cambio_color_center("****Gestion de usuarios****\n"))
                            print(cambio_color ("1.") + " Cambiar algun usuario de Administrador")
                            print(cambio_color ("2.") + " Cambiar algun usuario de Bibliotecarios") 
                            print(cambio_color ("3.") + " Salir\n") 
                            opcion2 = input("Ingresar una opcion: ")
                            if opcion2 == "1":
                                while True:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center(cambio_color_center("****Gestion de usuarios****\n")))
                                    user_admin = input("Ingresar Usuario: ").upper()
                                    pass_admin = input("Ingresar su contraseña: ").upper()
                                    user_admin_encript = encriptar(user_admin, lista1, lista2)
                                    pass_admin_encript = encriptar(pass_admin, lista1, lista2)
                                    
                                    archivo = open('administrador.key','r')
                                    administrador = archivo.readlines()
                                    archivo.close()
                                    encontrar = False
                                    for x in administrador:
                                        if x.strip() == user_admin_encript + "," + pass_admin_encript:
                                            encontrar = True
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print("\n")
                                            print(cambio_color_center("Usuario y contraseña validada!!"))
                                            time.sleep(2)
                                            break
                                    if encontrar == True:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        user_new = input("Ingresar nuevo usuario: ").upper()
                                        pass_new = input("Ingresar nueva contraseña: ").upper()
                                        usernew = encriptar(user_new, lista1, lista2)
                                        passnew = encriptar(pass_new, lista1, lista2)
                                        archivo = open("administrador.key", "r")
                                        usuarios = archivo.readlines()
                                        archivo.close()
                                        archivo = open("administrador.key", "w")
                                        for x in usuarios:
                                            if x.strip()!= user_admin_encript + "," + pass_admin_encript:
                                                archivo.write(x)
                                        archivo.write(usernew + "," + passnew + "\n")
                                        archivo.close()
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(cambio_color("Usuario cambiado exitosamente!!"))
                                        time.sleep(2)
                                        break
                            elif opcion2 == "2":
                                while True: 
                                    os.system('cls' if os.name == 'nt' else 'clear')  
                                    print (cambio_color_center("****Gestion de usuarios****\n"))
                                    user_bi = input("Ingrese Usuario: ").upper()
                                    pass_bi = input("Ingrese Contraseña: ").upper()
                                    user_bi = encriptar(user_bi, lista1, lista2)
                                    pass_bi = encriptar(pass_bi, lista1, lista2)
                                    archivo = open('bibliotecarios.key', 'r')
                                    bibliotecario = archivo.readlines()
                                    archivo.close()
                                    encontra = False
                                    for x in bibliotecario: 
                                        if x.strip()!= user_bi + "," + pass_bi:
                                            encontrar  = True
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print("\n")
                                            print(cambio_color("Usuario y contraseña validado exitosamente!!"))
                                            time.sleep(2)
                                            break
                                    if encontrar == True:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        user_new = input("Ingrese nuevo usuario: ").upper()
                                        pass_new = input("Ingresar nueva contraseña: "). upper()
                                        usernew = encriptar(user_new, lista1, lista2 )
                                        passnew = encriptar(pass_new, lista1, lista2 )
                                        archivo = open("bibliotecario.key", "r")
                                        usuarios = archivo.readlines()
                                        archivo.close()
                                        archivo = open("bibliotecario.key", "w")
                                        for x in usuarios:
                                            if x.strip()!= user_bi + "," + pass_bi:
                                                    archivo.write(x)
                                        archivo.write(usernew + "," + passnew + "\n")
                                        archivo.close()
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(cambio_color("Usuario cambiado exitosamente!!"))
                                        time.sleep(2)
                                        break
                            elif opcion2 == "3":
                                break
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center_rojo("Ingresar una opción válida!"))  
                                time.sleep(2)   
                    elif opcion1 == "3":                                                    
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(cambio_color_center("****Gestion de usuarios****\n"))
                            print(cambio_color("1.")+ " Eliminar algun usuario de Administrador")
                            print(cambio_color("2.")+ " Eliminar algun usuario de Bibliotecarios") 
                            print(cambio_color("3.")+ " Salir\n") 
                            opcion2 = input("Ingresar una opcion: ")
                            if opcion2 == "1":
                               while True:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center("**** Gestion de usuarios ****\n"))
                                    user_admin = input("Ingresar Usuario: ").upper()
                                    pass_admin = input("Ingresar su contraseña: ").upper()                                    
                                    user_admin_encript = encriptar(user_admin, lista1, lista2)
                                    pass_admin_encript = encriptar(pass_admin, lista1, lista2)                              
                                    with open('administrador.key', 'r') as archivo:
                                        administrador = archivo.readlines()                              
                                    encontrar = False
                                    for x in administrador:
                                        if x.strip() == user_admin_encript + "," + pass_admin_encript:
                                            encontrar = True
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print(cambio_color_center("\nUsuario y contraseña validado exitosamente!!"))
                                            time.sleep(2)
                                            break
                                    
                                    if encontrar == True:
                                        archivo = open("administradores.key", "w")
                                        for x in administrador:
                                            if x.strip()!= user_admin + "," + pass_admin:
                                                archivo.write(x)    
                                        archivo.close()
                                        print(cambio_color("Usuario eliminado exitosamente"))
                                        time.sleep(2)
                            elif opcion2 =="2":
                                while True: 
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center("**** Gestion de usuarios ****\n"))
                                    user_bi = input("Ingrese el usuario: ").upper()
                                    pass_bi = input("Ingrese su contraseña: ").upper()
                                    user_bi = encriptar(user_bi, lista1, lista2)
                                    pass_bi = encriptar(pass_bi, lista1, lista2)
                                    archivo = open('bibliotecarios.key', 'r')
                                    bibliotecario = archivo.readlines()
                                    archivo.close()
                                    archivo = open("bibliotecarios.key","w")
                                    encontrar = False
                                    for x in bibliotecario:
                                        if x.strip() == user_bi + "," + pass_bi:
                                            encontrar = True
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print("\n")
                                            print(cambio_color_center("Usuario y contraseña validado exitosamente!!"))
                                            time.sleep(2)
                                            break
                                    if encontrar == True:
                                        archivo = open("bibliotecarios.key", "w")
                                        for x in bibliotecario:
                                            if x.strip()!= user_bi + "," + pass_bi:
                                                archivo.write(x)
                                        archivo.close()
                                        print(cambio_color())
                                        time.sleep(2)
                            elif opcion2 == "3":
                                break
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center_rojo("Ingresar una opción válida"))
                                time.sleep(2)        
                    elif opcion1 == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(cambio_color_center("********* Gestion de usuarios ***********\n"))
                        print(cambio_color("** Administradores **\n"))
                        archivo = open('administrador.key', 'r') 
                        admin = archivo.readlines()
                        archivo.close()
                        contador = 0
                        p = 1
                        for x in admin:
                            x = encriptar(x, lista1, lista2)
                            contador += p
                            print(contador,".", x)
                        print("\n")
                        print(cambio_color("** Bibliotecarios **\n"))
                        archivo = open('bibliotecarios.key', 'r') 
                        bi = archivo.readlines()
                        archivo.close()
                        contador = 0
                        p = 1
                        for x in bi:
                            x = encriptar(x, lista1, lista2)
                            contador += p
                            print(contador,".", x)
                        print("\n")
                        input()
                    elif opcion1 == "5":
                        break
                    else: 
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(cambio_color_center_rojo("Seleccionar una opción válida"))
                        time.sleep(2)
            elif opcion == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cambio_color_center("********* Bienvenido Administrador ***********\n"))
                print(cambio_color("**Gestion de libros**\n"))
                print(cambio_color ("1." )  + " Agregar libros")
                print(cambio_color ("2." )  + " Cambiar algun dato del libro")
                print(cambio_color ("3." )  + " Eliminar algún libro")
                print(cambio_color ("4." )  + " Ver todos los libros")
                print(cambio_color ("5." )  + " Salir\n")
                opcion1 = input("Ingresar una opcion: ")
                if opcion1 == "1":
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        m = False
                        print(cambio_color_center("********* Agregar Libros ***********\n"))  
                        print(cambio_color_center("********* Categorías ***********\n"))
                        print(cambio_color ("1." )  + " 000 - Generalidades")
                        print(cambio_color ("2." )  + " 100 - Filosofía y Psicología")
                        print(cambio_color ("3." )  + " 200 - Religión")
                        print(cambio_color ("4." )  + " 300 - Ciencias Sociales")
                        print(cambio_color ("5." )  + " 400 - Lenguas")  
                        print(cambio_color ("6." )  + " 500 - Matemáticas y Ciencias Naturales")
                        print(cambio_color ("7." )  + " 600 - Tecnologías y Ciencias Aplicadas")
                        print(cambio_color ("8." )  + " 700 - Artes")
                        print(cambio_color ("9." )  + " 800 - Literatura")
                        print(cambio_color ("10." )  + " 900 - Historia y Geografía")
                        print(cambio_color ("11." )  + " Salir\n")
                        cod_libro  = input("Ingrese Categoría del libro: ").upper()
                        if cod_libro == "1":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 010 - Bibliografía")
                                print(cambio_color ("2." )  + " 020 - Bibliotecología y Ciencias de la Información")
                                print(cambio_color ("3." )  + " 030 - Enciclopedias Generales")
                                print(cambio_color ("4." )  + " 040 - ")
                                print(cambio_color ("5." )  + " 050 - Publicaciones en Serie")  
                                print(cambio_color ("6." )  + " 060 - Organizaciones y Museografía")
                                print(cambio_color ("7." )  + " 070 - Periodismo, Editoriales, Diarios")
                                print(cambio_color ("8." )  + " 080 - Colecciones Generales")
                                print(cambio_color ("9." )  + " 090 - Manuscritos y Libros Raros")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("010")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("020")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("030")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("040")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("050")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("060")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("070")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("080")
                                    m = True
                                    break   
                                elif cod_libro == "9":
                                    cod_libro = ("090")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                                    
                        elif cod_libro == "2":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 110 - Metafísica")
                                print(cambio_color ("2." )  + " 120 - Epistemología, Casualidad, Género Humano")
                                print(cambio_color ("3." )  + " 130 - Fenómenos Paranomarles")
                                print(cambio_color ("4." )  + " 140 - Escuelas Filosóficas Especifícas")
                                print(cambio_color ("5." )  + " 150 - Psicología")  
                                print(cambio_color ("6." )  + " 160 - Lógica")
                                print(cambio_color ("7." )  + " 170 - Ética (Filosfía Moral)")
                                print(cambio_color ("8." )  + " 180 - Filosofía Antigua, Medieval, Oriental")
                                print(cambio_color ("9." )  + " 190 - filosofía Moderna Occidental")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("110")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("120")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("130")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("140")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("150")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("160")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("170")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("180") 
                                    m = True
                                    break  
                                elif cod_libro == "9":
                                    cod_libro = ("190")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "3":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 210 - Filosofía y Tecnología de la Relig.")
                                print(cambio_color ("2." )  + " 220 - La Biblia")
                                print(cambio_color ("3." )  + " 230 - Cristianismo; Teología cristiana")
                                print(cambio_color ("4." )  + " 240 - Moral cristiana & teología piadosa")
                                print(cambio_color ("5." )  + " 250 - Ordenes cristianas & iglesia local")  
                                print(cambio_color ("6." )  + " 260 - Teología social y eclesiástica")
                                print(cambio_color ("7." )  + " 270 - Historia del cristianismo y de la iglesia cristiana")
                                print(cambio_color ("8." )  + " 280 - Confesiones & sectas cristianas")
                                print(cambio_color ("9." )  + " 290 - Religión comparada y otrasreligionesl")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("210")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("220")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("230")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("240")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("250")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("260")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("270")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("280") 
                                    m = True
                                    break  
                                elif cod_libro == "9":
                                    cod_libro = ("290")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "4":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 310 - Colecs. de estadística general")
                                print(cambio_color ("2." )  + " 320 - Ciencia política")
                                print(cambio_color ("3." )  + " 330 - Economía")
                                print(cambio_color ("4." )  + " 340 - Derecho")
                                print(cambio_color ("5." )  + " 350 - Administración pública y ciencia militar")  
                                print(cambio_color ("6." )  + " 360 - Problemas y servicios sociales; asociaciones")
                                print(cambio_color ("7." )  + " 370 - Educación")
                                print(cambio_color ("8." )  + " 380 - Comercio, comunicaciones, transporte")
                                print(cambio_color ("9." )  + " 390 - Costumbres, etiqueta, folclor")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("310")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("320")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("330")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("340")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("350")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("360")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("370")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("380")  
                                    m = True
                                    break 
                                elif cod_libro == "9":
                                    cod_libro = ("390")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "5":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 410 - Lingüística")
                                print(cambio_color ("2." )  + " 420 - Inglés e inglés antiguo")
                                print(cambio_color ("3." )  + " 430 - Lenguas germánicas Alemán")
                                print(cambio_color ("4." )  + " 440 - Lenguas romances Francés")
                                print(cambio_color ("5." )  + " 450 - Italiano, rumano, retorromano")  
                                print(cambio_color ("6." )  + " 460 - Lenguas española y portuguesa")
                                print(cambio_color ("7." )  + " 470 - Lenguas itálicas Latín")
                                print(cambio_color ("8." )  + " 480 - Lenguas helénicas Griego clásico")
                                print(cambio_color ("9." )  + " 490 - Otras lenguas")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("410")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("420")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("430")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("440")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("450")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("460")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("470")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("480") 
                                    m = True
                                    break  
                                elif cod_libro == "9":
                                    cod_libro = ("490")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "6":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 510 - Matemáticas")
                                print(cambio_color ("2." )  + " 520 - Astronomía y ciencias afines")
                                print(cambio_color ("3." )  + " 530 - Física")
                                print(cambio_color ("4." )  + " 540 - Química y ciencias afines")
                                print(cambio_color ("5." )  + " 550 - Ciencias de la tierra")  
                                print(cambio_color ("6." )  + " 560 - Paleontología, Paleozoología")
                                print(cambio_color ("7." )  + " 570 - Ciencias de la vida. Biología")
                                print(cambio_color ("8." )  + " 580 - Ciencias botánicas. Plantas")
                                print(cambio_color ("9." )  + " 590 - Ciencias zoológicas. Animales")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("510")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("520")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("530")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("540")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("550")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("560")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("570")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("580")  
                                    m = True
                                    break 
                                elif cod_libro == "9":
                                    cod_libro = ("590")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "7":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 610 - Ciencias médicas Medicina")
                                print(cambio_color ("2." )  + " 620 - Ingeniería & operaciones afines")
                                print(cambio_color ("3." )  + " 630 - Agricultura y tecnologías relacionadas")
                                print(cambio_color ("4." )  + " 640 - Economía doméstica & vida familiar")
                                print(cambio_color ("5." )  + " 650 - Gerencia y servicios auxiliares")  
                                print(cambio_color ("6." )  + " 660 - Ingeniería Química")
                                print(cambio_color ("7." )  + " 670 - Manufactura")
                                print(cambio_color ("8." )  + " 680 - Manufactura para usos específicos")
                                print(cambio_color ("9." )  + " 690 - Construcción")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("610")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("620")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("630")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("640")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("650")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("660")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("670")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("680") 
                                    m = True
                                    break  
                                elif cod_libro == "9":
                                    cod_libro = ("690")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "8":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 710 - Urbanismo & arte del paisaje")
                                print(cambio_color ("2." )  + " 720 - Arquitectura del paisaje")
                                print(cambio_color ("3." )  + " 730 - Artes plásticas, Escultura")
                                print(cambio_color ("4." )  + " 740 - Dibujo & artes decorativas")
                                print(cambio_color ("5." )  + " 750 - Pintura & pinturas")  
                                print(cambio_color ("6." )  + " 760 - Artes gráficas, Arte de grabar y grabados")
                                print(cambio_color ("7." )  + " 770 - Fotografía & fotografías")
                                print(cambio_color ("8." )  + " 780 - Música")
                                print(cambio_color ("9." )  + " 790 - Artes recreativas y de la actuación")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("710")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("720")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("730")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("740")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("750")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("760")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("770")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("780")   
                                    m = True
                                    break
                                elif cod_libro == "9":
                                    cod_libro = ("790")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "9":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 810 - Literatura norteamericana en inglés")
                                print(cambio_color ("2." )  + " 820 - Literatura inglesa e inglesa antigua")
                                print(cambio_color ("3." )  + " 830 - Literatura de las lenguas germánicas")
                                print(cambio_color ("4." )  + " 840 - Literaturas de las lenguas romances")
                                print(cambio_color ("5." )  + " 850 - Literaturas italiana, rumana, retorromana")  
                                print(cambio_color ("6." )  + " 860 - Literatura española & portuguesa")
                                print(cambio_color ("7." )  + " 870 - Literaturas itálicas, Literatura latina")
                                print(cambio_color ("8." )  + " 880 - Literaturas helénicas, Literatura griega clásica")
                                print(cambio_color ("9." )  + " 890 - Literatura de otras lenguas")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("810")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("820")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("830")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("840")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("850")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("860")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("870")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("880")  
                                    m = True
                                    break 
                                elif cod_libro == "9":
                                    cod_libro = ("890")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "10":
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(cambio_color_center("********* Subcategorías ***********\n"))
                                print(cambio_color ("1." )  + " 910 - Geografía y viajes")
                                print(cambio_color ("2." )  + " 920 - Biografía, genealogía, insignias")
                                print(cambio_color ("3." )  + " 930 - Historia del mundo antiguo")
                                print(cambio_color ("4." )  + " 940 - Historia general de Europa")
                                print(cambio_color ("5." )  + " 950 - Historia general de Asia. Lejano Oriente")  
                                print(cambio_color ("6." )  + " 960 - Historia general de África")
                                print(cambio_color ("7." )  + " 970 - Historia general de América del Norte")
                                print(cambio_color ("8." )  + " 980 - Historia general de América del Sur")
                                print(cambio_color ("9." )  + " 990 - Historia general de otras áreas")
                                print(cambio_color ("10." )  + " Salir\n")
                                cod_libro  = input("Ingrese Categoría del libro: ").upper()
                                if cod_libro == "1":
                                    cod_libro = ("910")
                                    m = True
                                    break
                                elif cod_libro == "2":
                                    cod_libro = ("920")
                                    m = True
                                    break
                                elif cod_libro == "3":
                                    cod_libro = ("930")
                                    m = True
                                    break
                                elif cod_libro == "4":
                                    cod_libro = ("940")
                                    m = True
                                    break
                                elif cod_libro == "5":
                                    cod_libro = ("950")
                                    m = True
                                    break
                                elif cod_libro == "6":
                                    cod_libro = ("960")
                                    m = True
                                    break
                                elif cod_libro == "7":
                                    cod_libro = ("970")
                                    m = True
                                    break
                                elif cod_libro == "8":
                                    cod_libro = ("980") 
                                    m = True
                                    break  
                                elif cod_libro == "9":
                                    cod_libro = ("990")
                                    m = True
                                    break
                                elif cod_libro == "10":
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(cambio_color_center_rojo("Seleccionar una opción válida"))
                                    time.sleep(2)
                        elif cod_libro == "11":
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(cambio_color_center_rojo("Seleccionar una opción válida"))
                            time.sleep(2)
                        break
                    if m == True:
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            nom_libro  = input("Ingresar el nombre del libro: ").upper()
                            mod__libro = input("Ingrese la edicion del libro: ").upper()
                            autor_libros = input("Ingrese el nombre del autor del libro: ").upper()                         
                            editorial_libro = input("Ingrese la editorial del libro: ").upper()            
                            precio_libro = input("Ingrese el precio del libro: ").upper()
                            est_libro  = input("Ingresar el estado del libro (usado,seminuevo,nuevo): ").upper()
                            archivo = open("libros.key","a")
                            archivo.write (f"{cod_libro},{nom_libro},{mod__libro},{autor_libros},{editorial_libro},{est_libro},{precio_libro}\n")
                            archivo.close()
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(cambio_color("El libro se agrego exitosamente el libro!!"))
                            time.sleep(2)
                            break
                       
                elif opcion1 == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center("********* Cambiar datos de libros ***********\n"))
                    print(cambio_color("**Gestión de libros**\n"))
                    archivo = open("libros.key", "r")
                    libros = archivo.readlines()
                    archivo.close()
                    for id, libro in enumerate(libros):
                        print(f"{id + 1}. {libro.strip()}")
                    libro_elegido = int(input("Elija el número del libro que quiera cambiar: ")) - 1
                    print("Elija el dato que quiera cambiar: ")
                    print(cambio_color ("1.") + " Cambiar código del libro")
                    print(cambio_color ("2.") + " Cambiar nombre del libro")
                    print(cambio_color ("3.") + " Cambiar edición del libro")
                    print(cambio_color ("4.") + " Cambiar autor del libro")
                    print(cambio_color ("5.") + " Cambiar editorial del libro")
                    print(cambio_color ("6.") + " Cambiar precio del libro")
                    print(cambio_color ("7.") + " Cambiar estado del libro")
                    print(cambio_color ("0.") + " Salir")
                    opcion2 = int(input("Ingrese la opción (0 para salir): "))

                    if opcion2 == 0:
                        exit()

                    valor_nuevo = input("Ingresa el nuevo valor del campo seleccionado: ")

                    archivo = open("libros.key", "r")
                    lineas = archivo.readlines()
                    archivo.close()

                    archivo = open("libros.key", "w")

                    for id, linea in enumerate(lineas):
                        if id == libro_elegido:
                            datos = linea.strip().split(",")

                            if opcion2 == 1:
                                datos[0] = valor_nuevo
                            elif opcion2 == 2:
                                datos[1] = valor_nuevo
                            elif opcion2 == 3:
                                datos[2] = valor_nuevo
                            elif opcion2 == 4:
                                datos[3] = valor_nuevo
                            elif opcion2 == 5:
                                datos[4] = valor_nuevo
                            elif opcion2 == 6:
                                datos[5] = valor_nuevo
                            elif opcion2 == 7:
                                datos[6] = valor_nuevo

                            nueva_linea = ", ".join(datos) + "\n"
                            archivo.write(nueva_linea)
                        else:
                            archivo.write(linea)

                    archivo.close()

                    print(cambio_color("Dato actualizado con éxito."))
                elif opcion1 == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center("********* Eliminar libros ***********\n"))
                    print(cambio_color("**Inventario de libros**\n"))
                    archivo = open('libros.key', 'r') 
                    libros = archivo.readlines()
                    archivo.close()
                    contador = 0
                    p = 1
                    lista_libros = ["--"]
                    encontrar = False
                    for x in libros:
                        contador += p
                        print(contador, x)
                        lista_libros.append(x)
                    l = int(input("Ingresar el numero del libro que desea eliminar: "))
                    for x in libros:
                        if x.strip() == lista_libros[l].strip():
                            encontrar = True
                            break
                   
                    if encontrar == True:
                        archivo = open("libros.key", "w")
                        for x in libros:
                            if x.strip()!= lista_libros[l].strip():
                                archivo.write(x)
                        archivo.close()
                        print(cambio_color("Usuario eliminado exitosamente!!!!!"))
                        time.sleep(2)                    
                        
                    
                elif opcion1 == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center("********* Inventario de libros ***********\n"))
                    print(cambio_color("**Inventario de libros dispobibles**\n"))
                    archivo = open('libros.key', 'r') 
                    libros = archivo.readlines()
                    archivo.close()
                    contador = 0
                    p = 1
                    for x in libros:
                        contador += p
                        print(contador,".", x)
                    print("\n")
                    print(cambio_color_center("**Inventario de libros prestados**\n"))
                    archivo = open('prestados.key', 'r') 
                    libros = archivo.readlines()
                    archivo.close()
                    contador = 0
                    p = 1
                    for x in libros:
                        contador += p
                        print(contador,".", x)
                    print("\n\n")
                    input(cambio_color_center("*** Presionar enter para continuar\n"))
                elif opcion1 == "5":
                    break
                else: 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center_rojo("Escribir una opcion válida!!"))
                    time.sleep(2)
            elif opcion == "3": 
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cambio_color_center_rojo("Ingresar una opcion válida"))
                time.sleep(2)
    elif opcion_menu == "2":
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(cambio_color_center("********* Bienvenido Bibliotecario ***********\n"))
            print("Por favor ingresar los siguientes datos: ")
            user_bibliotecario = input("Ingresar Usuario: ").upper()
            pass_bibliotecario = input("Ingresar su contraseña: ").upper()
            user_bibliotecario_encript = encriptar(user_bibliotecario, lista1, lista2)
            pass_bibliotecario_encript = encriptar(pass_bibliotecario, lista1, lista2)
            archivo = open('bibliotecarios.key','r')
            bibliotecario = archivo.readlines()
            archivo.close()
            encontrar = False
            for x in bibliotecario:
                if x.strip() == user_bibliotecario_encript + "," + pass_bibliotecario_encript:
                    encontrar = True
                    break
            if encontrar == True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n")
                print(cambio_color_center("Acceso Válido!!"))
                time.sleep(2)
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cambio_color_center_rojo("Acceso Denegado!!"))
                time.sleep(2)
            if encontrar == True:
                break
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(cambio_color_center("********* Bienvenido Bibliotecario ***********\n"))
            print("Por favor seleccione una opción: \n")
            print(cambio_color ("1.") + " Prestamo de libros")
            print(cambio_color ("2.") + " Recepcion de libros")
            print(cambio_color ("3.") + " Salir\n")
            opcion = input("Por favor seleccione una opción: ")
            if opcion == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cambio_color_center("********* Bienvenido Bibliotecario ***********\n"))
                print(cambio_color ("**Prestamo de libros**"))
                print("Por favor seleccione una opción: \n")
                print(cambio_color ("1.") + " Gestionar el préstamo de libros")
                print(cambio_color ("2.") + " Reporte de libros prestados a la fecha")
                print(cambio_color ("3.") + " Salir\n")
                opcion1 = input("Por favor seleccione una opción: ")
                if opcion1 == "1":
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(cambio_color_center("********* Gestion de libros prestados ***********\n"))
                        print(cambio_color ("1.") + " Usuario existente")
                        print(cambio_color ("2.") + " Usuario nuevo")
                        print(cambio_color ("3.") + " Ver usuarios")
                        print(cambio_color ("4.") + " Salir\n")
                        opcion2 = input("Ingrese la opcion: ")

                            
                        if opcion2 == "1":
                            print(cambio_color_center("**Gestión de libros**\n"))
                            usuario_existente = input("Ingrese el carnet: ")
                            archivo = open("alumnos.key", "r")
                            lineas = archivo.readlines()
                            carnet = 0
                            encontrar = False
                            for x in lineas:
                                if usuario_existente in x:
                                    encontrar = True
                            if encontrar == True:
                                # vamos a asignarle a estas variables los archivos que vamos a uar
                                libros_archivo = 'libros.key'
                                prestados_archivo = 'prestados.key'
                                usuarios_archivo = 'reporte_libros.key'
                                archivo_reporte = 'reporte_libros.key'
            

                                # aca vamos a crear una lista vacia para agregar los libros que ya estan 
                                #en el archivo de libros y los vamos a agregar a la lista vacia
                                libros = []
                                archivo_libros = open('libros.key', 'r')
                                for linea in archivo_libros:
                                    libros.append(linea.strip())
                                archivo_libros.close()

                                # aca lo unico que haremos es ver si hay libros disponibles en el archivo
                                if not libros:
                                    print("No hay libros disponibles para prestar.")
                                else:
                                    # si, si hay libros se los vamos a mostrar al usuario
                                    print("Libros disponibles:")
                                    for ix, libro in enumerate(libros, start=1):
                                        print(f"{ix}. {libro}")

                                    # aca vamos a permitir que el usuario elija el libro que quiere prestar
                                    print()
                                    eleccion = int(input("Ingrese el número del libro que desea prestar: ")) - 1
                                    if eleccion < 0 or eleccion >= len(libros):
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(cambio_color_center_rojo("\nAcceso Denegado!!"))
                                        time.sleep(2)
                                    else:
                                        libro_seleccionado = libros[eleccion]

                                        # vamos a mover el libro que el usuario quiere al nuevo archivo
                                        archivo_prestados = open(prestados_archivo, 'a')
                                        archivo_prestados.write(f"{libro_seleccionado}\n")
                                        archivo_prestados.close()
                                        archivo_libros = open(libros_archivo, 'w')
                                        for ix, libro in enumerate(libros):
                                            if ix != eleccion:
                                                archivo_libros.write(f"{libro}\n")
                                        archivo_libros.close()
                                        fecha_registro = datetime.date.today()
                                        fecha_devolucion = int(input("Ingrese cuantos dias se prestará el libro: "))
                                        dias_prestado = datetime.timedelta(days=fecha_devolucion)
                                        fecha_devolucion = fecha_registro + dias_prestado
                                        fecha_registro =  fecha_registro.strftime("%d/%m/%Y")
                                        fecha_devolucion =  fecha_devolucion.strftime("%d/%m/%Y")
                                        archivo_reporte= open("reporte_libros.key","a")
                                        
                                        archivo_reporte.write(f"{usuario_existente}, Fecha entrega: {fecha_registro}, Fecha esperada de devolucion: {fecha_devolucion} ,{libro_seleccionado} \n")
                                        archivo_reporte.close()
                                        
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(f"El libro '{libro_seleccionado}' ha sido prestado exitosamente.")
                                        time.sleep(3)
                        elif opcion2 == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            carnet = input("Ingresar carnet del estudiante: ")
                            nombre = input("Ingresar Nombre completo del estudiante: ")
                            print("\n**Datos de contacto**\n")
                            correo = input("Ingrese el correo del estudiante:") 
                            numero_telefono = input("Ingrese el numero de telefono del estudiante: ")
                            archivo = open('alumnos.key','a')                
                            archivo.write(carnet+","+nombre+","+correo+","+numero_telefono+"\n")
                            archivo.close()
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(cambio_color_center("El estudiante ha sido registrado exitosamente."))
                            time.sleep(2)
                        elif opcion2 == "3":
                            print(cambio_color_center("********* Inventario de libros ***********\n"))
                            print(cambio_color("**Inventario de libros dispobibles**\n"))
                            archivo = open('alumnos.key', 'r') 
                            alumnos = archivo.readlines()
                            archivo.close()
                            contador = 0
                            p = 1
                            for x in alumnos:
                                contador += p
                                print(contador,".", x)
                            print("\n")    
                            input(cambio_color_center("********* Enter para continuar ***********"))
                        elif opcion2 == "4":
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(cambio_color_center_rojo("Ingresar una opción válida"))
                            time.sleep(2)  

                elif opcion1 == "2":
                    #luis y angel
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center("********* Inventario de libros prestados ***********\n"))
                    archivo = open('prestados.key', 'r') 
                    libros = archivo.readlines()
                    archivo.close()
                    contador = 0
                    p = 1
                    for x in libros:
                        contador += p
                        print(contador,".", x)
                    print("\n\n\n")
                    input(cambio_color_center("*** Presionar enter para continuar\n"))
                elif opcion1 == "3":
                    break
                else: 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center_rojo("Ingresar una opción válida"))
                    time.sleep(2)
            elif opcion == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cambio_color_center("********* Bienvenido Bibliotecario ***********\n"))
                print(cambio_color("\n**Recepción de Libros**"))
                print("\nPor favor seleccione una opción: \n")
                print(cambio_color ("1.") + " Gestionar la devolución de un libro")
                print(cambio_color ("2.") + " Reporte de libros")
                print(cambio_color ("3.") + " Salir\n")
                opcion1 = input("Por favor seleccione una opción: ")
                if opcion1 == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center("*Recepción de Libros*\n"))
                    carnet = input("Ingresar el carnet del alumno: ")
                    archivo = open("prestados.key", "r")
                    lineas = archivo.readlines()
                    archivo.close()
                    libros = []
                    for x in lineas:
                        libros.append(x.strip())
                    for ix, libro in enumerate(libros, start=1):
                        print(f"{ix}. {libro}")    
                    print("\n")   
                    eleccion = int(input("Ingrese el número del libro que desea devolver: ")) - 1
                    if eleccion < 0 or eleccion >= len(libros):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(cambio_color_center_rojo("\nAcceso Denegado!!"))
                        time.sleep(2)
                    else:
                        libro_seleccionado = libros[eleccion]
                        archivo_prestados = open("libros.key", 'a')
                        archivo_prestados.write(f"{libro_seleccionado}\n")
                        archivo_prestados.close()
                        archivo_libros = open("prestados.key", 'w')
                        for ix, libro in enumerate(libros):
                            if ix != eleccion:
                                archivo_libros.write(f"{libro}\n")
                        archivo_libros.close()  
                        fecha_registro = datetime.date.today()
                        fecha_registro =  fecha_registro.strftime("%d/%m/%Y")
                        archivo = open("reporte_libros.key", "a")
                        archivo.write(f"{carnet}, Fecha en la que entrega: {fecha_registro},{libro_seleccionado}\n")
                        archivo.close()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(cambio_color_center("Libro devuelvo con éxito!!"))
                        time.sleep(2)
                        
                elif opcion1 == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center("********* Reporte de libros prestados ***********\n"))
                    archivo = open('reporte_libros.key', 'r') 
                    libros = archivo.readlines()
                    archivo.close()
                    contador = 0
                    p = 1
                    for x in libros:
                        contador += p
                        print(contador,".", x)
                    print("\n\n\n")
                    input(cambio_color_center("*** Presionar enter para continuar\n"))
                elif opcion1 == "3":
                    break
                else: 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(cambio_color_center_rojo("Ingresar una opción válida"))
                    time.sleep(2)
            elif opcion == "3":
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cambio_color_center_rojo("Ingresar una opción válida"))
                time.sleep(2)
    elif opcion_menu == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(cambio_color_center("Gracias por utilizar el sistema!!"))
        time.sleep(2)
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(cambio_color_center_rojo("Ingresar una opción válida"))
        time.sleep(2)