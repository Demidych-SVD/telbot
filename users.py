#import io
#import telnetlib
#import os
#from csv import reader

#import pythonping
import config
import csv



def ban(id, first_name, last_name):
    """Проверка и внесение новых банов"""
    ban = examination_ban(id)
    name = first_name + " " + last_name
    if ban == True:
        return
    else:
        ban_list = '\n' + str(id) + "," + name
        with open('ban.csv', 'a') as f:
            f.write(str(ban_list), )
            print(ban_list)


def open_ban_list():
    """Открыте бан листа"""
    with open('ban.csv', 'r') as f:
        bane = csv.reader(f)
        id_bam = []
        for id_user in bane:
            id_bam.append(id_user[0])

    return id_bam


def examination_ban(id):
    """Проверка id и бан-листа"""
    id_ban = open_ban_list()
    for id_bane in id_ban:
        if str(id) == id_bane:
            return True


def users(id):
    """Проверка запросов"""
    if admins(id) == True:
        userss=[]
        with open('request.csv', 'r') as f:
            users_list = csv.reader(f)
            for user in users_list:
                userss.append(user)
            return userss


def admins(id):
    """Проверка админа"""
    with open('admin.csv', 'r') as f:
        administratirs= csv.reader(f)
        for admin in administratirs:
            if str(id) == admin[0]:
                return True


def add_user(id):
    """Добавление пользователя"""
    with open('request.csv', 'r') as f:
        users_list = csv.reader(f)
        for user in users_list:
            if user[0] == str(id):
                user_id = user[0]
                user_name = user[1]
                user_ful = "\n" + user_id + ":" + user_name
                with open('user.csv', 'a') as f:
                    f.write(str(user_ful))