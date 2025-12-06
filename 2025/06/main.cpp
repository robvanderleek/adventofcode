#include <cassert>
#include <fstream>
#include <iostream>
#include <numeric>
#include <regex>
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

std::vector<std::vector<long>> loadNumbersPartOne(const std::vector<std::string> &lines) {
    std::vector<std::vector<long>> result;
    for (int i = 0; i < lines.size() - 1; ++i) {
        std::vector<long> row;
        std::regex del("\\s+");
        std::sregex_token_iterator iter(lines[i].begin(), lines[i].end(), del, -1);
        std::sregex_token_iterator end;
        while (iter != end) {
            auto value = iter->str();
            if (!value.empty()) {
                row.push_back(std::stol(value));
            }
            ++iter;
        }
        result.push_back(row);
    }
    return result;
}

std::vector<std::vector<long>> loadNumbersPartTwo(const std::vector<std::string> &lines) {
    std::vector<std::vector<long>> result;
    std::vector<std::string> rotated(lines.size(), "");
    std::vector<long> v;
    for (int j = 0; j < lines[0].length() + 3; ++j) {
        std::stringstream ss;
        for (int k = 0; k < lines.size() - 1; ++k) {
            if (j >= lines[k].length()) {
                continue;
            }
            auto c = lines[k][j];
            if (c != ' ') {
                ss << lines[k][j];
            }
        }
        auto col = ss.str();
        if (col.empty()) {
            if (!v.empty()) {
                result.push_back(v);
                v = std::vector<long>();
            }
        } else {
            v.push_back(stol(col));
        }
    }
    return result;
}

std::vector<char> loadOperators(const std::string &line) {
    std::vector<char> result;
    std::regex del("\\s+");
    std::sregex_token_iterator iter(line.begin(), line.end(), del, -1);
    std::sregex_token_iterator end;
    while (iter != end) {
        auto value = iter->str();
        if (!value.empty()) {
            result.push_back(value[0]);
        }
        ++iter;
    }
    return result;
}

void partOne() {
    const auto input = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/06/input.txt");
    const auto numbers = loadNumbersPartOne(input);
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
    const auto input = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/06/input.txt");
    const auto columns = loadNumbersPartTwo(input);
    const auto operators = loadOperators(input[input.size() - 1]);
    std::vector<long> totals(columns.size(), 0);
    for (int j = 0; j < columns.size(); ++j) {
        if (operators[j] == '+') {
            totals[j] = std::reduce(columns[j].begin(), columns[j].end(), 0L);
        } else if (operators[j] == '*') {
            totals[j] = std::reduce(columns[j].begin(), columns[j].end(), 1L, std::multiplies{});
        }
    }
    long result = std::reduce(totals.begin(), totals.end());
    std::cout << result << std::endl;
    assert(result == 7229350537438);
}

int main() {
    partOne();
    partTwo();
    return 0;
}