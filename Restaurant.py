from tkinter import *
import random


class Clicker:
	def __init__(self, parent):

		self.imagem_vazia = Label(image = PhotoImage(file = "Vazio.png"))
		self.imagem_vazia.grid(row = 0, column = 2)
		self.numero_ingredientes = {}
		self.zerar_numero_ingredientes()

		self.maior_numero_permitido = {}
		self.maior_numero_permitido['Pão'] = 1
		self.maior_numero_permitido['Hamburguer'] = 2
		self.maior_numero_permitido['Queijo'] = 1
		self.maior_numero_permitido['Refrigerante de Cola'] = 1

		self.imagem_pao = PhotoImage(file = "Pao.png")
		self.imagem_hamburguer = PhotoImage(file = "Hamburguer.png")
		self.imagem_queijo = PhotoImage(file = "Queijo.png")
		self.imagem_refrigerante_de_cola = PhotoImage(file = "Refrigerante de Cola.png")
		self.barra_de_experiencia = PhotoImage(file = "Barra Exp 0%.png")


		self.dinheiro = 0
		self.parent = parent

		self.bandeja = []
		self.bandeja_acompanhamentos = []
		self.adicionar_ingredientes = {}


		self.nomes_sanduiches = ['Sanduiche Simples']
		self.level = 1



		self.pedido_atual = 'Sanduiche Simples'
		self.acompanhamento_atual = ''


	


		self.sanduiches = {}
		self.sanduiches['Sanduiche Simples'] = ['Hamburguer', 'Pão']
		self.sanduiches['Sanduiche Duplo'] = ['Hamburguer', 'Hamburguer', 'Pão']
		self.sanduiches['Cheeseburguer'] = ['Hamburguer', 'Pão', 'Queijo']

		self.lista_acompanhamentos = {}
		self.lista_acompanhamentos['Refrigerante de Cola'] = ['Refrigerante de Cola']


		self.acompanhamentos = ['Refrigerante de Cola']


		self.precos = {}
		self.precos['Sanduiche Simples'] = 5
		self.precos['Sanduiche Duplo'] = 8
		self.precos['Cheeseburguer'] = 10
		self.precos['Refrigerante de Cola'] = 5

		self.desbloquear_acompanhamento = False
		self.experiencia = 0
		self.experiencia_level_up = 5



		self.mostrar_acompanhamento = Label(parent)
		self.mostrar_acompanhamento.place(x = 200, y = 80)

		self.imagem_sanduiche =  PhotoImage(file = "Sanduiche Simples.png")
		self.botao_vender = Button(parent, image = self.imagem_sanduiche, command = lambda: self.vender())
		self.botao_vender.grid(row = 1, column = 3)

		self.label_pedido = Label(parent, text = "Pedido do Cliente:")
		self.label_pedido.grid(row = 0 , column = 3)


		
		self.label_barra_experiencia = Label(parent, image = self.barra_de_experiencia)
		self.label_barra_experiencia.grid(row = 4, column = 0)


		self.imagem_bandeja = PhotoImage(file = "Bandeja -[].png")

		self.mostrar_bandeja = Label(parent, image = self.imagem_bandeja)
		self.mostrar_bandeja.grid(row = 1, column = 1)


		self.mostrar_dinheiro = Label(parent, text = '%d coins' % self.dinheiro)
		self.mostrar_dinheiro.grid(row=2, column = 1)


		self.botao_limpar_bandeja = Button(parent, text = 'Limpar Bandeja', command = lambda : self.limpar_bandeja())
		self.botao_limpar_bandeja.grid(row = 0, column = 1)

		self.adicionar_ingredientes['Pão'] = Button(parent, image = self.imagem_pao, command = lambda: self.Adicionar('Pão'))
		self.adicionar_ingredientes['Pão'].grid(row = 0, column = 0)
		self.adicionar_ingredientes['Hamburguer'] = Button(parent, image = self.imagem_hamburguer, command = lambda: self.Adicionar('Hamburguer'))
		self.adicionar_ingredientes['Hamburguer'].grid(row = 1, column = 0)


	


	def Adicionar(self,ingrediente):
		if self.numero_ingredientes[ingrediente] < self.maior_numero_permitido[ingrediente]:
			self.bandeja.append(ingrediente)
			self.bandeja.sort()
			self.numero_ingredientes[ingrediente] += 1
			self.atualizar_bandeja()
			print(self.bandeja)



	def atualizar_bandeja (self):

		self.imagem_bandeja = PhotoImage(file = "Bandeja -"+ str(self.bandeja) +".png")
		self.mostrar_bandeja.config(image = self.imagem_bandeja)	
		self.mostrar_acompanhamento.config(image = PhotoImage(file = "Acompanhamento -Vazio.png"))
		self.imagem_acompanhamento_atual = Label(image = PhotoImage(file = "Acompanhamento -Vazio.png"))
	

	def limpar_bandeja(self):
		self.bandeja.clear()
		self.bandeja_acompanhamentos.clear()
		self.mostrar_bandeja.config(text =  'Bandeja : %s' % self.bandeja)
		self.atualizar_bandeja()
		print(self.bandeja)
		self.zerar_numero_ingredientes()


	def atualizar_cliente (self):

		self.pedido_atual = random.choice(self.nomes_sanduiches)


		if self.desbloquear_acompanhamento:
			x = random.randint(0,3)
			if x == 1:
				self.acompanhamento_atual = random.choice(self.acompanhamentos)
				self.file_imagem_acompanhamento = PhotoImage(file = "Acompanhamento -" + self.acompanhamento_atual +".png")
				self.imagem_acompanhamento_atual = Label(image = self.file_imagem_acompanhamento)
				self.imagem_acompanhamento_atual.place(x = 380, y = 80)
			else:
				self.acompanhamento_atual = ''
				self.file_imagem_acompanhamento = PhotoImage(file = "Acompanhamento -Vazio.png")
				self.imagem_acompanhamento_atual = Label(image = self.file_imagem_acompanhamento)
				self.imagem_acompanhamento_atual.place(x = 380, y = 80)




		self.imagem_sanduiche =  PhotoImage(file = self.pedido_atual + ".png")
		self.botao_vender.config(image = self.imagem_sanduiche)


	def vender(self):
		print(self.acompanhamento_atual)
		print(self.pedido_atual)
		if self.acompanhamento_atual and self.pedido_atual:
			if self.bandeja + self.bandeja_acompanhamentos == self.sanduiches[self.pedido_atual] + self.lista_acompanhamentos[self.acompanhamento_atual]:
				self.dinheiro += self.precos[self.pedido_atual]
				self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
				self.experiencia += 1
				self.atualizar_exp()
				self.limpar_bandeja()
				self.atualizar_cliente()
		elif self.acompanhamento_atual: 
			if  self.bandeja + self.bandeja_acompanhamentos == self.lista_acompanhamentos[self.acompanhamento_atual]:
				self.dinheiro += self.precos[self.pedido_atual]
				self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
				self.experiencia += 1
				self.atualizar_exp()
				self.limpar_bandeja()
				self.atualizar_cliente()
			
		else:
			if self.bandeja + self.bandeja_acompanhamentos == self.sanduiches[self.pedido_atual]:
				self.dinheiro += self.precos[self.pedido_atual]
				self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
				self.experiencia += 1
				self.atualizar_exp()
				self.limpar_bandeja()
				self.atualizar_cliente()


	def atualizar_exp(self):

		if self.experiencia >= self.experiencia_level_up:
			self.level_up()

		self.pixel = round(self.experiencia * 10 /self.experiencia_level_up)

		self.barra_de_experiencia = PhotoImage(file = "Barra Exp " + str(self.pixel * 10) + "%.png")
		self.label_barra_experiencia.config(image =  self.barra_de_experiencia)

	


	def desbloquear_receita(self, numero_receitas):
		
		if  numero_receitas == 1 and self.dinheiro >= 10:
			self.dinheiro -=  10
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.nomes_sanduiches.append('Sanduiche Duplo')
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.desbloquear_nova_receita_2.destroy()
	



		if numero_receitas == 2 and self.dinheiro >= 50:
			self.dinheiro -=  50
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.adicionar_ingredientes['Queijo'] = Button(image = self.imagem_queijo, command = lambda: self.Adicionar('Queijo'))
			self.adicionar_ingredientes['Queijo'].grid(row = 2, column = 0)
			self.desbloquear_nova_receita_4 = Button(text = 'Desbloquear nova receita (70)', command = lambda: self.desbloquear_receita(3))
			self.desbloquear_nova_receita_4.grid(row = 1, column = 4)
			self.desbloquear_nova_receita_3.destroy()

			


		if numero_receitas == 3 and self.dinheiro >= 70:
			self.dinheiro -=  70
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.nomes_sanduiches.append('Cheeseburguer')
			self.desbloquear_nova_receita_4.destroy()

		if numero_receitas == 4 and self.dinheiro >= 80:
			self.dinheiro -= 80
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.adicionar_ingredientes['Refrigerante de Cola'] = Button(image = self.imagem_refrigerante_de_cola, command = lambda: self.adicionar_acompanhamento('Refrigerante de Cola'))
			self.adicionar_ingredientes['Refrigerante de Cola'].grid(row = 3, column = 0)
			self.desbloquear_acompanhamento = True
			self.desbloquear_nova_receita_5.destroy()


	def adicionar_acompanhamento(self, acompanhamento):

		if self.numero_ingredientes[acompanhamento] < self.maior_numero_permitido[acompanhamento]:
			self.bandeja_acompanhamentos.append(acompanhamento)
			self.bandeja_acompanhamentos.sort()
			self.numero_ingredientes[acompanhamento] += 1
			self.imagem_acompanhamento = PhotoImage(file = "Acompanhamento -" + acompanhamento + ".png")
			self.mostrar_acompanhamento.config(image = self.imagem_acompanhamento)



	def  level_up(self):

		self.experiencia = 0
		self.level += 1
		self.experiencia_level_up = self.experiencia_level_up * 1.4

		if self.level == 2:
			self.desbloquear_nova_receita_2 = Button(text = 'Desbloquear nova receita (10)', command = lambda: self.desbloquear_receita(1))
			self.desbloquear_nova_receita_2.grid(row = 0 , column = 4)

		if self.level == 3:
			self.desbloquear_nova_receita_3 = Button(text = 'Contratar entrega de Queijo (50)', command = lambda: self.desbloquear_receita(2))
			self.desbloquear_nova_receita_3.grid(row = 1 , column = 4)

		if self.level == 4:
			self.desbloquear_nova_receita_5 = Button(text = 'Comprar maquina de refrigerante (80)', command = lambda: self.desbloquear_receita(4))
			self.desbloquear_nova_receita_5.grid(row = 2 , column = 4)



	def zerar_numero_ingredientes (self):
		self.numero_ingredientes['Hamburguer'] = 0
		self.numero_ingredientes['Pão'] = 0
		self.numero_ingredientes['Queijo'] = 0
		self.numero_ingredientes['Refrigerante de Cola'] = 0


root = Tk()
clicker = Clicker(root)
root.mainloop()
