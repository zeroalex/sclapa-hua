import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import sclapahua

from tkinter import PhotoImage, filedialog

#from model import Model
from ttkbootstrap import Style
#style = Style(theme='flatly')
style = Style(theme='cosmo')



class App:
    def __init__(self, root):
            
        self.janela = root.get_object("login")
        

        #self.botao=root.get_object("login_entrar_botao")

        #self.botao.configure(style='success.Outline.TButton')

        self.botao2=root.get_object("login_cancelar_botao")
        self.botao2.configure(style='primary.TButton')
        
        self.logo=root.get_object("logo")
        self.logo_img = PhotoImage(name='logo',file='img/logo.png')
       
        self.logo['image']=self.logo_img
        
        self.botao_seleciona_db = root.get_object("botao_seleciona_db")
        self.database = ''

        #self.login_matricula_entry=root.get_object("login_matricula_entry")
        #self.login_senha_entry=root.get_object("login_senha_entry")
        #self.cvar="asd"

        

    def logar(self):
        
        '''Mudar para coletar usuario da máquina 
        
        matricula = "5042"
        senha = "ASDF"
        
        self.usuario = self.madruga.buscar_usuario(matricula,senha)
        usuario = self.usuario
        '''
        self.usuario=''
        
            

        self.carregar_sistema()



    def selecionar_db(self,asd):
        
        filename = filedialog.askopenfilename(title = "Select a File",
                                        filetypes = (("Database",
                                                        "*.mdb*"),
                                                    ("all files",
                                                        "*.*")))
    
        self.database = filename
        self.botao_seleciona_db["text"]= filename

        pass    
    def carregar_sistema(self):
        ui = pygubu.Builder()
        ui.add_from_file("window_main.ui")

        
        win =ui.get_object("principal2")
        win.master.title("HUA - Shopping Center LAPA | Alex Odisseus")
        win.master.geometry('900x1150')
        win.master.geometry('+1+1')
        
        self.janela_quit()
        self.usuario = self.database
        ui.connect_callbacks(sclapahua.abil(ui,self.usuario))


    def janela_quit(self):

        self.janela.destroy()
        pass
    def janela_destroy(self):

        self.janela.quit()

        
    def buscar_infracao_lateral(self):
    	print('asdf')


ui2 = pygubu.Builder()
ui2.add_from_file("window_login.ui")

labil = App(ui2)
ui2.connect_callbacks(labil)



win =ui2.get_object("login")
win.master.title("HUA - Shopping Center LAPA | Alex Odisseus")
win.mainloop()