#https://datatofish.com/how-to-connect-python-to-ms-access-database-using-pyodbc/
#!/usr/bin/python
# -*- coding: latin-1 -*-

import pyodbc
from donaclotilde import *

from datetime import date
#import sqlite3






def pprint():
	print("old model")




class Model(Donaclotilde):
	"""docstring for Model"""
	def __init__(self, data_local = None):
		super().__init__()
		
		
		self.data_local = data_local
		self.usuario="defalt"
		

	def connect_db(self):
		#self.conn = sqlite3.connect('Z:/DEPEC/SECME/ADMINISTRATIVO/normas/database.db')
		"""		
		if self.data_local == None or self.data_local == '':
			
			self.conn = sqlite3.connect('database.db')
			self.cursor = self.conn.cursor()			

		else:
		"""
		self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+self.data_local+';')
		self.cursor = self.conn.cursor()

	

	def multa_salvar(self,kwargs):
		
		data_hoje = date.today()
		kwargs["Implantado"] = str(data_hoje)
		
		valores=[]
		for x in kwargs.values():
			valores.append(x)

		colunas=[]
		for x in kwargs.keys():
			colunas.append(x)

		sql = self.set("Cotistas",valores,colunas)
		#print(sql)
		
		verifica = self.buscar_cotista_repetida(kwargs)
		
		if verifica != []:
			return verifica
		else:
			self.insert(sql)
			return True
		
	


	def buscar_cotista_repetida(self,dados):
		
		self.select('Nome')
		self.from_table("Cotistas")

		self.where(dados['Nome'],"Nome","=")
		
		"""
		self.where_combining(dados['infracao_multa'],"infracao_multa","AND","=")
		self.where_combining(dados['data_multa'],"data_multa","AND","=")
		"""
		sql = self.get()
		data = self.result_list(sql)
		
		print(data)

		return data


	def listall(self):

		self.select('codigo_infracao')
		#self.select('data_termo')
		self.select('peso_infracao')
		self.select('descricao_infracao')
		self.select('codigo_infracao')
		#self.select('data_termo')
		self.select('peso_infracao')
		self.select('descricao_infracao')
		self.select('descricao_infracao')
		
		self.from_table("infracao")
		sql = self.get()
		data = self.result_list(sql)

		return data

	def listar_infracao_filtro(self,busca):

		self.select('codigo_infracao')
		self.select('descricao_infracao')
		
		self.from_table("infracao")
		if busca:
			self.where(busca,"descricao_infracao")
		

		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass
	def listar_infracao_ambulante(self,busca):

		self.select('codigo_infracao')
		self.select('descricao_infracao')
		
		self.from_table("infracao_ambulantes")

		if busca:
			self.where(busca,"descricao_infracao")
			
		sql = self.get()
		data = self.result_list(sql)
		return data

	def listar_empresa_filtro(self,busca):
		
		self.select('nome_permissionario')
		
		self.from_table("empresas_area")
		if busca:
			self.where(busca,"nome_permissionario")
			
		sql = self.get()
		data = self.result_list(sql+" GROUP BY nome_permissionario")
		return data		
		pass

	def listar_local_empresa_filtro(self,busca):
		
		self.select('pavilhao')
		self.select('area_banca')
		
		self.from_table("empresas_area")
		if busca:
			self.where(busca,"nome_permissionario","=")
			
		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass


	def listar_multa(self,busca=None,lista_busca=None , data_inicial=None, data_final=None):
		
		"""
		if busca!=None:
			sql = sql +f"where Nome Like '%{busca}%'"
		"""
	
		self.select('*')
		
		self.from_table(" Cotistas ")
		
		if busca:
			self.where(busca,"Nome")

	
		sql = self.get()
		print(sql)
		data = self.result_list(sql)
		return data
		
		
	def listar_multa_sobe(self,busca=None):
		
		self.select('*')
		

		self.from_table("cadastro_multa")


		sql = self.get()
		
		
		data = self.result_list(sql)
		return data		

	def busca_termo_resumo(self,busca=''):
		#Código -
		#Nome c
		#FisJur c
		#Documento c

		#Endereço c
		#Cidade c 
		#Estado c
		#Cep1 c
		#Cep2 c
		
		#Banco
		#Agencia
		#Conta
		
		#SujeitoIR -
		#CodFolha -
		#Implantado -
		#Pagamento -
		

		self.select('*') # 00
		
		self.from_table("Cotistas")
		if busca!='':

			self.where(busca,"Nome","=")
			
		sql = self.get()
		print(sql)
		data = self.result_list(sql)
		print(data)
		return data



	def busca_norma_resumo(self,busca):
		self.select('peso_infracao')
		self.select('descricao_infracao')

		
		self.from_table("infracao")
		if busca:
			self.where(busca,"codigo_infracao","=")
			
		sql = self.get()
		data = self.result_list(sql)
		return data

		pass
	def busca_norma_resumo_ambulante(self,busca):
		self.select('peso_infracao')
		self.select('descricao_infracao')

		
		self.from_table("infracao_ambulantes")
		if busca:
			self.where(busca,"codigo_infracao","=")
			
		sql = self.get()
		data = self.result_list(sql)
		return data

		pass
	def buscar_reincidencia(self,empresa,infracao,data):
		
		self.select('empresa_multa')
		self.select('infracao_multa')
		self.select('data_multa')
		self.select('status_multa')
		self.select('termo_multa')
		self.select('local_infracao_multa')
		
		self.from_table("cadastro_multa")
		
		self.where(empresa,"empresa_multa","=")
		self.where_combining(infracao,"infracao_multa", "AND", "=")
		self.where_combining("Pendente","status_multa", "AND", "<>")
		self.where_combining("Recurso","status_multa", "AND", "<>")
		
		self.where_combining(data,"data_multa", "AND", "<")
		
		#calculo de 1 ano anterior
		
		data = data.split("-")
		data[0] = str(int(data[0])-1)
		data_ano = "-".join(data)
		
		self.where_combining(data_ano,"data_multa", "AND", ">")

		sql = self.get()
		data = self.result_list(sql)
		return data
	def buscar_reincidencia_historico(self,empresa,infracao,data, status_empresa, status_infracao):
		
		self.select('termo_multa')
		self.select('infracao_multa')		
		self.select('data_multa')

		self.select('empresa_multa')
		self.select('status_multa')
		
		self.select('local_infracao_multa')
		
		self.from_table("cadastro_multa")
		
		self.where("Pendente","status_multa","<>")
	
		if status_empresa:
			self.where_combining(empresa,"empresa_multa","AND","=")
		if status_infracao:
			self.where_combining(infracao,"infracao_multa", "AND", "=")
	
		self.where_combining("Recurso","status_multa", "AND", "<>")
		
		#modificar query para calcular 1 ano
		self.where_combining(data,"data_multa", "AND", "<>")


		sql = self.get()
		data = self.result_list(sql)
		return data


	def calcular_reincidencia(self,reincidencia,peso):
		
		self.select('solucao')
		self.select('qnt_ufesp')
		self.select('valor')

		self.from_table("preco_multas")
		
		self.where(peso,"peso","=")
		self.where_combining(reincidencia,"reincidencia", "AND", "=")

		sql = self.get()
		data = self.result_list(sql)
		return data
		
	def multa_aplicar(self,kwargs):

		data_hoje = date.today()
		kwargs["criado_em_multa"] = str(data_hoje)
		valores=[]
		for x in kwargs.values():
			valores.append(x)

		colunas=[]
		for x in kwargs.keys():
			colunas.append(x)

		self.where( kwargs['termo_multa'] , "termo_multa","=")

		sql = self.setup("cadastro_multa",valores,colunas)
		self.insert(sql)

	def busca_proximo_termo(self):

		self.select('termo_multa')
		self.from_table("cadastro_multa")

		sql = self.get()
		data = self.result_list(sql + " WHERE id=(SELECT max(id) FROM cadastro_multa)")
		return data

	def busca_fiscal(self):

		self.select('nome')
		self.select('matricula')
		self.from_table("cadastro_funcionarios")

		sql = self.get()
		data = self.result_list(sql)
		return data

		pass
	def buscar_dados_exportar(self,data_inicial,data_final , status_concluido, status_pendente,status_cancelado,status_recurso):


		self.select('termo_multa')	
		self.select('infracao_multa')	
		self.select('empresa_multa')
		self.select('status_multa')
		self.select('local_empresa_multa')
		self.select('data_multa')
		self.select('fiscal_multa')
		self.select('data_recebimento_multa')
		self.select('processo_multa')
		
		self.from_table("cadastro_multa")
		if data_inicial:
			self.where(data_inicial,"data_multa",">")
		else:
			self.where("2000-01-01","data_multa",">")


					
		sql = self.get()
		
		data = self.result_list(sql)
		return data		



		pass
	def buscar_usuario(self, login, senha):
		
		self.select('nome')	
		self.select('matricula')	
		self.from_table("cadastro_funcionarios")

		self.where(login,"matricula","=")
		self.where_combining(senha,"senha", "AND", "=")
		
		sql = self.get()
		
		data = self.result_list(sql)
		return data
				
	def buscar_termos(self):

		self.select('termo_multa')
		
		self.from_table("cadastro_multa")

		sql = self.get()
		
		data = self.result_list(sql)
		return data

	def listar_pavilhao(self):
		self.select('grupo_pavilhao')	
		self.from_table("empresas_area")

		sql = self.get()
		
		data = self.result_list(sql+" GROUP BY grupo_pavilhao")
		return data




	def buscar_subpavilhao(self, pavilhao):
		
		self.select('pavilhao')	
		self.from_table("empresas_area")
		
		self.where(pavilhao,"grupo_pavilhao","=")




		sql = self.get()
		
		data = self.result_list(sql+" GROUP BY pavilhao")
		return data

	
	def procurar_busca_empresa(self, busca='',pavilhao=None ,subpavilhao=None ):

		self.select('grupo_pavilhao')	
		self.select('pavilhao')	
		self.select('area_banca')	
		self.select('nome_permissionario')

		self.from_table("empresas_area")
		
		self.where(busca,"nome_permissionario")
		
		if pavilhao != "" and pavilhao != " " and pavilhao != None:
			self.where_combining(pavilhao,"grupo_pavilhao","AND","=")
		
		if subpavilhao != " " and subpavilhao != None:
			self.where_combining(subpavilhao,"pavilhao","AND")
		


		sql = self.get()
		

		data = self.result_list(sql)
		return data


	def emissao_data_aplicar(self,kwargs):


		valores=[]
		for x in kwargs.values():
			valores.append(x)

		colunas=[]
		for x in kwargs.keys():
			colunas.append(x)

		self.where( kwargs['termo_multa'] , "termo_multa","=")

		sql = self.setup("cadastro_multa",valores,colunas)
		self.insert(sql)


	def pos_secme_aplicar(self,kwargs):

		valores=[]
		for x in kwargs.values():
			valores.append(x)

		colunas=[]
		for x in kwargs.keys():
			colunas.append(x)

		self.where( kwargs['termo_multa'] , "termo_multa","=")

		sql = self.setup("cadastro_multa",valores,colunas)
		self.insert(sql)