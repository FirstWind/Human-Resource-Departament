from PyQt6 import QtWidgets, QtSql
import sys

app = QtWidgets.QApplication(sys.argv)

conBase = QtSql.QSqlDatabase.addDatabase('QPSQL')
conBase.setHostName('localhost')
conBase.setDatabaseName('work')
conBase.setUserName('postgres')
conBase.setPassword('Wellcome')

def tableSelect(SelectTxt):
    query = QtSql.QSqlQuery()
    query.exec(SelectTxt)
    lst = []
    if query.isActive():
        query.first()
        while query.isValid():
            lst.append(query.value('personal_number') + ': ' + str(query.value('first_name')))
            query.next()
    return lst

conBase.open()
if 'men' in conBase.tables():
    print('Таблица существует')
    for i in tableSelect('select * from men'): print(i)

conBase.close()
