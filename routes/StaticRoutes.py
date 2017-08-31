from bottle import static_file

def staticHandler(filepath):
    print 'hola'
    return static_file(filepath, root='./static/')
