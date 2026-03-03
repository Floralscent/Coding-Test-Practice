#include <iostream>
using namespace std;

class TreeNode {
public:
    int data;
    TreeNode *left, *right;
    TreeNode(int d = 0, TreeNode* l = NULL, TreeNode* r = NULL) 
        : data(d), left(l), right(r) {}
};

class BinSrchTree {
    TreeNode* root;
public:
    BinSrchTree() : root(NULL) {}
    TreeNode* getRoot() { return root; }

    void insert(TreeNode*& r, int val) {
        if (r == NULL) r = new TreeNode(val);
        else if (val < r->data) insert(r->left, val);
        else if (val > r->data) insert(r->right, val);
    }

    void inorder(TreeNode* n) {
        if (n) {
            inorder(n->left);
            cout << n->data << " ";
            inorder(n->right);
        }
    }

    int getCount(TreeNode* n) {
        if (n == NULL) return 0;
        return 1 + getCount(n->left) + getCount(n->right);
    }
};

int main() {
    BinSrchTree tree;
    TreeNode* root = NULL;
    int data[] = {5, 2, 3, 6, 8, 7, 9};
    
    for(int d : data) tree.insert(root, d);
    
    cout << "Inorder traversal (정렬 결과): ";
    tree.inorder(root);
    cout << "\n노드 개수: " << tree.getCount(root) << endl;
    return 0;
}