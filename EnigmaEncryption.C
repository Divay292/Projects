
#include <stdio.h>
#include<string.h>
#include<ctype.h>
#define USERCHARS 200
#define ROTORLEN 26
int rotor0[ROTORLEN] = { 6, 12 ,11, 18, 25, 7, 0, 5, 17, 14, 22, 2, 1, 19, 9, 21, 23, 8, 3, 13, 24, 15, 10, 16, 20, 4 };
int rotor1[ROTORLEN] = { 7, 8, 15, 14, 17, 23, 24, 0, 1, 21, 16, 12, 11, 19, 3, 2, 10, 4, 20, 13, 18, 9, 25, 5, 6, 22 };
int rotor2[ROTORLEN] = { 5, 8, 24, 12, 17, 0, 11, 20, 1, 23, 15, 6, 3, 22, 19, 10, 18, 4, 16, 14, 7, 25, 13, 9, 2, 21};
int reflector[ROTORLEN] = { 3, 16, 12, 0, 18, 11, 24, 22, 25, 17, 15, 5, 2, 23, 20, 10, 1, 9, 4, 21, 14, 19, 7, 13, 6, 8};
int backwards(int value, int rotor[]);
int main(int argc, char **argv)
{
	int letter, letterNum, rotor0Out, rotor1Out, rotor2Out, reflectorOut;
    char userInput[USERCHARS];
    printf("Welcome to ENIGMA\n");
    printf("Enter transmission:\n\n");
    fgets(userInput, USERCHARS,stdin);
    while(strcmp(userInput,"done\n") !=0) {
        for(int i = 0; i< strlen(userInput); i++)
        {
            letter = userInput[i];
            if(isupper(letter))
            {
                letterNum = letter - 'A';
                rotor0Out = rotor0[letterNum];
                rotor1Out = rotor1[rotor0Out];
                rotor2Out = rotor2[rotor1Out];
                reflectorOut = reflector[rotor2Out];
                rotor2Out = backwards(reflectorOut, rotor2);
                rotor1Out = backwards(rotor2Out, rotor1);
                rotor0Out = backwards(rotor1Out, rotor0);
                printf("%c", rotor0Out + 'A');
            }
        }
        printf("\n");
        fgets(userInput,USERCHARS,stdin);
    }
	return 0;
}
int backwards (int value, int rotor[]){
    for(int i= 0; i<ROTORLEN; i++)
    {
        if(value==rotor[i]) {
            return i;
        }
    }
}
