#include <stdio.h>
#include <limits.h>
#define WINDOW_SIZE 3
int getWindowSum(int * windowValues){
    int index=0;
    int sum=0;
    while(index<WINDOW_SIZE){
        sum+=windowValues[index];
        index++;
    }
    return sum;
}

int getWindowIncreases(){
    FILE *fileHandleIn = fopen("input.txt","r");
    int windowValues[3];
    int index=0;
    int current=0;
    int previous=INT_MAX;
    int increaseCounter=0;
    //TODO:Reset index instead of count up
    while (fscanf(fileHandleIn,"%d",&windowValues[index%WINDOW_SIZE])==1){
        if(index>=2){
            current=getWindowSum(windowValues);
            if(current>previous){
                increaseCounter++;
            }
            previous=current;
        }
        index++;
    }
    return increaseCounter;
}
int main(){

    printf("%d",getWindowIncreases());
}


