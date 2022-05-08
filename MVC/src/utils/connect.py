from msilib.schema import Error
from flask import Flask, request, jsonify, json, Response
import pymysql
import logging as log

from sqlalchemy import null
from config import *
from config import Conf

class Database: 
    def connect():
        db = pymysql.connect(
            database=Conf.BDD_NAME,
            port=Conf.BDD_PORT,
            host=Conf.BDD_HOST, 
            user=Conf.BDD_USER, 
            password=Conf.BDD_PASS, 
            ssl_disabled= True)
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')              
        print("Connexion réussie")
        return db
    
    def disconect():
        return
