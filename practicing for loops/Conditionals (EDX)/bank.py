greet = input("Greetings: ")

match greet:
    
    case 'hey'|'Hey'|'how you doing?'|'How you doing?'|"how's it going?"|"How's it going?":
        print('$20')
    case  "what's happening?"|"What's happening?"|"what's up?"|"What's up?":
        print('$100')   
    case _:
        print("$0")    