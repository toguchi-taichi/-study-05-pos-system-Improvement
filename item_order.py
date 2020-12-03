import pandas as pd
import sys
import datetime

ITEM_MASTER_CSV_PATH="./item_master.csv"
RECEIPT_FOLDER="./receipt"


class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price


class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_count_list=[]
        self.item_master=item_master
        self.set_datetime()
        
        
    def set_datetime(self):
        self.datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
    def add_item_order(self,item_code,item_count):
        self.item_order_list.append(item_code)
        self.item_count_list.append(item_count)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))
            
    
    def get_item_data(self,item_code):
        for m in self.item_master:
            if item_code==m.item_code:
                return m.item_name,m.price
    
    
    
    def change_money(self, amount_custody):
        print('お釣りの計算をします')
        print(self.total_fee)
        self.change_money = int(amount_custody) - self.total_fee #おつり
        if self.change_money>=0:
            self.write_receipt("お預り金:￥{}".format(amount_custody))
            return self.write_receipt("お釣り：￥{}".format(self.change_money))
        else:
            print("￥{}　不足しています。再度入力してください".format(self.change_money))
            return "￥{}　不足しています。再度入力してください".format(self.change_money)
            
        print("お買い上げありがとうございました！")
            
    def write_receipt(self,text):
        print(text)
        with open(RECEIPT_FOLDER + "/" + self.datetime, mode="a", encoding="utf-8_sig") as f:
            f.write(text+"\n") 
        return text
            
    def total_price(self, item_code, quanty): # 合計金額の取得
        item_name, item_price = self.get_item_data(item_code)
        self.total_fee = int(item_price) * int(quanty)
        return self.total_fee    
        

def add_item_master_by_csv(csv_path):
    print("------- マスタ登録開始 ---------")
    item_master=[]
    count=0
    try:
        item_master_df=pd.read_csv(csv_path,dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
        for item_code,item_name,price in zip(list(item_master_df["item_code"]),list(item_master_df["item_name"]),list(item_master_df["price"])):
            item_master.append(Item(item_code,item_name,price))
            print("{}({})".format(item_name,item_code))
            count+=1
        print("{}品の登録を完了しました。".format(count))
        print("------- マスタ登録完了 ---------")
        return item_master
    except:
        print("マスタ登録が失敗しました")
        print("------- マスタ登録完了 ---------")
        sys.exit()
        



