from lxml import etree

html = '''
<!DOCTYPE html>
<!-- saved from url=(0031)https://www.cnblogs.com/danmai/ -->
<html lang="zh-cn"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="origin">
    <meta http-equiv="Cache-Control" content="no-transform">
    <meta http-equiv="Cache-Control" content="no-siteapp">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>歪脖子姐姐 - 博客园</title>
    <link rel="stylesheet" href="./新建文本文档_files/blog-common.min.css">
    <link id="MainCss" rel="stylesheet" href="./新建文本文档_files/bundle-red_autumnal_leaves.min.css">
    <link id="mobile-style" media="only screen and (max-width: 767px)" type="text/css" rel="stylesheet" href="./新建文本文档_files/bundle-red_autumnal_leaves-mobile.min.css">
    <link type="application/rss+xml" rel="alternate" href="https://www.cnblogs.com/danmai/rss">
    <link type="application/rsd+xml" rel="EditURI" href="https://www.cnblogs.com/danmai/rsd.xml">
    <link type="application/wlwmanifest+xml" rel="wlwmanifest" href="https://www.cnblogs.com/danmai/wlwmanifest.xml">
    <script async="" src="./新建文本文档_files/analytics.js.下载"></script><script src="./新建文本文档_files/jquery-2.2.0.min.js.下载"></script>
    <script src="./新建文本文档_files/blog-common.min.js.下载"></script>
    <script>
        var currentBlogId = 169292;
        var currentBlogApp = 'danmai';
        var cb_enable_mathjax = false;
        var isLogined = false;
    </script> 
</head>
<body>
    <a name="top"></a>
<!--done-->
<div id="home">
<div id="header">
	<div id="blogTitle">
        <a id="lnkBlogLogo" href="https://www.cnblogs.com/danmai/"><img id="blogLogo" src="./新建文本文档_files/logo.gif" alt="返回主页"></a>		
<!--done-->
<h1><a id="Header1_HeaderTitle" class="headermaintitle HeaderMainTitle" href="https://www.cnblogs.com/danmai/">歪脖子姐姐</a>
</h1>
<h2>
学如逆水行舟，不进则退
</h2>	
	</div><!--end: blogTitle 博客的标题和副标题 -->
	<div id="navigator">
		
<ul id="navList">
<li><a id="blog_nav_sitehome" class="menu" href="https://www.cnblogs.com/">
博客园</a>
</li>
<li>
<a id="blog_nav_myhome" class="menu" href="https://www.cnblogs.com/danmai/">
首页</a>
</li>
<li>
<a id="blog_nav_newpost" class="menu" href="https://i.cnblogs.com/EditPosts.aspx?opt=1">
新随笔</a>
</li>
<li>
<a id="blog_nav_contact" class="menu" href="https://msg.cnblogs.com/send/%E6%AD%AA%E8%84%96%E5%AD%90%E5%A7%90%E5%A7%90">
联系</a></li>
<li>
<a id="blog_nav_rss" class="menu" href="https://www.cnblogs.com/danmai/rss/">
订阅</a>
<!--<partial name="./Shared/_XmlLink.cshtml" model="Model" /></li>--></li>
<li>
<a id="blog_nav_admin" class="menu" href="https://i.cnblogs.com/">
管理</a>
</li>
</ul>
		<div class="blogStats">
			
			<span id="stats_post_count">随笔 - 
28&nbsp; </span>
<span id="stats_article_count">文章 - 
0&nbsp; </span>
<span id="stats-comment_count">评论 - 
5</span>	
		</div><!--end: blogStats -->
	</div><!--end: navigator 博客导航栏 -->
</div>
</div><!--end: home 自定义的最大容器 -->
</body></html>
'''
dome = etree.HTML(html)
node = dome.xpath('//*[@id="blog_nav_sitehome"]')
print(node)
text = node[0].text
print(text)
