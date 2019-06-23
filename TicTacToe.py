import os

d={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
def dict_updater():
        for key,value in d.items():
                d[key]=' '
def GRID():
        os.system('clear')
        print ('\n'*22)
        print (f'{d.get("1")} | {d.get("2")} | {d.get("3")}'.center(135,' '))
        print ('-----------'.center(136,' '))
        print (f'{d.get("4")} | {d.get("5")} | {d.get("6")}'.center(135,' '))
        print ('-----------'.center(136,' '))
        print (f'{d.get("7")} | {d.get("8")} | {d.get("9")}'.center(135,' '))
        print ('\n'*22)
def determiner(player_no):
        if (d.get("1") != ' ' and d.get("1") == d.get("2") and d.get("2") == d.get("3")):
                return (f'player a {player_no} won\n')
        elif (d.get("1") != ' ' and d.get("1") == d.get("4") and d.get("4") == d.get("7")):
                return (f' player b  {player_no} won\n')
        elif (d.get("3") != ' ' and d.get("3") == d.get("6") and d.get("6") == d.get("9")):
                return (f' player c {player_no} won\n')
        elif (d.get("7") != ' ' and d.get("7") == d.get("8") and d.get("8") == d.get("9")):
                return (f' player d {player_no} won\n')
        elif (d.get("2") != ' ' and d.get("2") == d.get("5") and d.get("5") == d.get("8")):
                return (f' player e {player_no} won\n')
        elif (d.get("4") != ' ' and d.get("4") == d.get("5") and d.get("5") == d.get("6")):
                return (f' player f {player_no} won\n')
        elif (d.get("1") != ' ' and d.get("1") == d.get("5") and d.get("5") == d.get("9")):
                return (f' player g {player_no} won\n')
        elif (d.get("3") != ' ' and d.get("3") == d.get("5") and d.get("5") == d.get("7")):
                return (f' player h {player_no} won\n')
        else:
                return ' '
count=0
while True:
        GRID()
        if ' ' in d.values():
                try:
                        data=input(f'enter the placehoder number in the grid player {count}:')                        
                        if data and count%2==0 and d[data] == ' ':
                                d[data]='X'
                                GRID()
                                res=determiner(count)
                                count+=1
                                if res != ' ':
                                        print (res)
                                        dict_updater()
                                        resume=input("do you want to play further (y/n) : ")
                                        if resume == 'y':
                                                continue
                                        elif resume == 'n':
                                                break
                                        else:
                                                pass
                                else:
                                        pass
                        elif data and count%2 != 0 and d[data] == ' ':
                                d[data]='O'
                                GRID()
                                res=determiner(count)
                                count-=1
                                if res != ' ':
                                        print (res)
                                        dict_updater()
                                        resume=input("do you want to play further (y/n) : ")
                                        if resume == 'y':
                                                continue
                                        elif resume == 'n':
                                                break
                                        else:
                                                pass
                                else:
                                        pass                
                        else:
                                pass
                except:
                        pass
        else:
                dict_updater()
                resume=input("its a Tie do you want to play further (y/n) : ")
                if resume == 'y':
                        continue
                elif resume == 'n':
                        break
                else:
                        pass                