#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int cal {0};
    int total_cals {0};
    int cals[3];
    int max_cals={0};
    string line;
    ifstream InputFile("cals.txt");
    while (getline(InputFile, line))
    {
        if (sscanf(line.c_str(), "%d", &cal) == 1)
        {
            total_cals+=cal;
        }
        if (line.length() == 0)
        {
            max_cals=(max_cals < cals) ? cals: max_cals;
            total_cals=0;
        }
    }
    InputFile.close();
    cout<<max_cals<<endl;
}