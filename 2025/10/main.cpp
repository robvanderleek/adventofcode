#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>

typedef std::vector<std::vector<int>> Wiring;

struct Machine {
    std::string startLights;
    std::vector<Wiring> wiring;
};

Wiring parseLine(const std::string& line) {
    Wiring result;
    std::istringstream iss(line);
    char ch;

    while (iss >> ch) {
        if (ch == '(') {
            int first, second;
            char comma;

            // Read first number
            iss >> first;

            // Check if there's a comma (pair) or closing paren (single)
            iss >> ch;

            if (ch == ',') {
                // It's a pair
                iss >> second;
                iss >> ch; // Read closing ')'
                result.push_back(std::make_pair(first, second));
            } else if (ch == ')') {
                // It's a single number
                result.push_back(first);
            }
        }
    }

    return result;
}

std::vector<std::string> loadInput(const std::string &filename) {
    std::vector<std::string> result;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        std::string startLights = line.substr(1, line.find(']') - 1);

        std::cout << startLights << std::endl;
        result.push_back(line);
    }
    return result;
}

void partOne() {
    const auto machines = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/10/input-small-part-one.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

void partTwo() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/10/input-small-part-one.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

int main() {
    partOne();
    // partTwo();
    return 0;
}