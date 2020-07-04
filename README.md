# Gerapy Auto Extractor

This is the Auto Extractor Module for Gerapy.

You can also use it separately.

## Installation

```
pip3 install gerapy-auto-extractor
```

## Usage

This package implemented this column for different pages:

### Detail Page

* title
* content
* datetime

### List Page

* href
* title

Usage example:

```python
from gerapy_auto_extractor.extractors.list import extract_list
from gerapy_auto_extractor.extractors import extract
import json
from os.path import join, dirname, abspath

html = open(join(dirname(abspath(__file__)), 'samples/list/sample4.html'), encoding='utf-8').read()
print(json.dumps(extract_list(html), indent=2, ensure_ascii=False, default=str))


html = open(join(dirname(abspath(__file__)), 'samples/content/sample2.html'), encoding='utf-8').read()
print(json.dumps(extract(html), indent=2, ensure_ascii=False, default=str))
```

HTML files can be found in [samples](./samples).

Below are outputs:

```
[
  {
    "title": "00后比90后少了4700万！这些大省出手了！专家：人口负增长拐点或在2027年前到来",
    "href": "https://new.qq.com/omn/20200704/20200704A04HVX00.html"
  },
  {
    "title": "三大战区海军演练",
    "href": "https://new.qq.com/omn/20200704/20200704V05JOU00.html"
  },
  {
    "title": "专题传奇落幕！林丹正式宣布退役无缘第五次征战奥运",
    "href": "https://new.qq.com/zt/template/?id=SPO2020070400561800"
  },
  {
    "title": "丹麦国宝小美人鱼雕像被喷上“种族主义鱼”涂鸦，警方在查！",
    "href": "https://new.qq.com/omn/20200704/20200704A05G9A00.html"
  },
  {
    "title": "专题中移动招标风波细节曝光：美的举报格力造假，格力称系小失误",
    "href": "https://new.qq.com/zt/template/?id=FIN2020070400288400"
  },
  {
    "title": "想引2000名博士硕士遭热议，这个弱省会城市如何破局",
    "href": "https://new.qq.com/omn/20200704/20200704A06UAW00.html"
  },
  {
    "title": "每天“像狗一样被殴打”，韩国22岁女运动员因长期遭霸凌选择自尽",
    "href": "https://new.qq.com/omn/20200704/20200704A0946000.html"
  },
  {
    "title": "贵州毕节发生4.5级地震幼儿园老师带176名孩子17秒撤离",
    "href": "https://new.qq.com/omn/20200703/20200703V0G4E800.html"
  },
  {
    "title": "浙江法华寺招聘抖音视频编导：朝九晚五，月薪过万",
    "href": "https://new.qq.com/omn/20200704/20200704A09CJO00.html"
  },
  {
    "title": "新京报评论：“野火青年”们，别假装关心洪灾受灾同胞了",
    "href": "https://new.qq.com/omn/20200704/20200704A07ENE00.html"
  }
]

{
  "title": "美国新冠肺炎确诊病例超278万例 死亡129227例",
  "datetime": "2020-07-04 01:55:04+08:00",
  "content": "\n                        （原标题：美国新冠肺炎确诊病例超过278万例）\n                    \n根据约翰斯·霍普金斯大学的最新数据统计，截至美东时间7月3日。新增确诊病例数较当日9时33分公布的数据增长了40563例。\n目前，美国至少有19个州已经下令要求民众在公共场合佩戴口罩。佛罗里达州坦帕市市长简·卡斯特在7月3日接受电视采访时，但她表示最好的方式“是各市与县政府自行发出命令。”除该市外，佛罗里达州的迈阿密，杰克逊维尔和棕榈滩县也开始要求民众在公共场所戴口罩。\n截至目前，佛罗里达有接近17万人\n【世卫：即使20%的人拥有抗体 新冠病毒还能有效传播】\n当地时间7月3日，世卫组织召开新冠肺炎发布会，世卫组织卫生紧急项目负责人迈克尔·瑞安表示，人群中出现任何程度的抗体能够有效传播，同时还要考虑抗体所能提供的保护时长。\n详情>>\n【美国西雅图一大学宿舍区超100名学生感染新冠肺炎】\n当地时间7月3日，据当地媒体报道，西雅图华盛顿大学的宿舍方表示，目前至少有800名学生进行了新冠病毒检测，其中至少62名确诊学生同属一个社团，目前学校已被通知停止学生一切聚会活动。\n【白宫“不顾疫情”大搞独立日庆典 预计7500人参下发表演讲，届时还将举行烟花表演。据法新社报道，这场活动预计吸引7500人参加，然而戴口罩、保持社交距离等防疫措施依然是靠民众自觉。\n详情>>\n【美国至少37州疫情反弹 至少增记录，另有蒙大拿、爱达荷、内华达、佛罗里达、佐治亚、田纳西、路易斯安那、阿拉斯加，以及特拉华州新增病例数超过50%。\n详情>>\n【非洲地区新冠肺炎确诊病例快速增长至43.家报告了新冠肺炎确诊病例433500例，死亡10658例，208400人康复。\n尽管非洲确诊病例数仍在持续增加，但尼日利亚、塞拉利昂等国已决定恢复通航。\n尼日利亚表示，各大机场将于近候宣布。\n【巴西卫生部：新冠肺炎感染人数或已超过1050万】\n巴西卫生部针对巴西全国的一项调查显示，巴西新冠肺炎实际感染人数可能已超过1050万，是目前巴西公布的已确诊新冠这一调查结果2日发表在巴西联邦政府的报告中。这项调查分三个阶段，通过对巴西133定点人口分布最多的城市进行抽样调查，估算出具有新冠病毒抗体的人群比例，并分析巴西全国感染人群的演变。\n巴西联邦政府希望通过这个研究，帮助地方政府制定相应的经济活动开放或限制措施。\n\n"
}
```

Just for Beta.

Needs more effort to improve.
