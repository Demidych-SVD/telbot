import config
import csv
from pythonping import ping
#from config import status



def test():
    """Запрашивает весь список серверов и создает отчет"""
    name_file = config.server
    messag = []

    for name, file in name_file.items():
        p = examination_file(name, file)
        messag.append(p)
    return messag


def examination_file(name, file):
    """Проверка доступны ли диски"""
    try:
        try:
            with open(file, 'r') as f:
                # test_file = f.read()
                p = name + '-ok✅'
                return p
        except FileNotFoundError:
            p = name + '-error❌'
            return p
    except OSError:
        p = name + '-❌error❌'
        return p


def ping_serv(ip):
    """Ping"""
    # for ip, name in host.items():
    reports = f"{ping(ip, count=1)}"
    # print(reports)
    report_list = reports.split()
    for report in report_list:
        if report == 'Request':
            r = 'Oflline🔴'
            return r
        else:
            r = 'Online🟢'
            return r


def ping_all_server():
    """ping весь список серверов"""
    servers = config.server_ip
    # print(servers)
    reports = {}
    for name, ip in servers.items():
        # print(name)
        report = ping_serv(ip)
        reports[name] = report
    return reports


def authorization(id, first_name, last_name="off"):
    """Водит список запросов на регистрацию"""
    name = "\n" + str(id) + "," + first_name + " " + last_name
    with open('request.csv', 'a') as f:
        f.write(name)
        return name



def authorized(id):
    """Проверка зарегистрированых пользователей"""
    with open('user.csv', 'r') as f:
        user_list = csv.reader(f)
        for user in user_list:
            if str(id) == user[0]:
                return True


def admin(id):
    """Проверка зарегистрированых пользователей"""
    with open('admin.csv', 'r') as f:
        user_list = csv.reader(f)
        for user in user_list:
            if str(id) == user[0]:
                return True

def loading(file):
    object_list = {}
    with open(file, 'r') as f:
        list = csv.reader(f)
        for objectt in list:
            object_list[objectt[0]]=objectt[1]
        return  object_list

def open_token():
    with open("token.csv", 'r') as f:
        list=f.read()
        return list
