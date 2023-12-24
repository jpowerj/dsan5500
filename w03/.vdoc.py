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
gtown_loc = (38.9076, -77.0723)
gtown_loc
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
my_list = ['a','b','c']
for list_element in my_list:
  print(list_element)
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
my_nums = [4,5,6,7]
my_squares = [num ** 2 for num in my_nums]
my_squares
#
#
#
#
#
my_odd_squares = [num ** 2 for num in my_nums if num % 2 == 1]
my_odd_squares
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
animals_i_saw = ['bird','bird','fish','bird','cat','bird','lizard']
print(f"Number of animals I saw: {len(animals_i_saw)}")
#
#
#
unique_animals_me = set(animals_i_saw)
print(f"Set of unique animals: {unique_animals_me}")
print(f"Number of unique animals: {len(unique_animals_me)}")
#
#
#
#
#
#
#
#
animals_you_saw = ['lizard','dog','bird','bird','bird']
unique_animals_you = set(animals_you_saw)
unique_animals_both = unique_animals_me.intersection(unique_animals_you)
print(f"Animals we both saw: {unique_animals_both}")
#
#
#
unique_animals_either = unique_animals_me.union(unique_animals_you)
print(f"Animals either of us saw: {unique_animals_either}")
#
#
#
unique_animals_meonly = unique_animals_me - unique_animals_you
print(f"Animals I saw that you didn't see: {unique_animals_meonly}")
unique_animals_youonly = unique_animals_you - unique_animals_me
print(f"Animals you saw that I didn't see: {unique_animals_youonly}")
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
gtown_data = {
  'name': 'Georgetown University',
  'founded': 1789,
  'coordinates': (38.9076, -77.0723),
  'location': {
    'city': 'Washington',
    'state': 'DC', # <__<
    'country': 'USA'
  }
}
print(gtown_data.keys())
print(gtown_data.values())
#
#
#
#
#
#
#
#
for k in gtown_data:
  print(k)
#
#
#
#
#
for k, v in gtown_data.items():
  print(k, v)
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
class MyTuple:
  def __init__(self, thing1, thing2):
    self.thing1 = thing1
    self.thing2 = thing2

  def __repr__(self):
    return f"({self.thing1}, {self.thing2})"

  def __str__(self):
    return self.__repr__()

t1 = MyTuple('a','b')
t2 = MyTuple(111, 222)
print(t1, t2)
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
class MyList:
  def __init__(self):
    self.root = None

  def append(self, new_item):
    if self.root is None:
      self.root = MyListItem(new_item)
    else:
      self.root.append(new_item)

  def __repr__(self):
    return self.root.__repr__()
#
#
#
#
#
#
#
#
class MyListItem:
  def __init__(self, content):
    self.content = content
    self.next = None

  def append(self, new_item):
    if self.next is None:
      self.next = MyListItem(new_item)
    else:
      self.next.append(new_item)

  def __repr__(self):
    my_content = self.content
    return my_content if self.next is None else f"{my_content}, {self.next.__repr__()}"
#
#
#
#
#
#
users = MyList()
users.append('Jeff')
users.append('Alma')
users.append('Bo')
print(users)
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
t1.thing1
#
#
#
#
#
t1.thing2
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
print(users.root.content)
#
#
#
#
#
current_node = users.root
while current_node.next is not None:
  current_node = current_node.next
print(current_node.content)
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
cur_pointer1 = users.root
while cur_pointer1 is not None:
  cur_pointer2 = users.root
  while cur_pointer2 is not None:
    print(cur_pointer1.content + cur_pointer2.content)
    cur_pointer2 = cur_pointer2.next
  cur_pointer1 = cur_pointer1.next
#
#
#
#
#
#
#
printed_items = []
cur_pointer1 = users.root
while cur_pointer1 is not None:
  cur_pointer2 = users.root
  while cur_pointer2 is not None:
    print(cur_pointer1.content + cur_pointer2.content)
    printed_items.append(cur_pointer1.content)
    printed_items.append(cur_pointer2.content)
    cur_pointer2 = cur_pointer2.next
  cur_pointer1 = cur_pointer1.next
