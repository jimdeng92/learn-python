def copy_file(src,dst):
    src_file = open(src,'rb')
    dst_file = open(dst,'wb')

    while content := src_file.read(1024):
        dst_file.write(content)

    src_file.close()
    dst_file.close()

copy_file('text.txt','text_copy.txt')
