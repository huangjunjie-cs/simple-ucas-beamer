================================
FAQ (Frequently Asked Questions)
================================


为什么做这个项目
================


做这个项目的初衷是一直以来都自己在用的一个模板，在毕业之际，封装出来，供人查看也好，自己回顾也好，算是一个对自己的交代。

最开始做这个项目的原因是因为之前流传一个带有国科大的logo的模板，其中footer的图片（见下图），还挺有意思的 (雁栖湖+大学），但是由于最早的版本是png的。这对于logo类图片的矢量化的趋势是矛盾的。因此，基于那个图片，我用tikz的工具简单花了一下（主要是画直线）。


.. figure:: ../../assets/footer_ucas_logo.png
   :alt: a footer ucas logo used in this project 

   

另外，值得一题的是，在国科大硕博论文模板中，我发现其中的 [logo圆不圆]_ ，提交了issues，并没有人关注。也是可惜...

.. figure:: https://user-images.githubusercontent.com/11959047/138208393-28203c7e-d7ec-4880-b1dc-9b329ea185f6.png
   :alt: logo问题

其实国科大的logo是很容易得到矢量图的。不过大家科研太忙，[nbcs]_ 罢了...
[国科大官网logo]_ 给出了原版AI的图，使用AI工具简单导出一下就行...

.. dropdown:: 小声细语（🤫)

   Be to honest, 一个每年毕业上万理工科学生的模板，连学校的logo的圆都画不圆真心有点...



部分页面不需要背景
==================

.. code-block:: latex

   {
   \usebackgroundtemplate{}
   \begin{frame}{xxx}

   ...
   \end{frame}
   }





如何引用中带入会议名称
======================

常见的beamer中，引用使用 \ :code:`\\cite`\。但是在计算机会议中，我们通常会有一些简写，例如AAAI, ICML, ICLR等。因此，需要定义一个新的命令如下

.. code-block:: latex

   \newcommand{\tinycite}[2][2]{{~\tiny{(\citeauthor[#1]{#2}})}}

使用如下:

.. code-block:: latex

   \tinycite[AAAI2021]{xxx}




如何加入Reference页
===================

这个倒不算复杂，需要注意的问题主要是：

+ 不断页，尽量压缩（字体小)
+ 无页脚number\ 
+ 



References
==========



.. [国科大官网logo] https://www.ucas.edu.cn/site/11?zu=64925

.. [logo圆不圆] https://github.com/mohuangrui/ucasthesis/issues/360

.. [nbcs] Nobody cares.
