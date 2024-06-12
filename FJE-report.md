<a name="MSP75"></a>
### UML类图
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38921555/1718179635513-5e457c6b-6412-47e8-84fd-88a98c470909.png#averageHue=%23f5f5f5&clientId=uef824ae3-be2f-4&from=paste&height=590&id=ua7c711f9&originHeight=1180&originWidth=2612&originalType=binary&ratio=2&rotation=0&showTitle=false&size=260655&status=done&style=none&taskId=u216c7977-5378-47de-8ab1-da903185207&title=&width=1306)

<a name="lLBY5"></a>
### 结果截图
<a name="CmMTj"></a>
##### tree style+default icon (no icon)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38921555/1718180296158-258b42f1-4a19-4733-893a-c14656165f9e.png#averageHue=%23212326&clientId=uef824ae3-be2f-4&from=paste&height=237&id=uec001243&originHeight=473&originWidth=1204&originalType=binary&ratio=2&rotation=0&showTitle=false&size=64055&status=done&style=none&taskId=uceff5aaa-beaa-4f60-a806-0bf0697e41c&title=&width=602)
<a name="vLmDk"></a>
##### tree style+poker icon
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38921555/1718180399773-2a49dab8-089c-4353-8826-09665c7ac30a.png#averageHue=%23212226&clientId=uef824ae3-be2f-4&from=paste&height=259&id=u26e4b75f&originHeight=517&originWidth=1249&originalType=binary&ratio=2&rotation=0&showTitle=false&size=72757&status=done&style=none&taskId=u4a2c88b7-1fc4-493d-a40d-aee7e75cfae&title=&width=624.5)
<a name="fQexS"></a>
##### tree style+自定义 icon
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38921555/1718180311432-461c2276-016e-4815-aa97-bcde9ee2da1f.png#averageHue=%23212226&clientId=uef824ae3-be2f-4&from=paste&height=270&id=u54be80b3&originHeight=540&originWidth=1239&originalType=binary&ratio=2&rotation=0&showTitle=false&size=66593&status=done&style=none&taskId=u31e492cd-ed34-4fd6-b04e-ba9c1ee786a&title=&width=619.5)
> 写着玩新增功能，语法为-i "中间icon,叶icon"

<a name="sBa6m"></a>
##### rectangle style + default icon(no icon)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38921555/1718180537568-cc302bcd-6085-44de-8410-acdd521f0ac3.png#averageHue=%23232528&clientId=uef824ae3-be2f-4&from=paste&height=282&id=u72d5d141&originHeight=563&originWidth=1267&originalType=binary&ratio=2&rotation=0&showTitle=false&size=63577&status=done&style=none&taskId=ud592293c-e947-4e3d-82b2-145dd6b0d74&title=&width=633.5)
<a name="rQnBH"></a>
##### rectangle style + poker
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38921555/1718180526480-cbeb5832-1bfb-4791-ab93-39eb6debfc94.png#averageHue=%23242529&clientId=uef824ae3-be2f-4&from=paste&height=261&id=u74d0940c&originHeight=521&originWidth=1251&originalType=binary&ratio=2&rotation=0&showTitle=false&size=62302&status=done&style=none&taskId=u3899278e-2bed-4170-88d7-fb59494a6b7&title=&width=625.5)
<a name="V0lUn"></a>
##### rectangle style + diy icon
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38921555/1718180557991-04504404-7fed-427f-beb4-afc5db5d98ca.png#averageHue=%23242529&clientId=uef824ae3-be2f-4&from=paste&height=287&id=u58b2db89&originHeight=574&originWidth=1271&originalType=binary&ratio=2&rotation=0&showTitle=false&size=72483&status=done&style=none&taskId=ub653594f-82fb-4de2-99bd-d32495c10a6&title=&width=635.5)
<a name="YpG7N"></a>
### code文件结构

- main.py
   - 命令行指令处理函数
   - 主函数
      - 按指令创建树形/矩形树
   - 执行入口
- FunnyJsonExplorer.py
   - load指令
   - build_tree递归创建树
   - 调用根的draw()作为绘图入口
- factory.py
   - 抽象工厂
      - 解析icon
      - 创建container，leaf函数
   - TreeFactory/RectangleFactory
      - 继承抽象工厂创建树形/矩形树，实现工厂模式
- leaf.py
   - component接口
      - 提供add_child和draw功能接口
   - leaf/RecLeaf类
      - 树形/矩形叶子结点，实现了叶子的draw
   - container/recontainer类
      - 容器类，包含容器/叶，负责容器的draw
<a name="swVVE"></a>
### 设计模式分析
<a name="sOr8o"></a>
##### 工厂模式
主要通过具体工厂类（如TreeFactory和RectangleFactory）实现，用于创建具体的Leaf和Container对象

- 优点：
   -  封装了对象的创建过程
   -  需要改变对象的创建逻辑或者添加新的对象类型时，只需修改或扩展工厂，提高了代码的可维护性。  
<a name="ipXpf"></a>
##### 抽象工厂模式
TreeFactory和RectangleFactory都是AbstractFactory这一抽象工厂的实现。通过定义一个包含多个工厂方法的接口（AbstractFactory），允许创建一系列相关或依赖的对象，而无需指定它们具体的类。  

- 优点：
   -  因为具体工厂类都实现自同一个接口， 方便客户端更换工厂
   -  确保了一次只能使用来自同一产品族的对象，保证一致性
<a name="CyTRM"></a>
##### 组合模式
Container由Leaf对象或其他Container对象组合而成。形成了树形结构

- 优点：
   - 保证组合对象调用上的一致性，减少代码量
   - 灵活组织树的结构，方便新组件的设计
<a name="PlnTu"></a>
##### 建造者模式

