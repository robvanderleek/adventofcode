#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>

struct Point {
    int x;
    int y;
};

std::vector<Point> loadInput(const std::string &filename) {
    std::vector<Point> result;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        auto comma = line.find(',');
        int x = std::stoi(line.substr(0, comma));
        int y = std::stoi(line.substr(comma + 1));
        result.push_back({x, y});
    }
    return result;
}

void partOne() {
    const auto points = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/09/input.txt");
    unsigned long long result = 0;
    for (int i = 0; i < points.size(); ++i) {
        for (int j = i + 1; j < points.size(); ++j) {
            auto p1 = points[i];
            auto p2 = points[j];
            long length = (p1.x > p2.x ? p1.x - p2.x : p2.x - p1.x) + 1;
            long height = (p1.y > p2.y ? p1.y - p2.y : p2.y - p1.y) + 1;
            long area = length * height;
            if (area > result) {
                result = area;
            }
        }
    }
    std::cout << result << std::endl;
    assert(result == 4729332959);
}

bool intersect(Point pA, Point pB, Point pC, Point pD) {
    auto line1Horizontal = (pA.y == pB.y);
    auto line2Horizontal = (pC.y == pD.y);
    if ((line1Horizontal && line2Horizontal) || (!line1Horizontal && !line2Horizontal)) {
        return false;
    }
    if (line1Horizontal) {
        return pC.x >= (pA.x < pB.x ? pA.x : pB.x) && pC.x <= (pA.x > pB.x ? pA.x : pB.x) &&
               pA.y > (pC.y < pD.y ? pC.y : pD.y) && pA.y < (pC.y > pD.y ? pC.y : pD.y);
    }
    return pA.x >= (pC.x < pD.x ? pC.x : pD.x) && pA.x <= (pC.x > pD.x ? pC.x : pD.x) &&
           pC.y > (pA.y < pB.y ? pA.y : pB.y) && pC.y < (pA.y > pB.y ? pA.y : pB.y);
}

bool rectIntersects(const Point p1, const Point p2, const Point p3, const Point p4, const std::vector<Point> &points) {
    for (int k = 0; k < points.size(); ++k) {
        auto p = points[k];
        auto q = (k == points.size() - 1 ? points[0] : points[k + 1]);
        if (intersect(p1, p3, p, q) || intersect(p3, p2, p, q) || intersect(p2, p4, p, q) || intersect(p4, p1, p, q)) {
            return true;
        }
    }
    return false;
}

void partTwo() {
    const auto points = loadInput("/Users/rob/projects/robvanderleek/adventofcode/2025/09/input.txt");
    unsigned long long result = 0;
    for (int i = 0; i < points.size(); ++i) {
        for (int j = i + 1; j < points.size(); ++j) {
            auto p1 = points[i];
            auto p2 = points[j];
            long length = (p1.x > p2.x ? p1.x - p2.x : p2.x - p1.x) + 1;
            long height = (p1.y > p2.y ? p1.y - p2.y : p2.y - p1.y) + 1;
            long area = length * height;
            if (area > result) {
                auto p3 = Point{p1.x, p2.y};
                auto p4 = Point{p2.x, p1.y};
                if (rectIntersects(p1, p2, p3, p4, points))
                    continue;
                result = area;
            }
        }
    }
    std::cout << result << std::endl;
    assert(result == 24);
}

int main() {
    partOne();
    partTwo();
    return 0;
}
