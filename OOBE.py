import time
import uiautomation as auto
import os
import wmi,sys
user=os.getlogin()
SysVersion = wmi.WMI()
version = SysVersion.Win32_OperatingSystem()[0].BuildNumber
product=SysVersion.Win32_OperatingSystem()[0].Caption
class CreatPage:

    def __init__(self, header, control, name):
        self.header = header
        self.control = control
        self.name = name

    def do(self, control, name):
        if control == "Button_pwd":
           if len(sys.argv)==2:
                    auto.SendKeys('Tnb12345')
                    time.sleep(1)
                    auto.ButtonControl(Name=name).Click()
                    auto.SendKeys('Tnb12345')
                    time.sleep(1)
                    auto.ButtonControl(Name=name).Click()
                    x = open('c:\\wwan.txt','w+')
                    x.close()
           else:
                auto.ButtonControl(Name=name).Click()
        elif control == "Button":
            auto.ButtonControl(Name=name).Click()
        elif control == "EditUser":
            auto.EditControl(Name=name).Click()
            auto.EditControl(Name=name).SendKeys('LongRun')
            auto.ButtonControl(Name="下一页").Click()
        elif control == "Editpwd":
            auto.EditControl(Name=name).Click()
            auto.EditControl(Name=name).SendKeys('Tnb12345')
            auto.ButtonControl(Name="下一页").Click()
        elif control == "combom":
            auto.ComboBoxControl(Name="Security question (1 of 3)").Click()
            time.sleep(1)
            auto.ListItemControl(Name="What was your first pet’s name?").Click()
            time.sleep(1)
            auto.EditControl(Name="Your answer").Click()
            time.sleep(1)
            auto.SendKeys("TNB")
            time.sleep(1)
            auto.ButtonControl(Name=name).Click()
            auto.ComboBoxControl(Name="Security question (2 of 3)").Click()
            time.sleep(1)
            auto.ListItemControl(Name="What was your childhood nickname?").Click()
            time.sleep(1)
            auto.EditControl(Name="Your answer").Click()
            time.sleep(1)
            auto.SendKeys("TNB_1")
            time.sleep(1)
            auto.ButtonControl(Name=name).Click()
            auto.ComboBoxControl(Name="Security question (3 of 3)").Click()
            time.sleep(1)
            auto.ListItemControl(Name="What’s the first name of your oldest cousin?").Click()
            time.sleep(1)
            auto.EditControl(Name="Your answer").Click()
            time.sleep(1)
            auto.SendKeys("TNB_2")
            time.sleep(1)
            auto.ButtonControl(Name=name).Click()
        elif control == "combomGSKU":
            auto.ComboBoxControl(Name="安全问题(1/3)").Click()
            time.sleep(1)
            auto.ListItemControl(Name="你第一个宠物的名字是什么?").Click()
            time.sleep(1)
            auto.EditControl(Name="你的答案").Click()
            time.sleep(1)
            auto.SendKeys("TNB")
            time.sleep(1)
            auto.ButtonControl(Name=name).Click()
            auto.ComboBoxControl(Name="安全问题(2/3)").Click()
            time.sleep(1)
            auto.ListItemControl(Name="你出生城市的名称是什么?").Click()
            time.sleep(1)
            auto.EditControl(Name="你的答案").Click()
            time.sleep(1)
            auto.SendKeys("TNB_1")
            time.sleep(1)
            auto.ButtonControl(Name=name).Click()
            auto.ComboBoxControl(Name="安全问题(3/3)").Click()
            time.sleep(1)
            auto.ListItemControl(Name="你孩童时期的昵称是什么?").Click()
            time.sleep(1)
            auto.EditControl(Name="你的答案").Click()
            time.sleep(1)
            auto.SendKeys("TNB_2")
            time.sleep(1)
            auto.ButtonControl(Name=name).Click()
        elif control == "Hyperlink":
            auto.HyperlinkControl(Name=name).Click()
        elif control == "SendKeys":
            auto.SendKeys(name)
        elif control == "Edit":
            auto.EditControl(Name=name).Click()
            auto.EditControl(Name=name).SendKeys('LongRun')
            auto.ButtonControl(Name="Next").Click()
        elif control=="privacy":
            try:
                auto.SendKeys('{Enter}')
                time.sleep(1)
                auto.SendKeys('{Enter}')
                time.sleep(1)
                auto.ButtonControl(Name=name).Click()
            except LookupError:
                auto.ButtonControl(Name='Next, tab through all privacy settings to continue').Click()
                time.sleep(2)
                auto.ButtonControl(Name='Next, tab through all privacy settings to continue').Click()
                time.sleep(2)
                auto.ButtonControl(Name=name).Click()
