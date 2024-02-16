user = input('File name: ')

if '.gif' in user:
    print('image/gif')
elif '.jpg' in user:
    print('image/jpeg')    
elif '.pdf' in user:
    print('application/pdf')
else:
    print('application/octet-stream')    