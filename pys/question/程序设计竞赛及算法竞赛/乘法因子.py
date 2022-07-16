def main():
    n=int(input())
    ans=0
    for i in range(int((n+1)/2)):
        while n%(i+2)==0 :
            n /= (i+2)
            ans+=1
    if(n!=1):
        ans+=1
    print(ans)

if __name__ == '__main__':
    main()