#include<stdio.h>
int main(){
    unsigned long int j,k;
    int a,c=0,d=0,i=0;
    scanf("%lu",&j);
    k=j;
    while (k!=0){
        i++;
        a=k%10;
        k=k/10;
        if (i%2==0){
            a=a*2;
            if ((a/10)!=0){
                a=a%10+a/10;
            }
            c=c+a;
        }
        else {
			d=d+a;
		}
    }
    c=c+d;
    if (c%10==0){
        printf("VISA");
    }
    else{
        printf("INVALID");
    }
}
