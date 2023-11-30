import streamlit as st
from all_queries import *
import pymysql
import sys
import boto3
import os
import pymysql.cursors

# connecting multtiple databases
from config import dbConfig


class DBAzure:
    def __init__(self):
        try:
            self.params=dbConfig('AZURE')
            print(self.params)
            self.conn=pymysql.connect(**self.params)
            print(self.conn)
        except (Exception, pymysql.OperationalError) as sqlerrors:
            print("Exception Raised", sqlerrors)
        finally:
            self.conn.ping(reconnect=True)

    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row)) for row in cursor.fetchall()]
            return query_results
        except pymysql.OperationalError:
            # if the connection was lost, then it reconnects
            self.conn.ping(reconnect=True) 
            cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row)) for row in cursor.fetchall()]
            return query_results
        finally:
            # if the connection was lost, then it reconnects
            self.conn.ping(reconnect=True) 
            cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row)) for row in cursor.fetchall()]
            return query_results


db = DBAzure()
