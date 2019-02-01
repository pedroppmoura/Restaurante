from tkinter import *
import random



class Clicker:
	def __init__(self, parent):


		self.dinheiro = 0
		self.parent = parent

		self.bandeja = []
		self.adicionar_ingredientes = {}


		self.nomes_sanduiches = ['Sanduiche Simples', 'Sanduiche Duplo']



		self.pedido_atual = 'Sanduiche Simples'

	


		self.sanduiches = {}
		self.sanduiches['Sanduiche Simples'] = ['Hamburguer', 'Pão']
		self.sanduiches['Sanduiche Duplo'] = ['Hamburguer', 'Hamburguer', 'Pão']

		self.receitas = {}
		self.receitas['Sanduiche Simples'] = '1 Hamburguer e 1 Pão'
		self.receitas['Sanduiche Duplo'] = '2 Hamburguers e 1 Pão'

		self.precos = {}
		self.precos['Sanduiche Simples'] = 5
		self.precos['Sanduiche Duplo'] = 8

		


		


		self.botao_vender = Button(parent, text = 'Vender Sanduiche Simples'  , command = lambda: self.vender())
		self.botao_vender.grid(row = 1, column = 1)

		self.receita = Label(parent, text = self.receitas['Sanduiche Simples'])
		self.receita.grid(row = 0, column = 2)

		self.mostrar_bandeja = Label(parent, text = 'Bandeja : %s' % self.bandeja)
		self.mostrar_bandeja.grid(row = 1, column = 2)

		self.mostrar_dinheiro = Label(parent, text = '%d coins' % self.dinheiro)
		self.mostrar_dinheiro.grid(row=0, column = 3)


		self.botao_limpar_bandeja = Button(parent, text = 'Limpar Bandeja', command = lambda : self.limpar_bandeja())
		self.botao_limpar_bandeja.grid(row = 0, column = 1)

		self.adicionar_ingredientes['Pão'] = Button(parent, text = 'Adicionar Pão', command = lambda: self.Adicionar('Pão'))
		self.adicionar_ingredientes['Pão'].grid(row = 0, column = 0)
		self.adicionar_ingredientes['Hamburguer'] = Button(parent, text = 'Adicionar Hamburguer', command = lambda: self.Adicionar('Hamburguer'))
		self.adicionar_ingredientes['Hamburguer'].grid(row = 1, column = 0)


	def Adicionar(self,ingrediente):
		self.bandeja.append(ingrediente)
		self.bandeja.sort()
		self.mostrar_bandeja.config(text =  'Bandeja : %s' % self.bandeja)
		print(self.bandeja)

	def limpar_bandeja(self):
		self.bandeja.clear()
		self.mostrar_bandeja.config(text =  'Bandeja : %s' % self.bandeja)
		print(self.bandeja)

	def atualizar_cliente (self):
		self.pedido_atual = random.choice(self.nomes_sanduiches)
		self.botao_vender.config(text = 'Vender %s' % self.pedido_atual)
		self.receita.config(text = self.receitas[self.pedido_atual])
		self.botao_vender.grid(row = 1, column = 1)


	def vender(self):
		if self.bandeja == self.sanduiches[self.pedido_atual]:
			self.dinheiro += self.precos[self.pedido_atual]
			self.mostrar_dinheiro.config(text = '%d coins' % self.dinheiro)
			self.limpar_bandeja()
			self.atualizar_cliente()
		else:
			print('Invalid')




root = Tk()
clicker = Clicker(root)
root.mainloop()
