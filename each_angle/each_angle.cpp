#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
    int sides;

    if(argc == 2) sides = atoi(argv[1]);
    else {
        cout << "\n\t Use: ./each_angle $NUMBER_SIDES\n" << endl;
        return -1;
    }

    if(sides >= 3){
        cout << "In a figure with " << sides << " sides," << endl;
        cout << "\n\tsum of all angles = " << (sides - 2) * 180.0 << "°" << endl;
        cout << "\t    average angle = " << (sides - 2) * 180.0 / sides << "°\n" << endl;
    } 
    else cout << "You need at least 3 sides to form a polygon." << endl;

    return 0;
}
