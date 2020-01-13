import wmi

c = wmi.WMI()
for s in c.Win32_Service (StartMode="Auto", State="Stopped"):
    if input("Restart {}? ".format(s.Caption)).upper() == "Y":
        s.StartService()
    else:
        print("Service non démarré.")