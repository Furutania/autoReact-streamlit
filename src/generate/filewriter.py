import re



def write_to_file(code, tempdir):
    #finds start file flag
    seperated= re.split('START_FILE:', code)
    for i in seperated:
        start = i.split('\n', 1)
        #uses regex to find file name
        filename = re.findall(r'\b\w+\.(?:js|css)\b', start[0])

        if len(filename) > 0:
            #finds end file flag
            code = start[1:][0].split('/*END_FILE:',1)
            file = open(f'{tempdir}/{filename[0]}', 'w')
            file.write(code[0])
            print(f'{tempdir}/{filename[0]}')

