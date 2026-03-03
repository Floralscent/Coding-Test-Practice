#include <stdio.h>
#include <iostream>
using namespace std;

#define INF 9999
#define MAX_VTXS 256

class WGraphDijkstra {
    int size;
    char vertices[MAX_VTXS];
    int adj[MAX_VTXS][MAX_VTXS];
    int dist[MAX_VTXS];
    int path[MAX_VTXS];
    int found[MAX_VTXS];

public:
    void load(int g[][7], int n) {
        size = n;
        for (int i = 0; i < n; i++) {
            vertices[i] = 'A' + i;
            for (int j = 0; j < n; j++) adj[i][j] = g[i][j];
        }
    }

    int chooseVertex() {
        int min = INF, minpos = -1;
        for (int i = 0; i < size; i++) {
            if (dist[i] < min && !found[i]) {
                min = dist[i];
                minpos = i;
            }
        }
        return minpos;
    }

    void ShortestPath(int start) {
        for (int i = 0; i < size; i++) {
            dist[i] = adj[start][i];
            path[i] = start;
            found[i] = 0;
        }
        found[start] = 1;
        dist[start] = 0;

        for (int i = 0; i < size - 1; i++) {
            int u = chooseVertex();
            if (u == -1) break;
            found[u] = 1;
            for (int w = 0; w < size; w++) {
                if (!found[w] && dist[u] + adj[u][w] < dist[w]) {
                    dist[w] = dist[u] + adj[u][w];
                    path[w] = u;
                }
            }
        }
    }

    void PrintPath(int start, int end) {
        printf("[최단경로: %c->%c] %c", vertices[start], vertices[end], vertices[end]);
        int curr = end;
        while (curr != start) {
            curr = path[curr];
            printf(" <- %c", vertices[curr]);
        }
        printf("\n");
    }
};

int main() {
    WGraphDijkstra g;
    int AMG[7][7] = {
        {0, 7, INF, INF, 3, 10, INF},
        {7, 0, 4, 10, 2, 6, INF},
        {INF, 4, 0, 2, INF, INF, INF},
        {INF, 10, 2, 0, 11, 9, 4},
        {3, 2, INF, 11, 0, INF, 5},
        {10, 6, INF, 9, INF, 0, INF},
        {INF, INF, INF, 4, 5, INF, 0}
    };
    g.load(AMG, 7);
    g.ShortestPath(0);
    printf("[Dijkstra 최단 경로 결과]\n");
    for (int i = 1; i < 7; i++) g.PrintPath(0, i);
    return 0;
}