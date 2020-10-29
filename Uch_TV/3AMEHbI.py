#!/usr/bin/env python3

# for Unix systems make executable: chmod +x filename

import datetime, time, sys
import ftplib
import telnetlib
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import pyautogui
import paramiko


print('\nПРОГРАММА ЗАМЕЩЕНИЯ ДЛЯ ОБЛАСТНОГО ОДНОЧАСОВОГО ВЕЩАНИЯ')
print('- '*25,'\n')

#-- стандартный шаблон:
channel_ovveride ='''@UCS

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 1;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 331;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 341;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 16:00:00;                    ! Activation Time
ET = DD-MMM-YYYY 16:20:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 211;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 2;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 331;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 343;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:00:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 213;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 3;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 302;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 303;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 4;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 326;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 301;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 5;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 327;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 304;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 6;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 329;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 306;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 7;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 355;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 311;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 8;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 360;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 302;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 9;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 389;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 300;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 10;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 403;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 312;                    ! Tier
}
'''

#-- УЧЕБНОЕ ТВ ПО КАЗАХСТАНУ (ПН-ПТ 9:00 - 17:00)
channel_ovveride_UCH_TV ='''
CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = evt_num;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 327;                    ! Destination channel channel number
}
AT = TO-MOR-ROWS 09:00:00;                    ! Activation Time
ET = TO-MOR-ROWS 17:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 9;                    ! Tier
}
'''

# ПРОВЕРКА В 14:30 (ВРЕМЕННО ОТКЛЮЧЕНА)
'''
CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 11;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 327;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 14:30:00;                    ! Activation Time
ET = DD-MMM-YYYY 14:31:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 1;                    ! Tier
}
'''

#-- субботняя добавка к пятнице:
channel_ovveride_SATURDAY ='''
CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 12;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 327;                    ! Destination channel channel number
}
AT = DD-SAT-YYYY 14:30:00;                    ! Activation Time
ET = DD-SAT-YYYY 14:31:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 1;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 13;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 331;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 341;                    ! Destination channel channel number
}
AT = DD-SAT-YYYY 16:00:00;                    ! Activation Time
ET = DD-SAT-YYYY 16:20:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 211;                    ! Tier
}
'''

#-- получаем текущую дату
dict_month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'}

today_str = str(datetime.date.today().day) + '-' + dict_month[datetime.date.today().month] + '-' + str(datetime.date.today().year)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
next_monday = datetime.date.today() + datetime.timedelta(days=3)
tomorrow_str = str(tomorrow.day) + '-' + dict_month[tomorrow.month] + '-' + str(tomorrow.year)
next_monday_str = str(next_monday.day) + '-' + dict_month[next_monday.month] + '-' + str(next_monday.year)

#-- исходя из текущей даты комбинируем шаблон для работы и записываем в файл
to_work = ''

#-- если сегодня ПЯТНИЦА, то добавить субботнее радио и уч.ТВ на понедельник...
if datetime.datetime.today().weekday() == 4:
    to_work = channel_ovveride + channel_ovveride_SATURDAY + channel_ovveride_UCH_TV
elif datetime.datetime.today().weekday() == 5:
    print ('\nСЕГОДНЯ, ОДНАКО, СУББОТА!!!')
    sys.exit()          
else:
    to_work = channel_ovveride + channel_ovveride_UCH_TV

print('\nСЕГОДНЯ: ',datetime.datetime.today().replace(microsecond=0),'\n'*2)

to_work = to_work.replace('DD-MMM-YYYY', today_str)
to_work = to_work.replace('DD-SAT-YYYY', tomorrow_str)
if datetime.datetime.today().weekday() < 4:
    to_work = to_work.replace('TO-MOR-ROWS', tomorrow_str).replace('evt_num', str(datetime.datetime.today().weekday() + 30))
elif datetime.datetime.today().weekday() == 4:
    to_work = to_work.replace('TO-MOR-ROWS', next_monday_str).replace('evt_num', str(datetime.datetime.today().weekday() + 33))
    

scr_file = today_str + '.SCR;1'
blk_file = today_str + '.BLK;1'
log_file = blk_file.replace('BLK','LOG')

with open(scr_file, 'w') as newfile:
    
    for string in to_work: newfile.write(string)


