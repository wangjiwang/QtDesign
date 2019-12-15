import bit
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from bit.network import NetworkAPI
from bit.transaction import calc_txid

class MyWinClass(QMainWindow):

    def __init__(self):
        super().__init__()
        win = uic.loadUi("bitcoin_alpha.ui", self)
        win.show()
        self.ButtonForUser.clicked.connect(self.create_user_testnet)
        self.ButtonForUserReal.clicked.connect(self.create_user)
        self.pushButton.clicked.connect(self.get_account_testnet)
        self.pushButton_real.clicked.connect(self.get_account)
        self.transport.clicked.connect(self.transport_bit)

    def create_user_testnet(self):

        key = bit.PrivateKeyTestnet()
        self.lineEdit_create_user.setText(key.address)
        print(key.address)
    def create_user(self):
        key = bit.PrivateKey()
        self.lineEdit_create_user_real.setText(key.address)
        print(key.address)


    def transport_bit(self):
        keyB_address = 'msQg1x6qkfY95uuSVbYjB7nAXqvRoMNEvF'
        # 交易信息
        tx_data = bit.PrivateKeyTestnet.prepare_transaction(
            unspents=key.get_unspents(),
            outputs=[(keyB_address, 100, 'satoshi')],
            leftover=key.address,
            address=None
        )
        tx_signed = key.sign_transaction(tx_data)
        # 发送交易信息
        NetworkAPI.broadcast_tx_testnet(tx_signed)

        # 交易编号
        calc_txid(tx_signed)

    def get_account_testnet(self):
        # 查询时界面设置
        self.label_2.setText( '查询中......' )
        self.pushButton.setEnabled(False)
        self.treeWidget.setHidden(True)

        # 网络查询余额
        addr = self.lineEdit.text()
        unspents = NetworkAPI.get_unspent_testnet(addr)

        # 查询后界面展现
        self.pushButton.setEnabled(True)
        if len(unspents)==0:
            self.label_2.setText( '<html><head/><body><p><span style=" color:#00aa00;">0</span></p></body></html>' )
        else:
            self.treeWidget.clear()
            self.treeWidget.setHidden(False)
            s=sum(unspent.amount for unspent in unspents)
            self.label_2.setText( '<html><head/><body><p><span style=" color:#00aa00;">%d</span></p></body></html>'%(s) )
            for utxo in unspents:
                root=QTreeWidgetItem(self.treeWidget)
                root.setText(0,'amount')
                root.setText(1,str(utxo.amount))
                txid = QTreeWidgetItem(root)
                txid.setText(0,'txid')
                txid.setText(1,utxo.txid)
                txindex = QTreeWidgetItem(root)
                txindex.setText(0,'txindex')
                txindex.setText(1,str(utxo.txindex))
                script = QTreeWidgetItem(root)
                script.setText(0,'script')
                script.setText(1,utxo.script)
                confirmations = QTreeWidgetItem(root)
                confirmations.setText(0,'confirmations')
                confirmations.setText(1,str(utxo.confirmations))
                segwit = QTreeWidgetItem(root)
                segwit.setText(0,'segwit')
                segwit.setText(1,str(utxo.segwit))

    def get_account(self):
        # 查询时界面设置
        self.label_23.setText( '查询中......' )
        self.pushButton_real.setEnabled(False)
        self.treeWidget_4.setHidden(True)

        # 网络查询余额
        addr = self.lineEdit_4.text()
        unspents = NetworkAPI.get_unspent(addr)

        # 查询后界面展现
        self.pushButton_real.setEnabled(True)
        if len(unspents)==0:
            self.label_23.setText( '<html><head/><body><p><span style=" color:#00aa00;">0</span></p></body></html>' )
        else:
            self.treeWidget_4.clear()
            self.treeWidget_4.setHidden(False)
            s=sum(unspent.amount for unspent in unspents)
            self.label_23.setText( '<html><head/><body><p><span style=" color:#00aa00;">%d</span></p></body></html>'%(s) )
            for utxo in unspents:
                root=QTreeWidgetItem(self.treeWidget_4)
                root.setText(0,'amount')
                root.setText(1,str(utxo.amount))
                txid = QTreeWidgetItem(root)
                txid.setText(0,'txid')
                txid.setText(1,utxo.txid)
                txindex = QTreeWidgetItem(root)
                txindex.setText(0,'txindex')
                txindex.setText(1,str(utxo.txindex))
                script = QTreeWidgetItem(root)
                script.setText(0,'script')
                script.setText(1,utxo.script)
                confirmations = QTreeWidgetItem(root)
                confirmations.setText(0,'confirmations')
                confirmations.setText(1,str(utxo.confirmations))
                segwit = QTreeWidgetItem(root)
                segwit.setText(0,'segwit')
                segwit.setText(1,str(utxo.segwit))

app = QApplication([])
myWin = MyWinClass()

app.exec_()