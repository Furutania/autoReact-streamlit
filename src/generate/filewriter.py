import re

# def write_to_file(code, tempdir):
#     files = split(code)

def write_to_file(code, tempdir):
    seperated= re.split('START_FILE:', code)
    filenames = []
    for i in seperated:
        start = i.split('\n', 1)
        filename = re.findall(r'\b\w+\.(?:js|css)\b', start[0])

        if len(filename) > 0:
            code = start[1:][0].split('/*END_FILE:',1)
            # print(code[0])
            file = open(f'{tempdir}/{filename[0]}', 'w')
            file.write(code[0])
            print(f'{tempdir}/{filename[0]}')

