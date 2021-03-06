# 结构模式-组合模式
## 意图
表示一个复杂的树形对象时，使用相同的类进行组合，而不是单独设计根结点、中间节点和叶子节点<br/>
以保持单个对象和组合对象的一致性<br/>
避免不同类的反复继承以及误用<br/>
## 适用性
1、需要表示一个有多种对象组合而成的树形结构<br/>
2、期望忽略组合与每个子对象之间的差异，使其可以动态地在结构中组合<br/>
## 场景
1、树形结构的node<br/>
2、多级菜单栏等<br/>
## 优缺点
1、可以自由调整节点的数量及层级<br/>
2、简化调用接口<br/>
## 实现
这里我们会提供两个demo<br/>
第一个demo是基于[leetcode（力扣）](https://leetcode-cn.com/)算法题中经典的二叉树Node进行拓展<br/>
第二个demo基于创建模式中，将手机制造中不同组件都看作一个节点的例子<br/>

demo1<br/>
继承力扣的二叉树Node，并新增一个parent属性，作为父节点<br/>
然后再生成一个一个拥有7个节点的搜索二叉树<br/>

demo2<br/>
我们提供一个component的类，作为组合模式的基础类<br/>
同时component类中拥有name、price和sub_components三个属性，分别表示这个组件的名称、价格以及自组件<br/>
调用get_info可以获取组件的基础信息以及自组件信息<br/>
作为叶子节点的组件sub_components属性为空，使得在调用get_info方法时，不会去读取叶子节点的子节点，以完成组合模式的目的<br/>
```python
from structural.composite.example import Node


class NodeWithParent(Node):
    """
    我们对leetcode原始的类进行改进
    添加parent属性，表示父节点
    """

    def __init__(self, val: int = None, left: Node.__subclasses__() = None, right: Node.__subclasses__() = None,
                 parent: Node.__subclasses__() = None):
        """
        在Node类的基础上增加parent属性
        :param val:
        :param left:
        :param right:
        :param parent:
        """
        super(NodeWithParent, self).__init__(val, left, right)
        self.parent = parent


# 以搜索二叉树为例
# 生成根结点
root = NodeWithParent(3)
# 生成根结点直属的左右子节点，并直接为它配置父节点
level_1_left = NodeWithParent(1, parent=root)
level_1_right = NodeWithParent(5, parent=root)
# 为根结点设置左右子节点
root.left = level_1_left
root.right = level_1_right
# 生成四个叶子节点
level_2_left_1 = NodeWithParent(0, parent=level_1_left)
level_2_left_2 = NodeWithParent(4, parent=level_1_right)
level_2_right_1 = NodeWithParent(2, parent=level_1_left)
level_2_right_2 = NodeWithParent(6, parent=level_1_right)
# 将叶子节点配置到根结点的左右子节点中
level_1_left.left = level_2_left_1
level_1_left.right = level_2_right_1
level_1_right.left = level_2_left_2
level_1_right.right = level_2_right_2
```
[具体实现代码](./example/binary_tree.py)

demo2<br/>
```python
class Component(object):
    def __init__(self, name: str, price: int, sub_components: iter = None):
        self.sub_components = sub_components
        self.name = name
        self.price = price

    def get_sub_component_info(self, level: int = 1):
        """
        获取子节点组件信息
        :param level:
        :return:
        """
        for sub_component in self.sub_components:
            sub_component.get_info(level + 1)

    def get_info(self, level: int = 0):
        """
        获取设备信息，同时获取子节点信息
        :param level:
        :return:
        """
        space = '\t' * level
        print(f'{space} component name: {self.name}')
        print(f'{space} component price: {self.price}')
        if self.sub_components:
            print(f'{space} here are the sub components of {self.name}')
            self.get_sub_component_info(level)

def make_pro_composites():
    """
    组合模式样例1
    :return:
    """
    phone_pro = Component('phone pro', 4999)
    screen_national = Component('national 2k screen', 300)
    camera = Component('leica adjusted camera', 250)
    mother_board = Component('pro mother board', 400)
    soc = Component('990', 200)
    memory = Component('64G', 80)
    battery = Component('5000mah', 300)
    phone_pro.sub_components = [screen_national, camera, mother_board, battery]
    mother_board.sub_components = [soc, memory]
    return phone_pro
```
[具体实现代码](./example/phone.py)