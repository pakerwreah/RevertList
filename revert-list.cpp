#include <iostream>
#include <sstream>

using namespace std;

template<class T>
class LinkedList {
	private:
		class Node {
			public:
				T content;
				Node *next;
				Node(T content);
		};
	
		int count;
		Node *head;
	public:
		LinkedList() {
			count = 0;
			head = NULL;
		}
	
		void add(T item);
		void revert();
		T item(int index);
		int size();
};

template<class T>
LinkedList<T>::Node::Node(T content) {
	this->content = content;
	next = NULL;
}

template<class T>
void LinkedList<T>::add(T item) {
	Node *node = new Node(item);
	if(head == NULL)
		head = node;
	else {
		Node *n = head;
		while(n->next!=NULL)
			n = n->next;
		
		n->next = node;
	}
	
	count++;
}

template<class T>
void LinkedList<T>::revert() {
	Node *prev = NULL, *curr = head;
	while(curr!=NULL) {
		Node *tmp = curr->next;
		curr->next = prev;
		prev = curr;
		curr = tmp;
	}
	
	head = prev;
}

template<class T>
T LinkedList<T>::item(int index) {

	Node *n = head;

	for(int i=0; i<index; i++)
		n = n->next;
		
	return n->content;
}

template<class T>
int LinkedList<T>::size() {
	return count;
}

template<class T>
string print(LinkedList<T> &list) {
	stringstream buf;

	for(int i=0; i<list.size(); i++)
		buf << list.item(i) << " ";
		
	buf << endl;
	
	return buf.str();
}

int main() {
	
	LinkedList<int> list;
	for(int i=0; i<10; i++)
		list.add(i+1);
		
	cout << print(list);
	list.revert();
	cout << print(list);
		
	LinkedList<string> str_list;
	for(int i=0; i<5; i++)
		str_list.add("str" + to_string(i+1));
		
	cout << print(str_list);
	str_list.revert();
	cout << print(str_list);
	
	cout << endl;
}
