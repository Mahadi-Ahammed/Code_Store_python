if input("cmmand: ").lower()=='git init':
    Commit_List=[]
    s=0
    serial_no=0
    git_command = ''
    while git_command!='exit':
        git_command = input('---> ').lower()
        if 'commit' in git_command:
            if git_command == 'git show all commit':
                for i in range(len(Commit_List)-1,-1,-1):
                    for (key,v) in Commit_List[i].items():
                        if key==s:
                            print('*',key,v)
                        else:
                            print(key,v)
            elif git_command == 'git show commit':
                for (key,v) in Commit_List[s-1].items():
                    print(v)

            elif 'git commit' in git_command:
                temp_command=git_command.split('"')
                l_dic={}
                for i in range(len(Commit_List)-1,-1,-1):
                    for (key,v) in Commit_List[i].items():
                        if key==s:
                            Commit_List=Commit_List[:i+1]
                serial_no+=1
                s = serial_no
                l_dic[serial_no] = temp_command[1]
                Commit_List.append(l_dic)
        elif 'jump' in git_command:
            temp_command=git_command.split()
            for i in range(len(Commit_List)-1,-1,-1):
                for (key,v) in Commit_List[i].items():
                    if key==int(temp_command[2]):
                        Commit_List.append(Commit_List.pop(i))
                        s = key
        elif 'move back' in git_command:
            for i in range(len(Commit_List)-1,-1,-1):
                for (key,v) in Commit_List[i].items():
                    if key==s:
                        if i != 0:
                            mb=i-1
            s=list(Commit_List[mb].keys())[0]
        elif 'update' in git_command:
            temp_command=git_command.split('"')
            for i in range(len(Commit_List)-1,-1,-1):
                for (key,v) in Commit_List[i].items():
                    if key==s:
                        Commit_List[i][key] = temp_command[1]
        elif 'delete' in git_command:
            temp_command=git_command.split()
            for i in range(len(Commit_List)-1,-1,-1):
                for (key,v) in Commit_List[i].items():
                    if key==int(temp_command[2]):
                        if key==s:
                            if i != 0:
                                mb=i-1
                            # print(mb)
                            s=list(Commit_List[mb].keys())[0]
                        Commit_List.pop(i)

else:
    print('Error: "Wrong command"')
