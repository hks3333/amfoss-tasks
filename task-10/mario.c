#include<stdio.h>
int main(){
    int h=0,i,j,k;
    while (h<=0 || h>=9){
        printf("Height: ");
        scanf("%d",&h);
    }
    for (i=1;i<=h;i++){
        for (j=h-i;j>=0;j--){
            printf(" ");
        }
        for (k=0;k<i;k++){
			printf("#");
		}
		printf("  ");
		for (k=0;k<i;k++){
			printf("#");
		}
		printf("\n");
	}
}
