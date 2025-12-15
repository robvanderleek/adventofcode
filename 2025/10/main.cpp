#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>

typedef std::vector<std::vector<int>> Wiring;

struct Machine {
    std::string lights;
    std::string endLights;
    Wiring wiring;
};

std::vector<Machine> loadInput(const std::string &filename) {
    std::vector<Machine> result;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        auto rSquareIndex = line.find(']');
        std::string startLights = line.substr(1, rSquareIndex - 1);
        bool inWiring = false;
        std::string numberBuffer;
        Wiring wiring;
        std::vector<int> currentWiring;
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
            }
        }
        result.emplace_back(Machine{std::string(startLights.length(), '.'), startLights, wiring});
    }
    return result;
}

std::string doMove(std::string current, const std::vector<int> &move) {
    std::string next = current;
    for (int i : move) {
        next[i] = current[i] == '.' ? '#' : '.';
    }
    return next;
}

int calcSteps(const Machine &m) {
    std::vector<std::string> states;
    states.push_back(m.lights);
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

void partOne() {
    const auto machines = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/10/input.txt");
    long result = 0;
    for (auto m : machines) {
        result += calcSteps(m);
    }
    std::cout << result << std::endl;
    assert(result == 558);
}

void partTwo() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/10/input-small-part-one.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

int main() {
    partOne();
    // partTwo();
    return 0;
}