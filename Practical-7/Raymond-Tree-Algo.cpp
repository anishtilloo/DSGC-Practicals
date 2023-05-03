#include <stdio.h>
#include <stdlib.h>
// Define Structure for Node
struct node {
	int id;
	int holderval;
	struct node* l;
	struct node* r;
	int require[20];
};
typedef struct node node;
//Function for inorder Traversal
void TraversalInorder(node* roonodeT)
{

	if (roonodeT == NULL) {
		return;
	}
	TraversalInorder(roonodeT->l);
	printf("%d %d\n", roonodeT->id, roonodeT->holderval);
	TraversalInorder(roonodeT->r);
}

void token(node* roonodeT, int NodeCS)
{

	if (NodeCS == roonodeT->id) {
		printf("%d\n", roonodeT->id);
		roonodeT->holderval = roonodeT->id;
		return;
	}
	else if (NodeCS < roonodeT->id) {
		roonodeT->holderval = (roonodeT->l)->id;
		printf("%d->", roonodeT->id);
		roonodeT = roonodeT->l;

		token(roonodeT, NodeCS);
	}
	else if (NodeCS > roonodeT->id) {
		roonodeT->holderval = (roonodeT->r)->id;
		printf("%d->", roonodeT->id);
		roonodeT = roonodeT->r;
		token(roonodeT, NodeCS);
	}
}

// Function to Insert Node
void NodeTinsert(node* nodeNew, node* roonodeT)
{
	if (nodeNew->id > roonodeT->id) {
		if (roonodeT->r == NULL) {
			roonodeT->r = nodeNew;
			nodeNew->holderval = roonodeT->id;
		}
		else
			NodeTinsert(nodeNew, roonodeT->r);
	}

	if (nodeNew->id < roonodeT->id) {
		if (roonodeT->l == NULL) {
			roonodeT->l = nodeNew;
			nodeNew->holderval = roonodeT->id;
		}
		else
			NodeTinsert(nodeNew, roonodeT->l);
	}
}

// Driver Function
int main()
{
	node *roonodeT = NULL, *nodeNew = NULL, *node1;
	int i;
	// Value to be given below
	int n = 5;
	int nodeT = 3;
	int idValue;
	int arr[5] = { 1, 2, 3, 4, 5 };
	int NodeCS, option;
	roonodeT = (struct node*)malloc(sizeof(node));
	node1 = (struct node*)malloc(sizeof(node));
	roonodeT->id = nodeT;
	roonodeT->r = roonodeT->l = NULL;
	roonodeT->holderval = roonodeT->id;
	for (i = 0; i < n; i++) {
		idValue = arr[i];
		nodeNew = (struct node*)malloc(sizeof(node));
		nodeNew->l = nodeNew->r = NULL;
		if (i == nodeT)
			i++;
		nodeNew->id = idValue;

		NodeTinsert(nodeNew, roonodeT);
	}
	TraversalInorder(roonodeT);
	NodeCS = 2;
	token(roonodeT, NodeCS);
	return -1;
}
