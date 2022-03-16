# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 00:22:17 2022

@author: Wissem
"""

import art
import os
import req

Owner = {
    "income":0    
}

state = {
    "Water":300,
    "Milk":200,
    "Coffee":100,
    "Money":0,
    "CAPPUCCINO":0,
    "LATTE":0,
    "ESPRESSO":0
}

admins = ["132","465","798"]
workers = ["JustMe"]

def stat():
    print("You have sold : ")
    print("[",state["CAPPUCCINO"],"] CAPPUCCINO")
    print("[",state["LATTE"],"] LATTE")
    print("[",state["ESPRESSO"],"] ESPRESSO")
    tot = state["CAPPUCCINO"] + state["LATTE"] + state["ESPRESSO"]
    best_sell = "ESPRESSO"
    if state["LATTE"] > state[best_sell]:
        best_sell = "LATTE"
    if state["CAPPUCCINO"] > state[best_sell]:
        best_sell = "CAPPUCCINO"
    if tot :
        print("Focus on ",best_sell,".Customers love this product !")
        

def Available(name):
    for i in range(len(req.REQ)):
        if req.REQ[i]["Name"] == name:
            break
    if req.REQ[i]["Water"]<=state["Water"] :
        if req.REQ[i]["Milk"]<=state["Milk"] :
            if req.REQ[i]["Coffee"]<=state["Coffee"] :
                return True
            else: 
                print("Sorry there is no enough Coffee")
        else: 
            print("Sorry there is no enough Milk")
    else: 
        print("Sorry there is no enough Water")
    return False
    
def insert_coin():
    print("INSERT A COIN : (ONLY USE 2 DT COINS)")
    while(True):
        coin = int(input("DT : "))
        if coin == 2 :
            return coin
        else:
            print("INVALID COIN USED")

def receipt(ind):
    print("----MW COFFEE MACHINE----")
    print("Product : ",req.REQ[ind]["Name"])
    print("Money inserted : 2DT")
    print("Product Price : ",req.REQ[ind]["Money"])
    print("Change : ",change(req.REQ[ind]["Name"]))
    print("Hope you like what we do !")
    print("Support Us on : https://github.com/wissemmtiri")
    print("-------------------------\n")
    
def process(name):
    for i in range(len(req.REQ)):
        if req.REQ[i]["Name"] == name:
            break
    state["Water"] -= req.REQ[i]["Water"]
    state["Milk"] -= req.REQ[i]["Milk"]
    state["Coffee"] -= req.REQ[i]["Coffee"]
    state["Money"] += req.REQ[i]["Money"]
    receipt(i)
    state[req.REQ[i]["Name"]] += 1
    
def change(name):
    for i in range(len(req.REQ)):
        if req.REQ[i]["Name"] == name:
            break
    return(2-req.REQ[i]["Money"])

def espresso():
    if Available("ESPRESSO"):
        coin = insert_coin()
        process("ESPRESSO")
        print("HERE IS YOUR CHANGE : ",change("ESPRESSO")," DT")
    else:
        print("DRINK UNAVAILABLE. Try Later")
    input()
    os.system('cls')
    Menu()


def latte():
    if Available("LATTE"):
        coin = insert_coin()
        process("LATTE")
        print("HERE IS YOUR CHANGE : ",change("LATTE")," DT")
    else:
        print("DRINK UNAVAILABLE. Try Later")
    input()
    os.system('cls')
    Menu()

def cappuccino():
    if Available("CAPPUCCINO"):
        coin = insert_coin()
        process("CAPPUCCINO")
        print("HERE IS YOUR CHANGE : ",change("CAPPUCCINO")," DT")
    else:
        print("DRINK UNAVAILABLE. Try Later")
    input()
    os.system('cls')
    Menu()
    
def report():
    os.system('cls')
    print("ARE YOU AN ADMIN ?")
    id_admin = input("TYPE YOUR IDENTIFIER : #")
    if (id_admin in admins):
        print("\n----MW COFFEE MACHINE----")
        print("Water :",state["Water"],"ml")
        print("Milk :",state["Milk"],"ml")
        print("Coffee :",state["Coffee"],"g")
        print("Money : ",state["Money"]," DT")
        stat()
        print("-------------------------\n")
    else:
        print("UNAVAILABLE COMMAND !")
    input()
    os.system('cls')
    Menu()

def recharge():
    os.system('cls')
    id_rech = input("YOUR IDENTIFIER PLEASE : #")
    if id_rech in workers:
        water = int(input("Water : "))
        Milk = int(input("Milk : "))
        Coffee = int(input("Coffee : "))
        state["Water"] += water
        state["Milk"] += Milk
        state["Coffee"] += Coffee
        print("Done")
        collect = input("Do you want to collect today's income ? Y|N : ")
        if collect == "Y" :
            Owner["income"] += state["Money"]
            state["Money"] = 0
            print("DONE")
    else:
        print("UNAUTHORIZED ACCESS")
    input()
    os.system('cls')
    Menu()
        
def Menu():
    print(art.logo)
    print("               WHAT WOULD YOU LIKE ?")
    print("        [1] ESPRESSO")
    print("        [2] LATTE")
    print("        [3] CAPPUCCINO")
    print("        [OFF] : TURN OFF")
    print("        [REPORT] : TAKE A REPORT")
    print("        [RECHARGE] : RECHARGE RESSOURCES")
    while(True):
        choice = input("==> ")
        if choice == "1":
            espresso()
            break
        elif choice == "2":
            latte()
            break
        elif choice == "3":
            cappuccino()
            break
        elif choice == "OFF":
            exit(1)
        elif choice == "REPORT":
            report()
            break
        elif choice == "RECHARGE":
            recharge()
            break
        else:
            print("INVALID INPUT. Try Again")

Menu()