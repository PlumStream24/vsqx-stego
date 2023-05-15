import xml.etree.ElementTree as ET

ns = '{http://www.yamaha.co.jp/vocaloid/schema/vsq4/}'


filename = input('Enter VSQx file name: ') or 'Glow.vsqx'

msg = input('Enter message: ') or 'HIDDEN_MESSAGE_HIDDEN_MESSAGE'
msg_arr = bytes(msg, 'utf-8')
msg_length = len(msg_arr)

try :
    tree = ET.parse(filename)
except:
    print(f'Error: No such file or directory {filename}.')
    exit()

root = tree.getroot()

note_length = len(root.findall(f'.//{ns}nStyle'))

if (msg_length > note_length) :
    print('Error: Message is too long.')
    print(f'msg_length = {msg_length}, note_length = {note_length}')
    exit()

i = 0
for nStyle in root.iter(f'{ns}nStyle'):

    if (i < msg_length) :
        new_v1 = nStyle.find('*[@id="decay"]')
        new_v2 = nStyle.find('*[@id="opening"]')
        if (i+1 >= msg_length) :
            new_v1.text = str(msg_arr[i])
        else :
            new_v1.text = str(msg_arr[i])
            new_v2.text = str(msg_arr[i+1])
        
    elif (i >= msg_length) :
        new_v = nStyle.find('*[@id="decay"]')
        new_v.text = '1000'
        break

    i += 2

ET.register_namespace('', "http://www.yamaha.co.jp/vocaloid/schema/vsq4/")
tree.write('output_exp.vsqx', encoding="UTF-8", xml_declaration=True)
