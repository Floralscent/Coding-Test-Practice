#include <iostream>
#include <string>

using namespace std;


struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class Queue {
private:
    Node* head;
    Node* tail; 
    int queueSize;

public:
    Queue() : head(nullptr), tail(nullptr), queueSize(0) {}

    void push(int x) {
        Node* newNode = new Node(x);
        if (empty()) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        queueSize++;
    }

    int pop() {
        if (empty()) return -1;
        Node* temp = head;
        int val = temp->data;
        head = head->next;
        delete temp;
        queueSize--;
        if (empty()) tail = nullptr; // 다 거내면 초기화
        return val;
    }

    int size() {
        return queueSize;
    }

    int empty() {
        return queueSize == 0 ? 1 : 0;
    }
    // 맨 앞
    int front() {
        if (empty()) return -1;
        return head->data;
    }
    // 맨 뒤
    int back() {
        if (empty()) return -1;
        return tail->data;
    }
    
    // 소멸자, 위에서 팝하면 딜리트 해놔서 메모리 커버
    ~Queue() {
        while (!empty()) pop();
    }
};

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    Queue q;

    while (N--) {
        string cmd;
        cin >> cmd;

        if (cmd == "push") {
            int x;
            cin >> x;
            q.push(x);
        } else if (cmd == "pop") {
            cout << q.pop() << "\n";
        } else if (cmd == "size") {
            cout << q.size() << "\n";
        } else if (cmd == "empty") {
            cout << q.empty() << "\n";
        } else if (cmd == "front") {
            cout << q.front() << "\n";
        } else if (cmd == "back") {
            cout << q.back() << "\n";
        }
    }

    return 0;
}