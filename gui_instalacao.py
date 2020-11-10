# -*- coding: utf-8 -*-
from tkinter import *
import subprocess
import os
import time

#funcoes
def resource_path(relative_path):
    #""" Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def xy_screen(w=300, h=200):
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws/2) - (w/2) 
	y = (hs/2) - (h/2)	
	return (x,y)

#GUI
class Application(Frame):
	
	def __init__(self, master=None):
	
		Frame.__init__(self, master)
		self.grid()
		self.master.title("Relatório de TUE, TUG e Iluminação")

		for lin in range(6):
			self.master.rowconfigure(lin, weight=1)    
		for col in range(5):
			self.master.columnconfigure(col, weight=1)
		
		#necessário checar se o arquivo existe antes de iniciar um novo relatorio
		if os.access("comodos.csv", os.R_OK):
			os.remove("comodos.csv")
	
		#arquivo de texto de saída
		arquivo_de_saida = open("comodos.csv", "w")
		subprocess.check_call(["attrib","+H","comodos.csv"]) #deixando o arquivo invisivel
		arquivo_de_saida.write("Comodo Area Perimetro Tipo \n")
		arquivo_de_saida.close()
		
		#nome
		lbl_comodo = Label(text="Nome")
		lbl_comodo.grid(column=0, row=0, sticky = "e")
		
		dsp_comodo = Entry(master, justify = "right", font="tahoma")
		dsp_comodo.grid( column = 1, row = 0)
		
		#area
		lbl_area = Label(text="Área (m²)")
		lbl_area.grid(column=0, row=1, sticky = "e")
		
		spin_area = Spinbox(master, from_=0, to=999) #999 apenas para ter um teto
		spin_area.grid( column = 1, row = 1)
		
		#perimetro
		lbl_2p = Label(text="Perímetro (m)")
		lbl_2p.grid(column=0, row=2, sticky = "e")
		
		spin_2p = Spinbox(master, from_=0, to=999)
		spin_2p.grid(column=1, row=2)
		
		#tipo de cômodo
		lbl_tipo = Label(text="Tipo de cômodo")
		lbl_tipo.grid(column=0, row=3, sticky = "e")
		
		tipo_comodo = StringVar(master) #string necessária para o menu
		tipo_comodo.set("Tipo") #valor default inicial
		
		menu_tipo = OptionMenu(master, tipo_comodo,"Sala", "Banheiro", "Varanda", "Molhado", "Demais")
		menu_tipo.grid( column=1, row=3, sticky = "e")
		
		
		#botao adc comodo
		def cmd_adc_comodo():
			nome = dsp_comodo.get()
			area = spin_area.get()
			perimetro = spin_2p.get()
			tipo = tipo_comodo.get()
			arquivo = open("comodos.csv", "a")
			arquivo.write(nome+' '+area+' '+perimetro+' '+tipo+'\n') 
			arquivo.close()
			
		btn_adc_comodo = Button (master, text="Adicionar", command = cmd_adc_comodo)
		btn_adc_comodo.grid(column=1, row=5, sticky="e")
		
		#botao concluir
		def concluir_projeto():
			
			#rodar codigo em c ja compilado
			subprocess.call([resource_path("tulum.exe")])
			#remover arquivo com entradas usadas
			os.remove("comodos.csv")
			
			#caixa de mensagem
			msg_bx_concluir = Toplevel()
			msg_bx_concluir.title("Pronto")
			msg_concluir = Message(msg_bx_concluir, text="Relatório se encontra na pasta do programa", width=300)
			msg_concluir.pack()
			
			button = Button(msg_bx_concluir, text="Sair", command=msg_bx_concluir.destroy)
			button.pack()
			msg_bx_concluir.focus_set()
			w=300
			h=50
			(x,y)=xy_screen(w,h)
			msg_bx_concluir.geometry('%dx%d+%d+%d' % (w, h, x, y))
			
			msg_bx_concluir.iconbitmap(resource_path("bolt.ico"))	
			
		btn_concluir = Button(master, text = "Relatório", command = concluir_projeto)
		btn_concluir.grid(column=2, row=5, sticky="e")



root = Tk()

w=400
h=200	
(x,y)=xy_screen(w,h)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.iconbitmap(resource_path("bolt.ico"))	
app=Application(master=root)
app.mainloop()