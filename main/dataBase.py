import sqlite3 as sql
from sqlite3 import Error
from os import path, mkdir
from itertools import zip_longest
from PyQt5.QtCore import QThread, pyqtSignal




class repairBoxDb(QThread):

    def __init__(self):
        super(repairBoxDb, self).__init__()
        self.connection = None
        # self.result = None
    def run(self):
        self.create_connection()
        self.createTables()
        self.addValueToTables()



    def create_connection(self):
        if path.exists("db"):
            try:
                self.connection = sql.connect("db/programme_data.db")
            except Error as bug:
                print(bug)

        else:
            mkdir("db")
            try:
                self.connection = sql.connect("db/programme_data.db")
            except Error as bug:
                print(bug)

    def createTables(self):
        ##########################################################################################
        # user table
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS USERS (ID INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,"
            "USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)"
        )
        ###########################################################################################
        # DEVICE TYPE

        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS DEVICE_TYPE (ID INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,"
            "TYPE_NAME TEXT NOT NULL)"
        )
        ##########################################################################################
        # COMPUTER_BRANDS
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS Ordinateur (ID INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,"
            "BRANDS_NAME TEXT NOT NULL)")
        ##########################################################################################
        # PHOTOCOPIERS_BRANDS
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS Photocopy (ID INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,"
            "BRANDS_NAME TEXT NOT NULL)")
        ##########################################################################################
        # PRINTER_BRANDS
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS Imprimant (ID INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,"
            "BRANDS_NAME TEXT NOT NULL)")
        ##########################################################################################
        # DEVICE COMPUTER BRANDS NAME  and photocopy and printer TABLES
        with open(file='dbmodels/gnmodels/computer.bmd', mode='r') as computer, open(
                file='dbmodels/gnmodels/photocopiers_BRANDS_NAME.bmd', mode='r')as \
                photocopy, open(file='dbmodels/gnmodels/Printer_BRAND_NAME.bmd', mode='r') as printer:

            for (computer, photocopy, printer) in zip_longest(computer, photocopy, printer):
                ##########################################################################################
                # DEVICE COMPUTER BRANDS NAME TABLES
                if computer is not None:
                    self.connection.execute(
                        f"CREATE TABLE IF NOT EXISTS {computer} (ID INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,"
                        "MODEL_NAME TEXT NOT NULL)")
                ##########################################################################################
                # photocopiers BRANDS NAME TABLES
                if photocopy is not None:
                    self.connection.execute(
                        f"""CREATE TABLE IF NOT EXISTS {photocopy} (ID INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,
                                        MODEL_NAME TEXT NOT NULL)""")
                #################################################################################
                # Printer BRAND NAME
                if printer is not None:
                    self.connection.execute(
                        f"""CREATE TABLE IF NOT EXISTS {printer} (ID INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,
                                        MODEL_NAME TEXT NOT NULL)""")
                ##################################################################################



    def addValueToTables(self):
        #################################################################################
        # add value to DEVICE_TYPE table
        self.connection.execute("""INSERT INTO DEVICE_TYPE VALUES(?,?)""", (0, 'Ordinateur'))
        self.connection.execute("""INSERT INTO DEVICE_TYPE VALUES(?,?)""", (1, 'Imprimant'))
        self.connection.execute("""INSERT INTO DEVICE_TYPE VALUES(?,?)""", (2, 'Photocopy'))
        ##################################################################################
        # add value to COMPUTER_BRANDS TABLE and PHOTOCOPIERS_BRANDS TABLE and PRINTER_BRANDS
        with open(file='dbmodels/gnmodels/computer.bmd', mode='r') as computer, open(file='dbmodels/gnmodels/photocopy.bmd',mode='r')as\
            photocopy, open(file='dbmodels/gnmodels/printer.bmd', mode='r') as printer:
            num = 0
            for (computer, photocopy, printer) in zip_longest(computer, photocopy, printer):
                if computer is not None:
                    self.connection.execute("""INSERT INTO Ordinateur VALUES (?,?)""",
                                            (num, computer))
                if photocopy is not None:
                    self.connection.execute(
                        """INSERT INTO Photocopy VALUES (?,?)""",
                        (num, photocopy))
                if printer is not None:
                    self.connection.execute(
                        """INSERT INTO Imprimant VALUES (?,?)""",
                        (num, printer))
                num += 1
        #################################################################################
        # add Values to COMPUTER BRANDS modelS name
        with open(file='dbmodels/CMmodelsname/asermodel.bmd', mode='r') as acer, open(file='dbmodels/CMmodelsname/alienwaremodels.bmd', mode ='r') as\
                alienware, open(file='dbmodels/CMmodelsname/appelmodels.bmd', mode='r') as appel, open(file='dbmodels/CMmodelsname/HP_COMPUTER_MODELS.bmd', mode='r') as \
                HP_Computer, open(file='dbmodels/CMmodelsname/Dell_models.bmd', mode='r') as Dell, open(file='dbmodels/CMmodelsname/Samsung_computer_models.bmd', mode='r') as \
                Samsung, open(file='dbmodels/CMmodelsname/Lenovo_Compute_models.bmd', mode='r') as Lenovo, open(file='dbmodels/CMmodelsname/Razer_models.bmd', mode='r') as \
                Razer, open(file='dbmodels/CMmodelsname/Microsoft_models.bmd', mode='r') as microsoft, open(file='dbmodels/CMmodelsname/MSI_models.bmd', mode='r') as \
                MSI, open(file='dbmodels/CMmodelsname/Asus_models.bmd', mode= 'r') as Asus, open(file='dbmodels/CMmodelsname/Google_models.bmd', mode='r') as \
                google, open(file='dbmodels/CMmodelsname/Huawei_models.bmd', mode='r') as Huawei, open(file="dbmodels/CMmodelsname/LG_models.bmd", mode='r') as \
                Lg, open(file='dbmodels/CMmodelsname/VAIO_models.bmd', mode='r') as VAIO, open(file='dbmodels/CMmodelsname/Xiaomi_models.bmd', mode='r') as \
                Xiaomi, open(file='dbmodels/CMmodelsname/Toshiba_computer_models.bmd', mode='r') as Toshiba:
            num = 0
            for (acccer, Alienware, Appel, HP, dell, samsung, lenovo, razer, Microsoft, MsI, asus, google, huawei,
                lg, vaio, xiaomi, toshiba)\
                    in zip_longest(
                acer, alienware, appel, HP_Computer, Dell, Samsung, Lenovo, Razer, microsoft, MSI, Asus, google, Huawei, Lg, VAIO,
                Xiaomi, Toshiba ):
                #######################################################################################
                # acer table
                if acccer is not None:
                    self.connection.execute("""INSERT INTO Acer VALUES (?,?)""",
                                            (num, acccer))
                #######################################################################################
                # Alienware table
                if Alienware is not None:
                    self.connection.execute("""INSERT INTO Alienware VALUES (?,?)""", (num, Alienware))
                #######################################################################################
                # Appel table
                if Appel is not None:
                    self.connection.execute("""INSERT INTO Apple VALUES (?,?)""", (num, Appel))
                #######################################################################################
                # HP table
                if HP is not None:
                    self.connection.execute("""INSERT INTO HP VALUES (?,?)""", (num, HP))
                #######################################################################################
                # DELL table
                if dell is not None:
                    self.connection.execute("""INSERT INTO Dell VALUES (?,?)""", (num, dell))
                #######################################################################################
                # SAMSUNG table
                if samsung is not None:
                    self.connection.execute("""INSERT INTO Samsung VALUES (?,?)""", (num, samsung))
                #######################################################################################
                # LENOVO table
                if lenovo is not None:
                    self.connection.execute("""INSERT INTO Lenovo VALUES (?,?)""", (num, lenovo))
                #######################################################################################
                # RAZER table
                if razer is not None:
                    self.connection.execute("""INSERT INTO Razer VALUES (?,?)""", (num, razer))
                #######################################################################################
                # Microsofr table
                if Microsoft is not None:
                    self.connection.execute("""INSERT INTO Microsoft VALUES (?,?)""", (num, Microsoft))
                #######################################################################################
                # MSI table
                if MsI is not None:
                    self.connection.execute("""INSERT INTO MSI VALUES (?,?)""", (num, MsI))
                #######################################################################################
                # ASUS table
                if asus is not None:
                    self.connection.execute("""INSERT INTO Asus VALUES (?,?)""", (num, asus))
                #######################################################################################
                # GOOGLE table
                if google is not None:
                    self.connection.execute("""INSERT INTO Google VALUES (?,?)""", (num, google))
                #######################################################################################
                # HUAWEI table
                if huawei is not None:
                    self.connection.execute("""INSERT INTO Huawei VALUES (?,?)""", (num, huawei))
                #######################################################################################
                # LG table
                if lg is not None:
                    self.connection.execute("""INSERT INTO LG VALUES (?,?)""", (num, lg))
                #######################################################################################
                # VAIO table
                if vaio is not None:
                    self.connection.execute("""INSERT INTO VAIO VALUES (?,?)""", (num, vaio))
                #######################################################################################
                # XIAOMI table
                if xiaomi is not None:
                    self.connection.execute("""INSERT INTO Xiaomi VALUES (?,?)""", (num, xiaomi))
                #######################################################################################
                # TOSHIBA table
                if toshiba is not None:
                    self.connection.execute("""INSERT INTO Toshiba VALUES (?,?)""", (num, toshiba))
                num += 1

        ####################################################################################
        # add Value to printer brand name
        with open(file='dbmodels/PrModels/Brother_models.bmd',mode='r') as Brother, open(file='dbmodels/PrModels/Canon_models.bmd', mode='r') as \
                Canon , open(file='dbmodels/PrModels/Epson_models.bmd', mode='r') as Epson, open(file='dbmodels/PrModels/Hp_models.bmd', mode='r') as \
                Hp, open(file='dbmodels/PrModels/Lexmark_models.bmd', mode='r') as Lexmark, open(file='dbmodels/PrModels/samsung_models.bmd', mode='r') as \
                Samsung, open(file='dbmodels/PrModels/Toshiba_models.bmd', mode='r') as Toshiba:
            num = 0
            for (brother, canon, epson, hp, lexmark, samsung, toshiba) in zip_longest(Brother, Canon, Epson, Hp, Lexmark, Samsung, Toshiba):
                ##############################################################################################
                # add Values to Brother printer table
                if brother is not None:
                    self.connection.execute("""INSERT INTO Brother_PRINTER VALUES (?,?)""", (num, brother))
                #############################################################################################
                # add Values to Canon printer table
                if canon is not None:
                    self.connection.execute("""INSERT INTO Canon_PRINTER VALUES (?,?)""", (num, canon))
                ##############################################################################################
                # add Values to epson printer table
                if epson is not None:
                    self.connection.execute("""INSERT INTO Epson_PRINTER VALUES (?,?)""", (num, epson))
                ##############################################################################################
                # add Values to hp printer table
                if hp is not None:
                    self.connection.execute("""INSERT INTO HP_PRINTER VALUES (?,?)""", (num, hp))
                ##############################################################################################
                # add Values to lexmark printer table
                if lexmark is not None:
                    self.connection.execute("""INSERT INTO Lexmark_PRINTER VALUES (?,?)""", (num, lexmark))
                ##############################################################################################
                # add Values to samsung printer table
                if samsung is not None:
                    self.connection.execute("""INSERT INTO Samsung_PRINTER VALUES (?,?)""", (num, samsung))
                ##############################################################################################
                # add Values to toshiba printer table
                if toshiba is not None:
                    self.connection.execute("""INSERT INTO Toshiba_PRINTER VALUES (?,?)""", (num, samsung))
                num += 1

        ###########################################################################################
        # add Value to Photocopiers brands name
        with open(file='dbmodels/PhCModels/Toshiba_models.bmd', mode='r') as Toshiba, open(file='dbmodels/PhCModels/canon.bmd', mode='r') as \
            Canon, open(file='dbmodels/PhCModels/EPSON.bmd', mode='r') as Epson, open(file='dbmodels/PhCModels/XEROX.bmd', mode='r') as \
            Xerox, open(file='dbmodels/PhCModels/KYOCERA.bmd', mode='r') as KYOCERA, open(file='dbmodels/PhCModels/Lexmark.bmd', mode='r') as \
            Lexmark, open(file='dbmodels/PhCModels/Ricoh_models.bmd', mode='r') as Ricoh, open(file='dbmodels/PhCModels/samsung_model.bmd', mode='r') as \
            Samsung, open(file='dbmodels/PhCModels/Sharp_models.bmd', mode='r') as Sharp:
            num = 0
            for (toshiba, canon, epson, xerox, kyocera, lexmark, ricoh, samsung, sharp) in zip_longest(
                Toshiba, Canon, Epson, Xerox, KYOCERA, Lexmark, Ricoh, Samsung, Sharp):

                if toshiba is not None:
                    self.connection.execute("INSERT INTO Toshiba_Photocopiers VALUES (?,?)",(num, toshiba))
                if canon is not None:
                    self.connection.execute("INSERT INTO CANON VALUES (?,?)", (num, canon))
                if epson is not None:
                    self.connection.execute("INSERT INTO EPSON VALUES (?,?)", (num, epson))
                if xerox is not None:
                    self.connection.execute("INSERT INTO XEROX VALUES (?,?)", (num, xerox))
                if kyocera is not None:
                    self.connection.execute("INSERT INTO KYOCERA VALUES (?,?)", (num, kyocera))
                if lexmark is not None:
                    self.connection.execute("INSERT INTO Lexmark VALUES (?,?)", (num, lexmark))
                if ricoh is not None:
                    self.connection.execute("INSERT INTO Ricoh VALUES (?,?)", (num, ricoh))
                if samsung is not None:
                    self.connection.execute("INSERT INTO SAMSUNG_PHOTOCOPIER VALUES (?,?)", (num, samsung))
                if sharp is not None:
                    self.connection.execute("INSERT INTO Sharp VALUES (?,?)", (num, sharp))
                num += 1
        #########################################################################################################

        self.connection.commit()
        #self.result = self.connection.execute("SELECT * FROM USERS")
        self.connection.close()
