from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser
import mysql.connector

banco=  mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database= 'planusfit',
 )

def cadastro():
     cadastrar= tela.nome.text() and tela.sobrenome.text() and tela.email.text and tela.senha.text and tela.peso.text and tela.altura.text and tela.gordura.text
     if cadastrar == '':
         QMessageBox.about(tela, 'Atenção', 'Preencha os campos solicitados.')

     else:
         QMessageBox.about(tela, 'Salvo com sucesso', 'Informações registradas')
         tela.close()
         tela1.show()
     nome= tela.nome.text()
     sobrenome= tela.sobrenome.text()
     email= tela.email.text()
     senha= tela.senha.text()
     peso= tela.peso.text()
     altura= tela.altura.text()
     gordura= tela.gordura.text()

     cursor= banco.cursor()
     sql= "INSERT INTO cadastro_1 (nome, sobrenome, email, senha, peso, altura, gordura) VALUES (%s, %s, %s, %s, %s, %s, %s)"
     colunas= (str(nome), str(sobrenome), str(email), str(senha), str(peso), str(altura), str(gordura))
     cursor.execute(sql, colunas)
     banco.commit()



def entrar():
     login_input = tela1.loginemail.text()
     senha_input = tela1.loginsenha.text()
     sql = "select senha from cadastro_1 where email = '{}'".format(login_input)
     cursor = banco.cursor()
     cursor.execute(sql)
     senha_banco = cursor.fetchall()

     if login_input != '' and senha_input != '':
         if senha_input == senha_banco[0][0]:
             QMessageBox.about(tela, "Bem-vindo(a)", "Seja Bem-vindo(a) ao PlanusFit.")
             tela5.show()
             tela1.close()

def logincadastro():
    tela.show()
    tela1.close()

def voltaplogin():
    tela.close()
    tela1.show()

########################################################

def larginina():
     webbrowser.open("https://www.gsuplementos.com.br/conteudo/arginina-beneficios/")

def creatina():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/creatina-beneficios")

def bcaa():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/bcaa-beneficios/")

def glutamina():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/glutamina-beneficios/")

def omega3():
    webbrowser.open("https://www.gsuplementos.com.br/oleo-de-peixe-omega-3-75-softgel-growth-supplements-p985848")

def whey():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/whey-beneficios/")

########################################################


def acessarcarol():
    webbrowser.open("https://www.youtube.com/@carolborba")

def acessaremi():
    webbrowser.open("https://www.youtube.com/@emiwong")

def acessaramanda():
    webbrowser.open("https://www.youtube.com/@amandabiuger")

def menutr():
    tela2.close()
    tela5.show()

def perfiltr():
    tela2.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))

def configtr():
    tela2.close()
    tela6.show()

def treinotr():
    tela2.close()
    tela7 .show()

########################################################

def menusup():
    tela3.close()
    tela5.show()

def perfilsup():
    tela3.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinosup():
    tela3.close()
    tela7.show()

def configsup():
    tela3.close()
    tela6.show()

########################################################

def menuper():
    tela4.close()
    tela5.show()

def perfilper():
    tela4.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))

def treinoper():
    tela4.close()
    tela7.show()

def configper():
    tela4.close()
    tela6.show()

########################################################

def treinoemcasa():
    tela5.close()
    tela2.show()

def suplementos():
    tela5.close()
    tela3.show()

def exercicio():
    tela5.close()
    tela7.show()

def menutop():
    tela5.close()
    tela5.show()

def perfiltop():
    tela5.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinotop():
    tela5.close()
    tela7.show()

def configtop():
    tela5.close()
    tela6.show()

########################################################

def menuconf():
    tela6.close()
    tela5.show()

def perfilconf():
    tela6.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinoconf():
    tela6.close()
    tela7.show()

def configconf():
    tela6.close()
    tela6.show()

def sair():
    tela6.close()
    tela1.show()

########################################################

def menupagtr():
    tela7.close()
    tela5.show()

def perfilpagtr():
    tela7.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinopagtr():
    tela7.close()
    tela7.show()

def definicao():
    tela7.close()
    tela8.show()

def configpagtr():
    tela7.close()
    tela6.show()

def hipertrofia():
    tela7.close()
    tela20.show()

    
########################################################

def menudef():
    tela8.close()
    tela5.show()

def perfildef():
    tela8.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinodef():
    tela8.close()
    tela7.show()

def configdef():
   tela8.close()
   tela6.show()

def defpeito():
    tela8.close()
    tela11.show()

def botaodeftriceps():
    tela8.close()
    tela13.show()

def botaodefcostas():
    tela8.close()
    tela9.show()

def botaodefbiceps():
    tela8.close()
    tela14.show()

