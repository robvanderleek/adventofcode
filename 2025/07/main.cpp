#include <cassert>
#include <fstream>
#include <iostream>
#include <set>
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

void partOne() {
    const auto lines = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/07/input.txt");
    std::set<int> beams;
    long result = 0;
    for (const auto &line : lines) {
        for (int i = 0; i < line.length(); ++i) {
            char c = line[i];
            if (c == 'S') {
                beams.insert(i);
            } else if (c == '^' && beams.count(i)) {
                result++;
                beams.erase(i);
                beams.insert(i - 1);
                beams.insert(i + 1);
            }
        }
    }
    std::cout << result << std::endl;
    assert(result == 1507);
}

long trackBeam(std::vector<std::string> lines, int i, int j, std::map<std::pair<int, int>, long> &p) {
    if (i == lines.size() - 1) {
        return 1;
    }
    if (lines[i][j] == '^') {
        if (p.count({i, j})) {
            return p.at({i, j});
        }
        long traces = trackBeam(lines, i + 1, j - 1, p) + trackBeam(lines, i + 1, j + 1, p);
        p[{i, j}] = traces;
        return traces;
    }
    return trackBeam(lines, i + 1, j, p);
}

void partTwo() {
    const auto lines = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/07/input.txt");
    std::map<std::pair<int, int>, long> p;
    long result = 0;
    for (int j = 0; j < lines[0].length(); ++j) {
        char c = lines[0][j];
        if (c == 'S') {
            result = trackBeam(lines, 0, j, p);
            break;
        }
    }
    std::cout << result << std::endl;
    assert(result == 1537373473728);
}

int main() {
    partOne();
    partTwo();
    return 0;
}