check_pointer = users.root
while check_pointer is not None:
  if check_pointer.content in printed_items:
    print(f"Phew. {check_pointer.content} printed at least once.")
  else:
    print(f"Oh no! {check_pointer.content} was never printed!!!")
  check_pointer = check_pointer.next
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
#| code-fold: true
#| fig-align: center
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
n_vals = [np.power(10, k) for k in np.arange(1, 2.75, 0.25)]
runtime_df = pd.DataFrame({'$n$': n_vals})
runtime_df['$n^2 + 50n$'] = runtime_df['$n$'].apply(lambda x: np.power(x, 2) + 50*x)
runtime_df['$n^2 + 10000$'] = runtime_df['$n$'].apply(lambda x: np.power(x, 2) + 10000)
runtime_df['$O(n)$'] = runtime_df['$n$'].copy()
runtime_df['$O(nlogn)$'] = runtime_df['$n$'].apply(lambda x: x * np.log(x))
runtime_df['$O(n^2)$'] = runtime_df['$n$'].apply(lambda x: np.power(x, 2))
runtime_df['$O(n^2logn)$'] = runtime_df['$n$'].apply(lambda x: np.power(x,2) * np.log(x))
runtime_df['$O(n^3)$'] = runtime_df['$n$'].apply(lambda x: np.power(x, 3))
runtime_df['$O(n^3logn)$'] = runtime_df['$n$'].apply(lambda x: np.power(x, 3) * np.log(x))
# Get the max values, for labeling the ends of lines
max_vals = runtime_df.max().to_dict()
plot_df = runtime_df.melt(id_vars=['$n$'])
#print(plot_df)
style_map = {col: '' if (col == '$n^2 + 50n$') or (col == '$n^2 + 10000$') else (2,1) for col in runtime_df.columns}
fig, ax = plt.subplots(figsize=(11,5))
sns.lineplot(plot_df, x='$n$', y='value', hue='variable', style='variable', dashes=style_map)
#plt.xscale('log')
plt.yscale('log')
# extract the existing handles and labels
h, l = ax.get_legend_handles_labels()
# slice the appropriate section of l and h to include in the legend
ax.legend(h[0:2], l[0:2])
for label, val in max_vals.items():
  if (label == '$n$') or (label == '$n^2 + 50n$') or (label == '$n^2 + 10000$'):
    continue
  if 'logn' in label:
    label = label.replace('logn', r'\log(n)')
  ax.text(x = max_vals['$n$'] + 2, y = val, s=label, va='center')
# Hide the right and top spines
ax.spines[['right', 'top']].set_visible(False)
plt.show()
#
#
#
#
#
#
#
#| code-fold: true
rt_const_df = runtime_df.drop(columns=['$n^2 + 50n$','$n^2 + 10000$']).copy()
rt_const_df['$20n^2$'] = rt_const_df['$n$'].apply(lambda x: 20*np.power(x,2))
# Get the max values, for labeling the ends of lines
max_vals = rt_const_df.max().to_dict()
plot_df_const = rt_const_df.melt(id_vars=['$n$'])
style_map = {col: '' if (col == '$20n^2$') else (2,1) for col in rt_const_df.columns}
fig_const, ax_const = plt.subplots(figsize=(11,5))
sns.lineplot(plot_df_const, x='$n$', y='value', hue='variable', style='variable', dashes=style_map)
#plt.xscale('log')
plt.yscale('log')
# extract the existing handles and labels
h_const, l_const = ax.get_legend_handles_labels()
# slice the appropriate section of l and h to include in the legend
ax_const.legend(h_const[0:2], l_const[0:2])
for label, val in max_vals.items():
  if (label == '$n$'):
    continue
  if 'logn' in label:
    label = label.replace('logn', r'\log(n)')
  ax_const.text(x = max_vals['$n$'] + 2, y = val, s=label, va='center')
# Hide the right and top spines
ax_const.spines[['right', 'top']].set_visible(False)
plt.show()
#
#
#
