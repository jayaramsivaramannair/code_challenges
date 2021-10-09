/* 
Directions:
Implementation of a Linked List

Create a class to represent a Linked List. When created, a linked list should have 
"no" head node associated with it. The LinkedList instance will have one property, 
'head', which is a reference to the first node of the linked list. By default 'head'
should be 'null'

Example-

const list = new LinkedList()
list.head // Returns null

Linked List Methods:
- insertFirst(data)
Create a new Node from argument 'data' and assigns the resulting node to the 
'head' property. Make sure to handle the case in which the linked list already
has a node assigned to the 'head' property

Example - 
const list = new LinkedList()
list.insertFirst('Hi There'); // List has one node

- size
Returns the number of nodes in the linked list

Example  -

const list = new LinkedList()
list.insertFirst('a')
list.insertFirst('b')
list.insertFirst('c')
list.size() // Returns 3

- getFirst
Returns the first node of the linked list

const list = new LinkedList()
list.insertFirst('a');
list.insertFirst('b');
list.getFirst(); // Returns Node instance with data 'a'


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/