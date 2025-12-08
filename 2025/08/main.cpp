#include <cassert>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>

struct Node {
    int x, y, z;

    bool operator==(const Node &other) const {
        return x == other.x && y == other.y && z == other.z;
    }

    bool operator<(const Node &other) const {
        if (x != other.x)
            return x < other.x;
        if (y != other.y)
            return y < other.y;
        return z < other.z;
    }
};

struct Edge {
    const Node *from, *to;
    double length;
};

struct Graph {
    std::vector<Node> nodes;
    std::vector<Edge> edges;
};

double distance(const Node &a, const Node &b) {
    return std::sqrt(std::pow(a.x - b.x, 2) + std::pow(a.y - b.y, 2) + std::pow(a.z - b.z, 2));
}

Graph loadInput(const std::string &filename) {
    Graph graph;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        auto firstComma = line.find(',');
        auto secondComma = line.find(',', firstComma + 1);
        int x = std::stoi(line.substr(0, firstComma));
        int y = std::stoi(line.substr(firstComma + 1, secondComma - firstComma - 1));
        int z = std::stoi(line.substr(secondComma + 1));
        graph.nodes.push_back(Node{x, y, z});
    }
    for (int i = 0; i < graph.nodes.size(); ++i) {
        for (int j = i + 1; j < graph.nodes.size(); ++j) {
            auto d = distance(graph.nodes[i], graph.nodes[j]);
            graph.edges.push_back(Edge{&graph.nodes[i], &graph.nodes[j], d});
        }
    }
    std::sort(graph.edges.begin(), graph.edges.end(), [](const Edge &a, const Edge &b) {
        return a.length < b.length;
    });
    return graph;
}

bool append(std::vector<std::set<Node>> &circuits, const Edge &edge) {
    for (auto &c : circuits) {
        for (auto node : c) {
            if (node == *edge.from || node == *edge.to) {
                c.insert({*edge.from});
                c.insert({*edge.to});
                return true;
            }
        }
    }
    return false;
}

void partOne() {
    auto distanceGraph = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/08/input-small.txt");
    constexpr int numberOfConnections = 10;
    // constexpr int numberOfConnections = 1000;
    std::vector<std::set<Node>> circuits;
    for (int i = 0; i < numberOfConnections; ++i) {
        auto edge = distanceGraph.edges[i];
        if (!append(circuits, edge)) {
            circuits.push_back({*edge.from, *edge.to});
        }
    }
    sort(circuits.begin(), circuits.end(), [](const std::set<Node> &a, const std::set<Node> &b) {
        return a.size() > b.size();
    });
    unsigned long result = 1;
    for (int i = 0; i < 3; ++i) {
        std::cout << "Circuit " << i << " size: " << circuits[i].size() << std::endl;
        result *= circuits[i].size();
    }
    std::cout << result << std::endl;
    assert(result == 40);
}

void partTwo() {
    const auto ids = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/08/input-small.txt");
    long result = 0;
    std::cout << result << std::endl;
    assert(result == 0);
}

int main() {
    partOne();
    // partTwo();
    return 0;
}