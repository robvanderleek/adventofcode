#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
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

long largestJoltage(const std::string &bank, int length,
                    std::map<std::pair<std::string, int>, long> &lookupMap) {
    if (lookupMap.count(std::make_pair(bank, length))) {
        return lookupMap[std::make_pair(bank, length)]; // return cached result
    }
    long result = 0;
    for (int i = 0; i < bank.length(); ++i) {
        long prefix = static_cast<long>((bank[i] - '0') * pow(10, length - 1));
        long candidate = prefix;
        if (bank.length() - i < length) {
            continue;
        }
        if (length > 1) {
            long suffix = largestJoltage(bank.substr(i + 1), length - 1, lookupMap);
            candidate += suffix;
        }
        if (candidate > result) {
            result = candidate;
        }
    }
    lookupMap[std::make_pair(bank, length)] = result;
    return result;
}


void partOne() {
    const auto banks = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/03/input.txt");
    long result = 0;
    for (const auto &bank : banks) {
        std::map<std::pair<std::string, int>, long> lookupMap = {};
        result += largestJoltage(bank, 2, lookupMap);
    }
    std::cout << result << std::endl;
    assert(result == 17087);
}

void partTwo() {
    const auto banks = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/03/input.txt");
    long result = 0;
    for (const auto &bank : banks) {
        std::map<std::pair<std::string, int>, long> lookupMap = {};
        result += largestJoltage(bank, 12, lookupMap);
    }
    std::cout << result << std::endl;
    assert(result == 169019504359949);
}

int main() {
    partOne();
    partTwo();
    return 0;
}