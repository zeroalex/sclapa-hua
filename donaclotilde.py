#!/usr/bin/python
# -*- coding: latin-1 -*-

import sqlite3

class Donaclotilde:
    def __init__(self,):
        self.entrada_select=[]
        self.entrada_count=[]
        self.entrada_from_table=[]
        self.entrada_where=[]
        self.entrada_insert=[]
        self.query=[]
        self.banco_dados=[]

    def connect_db(self):
        #self.conn = sqlite3.connect('‪Z:/DEPEC/SECME/ADMINISTRATIVO/normas/database.db')
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()


    def banco(self, banco):

        self.banco_dados.append(banco)


    def select(self,kwargs):
        data= kwargs

        if type(data) is list:
            for x in data:
                if self.entrada_select:
                    self.entrada_select.append(" , ")
        
                self.entrada_select.append(x)
        else:
            if self.entrada_select:
                self.entrada_select.append(" , ")
            self.entrada_select.append(data)


    def count(self,busca):
        data= busca
        if not self.entrada_count:
            self.entrada_count.append("COUNT(")
        
        if type(data) is list:
            for x in data:
                self.entrada_count.append(x)
            self.entrada_count.append(")")
        else:
            self.entrada_count.append(data)
            self.entrada_count.append(")")

        #count funcionando sozinho tem que arrumar para funcionar junto con select
        #hoje ele imprimi: SELECT data COUNT( data visivel ) FROM autorizacao_debito
        #tem que imprimir: SELECT data, COUNT( data visivel ) FROM autorizacao_debito


    def where(self,busca, coluna, filtro='LIKE'):

        self.entrada_where.append("WHERE")

        self.entrada_where.append(coluna)
        self.entrada_where.append(filtro)
        if filtro=='LIKE':
            self.entrada_where.append('"%'+busca+'%"')
        else:
            self.entrada_where.append('"'+busca+'"')
    def where_combining(self, busca, coluna, operator, filtro='LIKE'):
        
        self.entrada_where.append(operator)
        self.entrada_where.append(coluna)
        self.entrada_where.append(filtro)
        if filtro=='LIKE':
            self.entrada_where.append('"%'+busca+'%"')
        else:
            self.entrada_where.append('"'+busca+'"')
        


    def from_table(self,kwargs):
        data= kwargs
        if not self.entrada_from_table:
            self.entrada_from_table.append("FROM")
        
        if type(data) is list:
            for x in data:
                self.entrada_from_table.append(x)
        else:
            self.entrada_from_table.append(data)


    def result_list(self,kwargs):
        sql = kwargs
        
        self.connect_db()

        self.cursor.execute(sql)
        dados=self.cursor.fetchall()
        self.conn.close()
        
        
        lista = []
        for dado in dados:
            iten = list(dado)
            if type(iten[0]) is int:
                iten[0]= str(iten[0])
            lista.append(iten)
                
        return lista
    def result_first(self,kwargs):

        sql = kwargs
        self.connect_db()
        
        self.cursor.execute(sql)
        dado=self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        
            
        return dado
    def limit(self,kwargs):
        #falta
        pass
    def order(self,kwargs):
        #escrever se é crescente ou decresente


        pass

        
    def result_dict(self,kwargs):
        sql = kwargs
        self.connect_db()
        self.cursor.execute(sql)
        dados=self.cursor.fetchall()
        self.conn.close()

        return dados
    

    def get(self):
        self.query.append("SELECT")
        if self.entrada_select:
            for x in self.entrada_select:
                self.query.append(x)
        if self.entrada_count:
            if self.entrada_select:
                self.query.append(" , ")
            for x in self.entrada_count:
                self.query.append(x)

        if self.entrada_from_table:
            for x in self.entrada_from_table:
                self.query.append(x)
        data = self.query
        if self.entrada_where:
            for x in self.entrada_where:
                self.query.append(x)
        data = self.query

        self.entrada_select=[]
        self.entrada_count=[]
        self.entrada_from_table=[]
        self.entrada_insert=[]
        self.entrada_where=[]
        self.query=[]
        self.banco_dados=[]
        
        sql=self.turn_sql_string(data)
            
        return sql

    def set(self,tabela,valores,colunas):
        
        self.entrada_insert.append("INSERT INTO")
        
        self.entrada_insert.append(tabela)
        self.entrada_insert.append("(")
        
        for x in colunas:
            self.entrada_insert.append(x)
            self.entrada_insert.append(" , ")
        self.entrada_insert.pop()
        self.entrada_insert.append(")")

        self.entrada_insert.append("VALUES")
        self.entrada_insert.append("(")
        
        for x in valores:
            self.entrada_insert.append(' "'+x+'" ')
            self.entrada_insert.append(" , ")
        self.entrada_insert.pop()
    
        self.entrada_insert.append(")")


        data = self.entrada_insert

        self.entrada_select=[]
        self.entrada_from_table=[]
        self.entrada_insert=[]
        self.entrada_where=[]
        self.query=[]
        
        sql=self.turn_sql_string(data)
        return sql
    def setup(self,tabela,valores,colunas):
        
        self.entrada_insert.append("UPDATE")
        
        self.entrada_insert.append(tabela)
        self.entrada_insert.append("SET")
        self.entrada_insert.append("(")
        
        for x in colunas:
            self.entrada_insert.append(' "'+x+'" ')
            self.entrada_insert.append(" , ")
        self.entrada_insert.pop()
        self.entrada_insert.append(")")

        self.entrada_insert.append("=")
        self.entrada_insert.append("(")
        
        for x in valores:
            self.entrada_insert.append(' "'+x+'" ')
            self.entrada_insert.append(" , ")
        self.entrada_insert.pop()
    
        self.entrada_insert.append(")")

        if self.entrada_where:
        
            for x in self.entrada_where:
                self.entrada_insert.append(x)
        


        data = self.entrada_insert

        self.entrada_select=[]
        self.entrada_from_table=[]
        self.entrada_insert=[]
        self.entrada_where=[]
        self.query=[]
        
        sql=self.turn_sql_string(data)
        return sql
        
        
    def insert(self,kwargs):
        sql=kwargs
        self.connect_db()
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()
    def update(self,kwargs):
        sql=kwargs
        self.connect_db()
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

        
    def turn_sql_string(self,kwargs):
        sql=''
        for palavra in kwargs:
            sql=sql+" "+palavra
        return sql