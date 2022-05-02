from msilib.schema import Error
from flask import Flask, request, jsonify, json, Response
import pymysql
import logging as log

from sqlalchemy import null
from config import *

class Database: 
    def connect():
        db = pymysql.connect(
            database=BDD_NAME,
            port=BDD_PORT,
            host=BDD_HOST, 
            user=BDD_PASS, 
            password=BDD_PASS, 
            ssl_disabled= True)
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')              
        print("Connexion réussie")
        return db
    
    def disconect():
        return