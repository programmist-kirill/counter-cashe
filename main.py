import os
import platform
import pwd

def main(vsego_degen_user,system):
    print('Всего денег - ', vsego_degen_user)
    if system == 'Linux':
        print('1 - добавить деньги')
        print('2 - отнять деньги')
        deystvie = input('')
        if deystvie == '1':
            vsego_deneg_user = int(vsego_degen_user) + int(input('Введите количество денег - '))
            with open('/home/' + name_user + '/counter_cashe/vsego.log','w') as fp:
                fp.write(str(vsego_deneg_user))
            print('Итог - ', vsego_deneg_user)
            
        if deystvie == '2':
            vsego_deneg_user = int(vsego_degen_user) - int(input('Введите количество денег - '))
            with open('/home/' + name_user + '/counter_cashe/vsego.log','w') as fp:
                fp.write(str(vsego_deneg_user))
            print('Итог - ', vsego_deneg_user)

system = platform.system()
if system == 'Linux':
    uid = os.getuid()
    name_user = pwd.getpwuid(uid).pw_name
    if os.path.exists('/home/' + name_user + '/counter_cashe/vsego.log'):
        directory_to_file = '/home/' + name_user + '/counter_cashe/vsego.log'
        with open(directory_to_file) as file:
            vsego_degen_user = file.read()
        
        main(vsego_degen_user,system)
    else:
        vsego_degen_user = input('Сколько денег у вас - ')
        with open('/home/' + name_user + '/counter_cashe/vsego.log','w') as file:
            file.write(vsego_degen_user)
        
        main(vsego_degen_user,system)

if system == 'Windows':
    disk_in_program = input('на каком диске хранится программа - ')
    if os.path.exists(disk_in_program + 'Program Files/counter_cashe/vsego.log'):
        directory_to_file = disk_in_program + 'Program Files/counter_cashe/vsego.log'
        with open(directory_to_file) as file:
            vsego_degen_user = file.read()
        
        main(vsego_degen_user,system)

    else:
        vsego_degen_user = input('Сколько денег у вас - ')
        with open(disk_in_program + 'Program Files/counter_cashe/vsego.log','w') as file:
            file.write(vsego_degen_user)
        
        main(vsego_degen_user,system)