#Password Bank Project


def append_new_tag():
    with open('storage.txt','a') as f:
        UserName= input('please enter username')
        Password= input('please enter password')
        Detail= input('please enter Detail')
        UserNameC= ('UserName:'+ UserName + '\n')
        PasswordC= ('Password:'+ Password + '\n')
        DetailC= ('Detail:' + Detail + '\n')
        f.write(UserNameC)
        f.write(PasswordC)
        f.write(DetailC)
        print('your things have been saved')
        return

    


def read_info():
    tag= input('please input the username you want to search up')
    with open('storage.txt','r') as r:
        lines = r.readlines()
        tag_list=[]
        cnt= 0
        for line in lines:
            if tag in line:
                tag_list.append(lines[cnt])
                tag_list.append(lines[cnt+1])
                tag_list.append(lines[cnt+2])
            if cnt < (len(lines)-3):
                cnt=cnt+1
            else:
                pass
        clean_list=[]
        for item in tag_list:
            clean_item= item.strip('\n')
            clean_list.append(clean_item)
        print(clean_list)
        return
    


def dex_info_comp(search_para):
     with open('storage.txt') as d:
            lines= d.readlines()
            dex_list=[]
            for line in lines:
                if search_para in line:
                    line_add= line.strip('\n')
                    dex_list.append(line_add)
            print(dex_list)


def dex_info():
    parameter= input(' Please type , UserName, Password, or Detail (care: case sens):')
    correct_input = ['UserName', 'Password', 'Detail']
    if parameter in correct_input:
        dex_info_comp(parameter)
        return
    else:
        print('sry that was not a valid command, please check for correct case sens')
        return

     

while True:
    selection = input('please type, new, find, or dex:').lower()
    if selection == 'new':
        append_new_tag()
    elif selection == 'find':
        read_info()
    elif selection =="dex":
            dex_info()
    else:
        print('you must input one of the three commands')





