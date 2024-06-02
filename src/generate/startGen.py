from generate import camera
from generate import generateJS
from generate import filewriter
def start(filename, tempdir):
    base64_image = camera.encode_image(filename)
    code = generateJS.openai_gen(base64_image)
    filewriter.write_to_file(code,tempdir)