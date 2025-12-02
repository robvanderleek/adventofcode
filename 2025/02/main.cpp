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


bool isInvalidId(const std::string &id, const size_t maxParts = 2) {
    for (int i = 2; i <= maxParts; ++i) {
        if (id.length() % i == 0) {
            auto s = std::string();
            auto part = id.substr(0, id.length() / i);
            std::ostringstream os;
            for (int j = 0; j < i; j++) {
                os << part;
            }
            if (id == os.str()) {
                return true;
            }
        }
    }
    return false;
}

void partOne() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/02/input.txt");
    long result = 0;
    for (const auto &id : ids) {
        if (isInvalidId(id)) {
            result += std::stol(id);
        }
    }
    std::cout << result << std::endl;
    assert(result == 5398419778);
}

void partTwo() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/02/input.txt");
    long long result = 0;
    for (const auto &id : ids) {
        if (isInvalidId(id, id.length())) {
            result += std::stol(id);
        }
    }
    std::cout << result << std::endl;
    assert(result == 15704845910);
}

int main() {
    partOne();
    partTwo();
    return 0;
}