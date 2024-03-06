from pywinauto.application import  Application
import pywinauto
from pywinauto import mouse,keyboard
import os,time,pyautogui,json,wmi
from iupdatable.system.hardware import CSProduct
import shutil
import uiautomation as auto
cycle=open(r'C:\TNB_Integration_Tool\wiLongRun\cycle.txt')
cycle_1=str(cycle.read())
cycle.close()
user=os.getlogin()
inumber = CSProduct.get_identifying_number()
inumber_1 = CSProduct.get_name()
SNnumber = inumber_1 + inumber
pm_list_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v3.0\\PM_CLASS.txt')
pm_list_1_1 = pm_list_1.read()
pm_list_1_1_1 = json.loads(pm_list_1_1)
pm_list_1.close()
shutil.copy(r'C:\TNB_Integration_Tool\wiLongRun\FSU.Scenario',os.path.join('C:\\Users',user,'Documents'))
shutil.copy(r'C:\TNB_Integration_Tool\wiLongRun\CB.Scenario',os.path.join('C:\\Users',user,'Documents'))
if SNnumber not in pm_list_1_1_1:
    pm_class_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v3.0\\PM_CLASS.txt')
    pm_class_1_1 = pm_class_1.read().rstrip("}")
    pm_class_1_1_1 = str(pm_class_1_1)
    pm_class_1.close()
    newpm_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v3.0\\PM_CLASS.txt', 'w+')
    newpm_1_1 = ',' + ' ' + '"' + SNnumber + '"' + ':' + ' ' + '"' + 'WinLRFSU' + '"' + '}'
    newpm_1.write(pm_class_1_1_1 + newpm_1_1)
    newpm_1.close()
    os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    app_open = Application(backend='uia').start(r"C:\TNB_Integration_Tool\wiLongRun\wiLongRun.exe")
    proc_id = pywinauto.application.process_from_module("wiLongRun.exe")
    app_connect = Application(backend='uia').connect(process=proc_id)
    window_tittle = app_connect.window(title='wiLongRun - Wistron Long-Run Tool')
    close = window_tittle.child_window(auto_id="imgClose", control_type="Image")
    close.click_input()
    window_tittle.maximize()
    openfile = window_tittle.child_window(auto_id="btnLoadScenarioFile", control_type="Button").click_input()
    try:
        auto.EditControl(Name='File name:').SendKeys('FSU.Scenario')
    except LookupError:
        auto.EditControl(Name='文件名(N):').SendKeys('FSU.Scenario')
    try:
        window_tittle.child_window(title="Open", auto_id="1", control_type="Button").click_input()
    except pywinauto.findwindows.ElementNotFoundError:
        window_tittle.child_window(title="打开(O)", auto_id="1", control_type="Button").click_input()
    window_tittle_1 = app_connect.window(title='[FSU] wiLongRun')
    window_tittle_1.child_window(title="LilyTNB-CB_DeviceStatusCheck", control_type="Text").click_input()
    window_tittle_1.child_window(title="Stop Conditions", control_type="Text").click_input()
    window_tittle_1.child_window(title="150", auto_id="edMaxLoops", control_type="Edit").type_keys("^a").type_keys(
        cycle_1)
    window_tittle_1.child_window(title="Scenario Settings", control_type="Text").click_input()
    window_tittle_1.child_window(title="CheckedDeviceList", control_type="TabItem").click_input()
    time.sleep(2)
    window_tittle_1.child_window(auto_id="btnRefresh", control_type="Button").click_input()
    time.sleep(2)
    window_tittle_1.child_window(auto_id="RootCheckBox", control_type="CheckBox").click_input()
    place = pyautogui.position()
    time.sleep(2)
    window_tittle_1.child_window(auto_id="edSearch", control_type="Edit").type_keys('MSRRAS')
    window_tittle_1.child_window(auto_id="btnStartSearch", control_type="Button").click_input()
    time.sleep(2)
    window_tittle_2 = window_tittle_1.child_window(auto_id="frameContent", control_type="Pane")
    lists_1 = window_tittle_2.iter_children(control_type="Text")
    lists_new = []
    lists_new_1 = []
    lists_new_2 = []
    lists_new_3 = []
    for everylist in lists_1:
        lists_new.append(everylist.texts()[0])
    for text in lists_new:
        if 'MSRRAS' in text:
            lists_new_1.append(text)
    for text_1 in lists_new_1:
        window_tittle_2.child_window(title=text_1, control_type="Text").click_input()
        loction = window_tittle_2.child_window(title=text_1, control_type="Text").rectangle().mid_point()
        mouse.click(coords=(place.x, loction.y))
    window_tittle_1.child_window(auto_id="edSearch", control_type="Edit").type_keys("^a").type_keys('print')
    window_tittle_1.child_window(auto_id="btnStartSearch", control_type="Button").click_input()
    time.sleep(3)
    window_tittle_3 = window_tittle_1.child_window(auto_id="frameContent", control_type="Pane")
    lists_2 = window_tittle_3.iter_children(control_type="Text")
    for everylist_1 in lists_2:
        lists_new_2.append(everylist_1.texts()[0])
    for text_2 in lists_new_2:
        if 'PRINTENUM' in text_2:
            lists_new_3.append(text_2)
    for text_3 in lists_new_3:
        window_tittle_3.child_window(title=text_3, control_type="Text").click_input()
        loction_1 = window_tittle_3.child_window(title=text_3, control_type="Text").rectangle().mid_point()
        mouse.click(coords=(place.x, loction_1.y))
    window_tittle_1.child_window(auto_id="btnSaveAsScenarioFile", control_type="Button").click_input()
    try:
        window_tittle_1.child_window(title="Save", auto_id="1", control_type="Button").click_input()
        time.sleep(1)
    except pywinauto.findwindows.ElementNotFoundError:
        window_tittle_1.child_window(title="保存(S)", auto_id="1", control_type="Button").click_input()
        time.sleep(1)
    try:
        window_tittle_1.child_window(title="Yes", auto_id="6", control_type="Button").click_input()
    except pywinauto.findwindows.ElementNotFoundError:
        window_tittle_1.child_window(title="是(Y)", auto_id="6", control_type="Button").click_input()
    window_tittle_1.child_window(auto_id="btnStartTest", control_type="Button").click_input()
