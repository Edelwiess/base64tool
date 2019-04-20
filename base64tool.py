import base64, sys
def readbytesfile(filename):
        filecontent = open(filename, 'rb')
        file =  filecontent.read()
        filecontent.close()
        return file

def write_encode(filename, input):
    content = base64.b64encode(input)
    filecontent = open(filename, 'wt')
    filecontent.write(content.decode('ASCII'))
    filecontent.close()

def write_decode(filename, input):
    content = base64.b64decode(input)
    filecontent = open(filename, 'wb')
    filecontent.write(content)
    filecontent.close()



def help():
    print('Usage:')
    print('    base64tool.py <Mode> <Filename>')
    print()
    print('    <Mode>:      decode OR encode')
    print('    <Filename>:       abc.txt')
    print('    <Filename> should not contain space')
    print()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        help()
        sys.exit()
    else:
        mode, filename = sys.argv[1], sys.argv[2]
        if mode == 'encode':

            write_encode(filename + '.encoded', readbytesfile(filename))
        elif mode == 'decode':
            write_decode(filename + '.decoded', readbytesfile(filename))
        else:
            help()
            exit(0)
        print('[*] Success!')
        print()
else:
    print('[*] ERROR: Please run this script directly')
