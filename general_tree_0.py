'''
Hierarchical Data Structure
Top node: Root node
Remaining: Nodes
Nodes without children: Leaf nodes

Levels:
Level 0
Level 1
...
Level N

Recursive data structure
'''

'''
Useful links

Tree (General Tree) - Data Structures & Algorithms Tutorials In Python: 
https://www.youtube.com/watch?v=4r_XR9fUPhQ&t=248s

Exercise:
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md

'''


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------#
# General Tree Class #
#--------------------#

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self,):
        '''
        Get level by counting the number of ancestors
        '''
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self):
        '''
        Printing Data Elements in all nodes
        Recursion
        '''
        spaces = ' ' * 3 * self.get_level()
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        if (len(self.children) > 0): 
            for child in self.children:
                child.print_tree()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------#
# Funcitons #
#-----------#

def build_product_tree():
    '''
    Tree
    '''
    # Root Node (Level 0)
    root = TreeNode(data="Electronics")

    # Nodes (Level 1)
    laptop = TreeNode(data="Laptop")
    cellphone = TreeNode(data="Cellphone")
    tv = TreeNode(data="TV")

    root.add_child(child=laptop)
    root.add_child(child=cellphone)
    root.add_child(child=tv)

    # Leaf Nodes (Level 2)
    # Parent Node: Laptop
    mac_laptop, surface_laptop, thinkpad_laptop = TreeNode(data="Mac"), TreeNode(data="Surface"), TreeNode(data="Thinkpad")
    laptop.add_child(mac_laptop), laptop.add_child(surface_laptop), laptop.add_child(thinkpad_laptop)

    # Parent Node: Cellphone
    iphone_cellphone, google_pixle_cellphone, vivo_cellphone = TreeNode(data="Iphone"), TreeNode(data="Google Pixle"), TreeNode(data="Vivo")
    cellphone.add_child(child=iphone_cellphone), cellphone.add_child(child=google_pixle_cellphone), cellphone.add_child(child=vivo_cellphone)

    # Parent Node: TV
    samsung_tv, lg_tv = TreeNode(data="Samsung"), TreeNode(data="LG")
    tv.add_child(child=samsung_tv), tv.add_child(child=lg_tv)

    return root

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    root = build_product_tree()

    tree_dict = {'Laptop': [0, 1, 2], 'Cellphone': [0, 1, 2], 'TV': [0, 1]}

    for N_1, k_v in enumerate(tree_dict.items()):
        k, v = k_v
        for N_2, v_i in enumerate(v):
            print('{parent_node}: {leaf_node}'.format(parent_node=root.children[N_1].data, \
                                                      leaf_node=root.children[N_2].children[N_1].data))

    mac_node, surface_node, thinkpad_node = root.children[0].children[0].data, root.children[0].children[1].data, \
                                            root.children[0].children[2].data



    root.print_tree()









#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
