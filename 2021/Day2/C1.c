#include <stdio.h>
int compareString(char*cmd,char*instruction){
    int index=0;
    while(cmd[index]!='\0'){
        if(cmd[index]!=instruction[index]){
            return -1;
        }
        index++;
    }
    return 0;
}
int main()
{
    FILE *fileHandleIn = fopen("input.txt", "r");
    char buffer[20];
    int units=0;
    int horizontal=0;
    int depth=0;
    while ((fscanf(fileHandleIn, "%s", buffer)==1) && 
    (fscanf(fileHandleIn, "%d", &units)==1)){
       if(compareString("forward",buffer)==0){
           horizontal+=units;
       }else if (compareString("down",buffer)==0)
       {
           depth+=units;
       }else if (compareString("up",buffer)==0)
       {
           depth-=units;
       }
    }
    printf("%d",depth*horizontal);
}

