#!/usr/bin/env python3
from Agent import * # See the Agent.py file
from pysat.solvers import Glucose3

#### All your code can go here.
visited=set()
safe=[]
stack=[]
unsafe=set()
#knowledge base
kb=Glucose3()
kb.add_clause([-6])
kb.add_clause([-5])
kb.add_clause([-4])
kb.add_clause([-3])
kb.add_clause([-2])
kb.add_clause([-1])
kb.add_clause([-11])
kb.add_clause([-17])
kb.add_clause([-23])
kb.add_clause([-29])
kb.add_clause([-35])
kb.add_clause([-36])
kb.add_clause([-37])
kb.add_clause([-38])
kb.add_clause([-39])
kb.add_clause([-40])
ag = Agent()

    
def kb_update(loc,pcept):
    global kb
    x = loc[0]
    y = loc[1]
    var =5+x+6*(y-1)
    a = var+1
    b = var-1
    c = var+6
    if(var!=6):
        d = var-6
    else:
        d= 1
    if(pcept==0):
        '''if(valid(x+1,y)==true):
            kb.add_clause([-(var+1)])
        if(valid(x-1,y)==true):
            kb.add_clause([-(var-1)])
        if(valid(x,y-1)==true):
            kb.add_clause([-(var-5)])
        if(valid(x,y+1)==true):
            kb.add_clause([-(var+5)])'''
        kb.add_clause([-a])
        kb.add_clause([-b])
        kb.add_clause([-c])
        kb.add_clause([-d])
    if(pcept==1):
        kb.add_clause([(a),(b),(c),(d)])
        
        kb.add_clause([-(a),-(b)])
        kb.add_clause([-(a),-(c)])
        kb.add_clause([-(a),-(d)])

        kb.add_clause([-(b),-(a)])
        kb.add_clause([-(b),-(c)])
        kb.add_clause([-(b),-(d)])

        kb.add_clause([-(c),-(a)])
        kb.add_clause([-(c),-(b)])
        kb.add_clause([-(c),-(d)])

        kb.add_clause([-(d),-(a)])
        kb.add_clause([-(d),-(b)])
        kb.add_clause([-(d),-(c)])
    if(pcept==2):
        kb.add_clause([a,b,c])
        kb.add_clause([a,b,d])
        kb.add_clause([a,c,d])
        kb.add_clause([b,c,d])

        kb.add_clause([-a,-b,-c])
        kb.add_clause([-a,-b,-d])

        kb.add_clause([-b,-c,-a])
        kb.add_clause([-b,-c,-d])

        kb.add_clause([-c,-d,-a])
        kb.add_clause([-c,-d,-b])

        kb.add_clause([-a,-c,-d])
        kb.add_clause([-a,-c,-b])

        kb.add_clause([-a,-d,-b])
        kb.add_clause([-a,-d,-c])

        kb.add_clause([-b,-d,-a])
        kb.add_clause([-b,-d,-c])

    if(pcept==3):
        kb.add_clause([a,b])
        kb.add_clause([a,c])
        kb.add_clause([a,d])
        kb.add_clause([b,c])
        kb.add_clause([b,d])
        kb.add_clause([c,d])

        kb.add_clause([-a,-b,-c-d])  
    

def goldcheck(g1):
    a= g1+1
    b= g1-1
    c= g1+6
    d= g1-6
    if(kb.solve(assumptions=[-a])or kb.solve(assumptions=[-b]) or kb.solve(assumptions=[-c]) or kb.solve(assumptions=[-d])):
       return False
    else:
        return True
    
def valid(i):
    if(i>=6 and i<=34 and i!=11 and i!=17 and i!=23 and i!=29):
        return True
    else:
        return False
def pathfind(curr,a,visit,answer):
    global safe
    
    if(curr==a):   
        return answer
    #DFS
    '''print(curr)
    if(valid(curr-1)==True and curr-1 in safe and curr-1 not in visit):
        pathfind(curr-1,a,visit+[curr],answer+['Left'])
    if(valid(curr+1)==True and curr+1 in safe and curr+1 not in visit):
        pathfind(curr+1,a,visit+[curr],answer+['Right'])
    if(valid(curr+5)==True and curr+5 in safe and curr+5 not in visit):
        pathfind(curr+5,a,visit+[curr],answer+['Up'])
    if(valid(curr-5)==True and curr-5 in safe and curr-5 not in visit):
        pathfind(curr-5,a,visit+[curr],answer+['Down'])'''

    #BFS
    queue =[[curr,answer]]
    final=[]
    find=0
    while len(queue)!=0:
        front = queue.pop(0)
        curr2=front[0]
        #print(curr2)
        ans2=front[1]
        final=ans2
        if(curr2==a):
            find=1
            break
        visit.append(curr2)
        
        if(valid(curr2-1)==True and curr2-1 in safe and curr2-1 not in visit):
            queue.append([curr2-1,ans2+['Left']])
            
        if(valid(curr2+1)==True and curr2+1 in safe and curr2+1 not in visit):
            queue.append([curr2+1,ans2+['Right']])

        if(valid(curr2+6)==True and curr2+6 in safe and curr2+6 not in visit):
            queue.append([curr2+6,ans2+['Up']])

        if(valid(curr2-6)==True and curr2-6 in safe and curr2-6 not in visit):
            queue.append([curr2-6,ans2+['Down']])


    if(find==1):
        return final
    else:
        return 
        

#### You can change the main function as you wish. Run this program to see the output. Also see Agent.py code.


def main(ag):
    global stack
    global visited
    global kb
    #global ag
    global unsafe
    goldlist=[13,14,15,19,20,21,25,26,27]
    ans = []
    '''print('curLoc',ag.FindCurrentLocation())
    print('Percept ',ag.PerceiveCurrentLocation())
    ag.TakeAction('Right')
    print('Percept ',ag.PerceiveCurrentLocation())
    ag.TakeAction('Right')
    print('Percept ',ag.PerceiveCurrentLocation())'''
    #stack.append((1,1))
    #visited.add(6)
    goldfind=0
    position=0
    while True:
        for g1 in goldlist:
            if(goldcheck(g1)==True):
                print("Gold Found")
                goldfind=1
                position=g1
                break
        if(goldfind==1):
            break
        for i in range(6,35):
            if i in [11,17,23,29]:
                continue
            if(i not in safe):
                if(kb.solve(assumptions=[i])==False):
                    safe.append(i)
                    stack.append(i)
                    #print(safe)
                if(kb.solve(assumptions=[-i])==False):
                    unsafe.add(i)
                    #print(unsafe)
        
        if(stack==[]):
             print("Gold can't be found after visiting all the safe rooms")
             break

        #current location
        loc = ag.FindCurrentLocation()
        x = loc[0]
        y = loc[1]
        curr = 5+x+6*(y-1)
        
        a = stack.pop(0)
        #print("Legit",a)
        path= pathfind(curr,a,[],[])
        #print(a%6+1,a//6)
        #print(path)
        if(path==None):
            safe.remove(a)
            continue
        if(path==[]):
            pcept=ag.PerceiveCurrentLocation()
            loc=ag.FindCurrentLocation()
            kb_update(loc,pcept)
            visited.add(a)
        else:
            for i in path:
                ans.append(loc)
                print(loc)
                ag.TakeAction(i)
                pcept=ag.PerceiveCurrentLocation()
                loc=ag.FindCurrentLocation()
                kb_update(loc,pcept)
                visited.add(a)
    if(goldfind==1):   
        print(position%6+1,position//6)
        ans.append([position%6+1,position//6])
    return ans
if __name__=='__main__':
    main()
