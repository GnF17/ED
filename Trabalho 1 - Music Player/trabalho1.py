#@author: Giovanna Nogueira (GnF17)

def player(text):
    global queue, playing, stopped, funcionality
    caracter = False
    if len(funcionality)>4:
        funcionality.pop(0)
        funcionality.append(text)
    if len(text)>1:
        command = text[0]
        if text[1]=='*':
            caracter = text[1]
        else:
            music = text[1]
    else:
        command = text[0]
    if command=='fight':
        return print('Jedi Wagner, assuma o comando!')
    else:    
        if command=='add':
            queue.append(music)
            funcionality.append(text)
        elif command=='del':
            queue.remove(music)
            funcionality.append(text)
        elif command=='next':
            funcionality.append(text)
            #queue.remove(music)
            if music in queue[1:] and queue[0]!=music:
                queue.remove(music)
                #position = queue.index(music)
                queue.append('')
                if playing=='':
                    for u in range(len(queue)-1,0,-1):
                        queue[u]=queue[u-1]
                    queue[0]=music
                else:
                    for u in range(len(queue)-1,1,-1):
                        queue[u]=queue[u-1]
                    queue[1]=music
        elif command=='list':
            if len(queue)==0:
                print('[vazia]')
            else:
                for i in range(len(queue)-1):
                   print(queue[i] ,end=',')
                print(queue[-1], end='\n')
        elif command=='current':
            if len(queue)==0:
                print('Toque! Toque, Dijê!')
            elif stopped is True:
                print(queue[0])
            else:
                print(playing)
        elif command=='play':
            funcionality.append(text)
            playing=queue[0]
        elif command=='stop':
            playing=''
        elif command=='ended':
            if len(queue)>1:
                playing=queue[1]
                queue.append(queue[0])
                queue.pop(0)
            else:
                playing=''
            funcionality = []
            queue.append(queue.pop())
        elif command=='undo' or command=='undo *':
            if len(funcionality)>0:
                if caracter=='*':
                    if len(funcionality)<=4:
                        while len(funcionality)!=0:
                            undo = funcionality.pop(-1)
                            if undo[0]=='play':
                                playing=''
                            elif undo[0]=='add':
                                queue.remove(undo[1])
                            elif undo[0]=='del':
                                queue.append(undo[1])
                            else:
                                queue = queue[1:position-1]+musica+queue[position+1:]
                    else:
                        for i in range(4):
                            undo = funcionality.pop(-1)
                            if undo[0]=='play':
                                playing=''
                            elif undo[0]=='add':
                                queue.remove(undo[1])
                            elif undo[0]=='del':
                                queue.append(undo[1])
                            else:
                                queue = queue[1:position-1]+musica+queue[position+1:]
                else:
                    undo = funcionality.pop(-1)
                    if undo[0]=='play':
                        playing=''
                    elif undo[0]=='add':
                        queue.remove(undo[1])
                    elif undo[0]=='del':
                        queue.append(undo[1])
                    else:
                        queue = queue[1:position-1]+musica+queue[position+1:]
            #print(funcionality)
        (player(input().split())) 
        
funcionality = []
queue = []
stopped = True
playing = ''
player(input().split())