def PageClick(Pagelist, Text):
    for p in Pagelist:
        if p.header == Text:
            p.do(p.control, p.name)
            break



if __name__ == "__main__":
    if int(version) >= 20000:
        auto.ButtonControl(Name="Yes").Click()
        Page1 = CreatPage("Is this the right country or region?",
                          "Button", "Yes")
        Page2 = CreatPage("Is this the right keyboard layout or input method?",
                          "Button", "Yes")
        Page3 = CreatPage("Want to add a second keyboard layout?",
                          "Button", "Skip adding a second keyboard layout")
        Page4 = CreatPage("Let's connect you to a network",
                          "Hyperlink", "I don't have internet")
        Page5 = CreatPage("Connect now to quickly get started on your device",
                          "Button", "Continue with limited setup")
        Page6 = CreatPage("Please review the License Agreement","SendKeys", "{Enter}")
        Page7 = CreatPage("Who’s going to use this device?","Edit", "Enter your name")
        Page8 = CreatPage("Create a super memorable password","Button_pwd", "Next")
        Page9 = CreatPage("Choose privacy settings for your device","privacy", "Accept all privacy settings")
        Page11 = CreatPage("Protect your device", "Button", "Skip")
        Page12 = CreatPage("Now add security questions", "combom", "Next")
        Page13 = CreatPage("Want to use your fingerprint to sign in faster and more securely?", "Button", "Skip for now")
        Pagelist = [Page1,Page2,Page3,Page4,Page5,
                    Page6,Page7,Page8,Page9,Page11,Page12,Page13]
    elif int(version) < 20000 and '神州' not in product:

        Page1 = CreatPage("Continue in selected language?","Button", "Yes")
        Page2 = CreatPage("Let’s start with region. Is this right?", "Button", "Yes")
        Page3 = CreatPage("Is this the right keyboard layout?","Button", "Yes")
        Page4 = CreatPage("Want to add a second keyboard layout?","Button", "Skip")
        Page5 = CreatPage("Let's connect you to a network","Hyperlink","I don't have internet")
        Page6 = CreatPage("There’s more to discover when you connect to the internet","Button", "Continue with limited setup")
        Page7 = CreatPage("Windows 10 License Agreement","SendKeys", "{Enter}")
        Page8 = CreatPage("Who’s going to use this PC?",
                          "Edit", "Name")
        Page9= CreatPage("Create a super memorable password",
                          "Button_pwd", "Next")
        Page10 = CreatPage("Choose privacy settings for your device",
                          "Button", "Accept")
        Page11 = CreatPage("Let Cortana help you get things done",
                           "Button", "Not now")
        Page14 = CreatPage("Protect your device", "Button", "Skip")
        Page15 = CreatPage("Create security questions for this account", "combom", "Next")
        Page16 = CreatPage("Use your fingerprint to sign in faster and more securely", "Button",
                           "Skip for now")
        
        Pagelist = [Page1, Page2, Page3, Page4, Page5,
                    Page6, Page7, Page8, Page9, Page10, Page11,Page14,Page15,Page16]
    elif '神州' in product:
        Page2 = CreatPage("谁将会使用这台电脑?", "EditUser", '姓名')
        Page3 = CreatPage("创建容易记住的密码", "Editpwd", '密码')
        Page4 = CreatPage("确认你的密码", "Editpwd", "确认密码")
        Page5 = CreatPage("为此帐户创建安全问题", "combomGSKU", "下一页")
        Page6 = CreatPage("为你的设备选择隐私设置", "Button", "接受")
        Pagelist = [Page2, Page3, Page4, Page5,
                    Page6]

    while os.system('tasklist | findstr WWAHost.exe')==0:
        Text = auto.TextControl(FrameworkId='MicrosoftEdge').Name
        PageClick(Pagelist, Text)
    