else:
    pm_list_1_1_1[SNnumber] = 'WinLRFSU'
    pm_list_1_1_1_1 = json.dumps(pm_list_1_1_1)
    pm_list_1_1_1_1_1 = open('C:\\TNB_Integration_Tool\\SetPrerequisites_v3.0\\PM_CLASS.txt', 'w+')
    pm_list_1_1_1_1_1_1 = pm_list_1_1_1_1_1.write(pm_list_1_1_1_1)
    pm_list_1_1_1_1_1.close()
    os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    app_open = Application(backend='uia').start(r"C:\TNB_Integration_Tool\wiLongRun\wiLongRun.exe")
    proc_id = pywinauto.application.process_from_module("wiLongRun.exe")
    app_connect = Application(backend='uia').connect(process=proc_id)
    window_tittle = app_connect.window(title='wiLongRun - Wistron Long-Run Tool')
    close = window_tittle.child_window(auto_id="imgClose", control_type="Image")
    close.click_input()
    window_tittle.maximize()
    openfile = window_tittle.child_window(auto_id="btnLoadScenarioFile", control_type="Button").click_input()
    try:
        auto.EditControl(Name='File name:').SendKeys('FSU.Scenario')
    except LookupError:
        auto.EditControl(Name='文件名(N):').SendKeys('FSU.Scenario')
    try:
        window_tittle.child_window(title="Open", auto_id="1", control_type="Button").click_input()
    except pywinauto.findwindows.ElementNotFoundError:
        window_tittle.child_window(title="打开(O)", auto_id="1", control_type="Button").click_input()
    window_tittle_1 = app_connect.window(title='[FSU] wiLongRun')
    window_tittle_1.child_window(title="LilyTNB-CB_DeviceStatusCheck", control_type="Text").click_input()
    window_tittle_1.child_window(title="Stop Conditions", control_type="Text").click_input()
    window_tittle_1.child_window(title="150", auto_id="edMaxLoops", control_type="Edit").type_keys("^a").type_keys(
        cycle_1)
    window_tittle_1.child_window(title="Scenario Settings", control_type="Text").click_input()
    window_tittle_1.child_window(title="CheckedDeviceList", control_type="TabItem").click_input()
    time.sleep(2)
    window_tittle_1.child_window(auto_id="btnRefresh", control_type="Button").click_input()
    time.sleep(2)
    window_tittle_1.child_window(auto_id="RootCheckBox", control_type="CheckBox").click_input()
    place = pyautogui.position()
    time.sleep(2)
    window_tittle_1.child_window(auto_id="edSearch", control_type="Edit").type_keys('MSRRAS')
    window_tittle_1.child_window(auto_id="btnStartSearch", control_type="Button").click_input()
    time.sleep(2)
    window_tittle_2 = window_tittle_1.child_window(auto_id="frameContent", control_type="Pane")
    lists_1 = window_tittle_2.iter_children(control_type="Text")
    lists_new = []
    lists_new_1 = []
    lists_new_2 = []
    lists_new_3 = []
    for everylist in lists_1:
        lists_new.append(everylist.texts()[0])
    for text in lists_new:
        if 'MSRRAS' in text:
            lists_new_1.append(text)
    for text_1 in lists_new_1:
        window_tittle_2.child_window(title=text_1, control_type="Text").click_input()
        loction = window_tittle_2.child_window(title=text_1, control_type="Text").rectangle().mid_point()
        mouse.click(coords=(place.x, loction.y))
    window_tittle_1.child_window(auto_id="edSearch", control_type="Edit").type_keys("^a").type_keys('print')
    window_tittle_1.child_window(auto_id="btnStartSearch", control_type="Button").click_input()
    time.sleep(3)
    window_tittle_3 = window_tittle_1.child_window(auto_id="frameContent", control_type="Pane")
    lists_2 = window_tittle_3.iter_children(control_type="Text")
    for everylist_1 in lists_2:
        lists_new_2.append(everylist_1.texts()[0])
    for text_2 in lists_new_2:
        if 'PRINTENUM' in text_2:
            lists_new_3.append(text_2)
    for text_3 in lists_new_3:
        window_tittle_3.child_window(title=text_3, control_type="Text").click_input()
        loction_1 = window_tittle_3.child_window(title=text_3, control_type="Text").rectangle().mid_point()
        mouse.click(coords=(place.x, loction_1.y))
    window_tittle_1.child_window(auto_id="btnSaveAsScenarioFile", control_type="Button").click_input()
    try:
        window_tittle_1.child_window(title="Save", auto_id="1", control_type="Button").click_input()
        time.sleep(1)
    except pywinauto.findwindows.ElementNotFoundError:
        window_tittle_1.child_window(title="保存(S)", auto_id="1", control_type="Button").click_input()
        time.sleep(1)
    try:
        window_tittle_1.child_window(title="Yes", auto_id="6", control_type="Button").click_input()
    except pywinauto.findwindows.ElementNotFoundError:
        window_tittle_1.child_window(title="是(Y)", auto_id="6", control_type="Button").click_input()
    window_tittle_1.child_window(auto_id="btnStartTest", control_type="Button").click_input()


































