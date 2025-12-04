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

bool canAccess(const std::vector<std::string> &grid, int row, int col) {
    int rolls = 0;
    std::stringstream ss;
    if (row > 0) {
        const std::string &topRow = grid[row - 1];
        ss << topRow.substr(std::max(0, col - 1), col == 0 ? 2 : 3);
    }
    ss << grid[row].substr(std::max(0, col - 1), col == 0 ? 2 : 3);
    if (row < grid.size() - 1) {
        const std::string &bottomRow = grid[row + 1];
        ss << bottomRow.substr(std::max(0, col - 1), col == 0 ? 2 : 3);
    }
    const std::string neighborsStr = ss.str();
    for (const char c : neighborsStr) {
        if (c == '@') {
            rolls++;
        }
    }
    return rolls - 1 /* self */ < 4;
}

std::vector<std::string> processGrid(std::vector<std::string> &grid) {
    std::vector<std::string> result;
    for (int rowIdx = 0; rowIdx < grid.size(); ++rowIdx) {
        std::string row = grid[rowIdx];
        std::string nextRow = row;
        for (int colIdx = 0; colIdx < row.length(); ++colIdx) {
            auto element = row[colIdx];
            if (element == '@' && canAccess(grid, rowIdx, colIdx)) {
                nextRow[colIdx] = '.';
                grid[rowIdx] = row;
            }
        }
        result.push_back(nextRow);
    }
    return result;
}

int countGrid(std::vector<std::string> &grid) {
    int result = 0;
    for (int rowIdx = 0; rowIdx < grid.size(); ++rowIdx) {
        for (int colIdx = 0; colIdx < grid[rowIdx].length(); ++colIdx) {
            if (grid[rowIdx][colIdx] == '@') {
                ;
                result++;
            }
        }
    }
    return result;
}

void partOne() {
    auto grid = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/04/input.txt");
    auto startCount = countGrid(grid);
    auto nextGrid = processGrid(grid);
    auto nextCount = countGrid(nextGrid);
    int result = startCount - nextCount;
    std::cout << result << std::endl;
    assert(result == 1495);
}

void partTwo() {
    auto grid = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/04/input.txt");
    auto startCount = countGrid(grid);
    auto nextGrid = processGrid(grid);
    auto previousCount = startCount;
    auto nextCount = countGrid(nextGrid);
    while (nextCount < previousCount) {
        previousCount = nextCount;
        nextGrid = processGrid(nextGrid);
        nextCount = countGrid(nextGrid);
    }
    long result = startCount - nextCount;
    std::cout << result << std::endl;
    assert(result == 8768);
}

int main() {
    partOne();
    partTwo();
    return 0;
}