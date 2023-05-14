import xml.etree.ElementTree as ET

ns = '{http://www.yamaha.co.jp/vocaloid/schema/vsq4/}'

filename = input('Enter VSQx file name: ') or 'output.vsqx'
msg_arr = []

try :
    tree = ET.parse(filename)
except:
    print(f'Error: No such file or directory {filename}.')
    exit()
root = tree.getroot()

for nStyle in root.iter(f'{ns}nStyle'):

    byte = nStyle.find('*[@id="stego"]')
    if (byte == None) :
        continue
    if (byte.text == '1000'):
        break

    msg_arr.append(int(byte.text))

msg_ret = bytearray(msg_arr).decode('utf-8')
print(msg_ret)