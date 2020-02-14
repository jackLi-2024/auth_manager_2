### 说明：
    1.框架运行
        本地运行: python3 lambda_function.py
        物理机部署: sh bin/start.sh
        aws-serverless运行: 入口为lambda_function.lambda_handler
    2.开发者需知
        开发者需要在resource新增自己python包
        例如实例中给出了test模块
            a.view  定义所有接口的地方
            b.utils  开发者自定义功能
            
            # 备注（重要）:开发者可以按文档全部调试自己的代码，也可以仅仅定义自己业务模块（例如test）,但是本机调试注意加上以下代码表示模块的查找路径
            `
            cur_dir = os.path.split(os.path.realpath(__file__))[0]
            sys.path.append("%s/" % cur_dir)
            `    
    3.备注
        开发者view中定义模型接口时，注意接口类必须继承BaseApi

            
 **请求URL：**
- ` http://127.0.0.1:4901/graphql_api `
- ` https://cq-platform.pand-iot.com/auth2/graphql_doc_ui` 线上环境
- ` https://cq-platform.pand-iot.com/auth2/graphql_api` 线上环境

**请求方式：**
- POST

**几个概念： **
- 菜单目录：主要创建菜单目录树，并方便为功能配置访问权限（资源权限），也方便为资源权限配置数据权限，例如"查询"
- 用户组：主要为用户关联的对象，例如"张三需要管理角色用户组中的超级管理员"
- 资源权限：主要将菜单功能与用户组绑定，也就是该用户组的用户都会拥有该菜单目录的访问权限
- 数据权限：主要是将资源权限的数据类型进行控制，资源权限控制接口的访问权限，数据权限控制资源权限相关的数据
- 数据组：例如数据组为城市，可以定义成都，重庆等
- 刷新token：在生成token过程中，会返回两种token，一种用于用于验证token用的accesstoken,一种刷新accesstoken的freshtoken，在本设计中验证的token过期时间是3分中有效，刷新token一天有效

![](http://222.180.198.30:4999/server/../Public/Uploads/2020-02-14/5e4659f4244b2.png)



            
    
