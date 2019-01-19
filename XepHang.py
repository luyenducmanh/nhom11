<<<<<<< HEAD
from markov.M_M_1 import M_M_1
from markov.M_M_1_K import M_M_1_K
from markov.M_M_S import M_M_S
from markov.M_M_S_K import M_M_S_K
import os
import sys

clear = lambda: os.system('cls')

def display_M_M_1():
    print("Mô hình hàng đợi một kênh phục vụ")
    try:
        x = float(input("Số lượng khách hàng đến trung bình:"))
        y = float(input("Số lượng khác được phục vụ trung bình:"))
    except BaseException:
        clear()
        print("Invalid")
        display_M_M_1()
    
    mar = M_M_1(x,y)
    print("Số khách hàng trung bình trong hệ thống: " + str(mar.L()))
    print("Số khách hàng trung bình trong hàng chờ: " + str(mar.Lq()))
    print("Thời gian phục vụ2 trung bình: "+ str(mar.W()))
    print("Thời gian chờ trung bình: "+ str(mar.Wq()))
    print("Hiệu suất phục vụ của hệ thống: "+ str(mar.P()))
    input()
    print("1. Tiếp tục")
    print("2. Trở lại")
    i = input()
    if i == '1':
       clear()
       display_M_M_1()
    elif i == '2':
        clear()
        displayMenu()

def display_M_M_s():
    print("Mô hình hàng đợi nhiều kênh phục vụ")
    try:
        s = float(input("Số kênh:"))
        x = float(input("Số lượng khách hàng đến trung bình:"))
        y = float(input("Số lượng khác đươcj phục vụ trung bình:"))
    except BaseException:
        clear()
        print("Invalid")
        display_M_M_s()
    
    mar = M_M_S(s,x,y)
    print("Số khách hàng trung bình trong hệ thống: " + str(mar.L()))
    print("Số khách hàng trung bình trong hàng chờ: " + str(mar.Lq()))
    print("Thời gian phục trung bình: "+ str(mar.W()))
    print("Thời gian chờ trung bình: "+ str(mar.Wq()))
    print("Hiệu suất phục vụ của hệ thống: "+ str(mar.P()))
    input()
    print("1. Tiếp tục")
    print("2. Trở lại")
    i = input()
    if i == '1':
       clear()
       display_M_M_s()
    elif i == '2':
        clear()
        displayMenu()
        
def display_M_M_1_k():
    print("Mô hình hàng đợi giới hạn kích thước một kênh phục vụ")
    try:
        x = float(input("So khach hang den trung binh:"))
        y = float(input("So khach hang duoc phuc trung binh:"))
        k = float(input("Gioi han khach hang trong hang doi:"))
    except BaseException:
        clear()
        print("Invalid")
        display_M_M_1_k()
        
    mar = M_M_1_K(x,y,k)
    print("Số khách hàng trung bình trong hệ thống: " + str(mar.L()))
    print("Số khách hàng trung bình trong hàng chờ: " + str(mar.Lq()))
    print("Thời gian phục trung bình: "+ str(mar.W()))
    print("Thời gian chờ trung bình: "+ str(mar.Wq()))
    print("Hiệu suất phục vụ của hệ thống: "+ str(mar.P()))
    input()
    print("1. Tiếp tục")
    print("2. Trở lại")
    i = input()
    if i == '1':
       clear()
       display_M_M_1_k()
    elif i == '2':
        clear()
        displayMenu()

def display_M_M_s_k():
    print("Mô hình hàng đợi giới hạn kích thước nhiều kênh phục vụ")
    try:
        s = float(input("So kenh phuc vu:"))
        x = float(input("So khach hang den trung binh:"))
        y = float(input("So khach hang duoc phuc trung binh:"))
        k = float(input("Gioi han khach hang trong hang doi:"))
    except BaseException:
        clear()
        print("Invalid")
        display_M_M_s_k()
        
    mar = M_M_S_K(s,x,y,k)
    print("Số khách hàng trung bình trong hệ thống: " + str(mar.L()))
    print("Số khách hàng trung bình trong hàng chờ: " + str(mar.Lq()))
    print("Thời gian phục trung bình: "+ str(mar.W()))
    print("Thời gian chờ trung bình: "+ str(mar.Wq()))
    print("Hiệu suất phục vụ của hệ thống: "+ str(mar.P()))
    input()
    print("1. Tiếp tục")
    print("2. Trở lại")
    i = input()
    if i == '1':
       clear()
       display_M_M_s_k()
    elif i == '2':
        clear()
        displayMenu()

def displayMenu():
    print("Chọn 1 trong các mô hình sau:")
    print("1. M/M/1")
    print("2. M/M/c")
    print("3. M/M/1/k")
    print("4. Thoát")
    x = input()
    if(x == '1'):
        clear()
        display_M_M_1()
    elif x == '2':
        clear()
        display_M_M_s()
    elif x == '3':
        clear()
        display_M_M_1_k()
    elif x == '4': 
        sys.exit
    else :
        clear()
        displayMenu()

