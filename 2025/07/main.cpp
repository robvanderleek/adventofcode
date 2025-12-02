#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>


void extractRange(const std::string &range, std::vector<std::string> &result) {
    const auto from = std::stol(range.substr(0, range.find('-')));
    const auto to = std::stol(range.substr(range.find('-') + 1));
    for (auto i = from; i <= to; ++i) {
        result.push_back(std::to_string(i));
    }
}

std::vector<std::string> loadInput(const std::string &filename) {
    std::vector<std::string> result;
    std::ifstream file(filename);
    std::string line;
    std::getline(file, line);
    size_t pos = 0;
    while ((pos = line.find(',')) != std::string::npos) {
        auto range = line.substr(0, pos);
        extractRange(range, result);
        line.erase(0, pos + 1);
    }
    extractRange(line, result);
    return result;
}

void partOne() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/07/input-small.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

void partTwo() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/07/input-small.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

int main() {
    partOne();
    partTwo();
    return 0;
}