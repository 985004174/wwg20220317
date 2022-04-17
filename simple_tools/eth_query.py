# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/11 9:18 PM 
# ide： PyCharm
# from web3 import Web3, HTTPProvider
#
# address = '0x1244f6037E541A3756209faDc51FCf416F57EAe7'
# rpc = 'https://bsc-dataseed1.binance.org:443'
#
# web3 = Web3(HTTPProvider(rpc))
# balance = web3.fromWei(web3.eth.getBalance(address), "ether")
# print(balance)

from web3 import Web3
w3= Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/fec0748419764975a7aba0627a8f0a24'))
w3.isConnected()
# w3.eth.get_block('latest')

w3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
w3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
a=w3.fromWei(w3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e'), 'ether')
print(a)