displayMenu()



=======
from markov.M_M_1 import M_M_1
from markov.M_M_1_K import M_M_1_K
from markov.M_M_S import M_M_S
from markov.M_M_S_K import M_M_S_K
import os
import sys

clear = lambda: os.system('cls')

def display_M_M_1():
    print("Mô hình hàng đợi một kênh phục vụ")
    try:
        x = float(input("Số lượng khách hàng đến trung bình:"))
        y = float(input("Số lượng khác được phục vụ trung bình:"))
    except BaseException:
        clear()
        print("Invalid")
        display_M_M_1()
    
    mar = M_M_1(x,y)
    print("Số khách hàng trung bình trong hệ thống: " + str(mar.L()))
    print("Số khách hàng trung bình trong hàng chờ: " + str(mar.Lq()))
    print("Thời gian phục vụ2 trung bình: "+ str(mar.W()))
    print("Thời gian chờ trung bình: "+ str(mar.Wq()))
    print("Hiệu suất phục vụ của hệ thống: "+ str(mar.P()))
    input()
    print("1. Tiếp tục")
    print("2. Trở lại")
    i = input()
    if i == '1':
       clear()
       display_M_M_1()
    elif i == '2':
        clear()
        displayMenu()

def display_M_M_s():
    print("Mô hình hàng đợi nhiều kênh phục vụ")
    try:
        s = float(input("Số kênh:"))
        x = float(input("Số lượng khách hàng đến trung bình:"))
        y = float(input("Số lượng khác đươcj phục vụ trung bình:"))
    except BaseException:
        clear()
        print("Invalid")
        display_M_M_s()
    
    mar = M_M_S(s,x,y)
    print("Số khách hàng trung bình trong hệ thống: " + str(mar.L()))
    print("Số khách hàng trung bình trong hàng chờ: " + str(mar.Lq()))
    print("Thời gian phục trung bình: "+ str(mar.W()))
    print("Thời gian chờ trung bình: "+ str(mar.Wq()))
    print("Hiệu suất phục vụ của hệ thống: "+ str(mar.P()))
    input()
    print("1. Tiếp tục")
    print("2. Trở lại")
    i = input()
    if i == '1':
       clear()
       display_M_M_s()
    elif i == '2':
        clear()
        displayMenu()
        
def display_M_M_1_k():
    print("Mô hình hàng đợi giới hạn kích thước một kênh phục vụ")
    try:
        x = float(input("So khach hang den trung binh:"))
        y = float(input("So khach hang duoc phuc trung binh:"))
        k = float(input("Gioi han khach hang trong hang doi:"))
    except BaseException:
        clear()
        print("Invalid")
        display_M_M_1_k()
        
    mar = M_M_1_K(x,y,k)
    print("Số khách hàng trung bình trong hệ thống: " + str(mar.L()))
    print("Số khách hàng trung bình trong hàng chờ: " + str(mar.Lq()))
    print("Thời gian phục trung bình: "+ str(mar.W()))
    print("Thời gian chờ trung bình: "+ str(mar.Wq()))
    print("Hiệu suất phục vụ của hệ thống: "+ str(mar.P()))
    input()
    print("1. Tiếp tục")
    print("2. Trở lại")
    i = input()
    if i == '1':
       clear()
       display_M_M_1_k()
    elif i == '2':
        clear()
        displayMenu()

def display_M_M_s_k():
    print("Mô hình hàng đợi giới hạn kích thước nhiều kênh phục vụ")
    try:
        s = float(input("So kenh phuc vu:"))
        x = float(input("So khach hang den trung binh:"))
        y = float(input("So khach hang duoc phuc trung binh:"))
        k = float(input("Gioi han khach hang trong hang doi:"))
    except BaseException:
        clear()
        print("Invalid")
        display_M_M_s_k()
        
    mar = M_M_S_K(s,x,y,k)
    print("Số khách hàng trung bình trong hệ thống: " + str(mar.L()))
    print("Số khách hàng trung bình trong hàng chờ: " + str(mar.Lq()))
    print("Thời gian phục trung bình: "+ str(mar.W()))
    print("Thời gian chờ trung bình: "+ str(mar.Wq()))
    print("Hiệu suất phục vụ của hệ thống: "+ str(mar.P()))
    input()
    print("1. Tiếp tục")
    print("2. Trở lại")
    i = input()
    if i == '1':
       clear()
       display_M_M_s_k()
    elif i == '2':
        clear()
        displayMenu()

def displayMenu():
    print("Chọn 1 trong các mô hình sau:")
    print("1. M/M/1")
    print("2. M/M/c")
    print("3. M/M/1/k")
    print("4. Thoát")
    x = input()
    if(x == '1'):
        clear()
        display_M_M_1()
    elif x == '2':
        clear()
        display_M_M_s()
    elif x == '3':
        clear()
        display_M_M_1_k()
    elif x == '4': 
        sys.exit
    else :
        clear()
        displayMenu()

displayMenu()



>>>>>>> 760338ccb5a931cd4ad5b70878693fd208d22ace
