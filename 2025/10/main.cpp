#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>

typedef std::vector<std::vector<int>> Wiring;

struct Machine {
    Wiring wiring;
    std::string startLights;
    std::string endLights;
    std::vector<int> startJoltage;
    std::vector<int> endJoltage;
};

std::vector<Machine> loadInput(const std::string &filename) {
    std::vector<Machine> result;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        auto rSquareIndex = line.find(']');
        std::string endLights = line.substr(1, rSquareIndex - 1);
        bool inWiring = false;
        bool injoltage = false;
        std::string numberBuffer;
        Wiring wiring;
        std::vector<int> currentWiring;
        std::vector<int> endJoltage;
        for (auto i = rSquareIndex + 1; i < line.length(); ++i) {
            if (line[i] == ')') {
                inWiring = false;
                currentWiring.push_back(std::stoi(numberBuffer));
                numberBuffer.clear();
                wiring.push_back(currentWiring);
            } else if (line[i] == '(') {
                inWiring = true;
                currentWiring.clear();
            } else if (inWiring) {
                if (line[i] == ',') {
                    currentWiring.push_back(std::stoi(numberBuffer));
                    numberBuffer.clear();
                } else {
                    numberBuffer += line[i];
                }
            } else if (line[i] == '{') {
                injoltage = true;
            } else if (line[i] == '}') {
                injoltage = false;
                endJoltage.push_back(std::stoi(numberBuffer));
                numberBuffer.clear();
            } else if (injoltage) {
                if (line[i] == ',') {
                    endJoltage.push_back(std::stoi(numberBuffer));
                    numberBuffer.clear();
                } else {
                    numberBuffer += line[i];
                }
            }
        }
        result.emplace_back(Machine{wiring, std::string(endLights.length(), '.'), endLights,
                                    std::vector<int>(endJoltage.size(), 0), endJoltage});
    }
    return result;
}

std::string doMove(const std::string &current, const std::vector<int> &move) {
    std::string next = current;
    for (int i : move) {
        next[i] = current[i] == '.' ? '#' : '.';
    }
    return next;
}

int calcSteps(const Machine &m) {
    std::vector<std::string> states;
    states.push_back(m.startLights);
    int step = 1;
    while (true) {
        std::vector<std::string> nextStates;
        for (const auto &state : states) {
            for (const auto &move : m.wiring) {
                auto nextState = doMove(state, move);
                if (nextState == m.endLights) {
                    return step;
                }
                nextStates.push_back(nextState);
            }
        }
        step++;
        states = nextStates;
    }
}

std::vector<int> doMovePartTwo(const std::vector<int> &current, const std::vector<int> &move) {
    std::vector<int> next = current;
    for (int i : move) {
        next[i] = current[i] - 1;
    }
    return next;
}

std::vector<int> minElementIndices(const std::vector<int> &v) {
    std::vector<int> result;
    auto minElement = 0;
    for (int i : v) {
        if (minElement == 0) {
            minElement = i;
        } else if (i > 0 && i < minElement) {
            minElement = i;
        }
    }
    for (int i = 0; i < v.size(); ++i) {
        if (v[i] == minElement) {
            result.push_back(i);
        }
    }
    return result;
}

bool contains(const std::vector<int> &v, std::vector<int> values) {
    for (auto value : values) {
        if (std::find(v.begin(), v.end(), value) != v.end()) {
            return true;
        }
    }
    return false;
}

int calcStepsPartTwo(const Machine &m) {
    std::vector<std::vector<int>> states;
    states.push_back(m.endJoltage);
    int step = 1;
    while (true) {
        std::vector<std::vector<int>> nextStates;
        for (const auto &s : states) {
            auto indices = minElementIndices(s);
            for (const auto &w : m.wiring) {
                if (!contains(w, indices)) {
                    continue;
                }
                auto nextState = doMovePartTwo(s, w);
                if (nextState == m.startJoltage) {
                    return step;
                }
                if (*std::min_element(nextState.begin(), nextState.end()) < 0) {
                    continue;
                }
                if (std::find(nextStates.begin(), nextStates.end(), nextState) == nextStates.end()) {
                    nextStates.push_back(nextState);
                }
            }
        }
        step++;
        states = nextStates;
    }
}

void partOne() {
    const auto machines = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/10/input.txt");
    long result = 0;
    for (const auto &m : machines) {
        result += calcSteps(m);
    }
    std::cout << result << std::endl;
    assert(result == 558);
}

void partTwo() {
    const auto machines = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/10/input-small.txt");
    long result = 0;
    for (int i = 0; i < machines.size(); ++i) {
        std::cout << "Processing machine " << i + 1 << " of " << machines.size() << std::endl;
        result += calcStepsPartTwo(machines[i]);
    }
    std::cout << result << std::endl;
    assert(result == 0);
}

int main() {
    partOne();
    partTwo();
    return 0;
}