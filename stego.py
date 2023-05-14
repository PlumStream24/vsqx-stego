import xml.etree.ElementTree as ET

ns = '{http://www.yamaha.co.jp/vocaloid/schema/vsq4/}'


filename = input('Enter VSQx file name: ') or 'Glow.vsqx'

msg = input('Enter message: ')
msg_arr = bytes(msg, 'utf-8')
msg_length = len(msg_arr)

try :
    tree = ET.parse(filename)
except:
    print(f'Error: No such file or directory {filename}.')
    exit()

root = tree.getroot()
#vsTrack = root.find(f'{ns}vsTrack')
#vsPart = vsTrack.find(f'{ns}vsPart')

note_length = len(root.findall(f'.//{ns}nStyle'))

if (msg_length > note_length) :
    print('Error: Message is too long.')
    print(f'msg_length = {msg_length}, note_length = {note_length}')
    exit()

i = 0
for nStyle in root.iter(f'{ns}nStyle'):
    #nStyle = note.find(f'{ns}nStyle')

    if (i < msg_length) :
        new_v = ET.Element('v', {'id': 'stego'})
        new_v.text = str(msg_arr[i])

        nStyle.append(new_v)
        
    elif (i == msg_length) :
        new_v = ET.Element('v', {'id': 'stego'})
        new_v.text = '1000'

        nStyle.append(new_v)
        break

    i += 1

ET.register_namespace('', "http://www.yamaha.co.jp/vocaloid/schema/vsq4/")
#tree.write('output.vsqx', encoding="UTF-8", xml_declaration=True)
