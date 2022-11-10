import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import HORIZONTAL
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm 
import matplotlib.pyplot as plt
import numpy as np


class Aplication:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Simulacion")
        self.root.config(bg="#FFFCDF")
        self.root.resizable(False,False)
        self.componentes()
        self.option_menu()
        self.root.mainloop()

    def componentes(self):
        
        self.title =tk.Label(self.root, text="Bienvenido a la herramienta\nGraficadora de cuadricas",font=('Times new roman', 15), bd=10,bg="#FFEAB1",width="25")
        self.title.pack()

        self.line = ttk.Separator(self.root, orient=HORIZONTAL)
        self.line.pack(fill='x')


        self.payment_label =tk.Label(self.root, text="Elija la funcion cuadrica a graficar: ", bd=10,bg="#FFFCDF")
        self.payment_label.pack(anchor='w')

        self.opcion = tk.IntVar()

###----------------------------------------------------------------------------Elipsoide---------------------------------------------------------------------------###
        self.Elipsoide= tk.Radiobutton(self.root, text="Elipsoide", variable=self.opcion,value=1, command=self.Deploy_info,bg="#FFFCDF")
        self.Elipsoide.pack(anchor='nw',pady="12")

        self.Img_Elipsoide=tk.PhotoImage(file=r"D:\Universidad\Tercer Semestre\Calculo Multivariable\ProyectoMultivariable\Tkinter\Img_Elipsoide.png")
        self.Lbl_Img1=tk.Label(self.root, image= self.Img_Elipsoide,bg="#FFFCDF")
###----------------------------------------------------------------------------------------------------------------------------------------------------------------###


###---------------------------------------------------------------------------Cono Eliptico------------------------------------------------------------------------###
        self.Cono_elip = tk.Radiobutton(self.root, text="Cono Eliptico", variable=self.opcion,value=2, command=self.Deploy_info,bg="#FFFCDF")
        self.Cono_elip.pack(anchor='nw',pady="12")

        self.Img_Cono_elip=tk.PhotoImage(file=r"D:\Universidad\Tercer Semestre\Calculo Multivariable\ProyectoMultivariable\Tkinter\Img_Cono_elip.png")
        self.Lbl_Img2=tk.Label(self.root, image= self.Img_Cono_elip,bg="#FFFCDF")
###----------------------------------------------------------------------------------------------------------------------------------------------------------------###


###----------------------------------------------------------------------------Paraboloide-------------------------------------------------------------------------###
        self.Paraboloide = tk.Radiobutton(self.root, text="Paraboloide", variable=self.opcion,value=3, command=self.Deploy_info,bg="#FFFCDF")
        self.Paraboloide.pack(anchor='nw',pady="12")
        self.Img_Paraboloide=tk.PhotoImage(file=r"D:\Universidad\Tercer Semestre\Calculo Multivariable\ProyectoMultivariable\Tkinter\Img_Paraboloide.png")
        self.Lbl_Img3=tk.Label(self.root, image= self.Img_Paraboloide,bg="#FFFCDF")
###----------------------------------------------------------------------------------------------------------------------------------------------------------------###


###----------------------------------------------------------------------Paraboloide Hiperbolico-------------------------------------------------------------------###
        self.Paraboloide_hip = tk.Radiobutton(self.root, text="Paraboloide Hiperbolico", variable=self.opcion,value=4, command=self.Deploy_info,bg="#FFFCDF")
        self.Paraboloide_hip.pack(anchor='nw',pady="12")
        self.Img_Paraboloide_hip=tk.PhotoImage(file=r"D:\Universidad\Tercer Semestre\Calculo Multivariable\ProyectoMultivariable\Tkinter\Img_Paraboloide_hip.png")
        self.Lbl_Img4=tk.Label(self.root, image= self.Img_Paraboloide_hip,bg="#FFFCDF")
###----------------------------------------------------------------------------------------------------------------------------------------------------------------###


###---------------------------------------------------------------------Hiperboloide de una hoja-------------------------------------------------------------------###
        self.Hiperboloide_1h = tk.Radiobutton(self.root, text="Hiperboloide de una hoja", variable=self.opcion,value=5, command=self.Deploy_info,bg="#FFFCDF")
        self.Hiperboloide_1h.pack(anchor='nw',pady="12")
        self.Img_Hiperboloide_1h=tk.PhotoImage(file=r"D:\Universidad\Tercer Semestre\Calculo Multivariable\ProyectoMultivariable\Tkinter\Img_Hiperboloide_1h.png")
        self.Lbl_Img5=tk.Label(self.root, image= self.Img_Hiperboloide_1h,bg="#FFFCDF")
###----------------------------------------------------------------------------------------------------------------------------------------------------------------###