# Загрузка .SCR файла по FTP на KATEL2 и KATEL3
# - - - - - - - - - - - - - - - - - - - - - - - 
print('ГРУЗИМ ФАЙЛ: ', scr_file, ' по FTP на KATEL2 и KATEL3','\n')
KATEL2 = '172.31.176.4'
KATEL3 = '172.31.177.4'

path = 'sys$sysdevice:[dc2.ucs.script]'

ftp = ftplib.FTP(KATEL2, 'ucsmanager', 'gotalife')
ftp.cwd(path)
with open(scr_file, 'rb') as file:
    ftp.storbinary('STOR ' + scr_file, file)
ftp.close()
print('for KATEL2 ... DONE!\n')

ftp = ftplib.FTP(KATEL3, 'ucsmanager', 'gotalife')
ftp.cwd(path)
with open(scr_file, 'rb') as file:
    ftp.storbinary('STOR ' + scr_file, file)
ftp.close()
print('for KATEL3 ... DONE!\n')



# TELNET - - - - - - - - - - - - - - - - - - - -
def telnet_script(host):
    #print ('\nhost: \n', host)
    if host == '172.31.176.4': hostname = 'KATEL2'
    if host == '172.31.177.4': hostname = 'KATEL3'
    print('\n на ', hostname, ': \n')
    rmt_scr_file = bytes(path + scr_file, 'utf-8')
    #print('rmt_scr_file =', rmt_scr_file)
    rmt_blk_file = bytes('sys$sysdevice:[dc2.ucs.bulk]' + blk_file, 'utf-8')
    #print('rmt_blk_file =', rmt_blk_file)
    rmt_log_file = bytes('dir ' + 'sys$sysdevice:[dc2.ucs.bulk]' + log_file + ' /size', 'utf-8')
    #print('rmt_log_file =', rmt_log_file)
    
    print('=>{} 1. telnet({})'.format(host,host))
    telnet = telnetlib.Telnet(host)

    print('=>{} 2. Username:'.format(host))
    telnet.read_until(b'Username:')

    print('=>{} 3. ucsmanager'.format(host))
    telnet.write(b'ucsmanager\r\n')

    print('=>{} 4. Password:'.format(host))
    telnet.read_until(b'Password:')

    print('=>{} 5. gotalife'.format(host))
    telnet.write(b'gotalife\r\n')

    print('=>{} 6. time.sleep(3)'.format(host))
    time.sleep(3)

    print('=>{} 7. (UCSMANAGER)$'.format(host))
    telnet.read_until(b'(UCSMANAGER)$')

    #-- ucs_bulktxt
    print('=>{} 8. ucs_bulktxt'.format(host))
    telnet.write(b'ucs_bulktxt\r\n')
    print('=>{} 9. time.sleep(1)'.format(host))
    time.sleep(1)

    #-- Log message contents (y or n)? y
    print('=>{} 10. Log message contents (y or n)?'.format(host))
    telnet.read_until(b'?')
    print('=>{} 11. y'.format(host))
    telnet.write(b'y\r\n')
    print('=>{} 12. time.sleep(1)'.format(host))
    time.sleep(1)

    #-- Enter bulk file specification:
    print('=>{} 13. Enter bulk file specification:'.format(host))
    telnet.read_until(b'specification:')
    print('=>{} 14. {}'.format(host,rmt_blk_file))
    telnet.write(rmt_blk_file + b'\r\n')
    print('=>{} 15. time.sleep(3)'.format(host))
    time.sleep(3)

    #-- Enter text file specification:
    print('=>{} 16. Enter text file specification:'.format(host))
    #telnet.read_until(b'specification:')
    print('=>{} 17. {}'.format(host,rmt_scr_file))
    telnet.write(rmt_scr_file + b'\r\n')
    print('=>{} 18. time.sleep(1)'.format(host))
    time.sleep(1)

    #-- Another file (y or n)? n
    print('=>{} 19. Another file (y or n)?'.format(host))
    telnet.read_until(b'?')
    print('=>{} 20. n'.format(host))
    telnet.write(b'n\r\n')
    print('=>{} 21. time.sleep(1)'.format(host))
    time.sleep(1)

    #-- ucs_offbulk
    print('=>{} 22. $'.format(host))
    telnet.read_until(b'$')
    print('=>{} 23. ucs_offbulk'.format(host))
    telnet.write(b'ucs_offbulk\r\n')
    print('=>{} 24. time.sleep(1)'.format(host))
    time.sleep(1)

    #-- bulk-файл для обрабокти
    print('=>{} 25. File name (64 char max) :'.format(host))
    telnet.read_until(b':')
    print('=>{} 26. {}'.format(host,rmt_blk_file))
    telnet.write(rmt_blk_file + b'\r\n')
    print('=>{} 27. time.sleep(1)'.format(host))
    time.sleep(1)

    #-- Y - для подтверждения
    print('=>{} 28. Y'.format(host))
    telnet.write(b'Y\r\n')
    print('=>{} 29. (UCSMANAGER)$'.format(host))
    telnet.read_until(b'(UCSMANAGER)$')
    print('=>{} 30. time.sleep(3)'.format(host))
    time.sleep(3)

    #-- проверка лог-файла на ошибки (если 0 - нет ошибок)
    #- - - - - - - - - - - - - - - - - - - - - - - - - - -
    print('=>{} 31. {}'.format(host,rmt_log_file))
    telnet.write(rmt_log_file + b'\r\n')
    print('=>{} 32. time.sleep(3)'.format(host))
    time.sleep(3)

    print('=>{} 33. ...проверка... \n'.format(host))
    check_log = telnet.read_until(b'(UCSMANAGER)$')
    print(check_log, '\n')
    print(check_log.split()[-4] + b' ' + check_log.split()[-3], '\n', '`'*20)
    if check_log.split()[-4] == b'0': print('\n', hostname, ' (', host,')\n','БЕЗ ОШИБОК!!! \n ВСЁ ОТЛИЧНО!!! \n ЗАПИШИТЕ ВСЁ В ЖУРНАЛ!!!\n')
    else: print('ЕСТЬ ОШИБКИ!!! \n НУЖНА ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА!!!\n')
        
    return {host: check_log.split()[-4] + b' ' + check_log.split()[-3]}

