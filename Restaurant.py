from tkinter import *
import random


class Clicker:
	def __init__(self, parent):

		self.parent = parent


		# Configurações padrão
		
		self.dinheiro = 0
		self.level = 1
		self.desbloquear_acompanhamento = False
		self.experiencia = 0
		self.experiencia_level_up = 5



		# Espaço entre colunas

		self.imagem_vazia =  PhotoImage(file = "Vazio.png")
		self.espaco_colunas = Label( bg = 'Light Gray', image = self.imagem_vazia)
		self.espaco_colunas.grid(row = 0, column = 2)

		self.canvas = Canvas(parent, bg= "Light Gray", width=1000, height=1000)
		self.canvas.place(x= 0, y = 0)

		# Delimita um numero de cada ingredientes que é possível adicionar a bandeja

		self.numero_ingredientes = {}
		self.zerar_numero_ingredientes()

		self.maior_numero_permitido = {}
		self.maior_numero_permitido['Pão'] = 1
		self.maior_numero_permitido['Hamburguer'] = 2
		self.maior_numero_permitido['Queijo'] = 1
		self.maior_numero_permitido['Refrigerante de Cola'] = 1
		self.maior_numero_permitido['Batata Frita'] = 1


		# Imagens

		self.imagem_pao = PhotoImage(file = "Pao.png")
		self.imagem_hamburguer = PhotoImage(file = "Hamburguer.png")
		self.imagem_queijo = PhotoImage(file = "Queijo.png")
		self.imagem_refrigerante_de_cola = PhotoImage(file = "Refrigerante de Cola.png")
		self.imagem_batata_frita = PhotoImage(file = "Batata Frita.png")
		self.imagem_barra_de_experiencia = PhotoImage(file = "Barra Exp 0%.png")


		# Bandejas

		self.bandeja = []
		self.bandeja_acompanhamentos = []


		self.botao_adicionar_ingredientes = {}


		# Lista de sanduiches desbloqueados

		self.nomes_sanduiches = ['Sanduiche Simples']
		self.acompanhamentos = ['Refrigerante de Cola', '']

		self.desbloquear_nova_receita = {}


		# Pedido padrão (Inicial)

		self.pedido_atual = 'Sanduiche Simples'
		self.acompanhamento_atual = ''


	
		# Receitas

		self.sanduiches = {}
		self.sanduiches['Sanduiche Simples'] = ['Hamburguer', 'Pão']
		self.sanduiches['Sanduiche Duplo'] = ['Hamburguer', 'Hamburguer', 'Pão']
		self.sanduiches['Cheeseburguer'] = ['Hamburguer', 'Pão', 'Queijo']

		self.lista_acompanhamentos = {}
		self.lista_acompanhamentos['Refrigerante de Cola'] = ['Refrigerante de Cola']
		self.lista_acompanhamentos['Batata Frita'] = ['Batata Frita']



		self.precos = {}
		self.precos['Sanduiche Simples'] = 50
		self.precos['Sanduiche Duplo'] = 8
		self.precos['Cheeseburguer'] = 10
		self.precos['Refrigerante de Cola'] = 5
		self.precos['Batata Frita'] = 5

		


		# Labels

		self.mostrar_acompanhamento = Label(parent)
		self.mostrar_acompanhamento.place(x = 200, y = 90)

		self.imagem_sanduiche =  PhotoImage(file = "Sanduiche Simples.png")
		self.botao_vender = Button(parent, bg = 'Light Gray' ,image = self.imagem_sanduiche, command = lambda: self.vender())
		self.botao_vender.grid(row = 1, column = 3)

		self.label_pedido = Label(parent, bg = 'Light Gray' ,text = "Pedido do Cliente:")
		self.label_pedido.grid(row = 0 , column = 3)


		
		self.label_barra_experiencia = Label(parent, bg = 'Light Gray', image = self.imagem_barra_de_experiencia)
		self.label_barra_experiencia.grid(row = 999, column = 0)


		self.imagem_bandeja = PhotoImage(file = "Bandeja -[].png")

		self.mostrar_bandeja = Label(parent, bg = 'Light Gray', image = self.imagem_bandeja)
		self.mostrar_bandeja.grid(row = 1, column = 1)


		self.mostrar_dinheiro = Label(parent, text = '%d coins' % self.dinheiro)
		self.mostrar_dinheiro.grid(row=2, column = 1)


		self.botao_limpar_bandeja = Button(parent, text = 'Limpar Bandeja', command = lambda : self.limpar_bandeja())
		self.botao_limpar_bandeja.grid(row = 0, column = 1)

		self.botao_adicionar_ingredientes['Pão'] = Button(parent, bg = 'Light Gray', image = self.imagem_pao, command = lambda: self.Adicionar('Pão'))
		self.botao_adicionar_ingredientes['Pão'].grid(row = 0, column = 0)
		self.botao_adicionar_ingredientes['Hamburguer'] = Button(parent, bg = 'Light Gray', image = self.imagem_hamburguer, command = lambda: self.Adicionar('Hamburguer'))
		self.botao_adicionar_ingredientes['Hamburguer'].grid(row = 1, column = 0)


	


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
		
	

	def limpar_bandeja(self):
		self.bandeja.clear()
		self.bandeja_acompanhamentos.clear()
		self.atualizar_bandeja()
		print(self.bandeja)
		self.zerar_numero_ingredientes()
		self.imagem_acompanhamento_vazio = PhotoImage(file = "Acompanhamento -.png")
		self.mostrar_acompanhamento.config(bg = 'Light Gray', image = self.imagem_acompanhamento_vazio)
		self.imagem_acompanhamento_atual = Label(bg = 'Light Gray' , image = self.imagem_acompanhamento_vazio)




	def atualizar_cliente (self):

		self.pedido_atual = random.choice(self.nomes_sanduiches)

		self.imagem_sanduiche =  PhotoImage(file = self.pedido_atual + ".png")
		self.botao_vender.config(image = self.imagem_sanduiche)

		if self.desbloquear_acompanhamento:
			self.x = random.choice(self.acompanhamentos)
			if self.x != 'Vazio':
				self.acompanhamento_atual = random.choice(self.acompanhamentos)
				self.file_imagem_acompanhamento = PhotoImage(file = "Acompanhamento -%s.png" % self.acompanhamento_atual)
				self.imagem_acompanhamento_atual = Label(bg = 'Light Gray', image = self.file_imagem_acompanhamento)
				self.imagem_acompanhamento_atual.place(x = 460, y = 95)
			else:
				print (2)



	def vender(self):
		print(self.acompanhamento_atual)
		print(self.pedido_atual)

		if self.acompanhamento_atual and self.pedido_atual:
			if self.bandeja + self.bandeja_acompanhamentos == self.sanduiches[self.pedido_atual] + self.lista_acompanhamentos[self.acompanhamento_atual]:
				self.dinheiro += self.precos[self.pedido_atual] + self.precos[self.acompanhamento_atual]
				self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
				self.experiencia += 10
				self.atualizar_exp()
				self.limpar_bandeja()
				self.atualizar_cliente()

		elif self.acompanhamento_atual: 
			if  self.bandeja + self.bandeja_acompanhamentos == self.lista_acompanhamentos[self.acompanhamento_atual]:
				self.dinheiro +=  self.precos[self.acompanhamento_atual]
				self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
				self.experiencia += 10
				self.atualizar_exp()
				self.limpar_bandeja()
				self.atualizar_cliente()
			
		else:
			if self.bandeja + self.bandeja_acompanhamentos == self.sanduiches[self.pedido_atual]:
				self.dinheiro += self.precos[self.pedido_atual]
				self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
				self.experiencia += 10
				self.atualizar_exp()
				self.limpar_bandeja()
				self.atualizar_cliente()


	def atualizar_exp(self):

		if self.experiencia >= self.experiencia_level_up:
			self.level_up()

		self.pixel = round(self.experiencia * 10 /self.experiencia_level_up)

		self.imagem_barra_de_experiencia = PhotoImage(file = "Barra Exp " + str(self.pixel * 10) + "%.png")
		self.label_barra_experiencia.config(image =  self.imagem_barra_de_experiencia)

	


	def desbloquear_receita(self, numero_receitas):
		
		if  numero_receitas == 1 and self.dinheiro >= 10:
			self.dinheiro -=  10
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.nomes_sanduiches.append('Sanduiche Duplo')
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.desbloquear_nova_receita_2.destroy()
	


		if numero_receitas == 2 and self.dinheiro >= 25:
			self.dinheiro -=  25
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.botao_adicionar_ingredientes['Queijo'] = Button(bg = 'Light Gray' ,image = self.imagem_queijo, command = lambda: self.Adicionar('Queijo'))
			self.botao_adicionar_ingredientes['Queijo'].grid(row = 2, column = 0)
			self.desbloquear_nova_receita_4 = Button(text = 'Desbloquear nova receita (70)', command = lambda: self.desbloquear_receita(3))
			self.desbloquear_nova_receita_4.grid(row = 1, column = 4)
			self.desbloquear_nova_receita_3.destroy()

			
		if numero_receitas == 3 and self.dinheiro >= 50:
			self.dinheiro -=  50
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.nomes_sanduiches.append('Cheeseburguer')
			self.desbloquear_nova_receita_4.destroy()


		if numero_receitas == 4 and self.dinheiro >= 70:
			self.dinheiro -= 70
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.botao_adicionar_ingredientes['Refrigerante de Cola'] = Button(bg = 'Light Gray' ,image = self.imagem_refrigerante_de_cola, command = lambda: self.adicionar_acompanhamento('Refrigerante de Cola'))
			self.botao_adicionar_ingredientes['Refrigerante de Cola'].grid(row = 3, column = 0)
			self.desbloquear_acompanhamento = True
			self.desbloquear_nova_receita_5.destroy()

		if numero_receitas == 5 and self.dinheiro >= 100:
			self.dinheiro -= 100
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.acompanhamentos.append('Batata Frita')
			self.botao_adicionar_ingredientes['Batata Frita'] = Button(bg = 'Light Gray' ,image = self.imagem_batata_frita, command = lambda: self.adicionar_acompanhamento('Batata Frita'))
			self.botao_adicionar_ingredientes['Batata Frita'].grid(row = 4, column = 0)
			self.desbloquear_acompanhamento = True
			self.desbloquear_nova_receita_6.destroy()





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
			self.desbloquear_nova_receita[str(self.level)] = Button(text = 'Desbloquear nova receita (10)', command = lambda: self.desbloquear_receita(1))
			self.desbloquear_nova_receita[str(self.level)].grid(row = self.level , column = 4)

		if self.level == 3:
			self.desbloquear_nova_receita[str(self.level)] = Button(text = 'Contratar entrega de Queijo (50)', command = lambda: self.desbloquear_receita(2))
			self.desbloquear_nova_receita[str(self.level)].grid(row = self.level , column = 4)

		if self.level == 4:
			self.desbloquear_nova_receita[str(self.level)] = Button(text = 'Comprar maquina de refrigerante (80)', command = lambda: self.desbloquear_receita(4))
			self.desbloquear_nova_receita[str(self.level)].grid(row = self.level , column = 4)

		if self.level == 5:
			self.desbloquear_nova_receita[str(self.level)] = Button(text = 'Comprar maquina de batata frita (100)', command = lambda: self.desbloquear_receita(5))
			self.desbloquear_nova_receita[str(self.level)].grid(row = self.level, column = 4)



	def zerar_numero_ingredientes (self):
		self.numero_ingredientes['Hamburguer'] = 0
		self.numero_ingredientes['Pão'] = 0
		self.numero_ingredientes['Queijo'] = 0
		self.numero_ingredientes['Refrigerante de Cola'] = 0
		self.numero_ingredientes['Batata Frita'] = 0


root = Tk()
clicker = Clicker(root)
root.mainloop()
