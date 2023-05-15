import xml.etree.ElementTree as ET

ns = '{http://www.yamaha.co.jp/vocaloid/schema/vsq4/}'

filename = input('Enter VSQx file name: ') or 'output_exp.vsqx'
msg_arr = []

try :
    tree = ET.parse(filename)
except:
    print(f'Error: No such file or directory {filename}.')
    exit()
root = tree.getroot()

for nStyle in root.iter(f'{ns}nStyle'):

    byte1 = nStyle.find('*[@id="decay"]')
    if (byte1 == None) :
        continue
    if (byte1.text == '1000'):
        break

    msg_arr.append(int(byte1.text))

    byte2 = nStyle.find('*[@id="opening"]')
    if (byte1 == None) :
        continue

    msg_arr.append(int(byte2.text))

msg_ret = bytearray(msg_arr).decode('utf-8')
print(msg_ret)