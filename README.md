# Quadruped loco-manipulation

四足移动操作文献库，收录 107 篇研究／方法论文和 7 篇综述。四足＋臂为主，轮足、人形、足端操作与通用基础方法分别标明。文献与核读记录更新至 2026-10-29。

## 交互网页

- [论文关系](literature-map.html) · [English](literature-map-en.html)：默认显示全部论文，支持搜索、筛选和关系溯源。
- [知识网络](knowledge-network.html) · [English](knowledge-network-en.html)：44 个机制节点，包含控制接口、接触、策略学习、观测与 VLA 执行，公式可离线阅读。

## 文献概括与阅读

- [技术发展脉络](literature/lineages.md)：区分原文承接、并行方法与问题对照。
- [论文阅读](literature/papers.md)：逐篇记录问题、接口、方法、原论文实验、复用与边界。
- [技术基础](literature/foundations.md)：先行方法及其在移动操作论文中的实际使用。
- [综述导读](literature/surveys.md)：综述的覆盖范围与文献线索。
- [知识说明](knowledge/network.md)及 [Deep WBC 训练详解](knowledge/deep-wbc.md)。
- [PDF 文献库](papers/)：供本地阅读的论文原文。

## 本地预览

在仓库根目录运行 `python -m http.server 8000`，打开 `http://localhost:8000/literature-map.html`。

公开站点只打包已整理的页面及共享资源。结构和构建方法见[部署说明](docs/deployment.md)。
