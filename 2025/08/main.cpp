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
        return x != other.x ? x < other.x : y != other.y ? y < other.y : z < other.z;
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

int walk(const std::vector<Edge> &edges, const Node &node, std::set<Node> &visited) {
    if (visited.find(node) != visited.end()) {
        return 0;
    }
    visited.insert(node);
    int count = 1;
    for (const auto &edge : edges) {
        if (*edge.from == node && visited.find(*edge.to) == visited.end()) {
            visited.insert(*edge.from);
            count += walk(edges, *edge.to, visited);
        } else if (*edge.to == node && visited.find(*edge.from) == visited.end()) {
            visited.insert(*edge.to);
            count += walk(edges, *edge.from, visited);
        }
    }
    return count;
}

void partOne() {
    auto distanceGraph = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/08/input.txt");
    constexpr int numberOfConnections = 1000;
    std::vector<Edge> edges;
    edges.reserve(numberOfConnections);
    for (int i = 0; i < numberOfConnections; ++i) {
        edges.push_back(distanceGraph.edges[i]);
    }
    std::set<Node> visited;
    std::vector<int> circuits;
    for (const auto &node : distanceGraph.nodes) {
        auto count = walk(edges, node, visited);
        if (count > 0)
            circuits.push_back(count);

    }
    sort(circuits.begin(), circuits.end(), [](int a, int b) {
        return a > b;
    });
    unsigned long result = 1;
    for (int i = 0; i < 3; ++i) {
        result *= circuits[i];
    }
    std::cout << result << std::endl;
    assert(result == 83520);
}

void partTwo() {
    const auto distanceGraph = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/08/input.txt");
    std::vector<Edge> edges;
    edges.reserve(5601);
    for (int i = 0; i < 5601; ++i) {
        edges.push_back(distanceGraph.edges[i]);
    }
    std::set<Node> visited;
    assert(walk(edges, distanceGraph.nodes[0], visited) == 1000);
    Edge edge = edges[edges.size() - 1];
    long result = edge.from->x * edge.to->x;
    std::cout << result << std::endl;
    assert(result == 1131823407);
}

int main() {
    partOne();
    partTwo();
    return 0;
}