#-- Разделение на потоки (2)
def thread_execution (function, host_dic):
     
    with ThreadPoolExecutor(max_workers=2) as executor:
        #print('ThreadPoolExecutor works with function: {} and host_dic: {}'.format(function, host_dic))
        th_exe_res = executor.map(function, host_dic)        
    return list(th_exe_res)


print('\n','УДАЛЕННО ПО ТЕЛНЕТ ЗАПУСКАЕМ СКРИПТЫ В ДВА ПОТОКА:','\n')
host_dic = {KATEL2:'KATEL2', KATEL3:'KATEL3'}
results = thread_execution(telnet_script, host_dic)
print('\nлог-файлы транзакций скриптов: \n (если размер 0 блоков, значит без ошибок)')
pprint(results)


dict_weekday = {0:'ПОНЕДЕЛЬНИК', 1:'ВТОРНИК', 2:'СРЕДУ', 3:'ЧЕТВЕРГ', 4:'ПЯТНИЦУ', 5:'СУББОТУ', 6:'ВОСКРЕСЕНЬЕ'}
dict_month = {1:'ЯНВАРЯ', 2: 'ФЕВРАЛЯ', 3: 'МАРТА', 4: 'АПРЕЛЯ', 5: 'МАЯ', 6: 'ИЮНЯ', 7: 'ИЮЛЯ', 8: 'АВГУСТА', 9: 'СЕНТЯБРЯ', 10: 'ОКТЯБРЯ', 11: 'НОЯБРЯ', 12: 'ДЕКАБРЯ'}

info_phrase = '\nРАСПИСАНИЕ ЗАМЕН НА {}, {} СОСТАВЛЕНО, ПРОВЕРЬТЕ, ПОЖАЛУЙСТА!'.format(dict_weekday[datetime.datetime.today().weekday()], str(datetime.date.today().day)+' '+dict_month[datetime.date.today().month]+' '+str(datetime.date.today().year)+'г.')


# через заббикс, который мониторит содержимое файла /zbx-msg, оповестить операторов:

ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.31.88.103',
            username='root',
            password='centos7_2017',
            look_for_keys=False,
            allow_agent=False)
ssh.exec_command('echo "{} ...далее: Подтвердить [v] и Закрыть проблему [v]" > /zbx-msg'.format(info_phrase))
print('файл /zbx-msg для заббикс-сообщения изменён')
ssh.close()

pyautogui.alert(text=info_phrase, title = 'Инфо', button = 'OK')
