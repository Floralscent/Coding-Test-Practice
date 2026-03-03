#include <iostream>
#include <vector>

using namespace std;

#define MAX_VTXS 256

class ConnectedComponentGraph {
    int size;
    int adj[MAX_VTXS][MAX_VTXS];
    bool visited[MAX_VTXS];
    int label[MAX_VTXS];

public:
    ConnectedComponentGraph(int n) : size(n) {
        for(int i=0; i<size; i++) {
            visited[i] = false;
            for(int j=0; j<size; j++) adj[i][j] = 0;
        }
    }

    void insertEdge(int u, int v) { adj[u][v] = adj[v][u] = 1; }

    void labelDFS(int v, int color) {
        visited[v] = true;
        label[v] = color;
        for (int w = 0; w < size; w++) {
            if (adj[v][w] != 0 && !visited[w]) labelDFS(w, color);
        }
    }

    void findComponents() {
        int count = 0;
        for (int i = 0; i < size; i++) {
            if (!visited[i]) labelDFS(i, ++count);
        }
        cout << "그래프 연결 성분 개수: " << count << endl;
        for (int i = 0; i < size; i++)
            cout << "노드 " << (char)('A'+i) << " : 그룹 " << label[i] << endl;
    }
};

int main() {
    ConnectedComponentGraph g(5);
    g.insertEdge(0, 1); // A-B 연결
    g.insertEdge(0, 2); // A-C 연결
    g.insertEdge(3, 4); // D-E 연결 (따로 떨어짐)

    cout << "[연결 성분 분석 결과]" << endl;
    g.findComponents();
    return 0;
}