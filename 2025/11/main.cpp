#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>

struct Edge {
    const std::string from, to;
};

struct Graph {
    std::vector<std::string> nodes;
    std::vector<Edge> edges;
};

Graph loadInput(const std::string &filename) {
    Graph result;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        auto colonIndex = line.find(':');
        std::string fromName = line.substr(0, colonIndex);
        result.nodes.push_back(fromName);
        for (unsigned int i = colonIndex + 2; i < line.length(); i = i + 4) {
            std::string toName = line.substr(i, 3);
            result.nodes.push_back(toName);
            result.edges.push_back(Edge{fromName, toName});
        }
    }
    return result;
}

long walk(const Graph &g, const std::string &startNode, const std::string &endNode, std::set<std::string> visited,
          std::map<std::string, long> &lookupMap) {
    std::vector<std::string> next;
    for (const auto &[from, to] : g.edges) {
        if (from == startNode) {
            next.push_back(to);
        }
    }
    visited.insert(startNode);
    long result = 0;
    for (const auto &nextNode : next) {
        if (nextNode == endNode) {
            return 1;
        }
        if (visited.find(nextNode) == visited.end()) {
            if (lookupMap.find(nextNode) != lookupMap.end()) {
                result += lookupMap.at(nextNode);
            } else {
                auto count = walk(g, nextNode, endNode, visited, lookupMap);
                lookupMap.insert({nextNode, count});
                result += count;
            }
        }
    }
    return result;
}

long traces(const Graph &g, const std::string &startNode, const std::string &endNode) {
    std::map<std::string, long> lookupMap;
    return walk(g, startNode, endNode, std::set<std::string>(), lookupMap);
}

void partOne() {
    const auto graph = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/11/input.txt");
    auto result = traces(graph, "you", "out");
    std::cout << result << std::endl;
    assert(result == 662);
}

void partTwo() {
    const auto graph = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/11/input.txt");
    std::map<std::string, long> lookupMap;
    long a1 = traces(graph, "svr", "dac");
    long a2 = traces(graph, "dac", "fft");
    long a3 = traces(graph, "fft", "out");
    long b1 = traces(graph, "svr", "fft");
    long b2 = traces(graph, "fft", "dac");
    long b3 = traces(graph, "dac", "out");
    long result = a1 * a2 * a3 + b1 * b2 * b3;
    std::cout << result << std::endl;
    assert(result == 662);
}

int main() {
    partOne();
    partTwo();
    return 0;
}