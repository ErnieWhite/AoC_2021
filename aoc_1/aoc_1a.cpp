#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream my_file("input.txt");
    vector<int> sonar_readings;
    int reading;
    if (my_file.is_open()) {
        while (my_file >> reading) {
            sonar_readings.push_back(reading);
        }
        my_file.close();
    } else {
        cout << "Unable to open file";
    }

    int increase = 0;
    vector<int>::iterator it = sonar_readings.begin();
    int previous_depth = *it;
    int current_depth = 0;
    for (it; it != sonar_readings.end(); ++it) {
        if (previous_depth < *it) {
            increase += 1;
        }
        previous_depth = *it;
    };
    cout << "increase: " << increase << '\n';

    return 0;
}

