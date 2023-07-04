# Purpose :- Creates JSON file required for HCL ONETEST automation verse
# Requirements python to be installed
import configparser,os,sys
config=configparser.RawConfigParser()
serverName=sys.argv[1]
config.read('create_json.properties')
new=config.get('server_path',serverName)
a=new.split(',')
mailServer=a[0]
userPassword=a[1]
cwd=os.getcwd()
str_LDIFPath=a[2]
cwd_ldif=cwd.replace('\\','\\\\')
whole_ldif=cwd_ldif+"\\\\"+str_LDIFPath
str1='{"mailServer":'
str2='"userPassword":'
str3='"str_LDIFPath":'
str4='}'
os.chdir('C:\\tmp')
files=os.path.isfile('jsonconf_verse.json')
if files==True :
    print("Jsonconf_verse file already exists deleting the file and will create new file")
    os.remove('jsonconf_verse.json')
print(str1+'"'+str(mailServer)+'"'+','+str2+'"'+str(userPassword)+'"'+','+str3+'"'+str(whole_ldif)+'"'+str4)
complete=str1+'"'+str(mailServer)+'"'+','+str2+'"'+str(userPassword)+'"'+','+str3+'"'+str(whole_ldif)+'"'+str4
with open ('jsonconf_verse.json','w') as verse_conf :
    verse_conf.writelines(complete)
print(mailServer)
print(userPassword)
print(whole_ldif)