def botaodefpernas():
    tela8.close()
    tela12.show()

def botaodefdeltoides():
    tela8.close()
    tela12.show()

########################################################

def menucos():
    tela9.close()
    tela5.show()

def perfilcos():
    tela9.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinocos():
    tela9.close()
    tela7.show()

def configcos():
    tela9.close()
    tela6.show()

########################################################

def menudel():
    tela10.close()
    tela5.show()

def perfildel():
    tela10.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinodel():
    tela10.close()
    tela7.show()

def configdel():
    tela10.close()
    tela6.show()

########################################################

def menuppe():
    tela11.close()
    tela5.show()

def perfilppe():
    tela11.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinoppe():
    tela11.close()
    tela7.show()

def configppe():
    tela11.close()
    tela6.show()

########################################################

def menupern():
    tela12.close()
    tela5.show()

def perfilpern():
    tela12.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinopern():
    tela12.close()
    tela7.show()

def configpern():
    tela12.close()
#   tela6.show()

########################################################

def menutri():
    tela13.close()
    tela5.show()

def perfiltri():
    tela13.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinotri():
    tela13.close()
    tela7.show()

def configtri():
    tela13.close()
    tela6.show()

########################################################

def menubi():
    tela14.close()
    tela5.show()

def perfilbi():
    tela14.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))

def treinobi():
    tela14.close()
    tela7.show()

def configbi():
    tela14.close()
    tela6.show()

#######################################################

def menua1():
    tela15.close()
    tela5.show()

def perfila1():
    tela15.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinoa1():
    tela15.close()
    tela7.show()

def configa1():
    tela15.close()
    tela6.show()

def exercicioa1():
    tela20.close()
    tela15.show()

def voltar_A_1():
    tela20.show()
    tela15.close()

#######################################################

def menuc1():
    tela16.close()
    tela5.show()

def perfilc1():
    tela16.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinoc1():
    tela16.close()
    tela7.show()

def configc1():
    tela16.close()
    tela6.show()

def botaohiperC():
    tela20.close()
    tela16.show()

def voltar_C_1():
    tela16.close()
    tela20.show()

#######################################################

def menub1():
    tela17.close()
    tela16.show()

def perfilb1():
    tela17.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinob1():
    tela17.close()
    tela7.show()

def configb1():
    tela17.close()
    tela6.show()

def botaohiperB():
    tela20.close()
    tela17.show()

def voltar_B_1():
    tela20.show()
    tela17.close()
#######################################################

def menub2():
    tela18.close()
    tela5.show()

def perfilb2():
    tela18.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinob2():
    tela18.close()
    tela7.show()

def configb2():
    tela18.close()
    tela6.show()

def voltar_B_2():
    tela20.show()
    tela18.close()


def botaohiperB_2():
    tela20.close()
    tela18.show()
#######################################################

def menuc2():
    tela19.close()
    tela5.show()

def perfilc2():
    tela19.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinoc2():
    tela19.close()
    tela7.show()

def configc2():
    tela19.close()
    tela6.show()

def botaohiperC_2():
    tela20.close()
    tela19.show()

def voltar_C_2():
    tela20.show()
    tela15.close()
#######################################################

def menua2():
    tela22.close()
    tela5.show()

def perfila2():
    tela22.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinoa2():
    tela22.close()
    tela7.show()

def configa2():
    tela22.close()
    tela6.show()

def botaohiperA_2():
    tela20.close()
    tela22.show()

def voltar_A_2():
    tela22.close()
    tela20.show()
############################################

def menuainf():
    tela23.close()
    tela5.show()

def perfilinf():
    tela23.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinoinf():
    tela23.close()
    tela7.show()

def configinf():
    tela23.close()
    tela6.show()

############################################

def menuahi():
    tela20.close()
    tela5.show()

def perfilhi():
    tela20.close()
    tela4.show()

    cursor= banco.cursor()
    sql= "select * from cadastro_1"
    cursor.execute(sql)
    dados= cursor.fetchall()
    tela4.tabela.setRowCount(len(dados))
    tela4.tabela.setColumnCount(3)

    for contador in range(0, len(dados)):
        for acessar in range(0,3):
            tela4.tabela.setItem(contador, acessar, QtWidgets.QTableWidgetItem(str(dados[contador][acessar])))


def treinohi():
    tela20.close()
    tela7.show()

def confighi():
    tela20.close()
    tela6.show()

def infor():
    tela23.show()
    tela7.close()

############voltar definição #############

def voltarbiceps():
    tela8.show()
    tela14.close()

def voltardel():
    tela8.show()
    tela10.close()

def voltarperna():
    tela8.show()
    tela12.close()

def voltartriceps():
    tela8.show()
    tela13.close()

