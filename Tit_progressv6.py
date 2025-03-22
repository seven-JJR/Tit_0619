import fnmatch
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QTimer
import os
import subprocess
import time
import uiautomation as auto
import wmi
from iupdatable.system.hardware import CSProduct
import shutil
import json
import re, datetime
import psutil
from TitUI_progress import Ui_MainWindow
import threading
from PyQt5.QtCore import pyqtSignal
import pythoncom

curent_time = datetime.datetime.now()
curent_time_1 = curent_time.strftime("%Y_%m_%d_%H_%M_%S")
SysVersion = wmi.WMI()
version = SysVersion.Win32_OperatingSystem()[0].BuildNumber
bios = wmi.WMI()
if int(version) >= 20000:
    system = 'Win11'
else:
    system = 'Win10'
biosver = bios.Win32_BIOS()[0].SMBIOSBIOSVersion[:-8]  # 去除bios版本后面的（1.09)
if int(version) < 26000:  #24H2这一段不适用
    inumber = CSProduct.get_identifying_number()
    inumber_1 = CSProduct.get_name()
    SNnumber = inumber_1 + inumber
else: #24H2
    inumber = bios.Win32_BIOS()[0].SerialNumber
    inumber_1 = bios.Win32_BaseBoard()[0].Product
    SNnumber = inumber_1 + inumber
winlr_server = 0
ProjectConfirm_List_1_copyt = []
sum_wangluozhongshu = 0
project_1tt = ''


