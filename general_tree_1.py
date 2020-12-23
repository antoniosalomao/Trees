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

    def get_level(self):
        '''
        Get level by counting the number of ancestors
        '''
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, print_version, max_level):
        '''
        Printing Data Elements in all nodes
        Recursion

        print only name -> print_version == 'Name'
        print only designation --> print_version == 'Designation'
        print all --> print_version == 'ALL'
        '''

        # Data
        spaces = ' ' * 3 * self.get_level()
        prefix = spaces + "|__" if self.parent else ""

        if self.get_level() <= max_level:
            if (print_version == 'Name'):
                data_to_print = prefix + self.data['Name']
            elif (print_version == 'Designation'):
                data_to_print = prefix + self.data['Designation']
            elif (print_version == 'both'):
                data_to_print = prefix + self.data['Name'] + ' ({d})'.format(d=self.data['Designation'])
            else:
                pass
            print(data_to_print)
            if (len(self.children) > 0):
                for child in self.children:
                    child.print_tree(print_version=print_version, max_level=max_level)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------#
# Main Functions #
#----------------#

def build_product_tree():
    '''
    Tree
    Company Hierarchy
    '''
    # Root Node (Level 0)
    root_node = {'Name': 'Nilupul', 'Designation': 'CEO'}
    root = TreeNode(data=root_node)

    # Nodes (Level 1) - CTO, HR Head
    cto_dict = {'Name': 'Chinmay', 'Designation': 'CTO'}
    hr_head_dict = {'Name': 'Gels', 'Designation': 'HR Head'}

    cto, hr_head = TreeNode(data=cto_dict), TreeNode(data=hr_head_dict)
    root.add_child(child=cto), root.add_child(child=hr_head)

    # Nodes (Level 2) - Infrastructure Head, Application Head, Recruitment Manager, Policy Manager
    infra_head_dict = {'Name': 'Vishwa', 'Designation': 'Infrastrucuture Head'}
    app_head_dict = {'Name': 'Aamir', 'Designation': 'Application Head'}
    rec_manager_dict = {'Name': 'Peter', 'Designation': 'Recruitment Manager'}
    policy_manager_dict = {'Name': 'Waqas', 'Designation': 'Policy Manager'}

    infra_head, app_head = TreeNode(data=infra_head_dict), TreeNode(data=app_head_dict)
    rec_manager, policy_manager = TreeNode(data=rec_manager_dict), TreeNode(data=policy_manager_dict)

    cto.add_child(child=infra_head), cto.add_child(child=app_head)
    hr_head.add_child(child=rec_manager), hr_head.add_child(child=policy_manager)

    # Nodes (Level 3) - Cloud Manager, App Manager
    cloud_manager_dict = {'Name': 'Dhaval', 'Designation': 'Cloud Manager'}
    app_manager_dict = {'Name': 'Abhijit', 'Designation': 'App Manager'}

    cloud_manager, app_manager = TreeNode(data=cloud_manager_dict), TreeNode(data=app_manager_dict)
    infra_head.add_child(child=cloud_manager), infra_head.add_child(child=app_manager)

    return root

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------#
# Main #
#------#

if __name__ == '__main__':

    root = build_product_tree()
    root.print_tree(print_version='both', max_level=2)


