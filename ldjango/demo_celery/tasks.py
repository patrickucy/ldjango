# coding=utf-8
import time
import subprocess
from celery import shared_task


@shared_task
def send_email(mail):
    print('sending mail ...' + mail['to'])
    time.sleep(3.0)
    print('mail sent.')
    return "rst: mail sent"


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def periodic_update_data():
    print("updating data ...")
    time.sleep(2.0)
    print("updated !")


@shared_task
def run_cmd(cmd):
    print("run cmd ...",  cmd)
    time.sleep(5)
    cmd_obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_rst = cmd_obj.stdout.read().decode("utf-8")
    print(cmd_rst)
    return cmd_rst
