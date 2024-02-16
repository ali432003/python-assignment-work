tym = input('What time is it? ')

def main():
    hours,min=tym.split(':')
    match hours or min:
        case '7'|'8'|'am':
            print('breakfast time')
        case '9'|'10'|'12'|'13'|'14'|'15'|'16'|'17':
            print('lunch time')
        case '18'|'19'|'20'|'21'|'22'|'23'|'pm':
            print('dinner time')
        case '11'|'11:11':
            print(None)          

main()                 
        
            

