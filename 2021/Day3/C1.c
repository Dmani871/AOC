#include <stdio.h>
#include <math.h>
#define MAX_NO_OF_BITS 12
// sets all starting acumulator values to 0
void intialiseAcumulator(int * acc){
    int index=0;
    while(index<MAX_NO_OF_BITS){
        acc[index]=0;
        index++;
    }
}
// computes the binary diagnostic number
int binaryDiagnostic(int noOfBinaryNums,int * acc){
    int index=0;
    int gamma_rate=0;
    int epsilon_rate=0;
    // threshold for most common in a column
    int most_common_thresh=noOfBinaryNums/2;
    int exponent=0;
    while(index<MAX_NO_OF_BITS){
        exponent=MAX_NO_OF_BITS-1-index;
        if(acc[index]>most_common_thresh){
            // when 1 is most common add bin rep to gamma rate
            gamma_rate+=(int) pow (2,exponent);
        }else{
            // when 0 is most common add bin rep to gamma rate
            epsilon_rate+=(int) pow (2,exponent);
        }
        index++;
    }
    return gamma_rate*epsilon_rate;
}

int readDiagnosticReport(int * acc){
    FILE *filehandleIn=fopen("input.txt","r");
    char buffer[MAX_NO_OF_BITS+1];
    int binaryStringCounter=0;
    // reads the binary string from each line into the buffer
    while (fscanf(filehandleIn,"%s",buffer)==1)
    {
        int index=0;
        while(buffer[index]!='\0'){
            // adds the read integer to acculator 1 or 0
            acc[index]+=buffer[index]-'0';
            index++;
        }
        binaryStringCounter++;
    }
    // returns the number of binary string read
    return binaryStringCounter;


    fclose(filehandleIn);

}
int main(){
    int bits_acumulator[MAX_NO_OF_BITS];
    intialiseAcumulator(bits_acumulator);
    int binaryCounter=readDiagnosticReport(bits_acumulator);
    int diagnosticNum=binaryDiagnostic(binaryCounter,bits_acumulator);
    printf("Diagnostic Number = %d \n",diagnosticNum);
}

