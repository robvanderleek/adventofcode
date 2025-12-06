#include <cassert>
#include <fstream>
#include <iostream>
#include <numeric>
#include <regex>

std::vector<std::vector<std::string>> loadInput(const std::string &filename) {
    std::vector<std::vector<std::string>> result;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        std::vector<std::string> row;
        std::regex del("\\s+");
        std::sregex_token_iterator iter(line.begin(), line.end(), del, -1);
        std::sregex_token_iterator end;
        while (iter != end) {
            auto value = iter->str();
            if (!value.empty()) {
                row.push_back(value);
            }
            ++iter;
        }
        result.push_back(row);
    }
    return result;
}

std::vector<std::vector<long>> loadNumbers(const std::vector<std::vector<std::string>> &rows) {
    std::vector<std::vector<long>> result;
    for (int i = 0; i < rows.size() - 1; ++i) {
        std::vector<long> row;
        for (const auto &value : rows[i]) {
            if (value == "+" || value == "*") {
                break;
            }
            row.push_back(std::stol(value));
        }
        result.push_back(row);
    }
    return result;
}

std::vector<char> loadOperators(const std::vector<std::string> &row) {
    std::vector<char> result;
    result.reserve(row.size());
    for (auto cell : row) {
        result.push_back(cell[0]);
    }
    return result;
}

void partOne() {
    const auto input = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/06/input.txt");
    const auto numbers = loadNumbers(input);
    const auto operators = loadOperators(input[input.size() - 1]);
    std::vector<long> totals(numbers[0].size(), 0);
    for (const auto &row : numbers) {
        for (int j = 0; j < row.size(); ++j) {
            if (totals[j] == 0) {
                totals[j] = row[j];
            } else if (operators[j] == '+') {
                totals[j] = totals[j] + row[j];
            } else if (operators[j] == '*') {
                totals[j] = totals[j] * row[j];
            }
        }
    }
    long result = std::reduce(totals.begin(), totals.end());
    std::cout << result << std::endl;
    assert(result == 7229350537438);
}

void partTwo() {
    const auto input = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/06/input-small.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

int main() {
    partOne();
    // partTwo();
    return 0;
}