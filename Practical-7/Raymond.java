import java.util.*;
public class Raymond{
    static class Node{
        int id;
        int holderval;
        Node l;
        Node r;
        Node(){}
    }
    static void TraversalInorder(Node roonodeT){
	if (roonodeT == null) {
		return;
	}
	TraversalInorder(roonodeT.l);
	System.out.println(roonodeT.id+"  | "+roonodeT.holderval);
	TraversalInorder(roonodeT.r);
}

    static void token(Node roonodeT, int NodeCS){
	if (NodeCS == roonodeT.id) {
		System.out.println(roonodeT.id);
		roonodeT.holderval = roonodeT.id;
		return;
	}
	else if (NodeCS < roonodeT.id) {
		roonodeT.holderval = (roonodeT.l).id;
		System.out.print(" "+roonodeT.id+"->");
		roonodeT = roonodeT.l;
		token(roonodeT, NodeCS);
	}
	else if (NodeCS > roonodeT.id) {
		roonodeT.holderval = (roonodeT.r).id;
		System.out.print(" "+roonodeT.id+"->");
		roonodeT = roonodeT.r;
		token(roonodeT, NodeCS);
	}
}

    static void NodeTinsert(Node nodeNew, Node roonodeT){
	if (nodeNew.id > roonodeT.id) {
		if (roonodeT.r == null) {
			roonodeT.r = nodeNew;
			nodeNew.holderval = roonodeT.id;
		}
		else
			NodeTinsert(nodeNew, roonodeT.r);
	}

	if (nodeNew.id < roonodeT.id) {
		if (roonodeT.l == null) {
			roonodeT.l = nodeNew;
			nodeNew.holderval = roonodeT.id;
		}
		else
			NodeTinsert(nodeNew, roonodeT.l);
	}
}
    
	public static void main(String[] args) {
	Node roonodeT = null, nodeNew = null;
	int i;
	int n = 5;
	int nodeT = 4;
	int idValue;
	int[]arr = { 1, 2, 3, 4, 5};
	int NodeCS, option;
	roonodeT = new Node();
	roonodeT.id=nodeT;
	roonodeT.l=roonodeT.r=null;
	roonodeT.holderval=roonodeT.id;
	
	for (i = 0; i < n; i++) {
		idValue = arr[i];
		nodeNew = new Node();
		nodeNew.l = nodeNew.r = null;
		if (i == nodeT)
			i++;
		nodeNew.id = idValue;

		NodeTinsert(nodeNew, roonodeT);
	}
	
    System.out.println("\nPractical No : 07 ");
    System.out.println("Problem Statement : To Demonstrate and Implement Mutual Exclusion Token Raymond Tree Based algorithm."); 
	
	System.out.println("\n---Tree ( inorder traversal ) ---");
	System.out.println("ID | Holder value");
	TraversalInorder(roonodeT);
	System.out.println("------");
	NodeCS = 2;
	System.out.println("Site ID "+nodeT+" Wants to execute CS which is currently executing Site ID "+NodeCS);
	token(roonodeT, NodeCS);
	}
}