###--------------------------------------------------------------------Hiperboloide de dos hojas-------------------------------------------------------------------###
        self.Hiperboloide_2h = tk.Radiobutton(self.root, text="Hiperboloide de dos hojas", variable=self.opcion,value=6, command=self.Deploy_info,bg="#FFFCDF")
        self.Hiperboloide_2h.pack(anchor='nw',pady="12")
        self.Img_Hiperboloide_2h=tk.PhotoImage(file=r"D:\Universidad\Tercer Semestre\Calculo Multivariable\ProyectoMultivariable\Tkinter\Img_Hiperboloide_2h.png")
        self.Lbl_Img6=tk.Label(self.root, image= self.Img_Hiperboloide_2h,bg="#FFFCDF")
###----------------------------------------------------------------------------------------------------------------------------------------------------------------###


###--------------------------------------------------------------------------------------------###
        self.line2 = ttk.Separator(self.root, orient=HORIZONTAL)
        self.line2.pack(fill='x')

        self.a =tk.Label(self.root, text="Un breve resumen:", bd=10,bg="#FFFCDF")

        self.boton1=tk.Button(self.root, text="Graficar", width=12,command=self.graficar)
        self.boton1.pack_forget()
###--------------------------------------------------------------------------------------------###

    def Deploy_info(self):
        self.a.pack_forget()

        self.Lbl_Img1.pack_forget()
        self.Lbl_Img2.pack_forget()
        self.Lbl_Img3.pack_forget()
        self.Lbl_Img4.pack_forget()
        self.Lbl_Img5.pack_forget()
        self.Lbl_Img6.pack_forget()

        self.boton1.pack_forget()

        if self.opcion.get()>0:
            self.a.pack(anchor='nw')

        if self.opcion.get()==1:
            self.Lbl_Img1.pack()

        elif self.opcion.get()==2:
            self.Lbl_Img2.pack()

        elif self.opcion.get()==3:
            self.Lbl_Img3.pack()

        elif self.opcion.get()==4:
            self.Lbl_Img4.pack()

        elif self.opcion.get()==5:
            self.Lbl_Img5.pack()

        elif self.opcion.get()==6:
            self.Lbl_Img6.pack()
        
        if self.opcion.get()>0:
            self.boton1.pack(anchor='center',padx="50",pady="10")

    def graficar(self):
        if self.opcion.get()==1:
            a=1;b=2;c=2
            fig = plt.figure(figsize=plt.figaspect(1))
            ax = fig.add_subplot(111, projection='3d')

            coefs = (a, b, c)
            rx, ry, rz = 1/np.sqrt(coefs)

            u = np.linspace(0, 2 * np.pi, 100)
            v = np.linspace(0, np.pi, 100)

            x = rx * np.outer(np.cos(u), np.sin(v))
            y = ry * np.outer(np.sin(u), np.sin(v))
            z = rz * np.outer(np.ones_like(u), np.cos(v))

            ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

            max_radius = max(rx, ry, rz)
            for axis in 'xyz':
                getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))

            plt.show()

            

        if self.opcion.get()==3:
            def f(x,y):
                return 2 * x**2 + y**2

            u = np.linspace(-2,2,10); v = np.linspace(-2,2,10)
            u, v = np.meshgrid(u,v)

            x = u; y = v; z = f(u,v)

            fig = plt.figure()

            ax = plt.axes(projection= "3d")

            ax.contour(x,y,z,30)

            plt.show()

        if self.opcion.get()==4:
            x = np.linspace(-2, 2, 100)
            y = np.linspace(-2, 2, 100)
            X, Y = np.meshgrid(x, y)
            Z = X**2 - Y**2

            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.plot_surface(X, Y, Z, color='b')


            plt.show()

        if self.opcion.get()==5:
            fig = plt.figure(figsize=plt.figaspect(1)) 
            ax = fig.add_subplot(111, projection='3d')

            r=1;
            u=np.linspace(-2,2,200);
            v=np.linspace(0,2*np.pi,60);
            [u,v]=np.meshgrid(u,v);

            a = 1
            b = 1
            c = 1

            x = a*np.cosh(u)*np.cos(v)
            y = b*np.cosh(u)*np.sin(v)
            z = c*np.sinh(u)

            ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

            plt.show()

        if self.opcion.get()==6:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            x = y = np.linspace(-3, 3, 10**3)
            X, Y = np.meshgrid(x, y)

            z = np.array([2+ x**2 + y**2 for x, y in zip(np.ravel(X), np.ravel(Y))])
            Z = z.reshape(X.shape)

            ax.plot_surface(X, Y, -np.sqrt(Z))
            ax.plot_surface(X, Y, np.sqrt(Z))

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            plt.xlim(-5,5)
            plt.ylim(-5,5)
            ax.set_zlim(-10, 10)


            ax.view_init(25, 45)

            plt.show()


    def option_menu(self):
        self.menubar1 = tk.Menu(self.root)
        self.root.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label="Ayuda", menu=self.opciones1) 
        self.opciones1.add_command(label="Acerca de...", command=self.info)
        

    def info(self):
        mb.showinfo("Información", "Este programa sirve para visualizar la grafica de algunas de las funciones cuadricas")   
    

Aplication=Aplication()