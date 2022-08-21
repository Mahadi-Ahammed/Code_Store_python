if input("cmd: ").lower()=='git init':
    l=[]
    order_li=[]
    curr=0
    curr_no=0
    cmd = ''
    while cmd!='exit':
        cmd = input('---> ').lower()
        if 'commit' in cmd:
            if cmd == 'git show all commit':
                for i in range(len(l)-1,-1,-1):
                    for (k,v) in l[i].items():
                        if k==curr:
                            print('*',k,v)
                        else:
                            print(k,v)
            elif cmd == 'git show commit':
                for (k,v) in l[curr-1].items():
                    print(v)

            elif 'git commit' in cmd:
                cmd_list=cmd.split('"')
                l_dic={}
                # if l!=
                for i in range(len(l)-1,-1,-1):
                    for (k,v) in l[i].items():
                        if k==curr:
                            # print(l)
                            l=l[:i+1]
                curr_no+=1
                curr = curr_no
                l_dic[curr_no] = cmd_list[1]
                l.append(l_dic)
                # print(l[curr-1][0])
        elif 'jump' in cmd:
            cmd_list=cmd.split()
            for i in range(len(l)-1,-1,-1):
                for (k,v) in l[i].items():
                    if k==int(cmd_list[2]):
                        l.append(l.pop(i))
                        curr = k
        elif 'move back' in cmd:
            # print("curr",curr)
            for i in range(len(l)-1,-1,-1):
                for (k,v) in l[i].items():
                    if k==curr:
                        # print(i)
                        if i != 0:
                            mb=i-1
                        # print(mb)
            curr=list(l[mb].keys())[0]
        elif 'update' in cmd:
            cmd_list=cmd.split('"')
            # print(curr)
            # print(l)
            for i in range(len(l)-1,-1,-1):
                for (k,v) in l[i].items():
                    if k==curr:
                        l[i][k] = cmd_list[1]
        elif 'delete' in cmd:
            cmd_list=cmd.split()
            for i in range(len(l)-1,-1,-1):
                for (k,v) in l[i].items():
                    if k==int(cmd_list[2]):
                        if k==curr:
                            if i != 0:
                                mb=i-1
                            # print(mb)
                            curr=list(l[mb].keys())[0]
                        l.pop(i)

else:
    print('Error: "Wrong command"')
