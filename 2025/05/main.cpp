#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>

std::vector<std::pair<long, long>> loadRanges(const std::string &filename) {
    std::vector<std::pair<long, long>> result;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        if (line.empty()) {
            break;
        }
        long start = std::stol(line.substr(0, line.find('-')));
        long end = std::stol(line.substr(line.find('-') + 1));
        result.emplace_back(start, end);
    }
    std::sort(result.begin(), result.end(), [](const auto &a, const auto &b) {
        return a.first < b.first;
    });
    return result;
}

std::vector<long> loadIds(const std::string &filename) {
    std::vector<long> result;
    std::ifstream file(filename);
    std::string line;
    bool parseIds = false;
    while (std::getline(file, line)) {
        if (line.empty()) {
            parseIds = true;
            continue;
        }
        if (parseIds) {
            long id = std::stol(line);
            result.push_back(id);
        }
    }
    return result;
}

void partOne() {
    std::string filename("/Users/rob/projects/robvanderleek/adventofcode/2025/05/input.txt");
    const auto ids = loadIds(filename);
    const auto ranges = loadRanges(filename);
    long result = 0;
    for (const auto &id : ids) {
        for (const auto &[start, end] : ranges) {
            if (id >= start && id <= end) {
                result++;
                break;
            }
        }
    }
    std::cout << result << std::endl;
    assert(result == 558);
}

std::vector<std::pair<long, long>> mergeRanges(const std::vector<std::pair<long, long>> &ranges) {
    std::vector<std::pair<long, long>> result;
    auto [start, end] = ranges[0];
    for (int i = 1; i < ranges.size(); ++i) {
        auto [nextStart, nextEnd] = ranges[i];
        if (nextStart > end) {
            result.emplace_back(start, end);
            start = nextStart;
            end = nextEnd;
        } else if (nextEnd > end) {
            end = nextEnd;
        }
    }
    result.emplace_back(start, end);
    return result;
}

void partTwo() {
    auto ranges = loadRanges("/Users/rob/projects/robvanderleek/adventofcode/2025/05/input.txt");
    auto mergedRanges = mergeRanges(ranges);
    long result = 0;
    for (auto [first, end] : mergedRanges) {
        result += end - first + 1;
    }
    std::cout << result << std::endl;
    assert(result == 344813017450467);
}

int main() {
    partOne();
    partTwo();
    return 0;
}