import os
import sys
import logging


import eel
import pandas as pd


from item_order import Order, Item, add_item_master_by_csv
import desktop


ITEM_MASTER_CSV_PATH = './masta.csv'
DIRECTORY = 'html'
FILE_NAME = 'index.html'
SIZE = (700,600)

logging.basicConfig(filename='./log/logger.log', level=logging.INFO)



def main():
    # jsから呼び出す関数の定義
    @eel.expose
    def return_product_detail(item_code): # 商品コードを引数に商品情報を返す
        item_name, price = order.get_item_data(item_code)
        return f'商品コード:{item_code}\n商品名:{item_name}\n価格:¥{price}'

    @eel.expose
    def return_total_price(item_code, quantity): # 合計金額を返す
        return f'合計金額:¥{order.total_price(item_code, quantity)}'


    @eel.expose
    def return_change_money(amount_custody): # お釣りを計算して返す
        change = order.change_money(amount_custody)
        return change



    # マスタをオーダーに登録
    item_master=add_item_master_by_csv(ITEM_MASTER_CSV_PATH)
    order=Order(item_master) 
    logging.info('マスタをオーダーに登録しました')
    
    # デスクトップ起動
    logging.info('デスクトップを起動します')
    desktop.start(DIRECTORY, FILE_NAME, SIZE)
    


if __name__ == '__main__':
    main()
    


    


    




 