def voltarcostas():
    tela8.show()
    tela9.close()

def voltarpeito():
    tela8.show()
    tela11.close()

#############################################

app = QtWidgets.QApplication([])
tela = uic.loadUi("pagina_de_cadastro.ui")
tela1 = uic.loadUi("login.ui")
tela2 = uic.loadUi("pagina_treino_em_casa.ui")
tela3 = uic.loadUi("suplementos1.ui")
tela4 = uic.loadUi("perfil.ui")
tela5 = uic.loadUi("topicos.ui")
tela6 = uic.loadUi("pagina_de_configuracoes.ui")
tela7 = uic.loadUi("pagina_de_treino.ui")
tela8 = uic.loadUi("pagina_de_definicao.ui")
tela9 = uic.loadUi("pagina_de_exercicios_Costas.ui")
tela10 = uic.loadUi("pagina_de_exercicios_Deltoides.ui")
tela11 = uic.loadUi("pagina_de_exercicios_Peito.ui")
tela12 = uic.loadUi("pagina_de_exercicios_Perna.ui")
tela13 = uic.loadUi("pagina_de_exercicios_Triceps.ui")
tela14 = uic.loadUi("pagina_de_exercicios_Biceps.ui")
tela15 = uic.loadUi("pagina de exercicios  A (1) Hipertrofia.ui")
tela16 = uic.loadUi("pagina_exercicios_C1_Hipertrofia.ui")
tela17 = uic.loadUi("pagina_de_exercicios_B1_Hipertrofia.ui")
tela18 = uic.loadUi("pagina de exercicios  B (2) Hipertrofia.ui")
tela19 = uic.loadUi("pagina de exercicios  C (2) Hipertrofia.ui")
tela20 = uic.loadUi("pagina_de_hipertrofia.ui")
tela22 = uic.loadUi("pagina de exercicios A (2).ui")
tela23 = uic.loadUi("pagina_de_informacoes.ui")


tela.cadastrar.clicked.connect(cadastro)
tela.voltaplogin.clicked.connect(voltaplogin)

tela1.entrar.clicked.connect(entrar)
tela1.cadastrarlog.clicked.connect(logincadastro)

 
tela3.l_arginina.clicked.connect(larginina)
tela3.bcaa.clicked.connect(bcaa)
tela3.whey.clicked.connect(whey)
tela3.creatina.clicked.connect(creatina)
tela3.glutamina.clicked.connect(glutamina)
tela3.omega3.clicked.connect(omega3)
tela3.menu_4.clicked.connect(menusup)  #Botões suplementos
tela3.perfil.clicked.connect(perfilsup) 
tela3.treino.clicked.connect(treinosup)  
tela3.config.clicked.connect(configsup)

tela2.menu_4.clicked.connect(menutr) 
tela2.perfil.clicked.connect(perfiltr) # botões treino em casa
tela2.treino.clicked.connect(treinotr)  
tela2.config.clicked.connect(configtr)
tela2.acessarcarol.clicked.connect(acessarcarol) # botões treino em casa yt
tela2.acessaremi.clicked.connect(acessaremi) 
tela2.acessaramanda.clicked.connect(acessaramanda)

tela4.menu_4.clicked.connect(menuper)
tela4.perfilbot.clicked.connect(perfilper) # botão perfil
tela4.treino.clicked.connect(treinoper) 
tela4.config.clicked.connect(configper)

tela5.treinoemcasa.clicked.connect(treinoemcasa)
tela5.suplementos.clicked.connect(suplementos)
tela5.exercicios.clicked.connect(exercicio)
tela5.menu_4.clicked.connect(menutop)
tela5.perfil.clicked.connect(perfiltop) # botão 
tela5.treino.clicked.connect(treinotop)  
tela5.config.clicked.connect(configtop)

tela6.menu_4.clicked.connect(menuconf)
tela6.perfil.clicked.connect(perfilconf) # botão 
tela6.treino.clicked.connect(treinoconf)  
tela6.config.clicked.connect(configconf)
tela6.sair.clicked.connect(sair)

tela7.menu_4.clicked.connect(menupagtr)
tela7.perfil.clicked.connect(perfilpagtr) # botão 
tela7.treino.clicked.connect(treinopagtr)  
tela7.config.clicked.connect(configpagtr)
tela7.definicao.clicked.connect(definicao)
tela7.hipertrofia.clicked.connect(hipertrofia)
tela7.infos.clicked.connect(infor)
tela8.menu_4.clicked.connect(menudef)
tela8.perfil.clicked.connect(perfildef) # botão 
tela8.treino.clicked.connect(treinodef)  
tela8.config.clicked.connect(configdef)
tela8.botaodefpeito.clicked.connect(defpeito)
tela8.botaodeftriceps.clicked.connect(botaodeftriceps)
tela8.botaodefcostas.clicked.connect(botaodefcostas)
tela8.botaodefbiceps.clicked.connect(botaodefbiceps)
tela8.botaodefpernas.clicked.connect(botaodefpernas)
tela8.botaodefdeltoides.clicked.connect(botaodefdeltoides)