class MainWindow(QMainWindow, Ui_MainWindow):
    mysignal = pyqtSignal(str)
    mysignal1 = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.progressBar.hide()
        self.pushButton_20.clicked.connect(self.HJSZXC)
        self.pushButton_18.clicked.connect(self.ACWBXC)
        self.pushButton_28.clicked.connect(self.DCWBXC)
        self.pushButton_29.clicked.connect(self.DCMSXC)
        self.pushButton_13.clicked.connect(self.FSUXC)
        self.pushButton_15.clicked.connect(self.S5XC)
        self.pushButton_34.clicked.connect(self.ATSLOG)
        self.pushButton_12.clicked.connect(self.ACS4XC)
        self.pushButton_30.clicked.connect(self.DCS4XC)
        self.pushButton_35.clicked.connect(self.ATSLOGCKXC)
        self.pushButton_17.clicked.connect(self.ACMSXC)
        self.pushButton_33.clicked.connect(self.TOOLCOPYXC)
        self.pushButton_33.clicked.connect(self.jindu)
        self.pushButton_21.clicked.connect(self.user_switch)
        self.pushButton_31.clicked.connect(self.WinLRFSUXC)
        self.pushButton_32.clicked.connect(self.WinLRCBXC)
        self.pushButton_36.clicked.connect(self.SUTADD)
        self.pushButton_37.clicked.connect(self.WinLRCombieXC)
        self.mysignal.connect(self.tishi)
        self.mysignal1.connect(self.tishi1)

    def tishi(self):
        print(4)
        self.timer.stop()
        self.progressBar.hide()
        QMessageBox.information(MainWindow, '提示', 'Copy成功')
        self.progressBar.reset()

    def tishi1(self):
        QMessageBox.information(MainWindow, "提示", "tool已存在")

    def ACMSXC(self):
        AC_1 = psutil.sensors_battery()
        AC_1_1 = AC_1.power_plugged
        if AC_1_1 == False or self.lineEdit.text() == '':
            if AC_1_1 == False and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请插AC并设置圈数')
            elif AC_1_1 == False:
                QMessageBox.warning(MainWindow, '提示', '请插AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_1 = threading.Thread(target=self.AC_MS)
            tr_1.setDaemon(True)
            tr_1.start()

    def ACS4XC(self):
        AC_2 = psutil.sensors_battery()
        AC_2_2 = AC_2.power_plugged
        if AC_2_2 == False or self.lineEdit.text() == '':
            if AC_2_2 == False and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请插AC并设置圈数')
            elif AC_2_2 == False:
                QMessageBox.warning(MainWindow, '提示', '请插AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_2 = threading.Thread(target=self.AC_S4)
            tr_2.setDaemon(True)
            tr_2.start()

    def DCMSXC(self):
        AC_3 = psutil.sensors_battery()
        AC_3_3 = AC_3.power_plugged
        if AC_3_3 == True or self.lineEdit.text() == '':
            if AC_3_3 == True and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请拔掉AC并设置圈数')
            elif AC_3_3 == True:
                QMessageBox.warning(MainWindow, '提示', '请拔掉AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_3 = threading.Thread(target=self.DC_MS)
            tr_3.setDaemon(True)
            tr_3.start()

    def DCS4XC(self):
        AC_4 = psutil.sensors_battery()
        AC_4_4 = AC_4.power_plugged
        if AC_4_4 == True or self.lineEdit.text() == '':
            if AC_4_4 == True and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请拔掉AC并设置圈数')
            elif AC_4_4 == True:
                QMessageBox.warning(MainWindow, '提示', '请拔掉AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_4 = threading.Thread(target=self.DC_S4)
            tr_4.setDaemon(True)
            tr_4.start()

    def ACWBXC(self):
        AC_5 = psutil.sensors_battery()
        AC_5_5 = AC_5.power_plugged
        if AC_5_5 == False or self.lineEdit.text() == '':
            if AC_5_5 == False and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请插AC并设置圈数')
            elif AC_5_5 == False:
                QMessageBox.warning(MainWindow, '提示', '请插AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_5 = threading.Thread(target=self.AC_WB)
            tr_5.setDaemon(True)
            tr_5.start()

    def DCWBXC(self):
        AC_6 = psutil.sensors_battery()
        AC_6_6 = AC_6.power_plugged
        if AC_6_6 == True or self.lineEdit.text() == '':
            if AC_6_6 == True and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请拔掉AC并设置圈数')
            elif AC_6_6 == True:
                QMessageBox.warning(MainWindow, '提示', '请拔掉插AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_6 = threading.Thread(target=self.DC_WB)
            tr_6.setDaemon(True)
            tr_6.start()

    def S5XC(self):
        AC_7 = psutil.sensors_battery()
        AC_7_7 = AC_7.power_plugged
        if AC_7_7 == False or self.lineEdit.text() == '':
            if AC_7_7 == False and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请插AC并设置圈数')
            elif AC_7_7 == False:
                QMessageBox.warning(MainWindow, '提示', '请插AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_7 = threading.Thread(target=self.S5)
            tr_7.setDaemon(True)
            tr_7.start()

    def FSUXC(self):
        AC_8 = psutil.sensors_battery()
        AC_8_8 = AC_8.power_plugged
        if AC_8_8 == False or self.lineEdit.text() == '':
            if AC_8_8 == False and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请插AC并设置圈数')
            elif AC_8_8 == False:
                QMessageBox.warning(MainWindow, '提示', '请插AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_8 = threading.Thread(target=self.FSU)
            tr_8.setDaemon(True)
            tr_8.start()

    def WinLRFSUXC(self):
        AC_9 = psutil.sensors_battery()
        AC_9_9 = AC_9.power_plugged
        if AC_9_9 == False or self.lineEdit.text() == '':
            if AC_9_9 == False and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请插AC并设置圈数')
            elif AC_9_9 == False:
                QMessageBox.warning(MainWindow, '提示', '请插AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_9 = threading.Thread(target=self.WinLRFSU)
            tr_9.setDaemon(True)
            tr_9.start()

    def WinLRCBXC(self):
        AC_12 = psutil.sensors_battery()
        AC_12_12 = AC_12.power_plugged
        if AC_12_12 == False or self.lineEdit.text() == '':
            if AC_12_12 == False and self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请插AC并设置圈数')
            elif AC_12_12 == False:
                QMessageBox.warning(MainWindow, '提示', '请插AC')
            elif self.lineEdit.text() == '':
                QMessageBox.warning(MainWindow, '提示', '请先设置圈数')
        else:
            tr_12 = threading.Thread(target=self.WinLRCB)
            tr_12.setDaemon(True)
            tr_12.start()

    def WinLRCombieXC(self):
        AC_14 = psutil.sensors_battery()
        AC_14_14 = AC_14.power_plugged
        if AC_14_14 == False:
            QMessageBox.warning(MainWindow, '提示', '请插AC')
        else:
            tr_14 = threading.Thread(target=self.WinLRCombine)
            tr_14.setDaemon(True)
            tr_14.start()

    def ATSLOGCKXC(self):
        tr_10 = threading.Thread(target=self.ATSLGCK)
        tr_10.setDaemon(True)
        tr_10.start()

    def HJSZXC(self):
        tr_11 = threading.Thread(target=self.HJSZ)
        tr_11.setDaemon(True)
        tr_11.start()

    def TOOLCOPYXC(self):
        tr_13 = threading.Thread(target=self.tool_copy)
        tr_13.setDaemon(True)
        tr_13.start()

    def user_switch(self):
        if os.getlogin()=="LongRun":
            os.system(r'C:\LR_TO_ADMIN.bat')
        elif os.getlogin()=="Administrator":
            os.system(r'C:\ADMIN_TO_LR.bat')


    def HJSZ(slef):
        if os.path.exists(r'C:\WDTFInstallText.log'):
            
            os.system(r'C:\TNB_Integration_Tool\SetPrerequisites_v4.0\Prepare.bat')
            time.sleep(5)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\SetPrerequisites.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\SetPrerequisites_v4.0\SetPrerequisites_Run.exe')
            time.sleep(30)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            os.system('shutdown -r -t 2')
        else:
            if int(version) >= 20000:
                os.system(r'C:\TNB_Integration_Tool\WDTF\Win11\WDTF.bat')
                time.sleep(10)
                os.system(r'C:\TNB_Integration_Tool\SetPrerequisites_v4.0\Prepare.bat')
                time.sleep(5)
                #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\SetPrerequisites.ps1'])
                subprocess.Popen(r'C:\TNB_Integration_Tool\SetPrerequisites_v4.0\SetPrerequisites_Run.exe')
                time.sleep(30)
                try:
                    auto.ButtonControl(Name='OK').Click()
                except LookupError:
                    auto.SendKeys('{Enter}')
                os.system('shutdown -r -t 2')
            elif int(version) < 20000:
                os.system(r'C:\TNB_Integration_Tool\WDTF\Win10\WDTF.bat')
                time.sleep(10)
                os.system(r'C:\TNB_Integration_Tool\SetPrerequisites_v4.0\Prepare.bat')
                time.sleep(5)
                #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\SetPrerequisites.ps1'])
                subprocess.Popen(r'C:\TNB_Integration_Tool\SetPrerequisites_v4.0\SetPrerequisites_Run.exe')
                time.sleep(30)
                try:
                    auto.ButtonControl(Name='OK').Click()
                except LookupError:
                    auto.SendKeys('{Enter}')
                os.system('shutdown -r -t 2')

    def AC_MS(self):
        self.label.setText(self.pushButton_17.text())
        pm_list_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        pm_list_1_1 = pm_list_1.read()
        pm_list_1_1_1 = json.loads(pm_list_1_1)
        pm_list_1.close()
        if SNnumber not in pm_list_1_1_1:
            pm_class_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
            pm_class_1_1 = pm_class_1.read().rstrip("}")
            pm_class_1_1_1 = str(pm_class_1_1)
            pm_class_1.close()
            newpm_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            newpm_1_1 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + self.label.text() + '"' + '}'
            newpm_1.write(pm_class_1_1_1 + newpm_1_1)
            newpm_1.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='S0i3').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* S0i3 Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* S0i3 Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            MainWindow.close()
        else:
            pm_list_1_1_1[SNnumber] = self.label.text()
            pm_list_1_1_1_1 = json.dumps(pm_list_1_1_1)
            pm_list_1_1_1_1_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            pm_list_1_1_1_1_1_1 = pm_list_1_1_1_1_1.write(pm_list_1_1_1_1)
            pm_list_1_1_1_1_1.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='S0i3').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* S0i3 Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* S0i3 Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            MainWindow.close()

    def DC_MS(self):
        self.label.setText(self.pushButton_29.text())
        pm_list_2 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        pm_list_2_2 = pm_list_2.read()
        pm_list_2_2_2 = json.loads(pm_list_2_2)
        pm_list_2.close()
        if SNnumber not in pm_list_2_2_2:
            pm_class_2 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
            pm_class_2_2 = pm_class_2.read().rstrip("}")
            pm_class_2_2_2 = str(pm_class_2_2)
            pm_class_2.close()
            newpm_2 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            newpm_2_2 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + self.label.text() + '"' + '}'
            newpm_2.write(pm_class_2_2_2 + newpm_2_2)
            newpm_2.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='S0i3').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* S0i3 Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* S0i3 Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            MainWindow.close()
        else:
            pm_list_2_2_2[SNnumber] = self.label.text()
            pm_list_2_2_2_2 = json.dumps(pm_list_2_2_2)
            pm_list_2_2_2_2_2 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            pm_list_2_2_2_2_2_2 = pm_list_2_2_2_2_2.write(pm_list_2_2_2_2)
            pm_list_2_2_2_2_2.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='S0i3').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* S0i3 Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* S0i3 Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            MainWindow.close()

    def AC_S4(self):
        self.label.setText(self.pushButton_12.text())
        pm_list_3 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        pm_list_3_3 = pm_list_3.read()
        pm_list_3_3_3 = json.loads(pm_list_3_3)
        pm_list_3.close()
        if SNnumber not in pm_list_3_3_3:
            pm_class_3 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
            pm_class_3_3 = pm_class_3.read().rstrip("}")
            pm_class_3_3_3 = str(pm_class_3_3)
            pm_class_3.close()
            newpm_3 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            newpm_3_3 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + self.label.text() + '"' + '}'
            newpm_3.write(pm_class_3_3_3 + newpm_3_3)
            newpm_3.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='S4').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* S4 Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* S4 Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            #auto.ButtonControl(Name='No').Click()
            MainWindow.close()
        else:
            pm_list_3_3_3[SNnumber] = self.label.text()
            pm_list_3_3_3_3 = json.dumps(pm_list_3_3_3)
            pm_list_3_3_3_3_3 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            pm_list_3_3_3_3_3_3 = pm_list_3_3_3_3_3.write(pm_list_3_3_3_3)
            pm_list_3_3_3_3_3.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='S4').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* S4 Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* S4 Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            MainWindow.close()

    def DC_S4(self):
        self.label.setText(self.pushButton_30.text())
        pm_list_4 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        pm_list_4_4 = pm_list_4.read()
        pm_list_4_4_4 = json.loads(pm_list_4_4)
        pm_list_4.close()
        if SNnumber not in pm_list_4_4_4:
            pm_class_4 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
            pm_class_4_4 = pm_class_4.read().rstrip("}")
            pm_class_4_4_4 = str(pm_class_4_4)
            pm_class_4.close()
            newpm_4 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            newpm_4_4 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + self.label.text() + '"' + '}'
            newpm_4.write(pm_class_4_4_4 + newpm_4_4)
            newpm_4.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='S4').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* S4 Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* S4 Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            #auto.ButtonControl(Name='No').Click()
            MainWindow.close()
        else:
            pm_list_4_4_4[SNnumber] = self.label.text()
            pm_list_4_4_4_4 = json.dumps(pm_list_4_4_4)
            pm_list_4_4_4_4_4 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            pm_list_4_4_4_4_4_4 = pm_list_4_4_4_4_4.write(pm_list_4_4_4_4)
            pm_list_4_4_4_4_4.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='S4').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* S4 Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* S4 Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            #auto.ButtonControl(Name='No').Click()
            MainWindow.close()

    def AC_WB(self):

        self.label.setText(self.pushButton_18.text())
        pm_list_5 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        pm_list_5_5 = pm_list_5.read()
        pm_list_5_5_5 = json.loads(pm_list_5_5)
        pm_list_5.close()
        if SNnumber not in pm_list_5_5_5:
            pm_class_5 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
            pm_class_5_5 = pm_class_5.read().rstrip("}")
            pm_class_5_5_5 = str(pm_class_5_5)
            pm_class_5.close()
            newpm_5 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            newpm_5_5 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + self.label.text() + '"' + '}'
            newpm_5.write(pm_class_5_5_5 + newpm_5_5)
            newpm_5.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='R').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* R Elapse time in seconds :').SendKeys('240')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            MainWindow.close()
        else:
            pm_list_5_5_5[SNnumber] = self.label.text()
            pm_list_5_5_5_5 = json.dumps(pm_list_5_5_5)
            pm_list_5_5_5_5_5 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            pm_list_5_5_5_5_5_5 = pm_list_5_5_5_5_5.write(pm_list_5_5_5_5)
            pm_list_5_5_5_5_5.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='R').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* R Elapse time in seconds :').SendKeys('240')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            MainWindow.close()

    def DC_WB(self):
        self.label.setText(self.pushButton_28.text())
        pm_list_6 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        pm_list_6_6 = pm_list_6.read()
        pm_list_6_6_6 = json.loads(pm_list_6_6)
        pm_list_6.close()
        if SNnumber not in pm_list_6_6_6:
            pm_class_6 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
            pm_class_6_6 = pm_class_6.read().rstrip("}")
            pm_class_6_6_6 = str(pm_class_6_6)
            pm_class_6.close()
            newpm_6 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            newpm_6_6 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + self.label.text() + '"' + '}'
            newpm_6.write(pm_class_6_6_6 + newpm_6_6)
            newpm_6.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='R').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* R Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            #auto.ButtonControl(Name='No').Click()
            MainWindow.close()
        else:
            pm_list_6_6_6[SNnumber] = self.label.text()
            pm_list_6_6_6_6 = json.dumps(pm_list_6_6_6)
            pm_list_6_6_6_6_6 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            pm_list_6_6_6_6_6_6 = pm_list_6_6_6_6_6.write(pm_list_6_6_6_6)
            pm_list_6_6_6_6_6.close()
            if os.path.exists('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                    shutil.rmtree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            #subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\LongRunATS_AOAC.ps1'])
            subprocess.Popen(r'C:\TNB_Integration_Tool\LongRunATS_AOAC_v6\ATS_PMLongRun_Run.exe')
            time.sleep(11)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='R').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* R Elapse time in seconds :').SendKeys('120')
            auto.SendKeys('{Enter}')
            time.sleep(1)
            MainWindow.close()

    def FSU(self):
        self.label.setText(self.pushButton_13.text())
        pm_list_7 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        pm_list_7_7 = pm_list_7.read()
        pm_list_7_7_7 = json.loads(pm_list_7_7)
        pm_list_7.close()
        if SNnumber not in pm_list_7_7_7:
            pm_class_7 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
            pm_class_7_7 = pm_class_7.read().rstrip("}")
            pm_class_7_7_7 = str(pm_class_7_7)
            pm_class_7.close()
            newpm_7 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            newpm_7_7 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + self.label.text() + '"' + '}'
            newpm_7.write(pm_class_7_7_7 + newpm_7_7)
            newpm_7.close()
            for file_13 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2'):
                if file_13.endswith('csv') or file_13.endswith('htm') or file_13.endswith('html') or file_13.endswith(
                        'txt') or file_13.endswith('bin'):
                    os.remove(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2', file_13))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            # subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\LongRunATS_Shutdown.ps1'])
            os.system(r'C:\TNB_Integration_Tool\LongRunATS_Shutdown_v5.2\Run.bat')
            time.sleep(9)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='FSU').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* FSU Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* FSU Elapse time in seconds :').SendKeys('240')
            auto.SendKeys('{Enter}')
            time.sleep(5)
            auto.ButtonControl(Name='No').Click()
            time.sleep(130)
            auto.ButtonControl(Name='Yes').Click()
            MainWindow.close()
        else:
            pm_list_7_7_7[SNnumber] = self.label.text()
            pm_list_7_7_7_7 = json.dumps(pm_list_7_7_7)
            pm_list_7_7_7_7_7 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            pm_list_7_7_7_7_7_7 = pm_list_7_7_7_7_7.write(pm_list_7_7_7_7)
            pm_list_7_7_7_7_7.close()
            for file_14 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2'):
                if file_14.endswith('csv') or file_14.endswith('htm') or file_14.endswith('html') or file_14.endswith('txt') or file_14.endswith('bin'):
                    os.remove(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2', file_14))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            # subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\LongRunATS_Shutdown.ps1'])
            os.system(r'C:\TNB_Integration_Tool\LongRunATS_Shutdown_v5.2\Run.bat')
            time.sleep(9)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='FSU').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* FSU Resume time in seconds:').SendKeys('120')
            auto.EditControl(Name='* FSU Elapse time in seconds :').SendKeys('240')
            auto.SendKeys('{Enter}')
            time.sleep(5)
            auto.ButtonControl(Name='No').Click()
            time.sleep(130)
            auto.ButtonControl(Name='Yes').Click()
            MainWindow.close()

    def S5(self):
        self.label.setText(self.pushButton_15.text())
        pm_list_8 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        pm_list_8_8 = pm_list_8.read()
        pm_list_8_8_8 = json.loads(pm_list_8_8)
        pm_list_8.close()
        if SNnumber not in pm_list_8_8_8:
            pm_class_8 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
            pm_class_8_8 = pm_class_8.read().rstrip("}")
            pm_class_8_8_8 = str(pm_class_8_8)
            pm_class_8.close()
            newpm_8 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            newpm_8_8 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + self.label.text() + '"' + '}'
            newpm_8.write(pm_class_8_8_8 + newpm_8_8)
            newpm_8.close()
            for file_15 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2'):
                if file_15.endswith('csv') or file_15.endswith('htm') or file_15.endswith('html') or file_15.endswith(
                        'txt') or file_15.endswith('bin'):
                    os.remove(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2', file_15))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            # subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\LongRunATS_Shutdown.ps1'])
            os.system(r'C:\TNB_Integration_Tool\LongRunATS_Shutdown_v5.2\Run.bat')
            time.sleep(9)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='FSD').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* FSD Resume time in seconds :').SendKeys('120')
            auto.EditControl(Name='* FSD Elapse time in seconds :').SendKeys('240')
            auto.SendKeys('{Enter}')
            time.sleep(5)
            auto.ButtonControl(Name='No').Click()
            time.sleep(130)
            auto.ButtonControl(Name='Yes').Click()
            MainWindow.close()
        else:
            pm_list_8_8_8[SNnumber] = self.label.text()
            pm_list_8_8_8_8 = json.dumps(pm_list_8_8_8)
            pm_list_8_8_8_8_8 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt', 'w+')
            pm_list_8_8_8_8_8_8 = pm_list_8_8_8_8_8.write(pm_list_8_8_8_8)
            pm_list_8_8_8_8_8.close()
            for file_16 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2'):
                if file_16.endswith('csv') or file_16.endswith('htm') or file_16.endswith('html') or file_16.endswith('txt') or file_16.endswith('bin'):
                    os.remove(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2', file_16))
            os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
            time.sleep(57)
            # subprocess.Popen(['powershell', 'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\LongRunATS_Shutdown.ps1'])
            os.system(r'C:\TNB_Integration_Tool\LongRunATS_Shutdown_v5.2\Run.bat')
            time.sleep(9)
            try:
                auto.ButtonControl(Name='OK').Click()
            except LookupError:
                auto.SendKeys('{Enter}')
            time.sleep(7)
            auto.RadioButtonControl(Name='Silent').Click()
            time.sleep(1)
            auto.ButtonControl(Name='FSD').Click()
            time.sleep(1)
            auto.EditControl(Name='* Iteration count :').SendKeys(self.lineEdit.text())
            auto.EditControl(Name='* FSD Resume time in seconds :').SendKeys('120')
            auto.EditControl(Name='* FSD Elapse time in seconds :').SendKeys('240')
            auto.SendKeys('{Enter}')
            time.sleep(5)
            auto.ButtonControl(Name='No').Click()
            time.sleep(130)
            auto.ButtonControl(Name='Yes').Click()
            MainWindow.close()

    def ATSLGCK(self):
        lgck_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
        lgck_1_1 = lgck_1.read()
        lgck_1_1_1 = json.loads(lgck_1_1)
        lgck_1.close()
        if SNnumber in lgck_1_1_1:
            key_1 = lgck_1_1_1[SNnumber]
            key_1_1 = re.compile(r'&(.*?)&')
            lgckproject_1 = key_1_1.search(key_1).group().replace('&', '')
            os.system('start' + ' ' + os.path.join('\\\\192.168.1.225', 'LR_Log', lgckproject_1))
        else:
            os.system('start' + ' ' + os.path.join('\\\\192.168.1.225', 'LR_Log'))

    def WinLRFSU(self):
        shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
        os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
        wlcyclef = open(r'C:\TNB_Integration_Tool\wiLongRun\cycle.txt', 'w+')
        wlcyclef_1 = wlcyclef.write(self.lineEdit.text())
        wlcyclef.close()
        os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
        time.sleep(20)
        subprocess.Popen(r'C:\TNB_Integration_Tool\wiLongRun\winlrFSU.exe')
        time.sleep(5)
        MainWindow.close()

    def WinLRCB(self):
        shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
        os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
        wlcyclec = open(r'C:\TNB_Integration_Tool\wiLongRun\cycle.txt', 'w+')
        wlcyclec_1 = wlcyclec.write(self.lineEdit.text())
        wlcyclec.close()
        os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
        time.sleep(20)
        subprocess.Popen(r'C:\TNB_Integration_Tool\wiLongRun\winlrCB.exe')
        time.sleep(5)
        MainWindow.close()

    def WinLRCombine(self):
        shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
        os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
        os.system('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\ClearLog.bat')
        time.sleep(20)
        subprocess.Popen(r'C:\TNB_Integration_Tool\wiLongRun\winlrCombine.exe')
        time.sleep(5)
        MainWindow.close()

    def jindu(self):
        ProjectConfirm_1_copyt = open(
            '\\\\192.168.1.225\\pm_tool\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\winlrtool.txt')
        ProjectConfirm_1_1_copyt = ProjectConfirm_1_copyt.read()
        global ProjectConfirm_List_1_copyt, winlr_server, sum_wangluozhongshu, project_1tt
        ProjectConfirm_List_1_copyt = json.loads(ProjectConfirm_1_1_copyt)
        ProjectConfirm_1_copyt.close()
        data_1tt = open('\\\\192.168.1.225\\pm_tool\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
        data_1_1tt = data_1tt.read()
        list_1tt = json.loads(data_1_1tt)
        data_1tt.close()
        phase_key_1tt = list_1tt[SNnumber]
        moban_1tt = re.compile(r'&(.*?)&')
        project_1tt = moban_1tt.search(phase_key_1tt).group().replace('&', '')
        if SNnumber in ProjectConfirm_List_1_copyt:
            ProjectConfirm_Message_copyt = ProjectConfirm_List_1_copyt[SNnumber]
            path1 = os.path.join('\\\\192.168.1.225', 'pm_tool', ProjectConfirm_Message_copyt, 'wiLongRun')
            for dirpath1, dirnames1, filenames1 in os.walk(path1):
                for file1 in filenames1:
                    path_1 = os.path.join(dirpath1, file1)
                    winlr_server = winlr_server + os.path.getsize(path_1)
            sum_wangluozhongshu = 47498231 + winlr_server
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

    def timeout(self):
        global ProjectConfirm_List_1_copyt, winlr_server, sum_wangluozhongshu, project_1tt
        self.value = 0
        self.TNB_Integration_Tool = 0
        self.bendi = 0
        if SNnumber not in ProjectConfirm_List_1_copyt and project_1tt != 'CH3_Intel' and project_1tt != 'Zeus3_Intel':
            for dirpath2, dirnames2, filenames2 in os.walk('C:\\TNB_Integration_Tool'):
                for file2 in filenames2:
                    path_2 = os.path.join(dirpath2, file2)
                    self.TNB_Integration_Tool = self.TNB_Integration_Tool + os.path.getsize(path_2)
            self.progressBar.setValue(int(self.TNB_Integration_Tool / 47498231 * 100))
        elif SNnumber in ProjectConfirm_List_1_copyt:
            for dirpath1w, dirnames1w, filenames1w in os.walk('C:\\TNB_Integration_Tool'):
                for file1w in filenames1w:
                    path_1w = os.path.join(dirpath1w, file1w)
                    self.bendi = self.bendi + os.path.getsize(path_1w)
            self.value = int(self.bendi / sum_wangluozhongshu * 100)
            self.progressBar.setValue(self.value)
        elif SNnumber not in ProjectConfirm_List_1_copyt and project_1tt == 'CH3_Intel' or project_1tt == 'Zeus3_Intel':
            for dirpath2, dirnames2, filenames2 in os.walk('C:\\TNB_Integration_Tool'):
                for file2 in filenames2:
                    path_2 = os.path.join(dirpath2, file2)
                    self.TNB_Integration_Tool = self.TNB_Integration_Tool + os.path.getsize(path_2)
            print(self.TNB_Integration_Tool, 95093151, int(self.TNB_Integration_Tool / 95093151 * 100))
            self.progressBar.setValue(int(self.TNB_Integration_Tool / 95093151 * 100))

    def tool_copy(self):
        if os.path.exists('C:\\TNB_Integration_Tool'):
            self.mysignal1.emit('2')
        else:
            self.progressBar.show()
            shutil.copytree('\\\\192.168.1.225\\pm_tool\\TNB_Integration_Tool', 'C:\\TNB_Integration_Tool')
            ProjectConfirm_1_copy = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\winlrtool.txt')
            ProjectConfirm_1_1_copy = ProjectConfirm_1_copy.read()
            ProjectConfirm_List_1_copy = json.loads(ProjectConfirm_1_1_copy)
            ProjectConfirm_1_copy.close()
            data_1t = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_1_1t = data_1t.read()
            list_1t = json.loads(data_1_1t)
            data_1t.close()
            phase_key_1t = list_1t[SNnumber]
            moban_1t = re.compile(r'&(.*?)&')
            project_1t = moban_1t.search(phase_key_1t).group().replace('&', '')
            if SNnumber in ProjectConfirm_List_1_copy:
                ProjectConfirm_Message_copy = ProjectConfirm_List_1_copy[SNnumber]
                shutil.copytree(os.path.join('\\\\192.168.1.225', 'pm_tool', ProjectConfirm_Message_copy, 'wiLongRun'), 'C:\\TNB_Integration_Tool\\wiLongRun')
                self.mysignal.emit('1')
            # elif project_1t == 'LCH3' or project_1t == 'Zeus3':
            #     shutil.copytree('\\\\192.168.1.225\\pm_tool\\All_PM_Tool\\AZ', 'C:\\TNB_Integration_Tool\\AZ')
            #     self.mysignal.emit('1')
            else:
                self.mysignal.emit('1')

    def SUTADD(self):
        data_1_s = open('\\\\192.168.1.225\\pm_tool\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
        data_1_1_s = data_1_s.read()
        data_1_1_1_s = str(data_1_1_s)
        list_1_s = json.loads(data_1_1_s)
        data_1_s.close()
        project_s=self.comboBox.currentText()
        if SNnumber in list_1_s:
            QMessageBox.information(MainWindow, '提示', '此机台已经添加过')
        else:
            text_2_s, ok_2_s = QInputDialog.getText(MainWindow, '提示', '请输入SKU')
            if ok_2_s:
                sku_s = text_2_s
                text_3_s, ok_3_s = QInputDialog.getText(MainWindow, '提示', '请输入phase')
                if ok_3_s:
                    phase_s = text_3_s
                    data_1_s_s = open('\\\\192.168.1.225\\pm_tool\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
                    data_1_s_s_s = data_1_s_s.read().rstrip("}")
                    data_1_s_s_s_s = str(data_1_s_s_s)
                    data_1_s_s.close()
                    new_data_s = open('\\\\192.168.1.225\\pm_tool\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                    new_data_s_s = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + '!' + sku_s + '!' + '&' + project_s + '&' + '%' + phase_s + '%' + '"' + '}'
                    new_data_s.write(data_1_s_s_s_s + new_data_s_s)
                    new_data_s.close()
                    if project_s == 'L13_AMD' or project_s == 'L13_Intel' or project_s == 'L1415_AMD' or project_s == 'L1415_Intel' or project_s == 'L1415_2_AMD' or project_s == 'L1415_2_Intel' or project_s == 'L13_2_AMD' or project_s == 'L13_2_Intel':
                        data_1_s_y = open('\\\\192.168.1.225\\pm_tool\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\winlrtool.txt')
                        data_1_s_s_y = data_1_s_y.read().rstrip("}")
                        data_1_s_s_s_y = str(data_1_s_s_y)
                        data_1_s_y.close()
                        new_data_ww = open('\\\\192.168.1.225\\pm_tool\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\winlrtool.txt', 'w+')
                        new_data_s_ww = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + project_s + '"' + '}'
                        new_data_ww.write(data_1_s_s_s_y + new_data_s_ww)
                        new_data_ww.close()
                    QMessageBox.information(MainWindow, '提示', '添加成功')

    def ATSLOG(self):
        log_pm = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\PM_CLASS.txt')
        log_pm_1 = log_pm.read()
        log_pm_1_1 = json.loads(log_pm_1)
        log_pm.close()
        if log_pm_1_1[SNnumber] == 'AC MS':
            data_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_1_1 = data_1.read()
            list_1 = json.loads(data_1_1)
            data_1.close()
            if SNnumber in list_1:
                phase_key_1 = list_1[SNnumber]
                moban_1 = re.compile(r'&(.*?)&')
                moban_1_1 = re.compile(r'%(.*?)%')
                moban_1_1_1 = re.compile(r'!(.*?)!')
                phase_1 = moban_1_1.search(phase_key_1).group().replace('%', '')
                project_1 = moban_1.search(phase_key_1).group().replace('&', '')
                SKU_1 = moban_1_1_1.search(phase_key_1).group().replace('!', '')
                path_1 = phase_1 + '_' + 'BIOS#' + biosver
                folder_1 = system + '_' + phase_1 + '_' + SKU_1 + '_' + 'AC' + '_' + 'S0i3' + '_' + curent_time_1
                path_1_1 = phase_1
                message_1 = '当前系统phase为:' + path_1_1 + '是否需要修改?'
                result_1 = QMessageBox.question(MainWindow, '提示', message_1, QMessageBox.Yes | QMessageBox.No)
                if result_1 == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_1, path_1, 'AC_S0i3', folder_1))
                    for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                        try:
                            shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_1, path_1, 'AC_S0i3', folder_1), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))))
                        except FileNotFoundError:
                            time.sleep(1)
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_1) + '"')
                else:
                    text_1, ok_1 = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_1:
                        newphase_1_1 = '%' + text_1 + '%'
                        newphase_1 = text_1
                        new_path_1 = newphase_1 + '_' + 'BIOS#' + biosver
                        new_folder_1 = system + '_' + newphase_1 + '_' + SKU_1 + '_' + 'AC' + '_' + 'S0i3' + '_' + curent_time_1
                        os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_1, new_path_1, 'AC_S0i3', new_folder_1))
                        for file_1 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                            try:
                                shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_1, new_path_1, 'AC_S0i3', new_folder_1), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_1))))
                            except FileNotFoundError:
                                time.sleep(1)
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        phase_1_1 = moban_1_1.search(phase_key_1).group()
                        phase_1_1_1 = list_1[SNnumber].rstrip(phase_1_1)
                        phase_1_1_1_1 = phase_1_1_1 + newphase_1_1
                        list_1[SNnumber] = phase_1_1_1_1
                        list_1_1 = json.dumps(list_1)
                        data_1_1_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_1_1_1.write(list_1_1)
                        data_1_1_1.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_1) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == '  DC MS':
            data_3 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_3_3 = data_3.read()
            list_3 = json.loads(data_3_3)
            data_3.close()
            if SNnumber in list_3:
                phase_key_3 = list_3[SNnumber]
                moban_3 = re.compile(r'&(.*?)&')
                moban_3_3 = re.compile(r'%(.*?)%')
                moban_3_3_3 = re.compile(r'!(.*?)!')
                phase_3 = moban_3_3.search(phase_key_3).group().replace('%', '')
                project_3 = moban_3.search(phase_key_3).group().replace('&', '')
                SKU3 = moban_3_3_3.search(phase_key_3).group().replace('!', '')
                path_3 = phase_3 + '_' + 'BIOS#' + biosver
                folder_3 = system + '_' + phase_3 + '_' + SKU3 + '_' + 'DC' + '_' + 'S0i3' + '_' + curent_time_1
                path_3_3 = phase_3
                message_3 = '当前系统phase为:' + path_3_3 + '是否需要修改?'
                result_3 = QMessageBox.question(MainWindow, '提示', message_3, QMessageBox.Yes | QMessageBox.No)
                if result_3 == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_3, path_3, 'DC_S0i3', folder_3))
                    for file_3 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                        try:
                            shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_3), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_3, path_3, 'DC_S0i3', folder_3), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_3))))
                        except FileNotFoundError:
                            time.sleep(1)
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_3) + '"')
                else:
                    text_3, ok_3 = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_3:
                        newphase_3_3 = '%' + text_3 + '%'
                        newphase_3 = text_3
                        new_path_3 = newphase_3 + '_' + 'BIOS#' + biosver
                        new_folder_3 = system + '_' + newphase_3 + '_' + SKU3 + '_' + 'DC' + '_' + 'S0i3' + '_' + curent_time_1
                        os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_3, new_path_3, 'DC_S0i3', new_folder_3))
                        for file_3 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                            try:
                                shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_3), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_3, new_path_3, 'DC_S0i3', new_folder_3), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_3))))
                            except FileNotFoundError:
                                time.sleep(1)
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        phase_3_3 = moban_3_3.search(phase_key_3).group()
                        phase_3_3_3 = list_3[SNnumber].rstrip(phase_3_3)
                        phase_3_3_3_3 = phase_3_3_3 + newphase_3_3
                        list_3[SNnumber] = phase_3_3_3_3
                        list_3_3 = json.dumps(list_3)
                        data_3_3_3 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_3_3_3.write(list_3_3)
                        data_3_3_3.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_3) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == ' AC S4':
            data_5 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_5_5 = data_5.read()
            list_5 = json.loads(data_5_5)
            data_5.close()
            if SNnumber in list_5:
                phase_key_5 = list_5[SNnumber]
                moban_5 = re.compile(r'&(.*?)&')
                moban_5_5 = re.compile(r'%(.*?)%')
                moban_5_5_5 = re.compile(r'!(.*?)!')
                phase_5 = moban_5_5.search(phase_key_5).group().replace('%', '')
                project_5 = moban_5.search(phase_key_5).group().replace('&', '')
                SKU_5 = moban_5_5_5.search(phase_key_5).group().replace('!', '')
                path_5 = phase_5 + '_' + 'BIOS#' + biosver
                folder_5 = system + '_' + phase_5 + '_' + SKU_5 + '_' + 'AC' + '_' + 'S4' + '_' + curent_time_1
                path_5_5 = phase_5
                message_5 = '当前系统phase为:' + path_5_5 + '是否需要修改?'
                result_5 = QMessageBox.question(MainWindow, '提示', message_5,
                                                QMessageBox.Yes | QMessageBox.No)
                if result_5 == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_5, path_5, 'AC_S4', folder_5))
                    for file_5 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                        try:
                            shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_5), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_5, path_5, 'AC_S4', folder_5), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_5))))
                        except FileNotFoundError:
                            time.sleep(1)
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    if os.path.getsize('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\LongRunATS_AOAC_Log.htm') == 0:
                        os.system('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\sleepstudy.bat')
                        time.sleep(7)
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_5) + '"')
                else:
                    text_5, ok_5 = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_5:
                        newphase_5_5 = '%' + text_5 + '%'
                        newphase_5 = text_5
                        new_path_5 = newphase_5 + '_' + 'BIOS#' + biosver
                        new_folder_5 = system + '_' + newphase_5 + '_' + SKU_5 + '_' + 'AC' + '_' + 'S4' + '_' + curent_time_1
                        os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_5, new_path_5, 'AC_S4', new_folder_5))
                        for file_5 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                            try:
                                shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_5), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_5, new_path_5, 'AC_S4', new_folder_5), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_5))))
                            except FileNotFoundError:
                                time.sleep(1)
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        phase_5_5 = moban_5_5.search(phase_key_5).group()
                        phase_5_5_5 = list_5[SNnumber].rstrip(phase_5_5)
                        phase_5_5_5_5 = phase_5_5_5 + newphase_5_5
                        list_5[SNnumber] = phase_5_5_5_5
                        list_5_5 = json.dumps(list_5)
                        data_5_5_5 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_5_5_5.write(list_5_5)
                        data_5_5_5.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_5) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == 'DC S4':
            data_7 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_7_7 = data_7.read()
            list_7 = json.loads(data_7_7)
            data_7.close()
            if SNnumber in list_7:
                phase_key_7 = list_7[SNnumber]
                moban_7 = re.compile(r'&(.*?)&')
                moban_7_7 = re.compile(r'%(.*?)%')
                moban_7_7_7 = re.compile(r'!(.*?)!')
                phase_7 = moban_7_7.search(phase_key_7).group().replace('%', '')
                project_7 = moban_7.search(phase_key_7).group().replace('&', '')
                SKU_7 = moban_7_7_7.search(phase_key_7).group().replace('!', '')
                path_7 = phase_7 + '_' + 'BIOS#' + biosver
                folder_7 = system + '_' + phase_7 + '_' + SKU_7 + '_' + 'DC' + '_' + 'S4' + '_' + curent_time_1
                path_7_7 = phase_7
                message_7 = '当前系统phase为:' + path_7_7 + '是否需要修改?'
                result_7 = QMessageBox.question(MainWindow, '提示', message_7, QMessageBox.Yes | QMessageBox.No)
                if result_7 == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_7, path_7, 'DC_S4', folder_7))
                    for file_7 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                        try:
                            shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_7), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_7, path_7, 'DC_S4', folder_7), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_7))))
                        except FileNotFoundError:
                            time.sleep(1)
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_7) + '"')
                else:
                    text_7, ok_7 = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_7:
                        newphase_7_7 = '%' + text_7 + '%'
                        newphase_7 = text_7
                        new_path_7 = newphase_7 + '_' + 'BIOS#' + biosver
                        new_folder_7 = system + '_' + newphase_7 + '_' + SKU_7 + '_' + 'DC' + '_' + 'S4' + '_' + curent_time_1
                        os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_7, new_path_7, 'DC_S4', new_folder_7))
                        for file_7 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                            try:
                                shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_7), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_7, new_path_7, 'DC_S4', new_folder_7), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_7))))
                            except FileNotFoundError:
                                time.sleep(1)
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        phase_7_7 = moban_7_7.search(phase_key_7).group()
                        phase_7_7_7 = list_7[SNnumber].rstrip(phase_7_7)
                        phase_7_7_7_7 = phase_7_7_7 + newphase_7_7
                        list_7[SNnumber] = phase_7_7_7_7
                        list_7_7 = json.dumps(list_7)
                        data_7_7_7 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_7_7_7.write(list_7_7)
                        data_7_7_7.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_7) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == ' AC WB':
            data_9 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_9_9 = data_9.read()
            list_9 = json.loads(data_9_9)
            data_9.close()
            if SNnumber in list_9:
                phase_key_9 = list_9[SNnumber]
                moban_9 = re.compile(r'&(.*?)&')
                moban_9_9 = re.compile(r'%(.*?)%')
                moban_9_9_9 = re.compile(r'!(.*?)!')
                phase_9 = moban_9_9.search(phase_key_9).group().replace('%', '')
                project_9 = moban_9.search(phase_key_9).group().replace('&', '')
                SKU_9 = moban_9_9_9.search(phase_key_9).group().replace('!', '')
                path_9 = phase_9 + '_' + 'BIOS#' + biosver
                folder_9 = system + '_' + phase_9 + '_' + SKU_9 + '_' + 'AC' + '_' + 'R' + '_' + curent_time_1
                path_9_9 = phase_9
                message_9 = '当前系统phase为:' + path_9_9 + '是否需要修改?'
                result_9 = QMessageBox.question(MainWindow, '提示', message_9, QMessageBox.Yes | QMessageBox.No)
                if result_9 == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_9, path_9, 'AC_R', folder_9))
                    for file_9 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                        try:
                            shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_9), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_9, path_9, 'AC_R', folder_9), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_9))))
                        except FileNotFoundError:
                            time.sleep(1)
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_9) + '"')
                else:
                    text_9, ok_9 = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_9:
                        newphase_9_9 = '%' + text_9 + '%'
                        newphase_9 = text_9
                        new_path_9 = newphase_9 + '_' + 'BIOS#' + biosver
                        new_folder_9 = system + '_' + newphase_9 + '_' + SKU_9 + '_' + 'AC' + '_' + 'R' + '_' + curent_time_1
                        os.makedirs(
                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_9, new_path_9, 'AC_R', new_folder_9))
                        for file_9 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                            try:
                                shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_9), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_9, new_path_9, 'AC_R', new_folder_9), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_9))))
                            except FileNotFoundError:
                                time.sleep(1)
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        phase_9_9 = moban_9_9.search(phase_key_9).group()
                        phase_9_9_9 = list_9[SNnumber].rstrip(phase_9_9)
                        phase_9_9_9_9 = phase_9_9_9 + newphase_9_9
                        list_9[SNnumber] = phase_9_9_9_9
                        list_9_9 = json.dumps(list_9)
                        data_9_9_9 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_9_9_9.write(list_9_9)
                        data_9_9_9.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_9) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == 'DC WB':
            data_11 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_11_11 = data_11.read()
            list_11 = json.loads(data_11_11)
            data_11.close()
            if SNnumber in list_11:
                phase_key_11 = list_11[SNnumber]
                moban_11 = re.compile(r'&(.*?)&')
                moban_11_11 = re.compile(r'%(.*?)%')
                moban_11_11_11 = re.compile(r'!(.*?)!')
                phase_11 = moban_11_11.search(phase_key_11).group().replace('%', '')
                project_11 = moban_11.search(phase_key_11).group().replace('&', '')
                SKU_11 = moban_11_11_11.search(phase_key_11).group().replace('!', '')
                path_11 = phase_11 + '_' + 'BIOS#' + biosver
                folder_11 = system + '_' + phase_11 + '_' + SKU_11 + '_' + 'DC' + '_' + 'R' + '_' + curent_time_1
                path_11_11 = phase_11
                message_11 = '当前系统phase为:' + path_11_11 + '是否需要修改?'
                result_11 = QMessageBox.question(MainWindow, '提示', message_11, QMessageBox.Yes | QMessageBox.No)
                if result_11 == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_11, path_11, 'DC_R', folder_11))
                    for file_11 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                        try:
                            shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_11), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_11, path_11, 'DC_R', folder_11), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_11))))
                        except FileNotFoundError:
                            time.sleep(1)
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_11) + '"')
                else:
                    text_11, ok_11 = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_11:
                        newphase_11_11 = '%' + text_11 + '%'
                        newphase_11 = text_11
                        new_path_11 = newphase_11 + '_' + 'BIOS#' + biosver
                        new_folder_11 = system + '_' + newphase_11 + '_' + SKU_11 + '_' + 'DC' + '_' + 'R' + '_' + curent_time_1
                        os.makedirs(
                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_11, new_path_11, 'DC_R', new_folder_11))
                        for file_11 in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs'):
                            try:
                                shutil.copytree(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_11), os.path.join(os.path.join('\\\\192.168.1.225', 'LR_Log', project_11, new_path_11, 'DC_R', new_folder_11), os.path.basename(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_AOAC_v6\\Logs', file_11))))
                            except FileNotFoundError:
                                time.sleep(1)
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        phase_11_11 = moban_11_11.search(phase_key_11).group()
                        phase_11_11_11 = list_11[SNnumber].rstrip(phase_11_11)
                        phase_11_11_11_11 = phase_11_11_11 + newphase_11_11
                        list_11[SNnumber] = phase_11_11_11_11
                        list_11_11 = json.dumps(list_11)
                        data_11_11_11 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_11_11_11.write(list_11_11)
                        data_11_11_11.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log', project_11) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == ' FSU':
            data_15 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_15_15 = data_15.read()
            list_15 = json.loads(data_15_15)
            data_15.close()
            if SNnumber in list_15:
                phase_key_15 = list_15[SNnumber]
                moban_15 = re.compile(r'&(.*?)&')
                moban_15_15 = re.compile(r'%(.*?)%')
                moban_15_15_15 = re.compile(r'!(.*?)!')
                phase_15 = moban_15_15.search(phase_key_15).group().replace('%', '')
                project_15 = moban_15.search(phase_key_15).group().replace('&', '')
                SKU_15 = moban_15_15_15.search(phase_key_15).group().replace('!', '')
                path_15 = phase_15 + '_' + 'BIOS#' + biosver
                folder_15 = system + '_' + phase_15 + '_' + SKU_15 + '_' + 'FSU' + '_' + curent_time_1
                path_15_15 = phase_15
                message_15 = '当前系统phase为:' + path_15_15 + '是否需要修改?'
                result_15 = QMessageBox.question(MainWindow, '提示', message_15, QMessageBox.Yes | QMessageBox.No)
                if result_15 == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_15, path_15, 'FSU', folder_15))
                    os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\batteryreport.bat')
                    time.sleep(1)
                    try:
                        shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\EVLogs\\Application.evtx',
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_15, path_15, 'FSU',
                                                 folder_15))
                    except FileNotFoundError:
                        time.sleep(1)
                    try:
                        shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\EVLogs\\System.evtx',
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_15, path_15, 'FSU',
                                                 folder_15))
                    except FileNotFoundError:
                        time.sleep(1)
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    if os.path.getsize(
                            'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\LongRunATS_Shutdown_Log.htm') == 0:
                        os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                        time.sleep(7)
                    for file in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2'):
                        if fnmatch.fnmatch(file, '*.htm') or fnmatch.fnmatch(file, '*.html') or fnmatch.fnmatch(file,
                                                                                                                '*.csv'):
                            shutil.move(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2', file),
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_15, path_15, 'FSU',
                                                     folder_15))
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                   project_15) + '"')
                else:
                    text_15, ok_15 = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_15:
                        newphase_15_15 = '%' + text_15 + '%'
                        newphase_15 = text_15
                        new_path_15 = newphase_15 + '_' + 'BIOS#' + biosver
                        new_folder_15 = system + '_' + newphase_15 + '_' + SKU_15 + '_' + 'FSU' + '_' + curent_time_1
                        os.makedirs(
                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_15, new_path_15, 'FSU', new_folder_15))
                        os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\batteryreport.bat')
                        time.sleep(1)
                        try:
                            shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\EVLogs\\Application.evtx',
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_15, path_15, 'FSU',
                                                     folder_15))
                        except FileNotFoundError:
                            time.sleep(1)
                        try:
                            shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\EVLogs\\System.evtx',
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_15, new_path_15, 'FSU',
                                                     new_folder_15))
                        except FileNotFoundError:
                            time.sleep(1)
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        if os.path.getsize(
                                'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_Log\\LongRunATS_Shutdown_Log.htm') == 0:
                            os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_Log\\sleepstudy.bat')
                            time.sleep(7)
                        for file in os.listdir('C:\\TNB_Integration_Tool\LongRunATS_Shutdown_v5.2'):
                            if fnmatch.fnmatch(file, '*.htm') or fnmatch.fnmatch(file, '*.html') or fnmatch.fnmatch(
                                    file, '*.csv'):
                                shutil.move(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2', file),
                                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_15, new_path_15, 'FSU',
                                                         new_folder_15))
                        phase_15_15 = moban_15_15.search(phase_key_15).group()
                        phase_15_15_15 = list_15[SNnumber].rstrip(phase_15_15)
                        phase_15_15_15_15 = phase_15_15_15 + newphase_15_15
                        list_15[SNnumber] = phase_15_15_15_15
                        list_15_15 = json.dumps(list_15)
                        data_15_15_15 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_15_15_15.write(list_15_15)
                        data_15_15_15.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                       project_15) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == ' S5':
            data_13 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_13_13 = data_13.read()
            list_13 = json.loads(data_13_13)
            data_13.close()
            if SNnumber in list_13:
                phase_key_13 = list_13[SNnumber]
                moban_13 = re.compile(r'&(.*?)&')
                moban_13_13 = re.compile(r'%(.*?)%')
                moban_13_13_13 = re.compile(r'!(.*?)!')
                phase_13 = moban_13_13.search(phase_key_13).group().replace('%', '')
                project_13 = moban_13.search(phase_key_13).group().replace('&', '')
                SKU_13 = moban_13_13_13.search(phase_key_13).group().replace('!', '')
                path_13 = phase_13 + '_' + 'BIOS#' + biosver
                folder_13 = system + '_' + phase_13 + '_' + SKU_13 + '_' + 'S5' + '_' + curent_time_1
                path_13_13 = phase_13
                message_13 = '当前系统phase为:' + path_13_13 + '是否需要修改?'
                result_13 = QMessageBox.question(MainWindow, '提示', message_13, QMessageBox.Yes | QMessageBox.No)
                if result_13 == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_13, path_13, 'S5', folder_13))
                    os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\batteryreport.bat')
                    time.sleep(1)
                    try:
                        shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\EVLogs\\Application.evtx',
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13, path_13, 'S5',
                                                 folder_13))
                    except FileNotFoundError:
                        time.sleep(1)
                    try:
                        shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\EVLogs\\System.evtx',
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13, path_13, 'S5',
                                                 folder_13))
                    except FileNotFoundError:
                        time.sleep(1)
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    if os.path.getsize(
                            'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\LongRunATS_Shutdown_Log.htm') == 0:
                        os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                        time.sleep(7)
                    for file in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2'):
                        if fnmatch.fnmatch(file, '*.htm') or fnmatch.fnmatch(file, '*.html') or fnmatch.fnmatch(file,
                                                                                                                '*.csv'):
                            shutil.move(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2', file),
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13, path_13, 'S5',
                                                     folder_13))
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                   project_13) + '"')
                else:
                    text_13, ok_13 = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_13:
                        newphase_13_13 = '%' + text_13 + '%'
                        newphase_13 = text_13
                        new_path_13 = newphase_13 + '_' + 'BIOS#' + biosver
                        new_folder_13 = system + '_' + newphase_13 + '_' + SKU_13 + '_' + 'S5' + '_' + curent_time_1
                        os.makedirs(
                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_13, new_path_13, 'S5', new_folder_13))
                        os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\batteryreport.bat')
                        time.sleep(1)
                        try:
                            shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\EVLogs\\Application.evtx',
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13, new_path_13, 'S5',
                                                     new_folder_13))
                        except FileNotFoundError:
                            time.sleep(1)
                        try:
                            shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\EVLogs\\System.evtx',
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13, new_path_13, 'S5',
                                                     new_folder_13))
                        except FileNotFoundError:
                            time.sleep(1)
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        if os.path.getsize(
                                'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\LongRunATS_Shutdown_Log.htm') == 0:
                            os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                            time.sleep(7)
                        for file in os.listdir('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2'):
                            if fnmatch.fnmatch(file, '*.htm') or fnmatch.fnmatch(file, '*.html') or fnmatch.fnmatch(
                                    file, '*.csv'):
                                shutil.move(os.path.join('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2', file),
                                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_13, new_path_13, 'S5',
                                                         new_folder_13))
                        phase_13_13 = moban_13_13.search(phase_key_13).group()
                        phase_13_13_13 = list_13[SNnumber].rstrip(phase_13_13)
                        phase_13_13_13_13 = phase_13_13_13 + newphase_13_13
                        list_13[SNnumber] = phase_13_13_13_13
                        list_13_13 = json.dumps(list_13)
                        data_13_13_13 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_13_13_13.write(list_13_13)
                        data_13_13_13.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                       project_13) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == 'WinLRFSU':
            data_13_wf = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_13_13_wf = data_13_wf.read()
            list_13_wf = json.loads(data_13_13_wf)
            data_13_wf.close()
            if SNnumber in list_13_wf:
                phase_key_13_wf = list_13_wf[SNnumber]
                moban_13_wf = re.compile(r'&(.*?)&')
                moban_13_13_wf = re.compile(r'%(.*?)%')
                moban_13_13_13_wf = re.compile(r'!(.*?)!')
                phase_13_wf = moban_13_13_wf.search(phase_key_13_wf).group().replace('%', '')
                project_13_wf = moban_13_wf.search(phase_key_13_wf).group().replace('&', '')
                SKU_13_wf = moban_13_13_13_wf.search(phase_key_13_wf).group().replace('!', '')
                path_13_wf = phase_13_wf + '_' + 'BIOS#' + biosver
                folder_13_wf = system + '_' + phase_13_wf + '_' + SKU_13_wf + '_' + 'WinLRFSU' + '_' + curent_time_1
                path_13_13_wf = phase_13_wf
                message_13_wf = '当前系统phase为:' + path_13_13_wf + '是否需要修改?'
                result_13_wf = QMessageBox.question(MainWindow, '提示', message_13_wf, QMessageBox.Yes | QMessageBox.No)
                if result_13_wf == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wf, path_13_wf, 'WinLRFSU',
                                             folder_13_wf))
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                    time.sleep(3)
                    while True:
                        time.sleep(1)
                        if os.path.exists(
                                'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html') == False:
                            continue
                        shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html',
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wf, path_13_wf, 'WinLRFSU',
                                                 folder_13_wf))
                        break
                    x = os.listdir(r'C:\TNB_Integration_Tool\wiLongRun\output')
                    x_1 = os.path.join(r'C:\TNB_Integration_Tool\wiLongRun\output', x[0])
                    shutil.move(os.path.join(x_1, 'Job0'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wf, path_13_wf, 'WinLRFSU',
                                             folder_13_wf))
                    for file in os.listdir(x_1):
                        shutil.copy(os.path.join(x_1, file),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wf, path_13_wf, 'WinLRFSU',
                                                 folder_13_wf))
                    shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
                    os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                   project_13_wf) + '"')
                else:
                    text_13_wf, ok_13_wf = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_13_wf:
                        newphase_13_13_wf = '%' + text_13_wf + '%'
                        newphase_13_wf = text_13_wf
                        new_path_13_wf = newphase_13_wf + '_' + 'BIOS#' + biosver
                        new_folder_13_wf = system + '_' + newphase_13_wf + '_' + SKU_13_wf + '_' + 'WinLRFSU' + '_' + curent_time_1
                        os.makedirs(
                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wf, new_path_13_wf, 'WinLRFSU',
                                         new_folder_13_wf))
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示',
                                                    '有memorydump生成,若需要请自行在本地收集')
                        os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                        time.sleep(3)
                        while True:
                            time.sleep(1)
                            if os.path.exists(
                                    'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html') == False:
                                continue
                            shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html',
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wf, new_path_13_wf,
                                                     'WinLRFSU', new_folder_13_wf))
                            break
                        x_4 = os.listdir(r'C:\TNB_Integration_Tool\wiLongRun\output')
                        x_5 = os.path.join(r'C:\TNB_Integration_Tool\wiLongRun\output', x_4[0])
                        shutil.move(os.path.join(x_5, 'Job0'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wf, new_path_13_wf,
                                                 'WinLRFSU', new_folder_13_wf))
                        for file in os.listdir(x_5):
                            shutil.copy(os.path.join(x_5, file),
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wf, new_path_13_wf,
                                                     'WinLRFSU', new_folder_13_wf))
                        shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
                        os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
                        phase_13_13_wf = moban_13_13_wf.search(phase_key_13_wf).group()
                        phase_13_13_13_wf = list_13_wf[SNnumber].rstrip(phase_13_13_wf)
                        phase_13_13_13_13_wf = phase_13_13_13_wf + newphase_13_13_wf
                        list_13_wf[SNnumber] = phase_13_13_13_13_wf
                        list_13_13_wf = json.dumps(list_13_wf)
                        data_13_13_13_wf = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_13_13_13_wf.write(list_13_13_wf)
                        data_13_13_13_wf.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                       project_13_wf) + '"')
            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')

        elif log_pm_1_1[SNnumber] == 'WinLRCB':
            data_13_wc = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_13_13_wc = data_13_wc.read()
            list_13_wc = json.loads(data_13_13_wc)
            data_13_wc.close()
            if SNnumber in list_13_wc:
                phase_key_13_wc = list_13_wc[SNnumber]
                moban_13_wc = re.compile(r'&(.*?)&')
                moban_13_13_wc = re.compile(r'%(.*?)%')
                moban_13_13_13_wc = re.compile(r'!(.*?)!')
                phase_13_wc = moban_13_13_wc.search(phase_key_13_wc).group().replace('%', '')
                project_13_wc = moban_13_wc.search(phase_key_13_wc).group().replace('&', '')
                SKU_13_wc = moban_13_13_13_wc.search(phase_key_13_wc).group().replace('!', '')
                path_13_wc = phase_13_wc + '_' + 'BIOS#' + biosver
                folder_13_wc = system + '_' + phase_13_wc + '_' + SKU_13_wc + '_' + 'WinLRCB' + '_' + curent_time_1
                path_13_13_wc = phase_13_wc
                message_13_wc = '当前系统phase为:' + path_13_13_wc + '是否需要修改?'
                result_13_wc = QMessageBox.question(MainWindow, '提示', message_13_wc, QMessageBox.Yes | QMessageBox.No)
                if result_13_wc == QMessageBox.No:
                    os.makedirs(
                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wc, path_13_wc, 'WinLRCB', folder_13_wc))
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                    time.sleep(3)
                    while True:
                        time.sleep(1)
                        if os.path.exists(
                                'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html') == False:
                            continue
                        shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html',
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wc, path_13_wc,
                                                 'WinLRCB', folder_13_wc))
                        break
                    x_8 = os.listdir(r'C:\TNB_Integration_Tool\wiLongRun\output')
                    x_9 = os.path.join(r'C:\TNB_Integration_Tool\wiLongRun\output', x_8[0])
                    shutil.move(os.path.join(x_9, 'Job0'),
                                os.path.
                                join('\\\\192.168.1.225', 'LR_Log', project_13_wc, path_13_wc,
                                     'WinLRCB', folder_13_wc))
                    for file in os.listdir(x_9):
                        shutil.copy(os.path.join(x_9, file),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wc, path_13_wc,
                                                 'WinLRCB', folder_13_wc))
                    shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
                    os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                   project_13_wc) + '"')
                else:
                    text_13_wc, ok_13_wc = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_13_wc:
                        newphase_13_13_wc = '%' + text_13_wc + '%'
                        newphase_13_wc = text_13_wc
                        new_path_13_wc = newphase_13_wc + '_' + 'BIOS#' + biosver
                        new_folder_13_wc = system + '_' + newphase_13_wc + '_' + SKU_13_wc + '_' + 'WinLRCB' + '_' + curent_time_1
                        os.makedirs(
                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wc, new_path_13_wc, 'WinLRCB',
                                         new_folder_13_wc))
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                        time.sleep(3)
                        while True:
                            time.sleep(1)
                            if os.path.exists(
                                    'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html') == False:
                                continue
                            shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html',
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wc, new_path_13_wc,
                                                     'WinLRCB', new_folder_13_wc))
                            break
                        x_12 = os.listdir(r'C:\TNB_Integration_Tool\wiLongRun\output')
                        x_13 = os.path.join(r'C:\TNB_Integration_Tool\wiLongRun\output', x_12[0])
                        shutil.move(os.path.join(x_13, 'Job0'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wc, new_path_13_wc,
                                                 'WinLRCB', new_folder_13_wc))
                        for file in os.listdir(x_13):
                            shutil.copy(os.path.join(x_13, file),
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wc, new_path_13_wc,
                                                     'WinLRCB', new_folder_13_wc))
                        shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
                        os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
                        phase_13_13_wc = moban_13_13_wc.search(phase_key_13_wc).group()
                        phase_13_13_13_wc = list_13_wc[SNnumber].rstrip(phase_13_13_wc)
                        phase_13_13_13_13_wc = phase_13_13_13_wc + newphase_13_13_wc
                        list_13_wc[SNnumber] = phase_13_13_13_13_wc
                        list_13_13_wc = json.dumps(list_13_wc)
                        data_13_13_13_wc = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_13_13_13_wc.write(list_13_13_wc)
                        data_13_13_13_wc.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                       project_13_wc) + '"')

            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')
        elif log_pm_1_1[SNnumber] == 'WinLRCombined':
            data_13_wz = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt')
            data_13_13_wz = data_13_wz.read()
            list_13_wz = json.loads(data_13_13_wz)
            data_13_wz.close()
            if SNnumber in list_13_wz:
                phase_key_13_wz = list_13_wz[SNnumber]
                moban_13_wz = re.compile(r'&(.*?)&')
                moban_13_13_wz = re.compile(r'%(.*?)%')
                moban_13_13_13_wz = re.compile(r'!(.*?)!')
                phase_13_wz = moban_13_13_wz.search(phase_key_13_wz).group().replace('%', '')
                project_13_wz = moban_13_wz.search(phase_key_13_wz).group().replace('&', '')
                SKU_13_wz = moban_13_13_13_wz.search(phase_key_13_wz).group().replace('!', '')
                path_13_wz = phase_13_wz + '_' + 'BIOS#' + biosver
                folder_13_wz = system + '_' + phase_13_wz + '_' + SKU_13_wz + '_' + 'WinLRCombine' + '_' + curent_time_1
                path_13_13_wz = phase_13_wz
                message_13_wz = '当前系统phase为:' + path_13_13_wz + '是否需要修改?'
                result_13_wz = QMessageBox.question(MainWindow, '提示', message_13_wz, QMessageBox.Yes | QMessageBox.No)
                if result_13_wz == QMessageBox.No:
                    os.makedirs(os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    if os.path.exists('C:\\Windows\\Memory.DMP'):
                        QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                    os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                    time.sleep(3)
                    while True:
                        time.sleep(1)
                        if os.path.exists(
                                'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html') == False:
                            continue
                        shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html',
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz,
                                                 'WinLRCombine',
                                                 folder_13_wz))
                        break
                    x_8z = os.listdir(r'C:\TNB_Integration_Tool\wiLongRun\output')
                    x_9z = os.path.join(r'C:\TNB_Integration_Tool\wiLongRun\output', x_8z[0])
                    shutil.move(os.path.join(x_9z, 'Job0'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job1'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job2'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job3'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job4'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job5'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job6'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job7'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job8'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job9'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job10'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job11'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    shutil.move(os.path.join(x_9z, 'Job12'),
                                os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz, 'WinLRCombine',
                                             folder_13_wz))
                    for file in os.listdir(x_9z):
                        shutil.copy(os.path.join(x_9z, file),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, path_13_wz,
                                                 'WinLRCombine', folder_13_wz))
                    shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
                    os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
                    os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                   project_13_wz) + '"')
                else:
                    text_13_wz, ok_13_wz = QInputDialog.getText(MainWindow, '提示', '请输入系统phase')
                    if ok_13_wz:
                        newphase_13_13_wz = '%' + text_13_wz + '%'
                        newphase_13_wz = text_13_wz
                        new_path_13_wz = newphase_13_wz + '_' + 'BIOS#' + biosver
                        new_folder_13_wz = system + '_' + newphase_13_wz + '_' + SKU_13_wz + '_' + 'WinLRCombine' + '_' + curent_time_1
                        os.makedirs(
                            os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz, 'WinLRCombine',
                                         new_folder_13_wz))
                        if os.path.exists('C:\\Windows\\Memory.DMP'):
                            QMessageBox.information(MainWindow, '提示', '有memorydump生成,若需要请自行在本地收集')
                        os.system('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy.bat')
                        time.sleep(3)
                        while True:
                            time.sleep(1)
                            if os.path.exists(
                                    'C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html') == False:
                                continue
                            shutil.move('C:\\TNB_Integration_Tool\\LongRunATS_Shutdown_v5.2\\sleepstudy-report.html',
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                     'WinLRCombine', new_folder_13_wz))
                            break
                        x_12z = os.listdir(r'C:\TNB_Integration_Tool\wiLongRun\output')
                        x_13z = os.path.join(r'C:\TNB_Integration_Tool\wiLongRun\output', x_12z[0])
                        shutil.move(os.path.join(x_13z, 'Job0'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job1'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job2'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job3'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job4'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job5'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job6'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job7'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job8'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job9'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job10'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job11'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        shutil.move(os.path.join(x_13z, 'Job12'),
                                    os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                 'WinLRCombine', new_folder_13_wz))
                        for file in os.listdir(x_13z):
                            shutil.copy(os.path.join(x_13z, file),
                                        os.path.join('\\\\192.168.1.225', 'LR_Log', project_13_wz, new_path_13_wz,
                                                     'WinLRCombine', new_folder_13_wz))
                        shutil.rmtree(r'C:\TNB_Integration_Tool\wiLongRun\output')
                        os.makedirs('C:\\TNB_Integration_Tool\\wiLongRun\\output')
                        phase_13_13_wz = moban_13_13_wz.search(phase_key_13_wz).group()
                        phase_13_13_13_wz = list_13_wz[SNnumber].rstrip(phase_13_13_wz)
                        phase_13_13_13_13_wz = phase_13_13_13_wz + newphase_13_13_wz
                        list_13_wz[SNnumber] = phase_13_13_13_13_wz
                        list_13_13_wz = json.dumps(list_13_wz)
                        data_13_13_13_wz = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v4.0\\SUT_config.txt', 'w+')
                        data_13_13_13_wz.write(list_13_13_wz)
                        data_13_13_13_wz.close()
                        os.system('start' + ' ' + '"' + '"' + ' ' + '"' + os.path.join('\\\\192.168.1.225', 'LR_Log',
                                                                                       project_13_wz + '"'))

            else:
                QMessageBox.information(MainWindow, '提示', r'请先添加机器信息')


if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
