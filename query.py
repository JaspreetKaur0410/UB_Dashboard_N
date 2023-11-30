import streamlit as st
from all_queries import *
import pymysql
import sys
import boto3
import os
import pymysql.cursors

# connecting multtiple databases
from config import dbConfig


class DB:
    def __init__(self):
        try:
            self.params=dbConfig('RDS')
            self.paramsazure=dbConfig('AZURE')
            self.conn1=pymysql.connect(**self.params)
            self.conn2=pymysql.connect(**self.paramsazure)
            self.cursor1=self.conn1.cursor()
            self.cursor2=self.conn2.cursor()
            print(self.conn1)
            print(self.conn2)
        except (Exception, pymysql.OperationalError) as sqlerrors:
            print("EXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXCEEEEEEEEEEEEEEEEEEEPPTIIIIIIIIIIIIIIIIIIOOOONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNn")
            print("Exception Raised", sqlerrors)
        finally:
            pass
            
    def query(self, sql):
        try:
            # cursor1 = self.conn1.cursor(buffered=True)
            self.cursor1.execute(sql)
            desc = self.cursor1.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row)) for row in self.cursor1.fetchall()]
            return query_results
        except Exception:
            # if the connection was lost, then it reconnects
            self.conn1.ping(reconnect=True) 
            # cursor1 = self.conn1.cursor(buffered=True)
            self.cursor1.execute(sql)
            desc = self.cursor1.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row)) for row in self.cursor1.fetchall()]
            return query_results
        finally:
            # if the connection was lost, then it reconnects
            self.conn1.ping(reconnect=True) 
            # cursor1 = self.conn1.cursor()
            self.cursor1.execute(sql)
            desc = self.cursor1.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row)) for row in self.cursor1.fetchall()]
            return query_results

    def query_azure(self, sql):
         try:
             # cursor2 = self.conn2.cursor()
             self.cursor2.execute(sql)
             desc = self.cursor2.description
             column_names = [col[0] for col in desc]
             query_results = [dict(zip(column_names, row)) for row in self.cursor2.fetchall()]
             return query_results
         except Exception:
             # if the connection was lost, then it reconnects
             self.conn2.ping(reconnect=True) 
             # cursor2 = self.conn2.cursor()
             self.cursor2.execute(sql)
             desc = self.cursor2.description
             column_names = [col[0] for col in desc]
             query_results = [dict(zip(column_names, row)) for row in self.cursor2.fetchall()]
             return query_results
         finally:
             # if the connection was lost, then it reconnects
             self.conn2.ping(reconnect=True) 
             # cursor2 = self.conn2.cursor()
             self.cursor2.execute(sql)
             desc = self.cursor2.description
             column_names = [col[0] for col in desc]
             query_results = [dict(zip(column_names, row)) for row in self.cursor2.fetchall()]
             return query_results


db = DB()

def view_all_data():
    query_results=db.query('''select age,location,gender,reason,source_type,skin_type,product_type,product_name,best_match from master_recomm order by id asc''')
    return query_results
    
def people_count_skin_type_age_groups():
    query_results=db.query(query_get_skintype_age)
    return query_results
    
# FAVOURITES  
def query_get_fav_cleanser():
    query_results=db.query(query_fav_cleanser)
    return query_results
     
def query_get_fav_mosturiser():
    query_results=db.query(query_fav_mosturiser)
    return query_results
    
def query_get_fav_sunscreen():
    query_results=db.query(query_fav_sunscreen)
    return query_results

def get_top5_cleanser_count_dry_skin():
    query_results=db.query(query_get_top5_cleanser_count_dry_skin)
    return query_results

def get_top5_cleanser_count_oily_skin():
    query_results=db.query(query_get_top5_cleanser_count_oily_skin)
    return query_results
     
def get_top5_cleanser_count_Combination_skin():
    query_results=db.query(query_get_top5_cleanser_count_Combination_skin)
    return query_results

def get_count_products_for_brand():
    query_results=db.query_azure(query_count_products_for_brand)
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    return query_results

def get_highest_price_by_brand():
    query_results=db.query_azure(query_highest_price_by_brand)
    return query_results

def get_people_count_by_brand():
    query_results=db.query_azure(query_people_count_by_brand)
    return query_results

def get_purchase_count_by_store():
    query_results=db.query_azure(query_purchase_count_by_store)
    return query_results

def get_shopmost_by_brand():
    query_results=db.query_azure(query_shopmost_by_brand)
    return query_results

def get_recommended_count():
    query_results=db.query_azure(query_recommended_count)
    return query_results

def get_most_recommended():
    query_results=db.query_azure(query_most_recommended)
    return query_results

def get_socialmedia_influencer_recomm():
    query_results=db.query_azure(query_socialmedia_influencer_recomm)
    return query_results


def get_users_data_filters():
    query_results=db.query_azure(query_users_data_filters)
    return query_results




