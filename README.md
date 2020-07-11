# Gerapy Auto Extractor

![Python package](https://github.com/Gerapy/GerapyAutoExtractor/workflows/Python%20package/badge.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gerapy-auto-extractor)
![PyPI](https://img.shields.io/pypi/v/gerapy-auto-extractor)
![PyPI - Downloads](https://img.shields.io/pypi/dm/gerapy-auto-extractor)
![License](https://img.shields.io/badge/license-Apache%202-blue)

This is the Auto Extractor Module for [Gerapy](https://github.com/Gerapy/Gerapy), You can also use it separately.

You can use this package to distinguish between list page and detail page, and we can use it to extract
`url` from list page and also extract `title`, `datetime`, `content` from detail page without any XPath or Selector.

It works better for Chinese News Website than other scenarios.

Introduction: [Introduction](https://www.v2ex.com/t/687948)

## Installation

You can use this command to install this package:

```
pip3 install gerapy-auto-extractor
```

## Usage

Below are the methods this package implemented:

### Extraction of List Page

For list page, you can use `extract_list` method to extract the main list urls and their titles.

### Extraction of Detail Page

For detail page, you can use `extract_title` method to extract title, use `extract_content` method to extract content,
use `extract_datetime` method to extract datetime.

Also you can use `extract_detail` method to extract all above attrs, results are joined as a json.

### Classification of List/Detail Page

You can use `is_list` or `is_detail` method to distinguish if this page is list page or detail page, the type of returned result is `bool`.
Also you can use `probability_of_list` or `probability_of_detail` method to get the probability of the classification of this page, the type of returned result is `float`.

Usage example:

```python
from gerapy_auto_extractor import extract_list, extract_detail, is_detail, is_list, probability_of_detail, probability_of_list
from gerapy_auto_extractor.helpers import content, jsonify

html = content('samples/list/sample.html')
print(jsonify(extract_list(html)))

html = content('samples/detail/sample.html')
print(jsonify(extract_detail(html)))

html = content('samples/detail/sample.html')
print(probability_of_detail(html), probability_of_list(html))
print(is_detail(html), is_list(html))

html = content('samples/list/sample.html')
print(probability_of_detail(html), probability_of_list(html))
print(is_detail(html), is_list(html), )
```

HTML files can be found in [samples](./samples).

Below are outputs:

```
[
  {
    "title": "山东通报\"苟晶事件\"：15人被处理部分事实有反转",
    "url": "http://news.163.com/20/0703/13/FGK7NCOR0001899O.html"
  },
  {
    "title": "胡锡进：香港这仗就是要让华盛顿明白，它管多了",
    "url": "https://news.163.com/20/0702/19/FGI8IUEP0001899O.html"
  },
  {
    "title": "山东一校长为儿子伪造档案11岁开始领国家工资",
    "url": "https://news.163.com/20/0702/21/FGIENBGS0001899O.html"
  },
  {
    "title": "大理西洱河又现\"鱼腾\"奇景市民沿岸围观有人徒手抓",
    "url": "https://news.163.com/20/0704/03/FGLOFC3P0001875P.html"
  },
  {
    "title": "陈国基被任命为香港特别行政区国安委秘书长",
    "url": "https://news.163.com/20/0702/12/FGHFAVS200018AOQ.html"
  },
  {
    "title": "孙力军等6名中管干部被查上半年反腐数据说明啥？",
    "url": "https://news.163.com/20/0703/00/FGIPQ11D0001899O.html"
  },
  {
    "title": "香港特区政府严厉谴责暴徒恶行全力支持警队严正执法",
    "url": "https://news.163.com/20/0702/09/FGH801750001899O.html"
  }
]
{
  "title": "美国新冠肺炎确诊病例超278万例 死亡129227例",
  "datetime": "2020-07-04 01:55:04+08:00",
  "content": "（原标题：美国新冠肺炎确诊病例超过278万例）\n根据约翰斯·霍普金斯大学的最新数据统计，截至美东时间7月3日16时33分，美国新冠肺炎确诊病例超过278万例，为2780916例，死亡病例为129227例。新增确诊病例数较当日9时33分公布的数据增长了40563例。\n目前，美国至少有19个州已经下令要求民众在公共场合佩戴口罩。佛罗里达州坦帕市市长简·卡斯特在7月3日接受电视采访时表示，“在美国的任何地方都没有反对戴口罩的好理由”。卡斯特已经下令要求该市民众必须在公众场合佩戴口罩，并认为没有理由反对在全州范围颁发“口罩强制令”，但她表示最好的方式“是各市与县政府自行发出命令。”除该市外，佛罗里达州的迈阿密，杰克逊维尔和棕榈滩县也开始要求民众在公共场所戴口罩。\n截至目前，佛罗里达有接近17万人确诊新冠肺炎，日增新确诊病例数于7月2日突破1万例，今日统计再新增9488例。\n【世卫：即使20%的人拥有抗体 新冠病毒还能有效传播】\n当地时间7月3日，世卫组织召开新冠肺炎发布会，世卫组织卫生紧急项目负责人迈克尔·瑞安表示，人群中出现任何程度的抗体都会提供一定的屏障，因为一旦有人得到保护，病毒就会更难传播，但要想达到防火墙一般的效果，就需要比例较高的人群呈抗体阳性。即使20%的人拥有抗体，病毒还是能够有效传播，同时还要考虑抗体所能提供的保护时长。\n详情>>\n【美国西雅图一大学宿舍区超100名学生感染新冠肺炎】\n当地时间7月3日，据当地媒体报道，西雅图华盛顿大学的宿舍区中暴发新冠肺炎疫情，其中至少105名学生被确诊为新冠肺炎患者。校方表示，目前至少有800名学生进行了新冠病毒检测，其中至少62名确诊学生同属一个社团，目前学校已被通知停止学生一切聚会活动。\n【白宫“不顾疫情”大搞独立日庆典 预计7500人参加】\n华盛顿特区的活动只是特朗普为独立日举办的盛大庆典的第二出。当地时间3日，特朗普将前往位于南达科他州的拉什莫尔山国家纪念公园，在著名的“总统山”下发表演讲，届时还将举行烟花表演。据法新社报道，这场活动预计吸引7500人参加，然而戴口罩、保持社交距离等防疫措施依然是靠民众自觉。\n详情>>\n【美国至少37州疫情反弹 至少19州发布\"口罩强制令\"】\n截至目前，全美至少37个州出现疫情反弹，其中加利福尼亚、亚利桑那、德克萨斯，以及佛罗里达州本周确诊病例数均高于此前日增记录，另有蒙大拿、爱达荷、内华达、佛罗里达、佐治亚、田纳西、路易斯安那、阿拉斯加，以及特拉华州新增病例数超过50%。\n详情>>\n【非洲地区新冠肺炎确诊病例快速增长至43.3万】\n截至非洲东部时间7月3日，非洲疾控中心数据显示：非洲地区54个国家报告了新冠肺炎确诊病例433500例，死亡10658例，208400人康复。\n尽管非洲确诊病例数仍在持续增加，但尼日利亚、塞拉利昂等国已决定恢复通航。\n尼日利亚表示，各大机场将于近期陆续恢复国内航班的运营，其中首都阿布贾和经济中心拉各斯的机场将于8日率先开放，其他城市机场将于11日起陆续开放。国际航班的恢复日期将在适当时候宣布。\n【巴西卫生部：新冠肺炎感染人数或已超过1050万】\n巴西卫生部针对巴西全国的一项调查显示，巴西新冠肺炎实际感染人数可能已超过1050万，是目前巴西公布的已确诊新冠肺炎病毒感染人数的7倍以上。\n这项调查是由巴西卫生部与佩洛塔斯联邦大学联合进行的。这一调查结果2日发表在巴西联邦政府的报告中。这项调查分三个阶段，通过对巴西133定点人口分布最多的城市进行抽样调查，估算出具有新冠病毒抗体的人群比例，并分析巴西全国感染人群的演变。\n巴西联邦政府希望通过这个研究，帮助地方政府制定相应的经济活动开放或限制措施。"
}

0.9990605314033392 0.0009394685966607814
True False
0.033477426883441685 0.9665225731165583
False True
```

Just for Beta.

Needs more effort to improve.

## Reference

### Paper

* [面向不规则列表的网页数据抽取技术的研究](http://www.cnki.com.cn/Article/CJFDTotal-JSYJ201509023.htm)
* [基于文本及符号密度的网页正文提取方法](https://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ&dbname=CJFDLAST2019&filename=GWDZ201908029&v=MDY4MTRxVHJXTTFGckNVUkxPZmJ1Wm5GQ2poVXJyQklqclBkTEc0SDlqTXA0OUhiWVI4ZVgxTHV4WVM3RGgxVDM=)
* [基于块密度加权标签路径特征的Web新闻在线抽取](https://kns.cnki.net/kcms/detail/detail.aspx?filename=PZKX201708010&dbcode=CJFQ&dbname=CJFD2017&v=)
* [基于DOM树和视觉特征的网页信息自动抽取](http://www.cnki.com.cn/Article/CJFDTOTAL-JSJC201310069.htm)

### Project

* [GeneralNewsExtractor](https://github.com/kingname/GeneralNewsExtractor)
* [Readability](https://github.com/buriy/python-readability)

## Citing 

If you use Gerapy Auto Extractor in your research or project, please add a reference using the following BibTeX entry.

```
@misc{cui2020gerapy,
  author =       {Qingcai Cui},
  title =        {Gerapy Auto Extractor},
  howpublished = {\url{https://github.com/Gerapy/GerapyAutoExtractor}},
  year =         {2020}
}
```

## Changelog

See [Changelog](./CHANGELOG.md)
