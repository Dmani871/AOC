#include <stdio.h>
#include <limits.h>
int main(){
    FILE *fileHandleIn = fopen("input.txt","r");
    int current=INT_MIN;
    int previous=INT_MAX;
    int increaseCounter=0;
    while (fscanf(fileHandleIn,"%d",&current)==1){
        if(current>previous){
            increaseCounter++;
        }
        previous=current;
    }
    printf("%d",increaseCounter);
}
