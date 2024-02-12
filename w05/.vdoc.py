# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: graphviz-setup
#| echo: false
import sys
sys.path.append('/Users/jpj/Library/CloudStorage/Dropbox/gtown/dsan5500-local/HW2/')
from IPython.display import display, HTML
import graphviz as gv # for visualizing a tree using Digraph
from graphviz import Digraph, nohtml
from hw2 import EmptyNode

def visualize_ll(ll):
  dot = Digraph(
      graph_attr={'rankdir': 'LR'},
        node_attr={'shape': 'record', 'height': '.1'}
    )
  prev_node_name = None
  node_pointer = ll.root
  while type(node_pointer) != EmptyNode:
    # New node
    cur_content = node_pointer.content
    cur_name = cur_content.item_name
    dot.node(name=cur_name, label=nohtml('{<f0> '+str(cur_name)+'|<f1>}'))
    # And edge from prev to cur, if not None
    if prev_node_name is not None:
      edge_from = f'{prev_node_name}:f1'
      dot.edge(edge_from, cur_name)
    # Now we can update prev_node_name
    prev_node_name = cur_name
    node_pointer = node_pointer.next
  display(dot)

def visualize(tree):
    dot = Digraph(
        node_attr={'shape': 'record', 'height': '.1'}
    )
    #dot.engine = 'sfdp'
    node_info_list = []
    if tree.root is not None:
      node_info_list.append({'node':tree.root, 'parent_name': None, 'dir': None})
    while len(node_info_list) > 0:
      cur_node_info = node_info_list.pop()
      cur_node = cur_node_info['node']
      cur_name = cur_node.content.item_name
      cur_parent_name = cur_node_info['parent_name']
      cur_dir = cur_node_info['dir']
      dot.node(name=cur_name, label=nohtml(f'<f0>|<f1> {cur_name}|<f2>'))
      if cur_parent_name is not None:
        # Nudge x coord based on parent
        which_port = 'f0'
        if cur_dir == 'R':
          which_port = 'f2'
        edge_from = f'{cur_parent_name}:{which_port}'
        edge_to = f'{cur_name}:f1'
        dot.edge(edge_from, edge_to, label=cur_dir)
      if cur_node.right is not None:
        node_info_list.append({'node': cur_node.right, 'parent_name': cur_name, 'dir': 'R'})
      if cur_node.left is not None:
        node_info_list.append({'node': cur_node.left, 'parent_name': cur_name, 'dir': 'L'})
    display(dot)
#
#
#
#| output-location: column
#| class-output: vertical-center
from hw2 import LinkedList, InventoryItem
ll = LinkedList()
item1 = InventoryItem('Mango', 50)
ll.append(item1)
item2 = InventoryItem('Pickle', 60)
ll.append(item2)
item3 = InventoryItem('Artichoke', 55)
ll.append(item3)
item5 = InventoryItem('Banana', 123)
ll.append(item5)
item6 = InventoryItem('Aardvark', 11)
ll.append(item6)
HTML(visualize_ll(ll))
#
#
#
#| output-location: column
from hw2 import BinarySearchTree
bst = BinarySearchTree()
item1 = InventoryItem('Mango', 50)
bst.add(item1)
item2 = InventoryItem('Pickle', 60)
bst.add(item2)
item3 = InventoryItem('Artichoke', 55)
bst.add(item3)
item5 = InventoryItem('Banana', 123)
bst.add(item5)
item6 = InventoryItem('Aardvark', 11)
bst.add(item6)
HTML(visualize(bst))
#
#
#
#
