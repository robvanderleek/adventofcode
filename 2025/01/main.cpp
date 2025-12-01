#include <cassert>
#include <fstream>
#include <iostream>

std::vector<std::pair<char, int>> loadInput(const std::string &filename) {
    std::vector<std::pair<char, int>> instructions;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        char direction = line[0];
        int distance = std::stoi(line.substr(1));
        instructions.emplace_back(direction, distance);
    }
    return instructions;
}

int calculateZeros(const std::vector<std::pair<char, int>> &instructions, const bool countDuring = false) {
    int dial = 50;
    int zeros = 0;
    for (auto i : instructions) {
        auto [direction, count] = i;
        if (count >= 100) {
            if (countDuring) {
                zeros += count / 100;
            }
            count = count % 100;
        }
        if (direction == 'L') {
            int nextDial = dial - count;
            if (nextDial < 0) {
                if (countDuring && dial > 0) {
                    zeros++;
                }
                nextDial = 100 + nextDial;
            }
            dial = nextDial;
        } else {
            int nextDial = dial + count;
            if (nextDial >= 100) {
                if (countDuring && nextDial != 100) {
                    zeros++;
                }
                nextDial = nextDial % 100;
            }
            dial = nextDial;
        }
        if (dial == 0) {
            zeros++;
        }
    }
    return zeros;
}

void partOne() {
    auto instructions = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/01/input.txt");
    auto result = calculateZeros(instructions);
    std::cout << result << std::endl;
    assert(result == 1064);
}

void partTwo() {
    const auto instructions = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/01/input.txt");
    const auto result = calculateZeros(instructions, true);
    std::cout << result << std::endl;
    assert(result == 6122);
}

int main() {
    partOne();
    partTwo();
    return 0;
}
