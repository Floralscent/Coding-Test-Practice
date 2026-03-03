#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

#define INF 9999
#define MAX_VTXS 256

// 간선 정보를 저장하는 노드
class HeapNode {
    int key, v1, v2;
public:
    HeapNode(int k = 0, int u = 0, int v = 0) : key(k), v1(u), v2(v) {}
    void set(int k, int u, int v) { key = k; v1 = u; v2 = v; }
    int getKey() { return key; }
    int getV1() { return v1; }
    int getV2() { return v2; }
};

// 가중치가 작은 간선을 우선적으로 꺼내기 위한 최소 힙
class MinHeap {
    HeapNode node[MAX_VTXS];
    int size;
public:
    MinHeap() : size(0) {}
    bool isEmpty() { return size == 0; }
    bool isFull() { return size == MAX_VTXS - 1; }
    void insert(int key, int u, int v) {
        if (isFull()) return;
        int i = ++size;
        while (i != 1 && key < node[i / 2].getKey()) {
            node[i] = node[i / 2];
            i /= 2;
        }
        node[i].set(key, u, v);
    }
    HeapNode remove() {
        if (isEmpty()) return HeapNode();
        HeapNode root = node[1];
        HeapNode last = node[size--];
        int parent = 1, child = 2;
        while (child <= size) {
            if (child < size && node[child].getKey() > node[child + 1].getKey()) child++;
            if (last.getKey() <= node[child].getKey()) break;
            node[parent] = node[child];
            parent = child;
            child *= 2;
        }
        node[parent] = last;
        return root;
    }
};

// 사이클 체크를 위한 Union-Find 구조
class VertexSets {
    int parent[MAX_VTXS];
public:
    VertexSets(int nSets) {
        for (int i = 0; i < nSets; i++) parent[i] = -1;
    }
    int findSet(int v) {
        while (parent[v] >= 0) v = parent[v];
        return v;
    }
    void unionSets(int s1, int s2) { parent[s1] = s2; }
};

class AdjMatGraph {
protected:
    int size;
    char vertices[MAX_VTXS];
    int adj[MAX_VTXS][MAX_VTXS];
public:
    AdjMatGraph() { size = 0; }
    void insertVertex(char name) { vertices[size++] = name; }
    void display() {
        for (int i = 0; i < size; i++) {
            printf("%c ", vertices[i]);
            for (int j = 0; j < size; j++) printf("%3d ", adj[i][j]);
            printf("\n");
        }
    }
};

class WGraphMST : public AdjMatGraph {
public:
    void load(int g[][7], int n) {
        size = n;
        for (int i = 0; i < n; i++) {
            vertices[i] = 'A' + i;
            for (int j = 0; j < n; j++) adj[i][j] = g[i][j];
        }
    }
    void Kruskal() {
        MinHeap heap;
        for (int i = 0; i < size; i++)
            for (int j = i + 1; j < size; j++)
                if (adj[i][j] < INF) heap.insert(adj[i][j], i, j);
        
        VertexSets sets(size);
        int accepted = 0;
        while (accepted < size - 1 && !heap.isEmpty()) {
            HeapNode e = heap.remove();
            int uset = sets.findSet(e.getV1());
            int vset = sets.findSet(e.getV2());
            if (uset != vset) {
                printf("간선 추가: %c%c (비용: %d)\n", vertices[e.getV1()], vertices[e.getV2()], e.getKey());
                sets.unionSets(uset, vset);
                accepted++;
            }
        }
    }
};

int main() {
    WGraphMST g;
    int AMG[7][7] = { 
        {0, 29, INF, INF, INF, 10, INF},
        {29, 0, 16, INF, INF, INF, 15},
        {INF, 16, 0, 12, INF, INF, INF},
        {INF, INF, 12, 0, 22, INF, 18},
        {INF, INF, INF, 22, 0, 27, 25},
        {10, INF, INF, INF, 27, 0, INF},
        {INF, 15, INF, 18, 25, INF, 0} 
    };
    g.load(AMG, 7);
    printf("인접 행렬 그래프:\n");
    g.display();
    printf("\n[Kruskal MST 결과]\n");
    g.Kruskal();
    return 0;
}