if __name__ == "__main__":
    from itertools import combinations
    s="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,1,2,3,4,5,6,7,8,9,0,!,@,#,$,%,^,&,*,(,)".split(',')     
    #All the characters that will make the word, each seperated by a comma
    l=8         #Characters in the word
    with open("wordlist{}chars.txt".format(l),"a+") as f:   #Name of the file that will be generated and will add new words at the end. 
        for i in combinations(s,l):
            m=str(''.join(i))
            f.write(m+'\n')