tela9.menu_4.clicked.connect(menucos)
tela9.perfil.clicked.connect(perfilcos) # botão 
tela9.treino.clicked.connect(treinocos)  
tela9.config.clicked.connect(configcos)

tela10.menu_4.clicked.connect(menudel)
tela10.perfil.clicked.connect(perfildel) # botão 
tela10.treino.clicked.connect(treinodel)  
tela10.config.clicked.connect(configdel)

tela11.menu_4.clicked.connect(menuppe)
tela11.perfil.clicked.connect(perfilppe) # botão 
tela11.treino.clicked.connect(treinoppe)  
tela11.config.clicked.connect(configppe)

tela12.menu_4.clicked.connect(menupern)
tela12.perfil.clicked.connect(perfilpern) # botão 
tela12.treino.clicked.connect(treinopern)  
tela5.config.clicked.connect(configpern)

tela13.menu_4.clicked.connect(menutri)
tela13.perfil.clicked.connect(perfiltri) # botão 
tela13.treino.clicked.connect(treinotri)  
tela13.config.clicked.connect(configtri)

tela14.menu_4.clicked.connect(menubi)
tela14.perfil.clicked.connect(perfilbi) # botão 
tela14.treino.clicked.connect(treinobi)  
tela14.config.clicked.connect(configbi)

tela15.menu_4.clicked.connect(menua1)
tela15.perfil.clicked.connect(perfila1) # botão 
tela15.treino.clicked.connect(treinoa1)  
tela15.config.clicked.connect(configa1)
tela15.voltar_A_1.clicked.connect(voltar_A_1)

tela16.menu_4.clicked.connect(menuc1)
tela16.perfil.clicked.connect(perfilc1) # botão 
tela16.treino.clicked.connect(treinoc1)  
tela16.config.clicked.connect(configc1)
tela16.voltar_C_1.clicked.connect(voltar_C_1)
tela17.menu_4.clicked.connect(menub1)
tela17.perfil.clicked.connect(perfilb1) # botão 
tela17.treino.clicked.connect(treinob1)  
tela17.config.clicked.connect(configb1)
tela17.voltar_B_1.clicked.connect(voltar_B_1)
tela18.menu_4.clicked.connect(menub2)
tela18.perfil.clicked.connect(perfilb2) # botão 
tela18.treino.clicked.connect(treinob2)  
tela18.config.clicked.connect(configb2)
tela18.voltar_B_2.clicked.connect(voltar_B_2)

tela19.menu_4.clicked.connect(menuc2)
tela19.perfil.clicked.connect(perfilc2) # botão 
tela19.treino.clicked.connect(treinoc2)  
tela19.config.clicked.connect(configc2)
tela19.voltar_C_2.clicked.connect(voltar_C_2)

tela22.menu_4.clicked.connect(menua2)
tela22.perfil.clicked.connect(perfila2) # botão 
tela22.treino.clicked.connect(treinoa2)  
tela22.config.clicked.connect(configa2)
tela22.voltar_A_2.clicked.connect(voltar_A_2)

tela23.menu_4.clicked.connect(menuainf)
tela23.perfil.clicked.connect(perfilinf) # botão 
tela23.treino.clicked.connect(treinoinf)  
tela23.config.clicked.connect(configinf)

tela20.menu_4.clicked.connect(menuahi)
tela20.perfil.clicked.connect(perfilhi) # botão 
tela20.treino.clicked.connect(treinohi)  
tela20.config.clicked.connect(confighi)
tela20.botaohiperA.clicked.connect(exercicioa1)
tela20.botaohiperB.clicked.connect(botaohiperB)
tela20.botaohiperC.clicked.connect(botaohiperC)
tela20.botaohiperC_2.clicked.connect(botaohiperC_2)
tela20.botaohiperA_2.clicked.connect(botaohiperA_2)
tela20.botaohiperB_2.clicked.connect(botaohiperB_2)

tela10.voltardel.clicked.connect(voltardel)
tela14.voltarbiceps.clicked.connect(voltarbiceps)
tela12.voltarperna.clicked.connect(voltarperna)
tela13.voltartriceps.clicked.connect(voltartriceps)
tela9.voltarcostas.clicked.connect(voltarcostas)
tela11.voltarpeito.clicked.connect(voltarpeito)

tela5.show()
app.exec()