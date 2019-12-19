Hexo博客搭建   

###1. 搭建博客   
使用hexo搭建个人博客前需要先在自己的电脑上装好git和node.js   

1. 首先在自己的电脑上创建一个空的文件夹'Hexo'  
2. 在gitbash中终端中通过`cd`指令进入到刚才创建的文件夹中   
3. 输入指令 `npm install -g hexo` 安装Hexo  
4. 输入指令 `hexo init` 进行初始化  
5. 依次输入指令`npm install` `hexo server` 启动服务器  
  博客内容发生改变后可以通过`hexo clean` `hexo generate` `hexo deploy ` `hexo server`刷新后重新启动    
###2. 部署博客  

1. 在github上创建一个空的仓库，仓库名： ``用户名.github.io``  
2. 修改博客本地仓库中的配置文件（Hexo目录下的_config.yml文件）,在文件末尾添加一下选中内容
  ![](/Users/yuting/Desktop/Files/Hexo/image1.png)  
3. 使用git部署, 输入指令`npm install hexo-deployer-git --save`  
4. 输入指令`hexo clean` `hexo generate` `hexo deploy ` 对博客进行提交
