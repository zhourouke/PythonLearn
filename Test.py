import itchat,time,xlwt
#自动登录 -- 命令行二维码
itchat.auto_login(hotReload=True, enableCmdQR=True)
itchat.dump_login_status()

subscription = itchat.get_mps(update=True)
subscription1 = itchat.search_mps(name='Wowpaper')

print(subscription)
print(subscription1)
