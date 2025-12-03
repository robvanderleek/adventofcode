#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>


std::vector<std::string> loadInput(const std::string &filename) {
    std::vector<std::string> result;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        result.push_back(line);
    }
    return result;
}

void partOne() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/08/input-small.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

void partTwo() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/08/input-small.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

int main() {
    partOne();
    // partTwo();
    return 0;
}