# 用综述校准四足移动操作文献

这些综述用来检查**分类、漏检和问题定义**；具体算法、真机条件及“某篇改进了某篇”的说法仍回到原论文确认。下表引用数为 OpenAlex 在 **2026-10-22** 返回的数值，可能受正式版与预印本合并方式影响，只作传播程度的粗略信号。

| 综述 | 可核实的来源与引用 | 在本项目中的用途与边界 |
|---|---|---|
| [Gu 等，*Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning*](https://doi.org/10.1109/TMECH.2025.3579247) | *IEEE/ASME Transactions on Mechatronics*, 2026；[本地 PDF](../papers/2501.02116_Humanoid_Locomotion_and_Manipulation_Current_Progress_and_Challenges_in_Control_Planning_and_Learning.pdf)；OpenAlex 约 **31** 引 | **方法框架首选。** 正文依次讨论多接触规划、不同精度的 MPC、WBC、RL/模仿学习、触觉及 foundation models，且明确比较模型和学习方法。平台是人形；足支撑、臂的相对质量和数据获取条件不能直接照搬到四足。预印本从 2025 年起公开，期刊发表年不意味着纳入了所有 2026 年工作。 |
| [Rahman 等，*Loco-Manipulation With Quadruped Robots: Modeling, Task Taxonomy, and Control Methods—A Critical Review*](https://doi.org/10.1109/ACCESS.2026.3672605) | *IEEE Access*, 2026；[本地 PDF](../papers/IEEE_Access_2026_Loco-Manipulation_With_Quadruped_Robots_Critical_Review.pdf)；OpenAlex 约 **2** 引 | **四足范围检查表。** 全文按建模、任务分类和控制方法组织，比较 WBC、MPC、RL/IL 及混合阻抗／力控制，并讨论地形、接触、载荷和感知延迟。可用其分类和参考文献回查候选原文；各方法的性能仍须核对原论文的任务和实验条件。“最新且专门”与“高引”在这里并不同时成立。 |
| [Gong 等，*Legged Robots for Object Manipulation: A Review*](https://doi.org/10.3389/fmech.2023.1142421) | *Frontiers in Mechanical Engineering*, 2023；[本地 PDF](../papers/2303.16865_Legged_Robots_for_Object_Manipulation_A_Review.pdf)；OpenAlex 约 **40** 引 | **任务／形态分类首选。** 区分身体推／踢、用行走腿操作、专用机械臂和多机操作。它帮助判断某项结果能否用于“背载臂轻接触操作”的论证；发表于本轮 2024–2026 大量新工作之前，不能单靠它确定当前技术水平。 |
| [Suomalainen 等，*A Survey of Robot Manipulation in Contact*](https://doi.org/10.1016/j.robot.2022.104224) | *Robotics and Autonomous Systems*, 2022；[本地 PDF](../papers/2112.01942_A_Survey_of_Robot_Manipulation_in_Contact.pdf)；OpenAlex 约 **168** 引 | **接触问题的概念依据。** 分清力控制、阻抗与导纳，以及连续／离散接触状态和学习方法；重点是物体接触操作，不负责四足稳定性、足接触和移动中末端误差。 |
| [Zhao 等，*A Survey of Optimization-Based Task and Motion Planning: From Classical to Learning Approaches*](https://doi.org/10.1109/TMECH.2024.3452509) | *IEEE/ASME Transactions on Mechatronics*, 2024 在线发表、2025 卷期；[本地 PDF](../papers/2404.02817_A_Survey_of_Optimization-Based_Task_and_Motion_Planning_From_Classical_to_Learning_Approaches.pdf)；OpenAlex 约 **59** 引 | **任务顺序与连续轨迹接口。** 尤其用于“接触模式／操作步骤能否规划、失败后何时重规划”，而不是四足底层控制性能的证据。 |
| [Ma 等，*A Survey on Vision–Language–Action Models for Embodied AI*](https://doi.org/10.1109/TNNLS.2025.3650584) | *IEEE Transactions on Neural Networks and Learning Systems*, 2026；[本地 PDF](../papers/2405.14093_A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI.pdf)；OpenAlex 约 **43** 引 | **VLA 定义与数据／评测接口。** 区分任务规划器、低层动作策略和端到端动作模型；综述覆盖 embodied AI，不应据此把纯桌面 VLA 或仅 VLM 选技能的系统算作四足 loco-manipulation。 |

另有 [Chai 等 2021 四足综述](https://doi.org/10.1016/j.birob.2021.100029)，OpenAlex 约 92 引，但它主要覆盖构型与动态行走，移动操作只是其中一部分；用于早期硬件背景，优先级低于上面三篇直接相关的综述。引用数不是质量分数：新综述没有累积引用的时间，老综述也可能已漏掉关键的 2025–2026 方法。

**可供扩展的预印本。** [Li 等，*From Passive Perception to Active Interaction: A Survey of Affordance Learning for Embodied AI*](https://doi.org/10.20944/preprints202610.0392.v1) 于 2026-10-07 发布在 Preprints.org；[本地 PDF](../papers/Preprints_202610.0392_v1_From_Passive_Perception_to_Active_Interaction_A_Survey_of_Affordance_Learning_for_Embodied_AI.pdf) 已核对全文（35 页），尚未查到正式期刊／会议版本。它没有提出或实测新的机器人算法。正文第 2–5 节将 affordance 分为：**感知**可交互位置、**推理**当前任务和机器人需要哪种交互、**指导动作**。其统一表示把预测结果拆成动作类型、目标区域，以及可选的 6D 姿态、移动方向或接触后轨迹；动作层再区分把这些结果交给运动规划器／预设技能，与把它们作为策略的显式输入、隐式特征或奖励信号。这比只预测“按钮／把手在哪里”更接近可执行操作，但仍须由机器人本体和控制器验证可达性与接触稳定性。

对本项目，最有价值的是第 7.1、7.4、7.5 节指出的**待验证问题**：显式接触目标和隐式特征究竟何时改善执行，需要在同一数据、策略和动作接口下做消融；物体状态随操作变化时，应利用观测和执行结果更新可操作性判断；视觉区域匹配分数不能代替本体可达性、实际成功率和不确定性校准。第 4.3 节举 [SceneTeract](https://arxiv.org/abs/2603.29798) 为把 navigability、reachability、interactability 等条件纳入目标筛选的例子；第 5 节列出 [RT-Affordance](https://doi.org/10.1109/ICRA55743.2025.11127525)、[PALM](https://arxiv.org/abs/2601.07060) 等动作／进度相关线索。这些只是综述的参考文献线索，需核原论文后再判断是否纳入库；该综述的操作表格主要列夹爪、灵巧手和双臂，**未给四足＋臂或移动中接触操作提供直接对照**。因此它用于定义感知—动作接口，不作为本项目 loco-manipulation 性能或方法继承的证据。

## 用综述回查后，主线怎样调整

1. **先问机器人靠什么操作。** Gong 的形态分类使足端操作、身体推物、背载臂和人形作品不能混成同一条性能曲线。本库的四足＋臂为主线，其他平台保留为明确标注的邻接方法。
2. **再问哪些变量由哪一层决定。** Gu 的章节把接触顺序规划、轨迹／力优化、在线 MPC/WBC 和 RL/IL 执行分开；同一论文可同时用几层，不能把“RL、VLA、WBC”当互斥流派。对每篇应记录运行时输入、动作输出、是否需要物体模型、足接触由谁决定、接触出错由谁恢复。
3. **接触表现要单独核查。** Suomalainen 的综述提醒位置误差、接触力、阻抗和任务成功不是一个指标。对四足轻操作，还需检查小幅迈步时的末端漂移、接触峰值和物体状态是否完成；不能用站立抓取成功率代替。
4. **语言层和动作层要分开。** Ma 的分类用于辨别 VLM 分解任务、视觉技能调用及严格 VLA 动作生成；然后再由原论文确认机器人是否真的在移动中操作物体。
5. **可操作性判断与执行可行性要分开。** Li 等的全文把动作类型、接触区域和执行参数区分开，并提醒只评估区域识别会漏掉本体可达性和实际操作结果。若用于四足＋臂，还需由运动学、足／手接触条件和控制实验检验目标是否真的可达、可安全持续接触；该综述未验证过这些四足方法。

这次沿综述参考文献回查，补入 [RoLoMa 逐篇卡片](../literature/papers.md)：*Autonomous Robots* 2023，四足＋臂真机，把最不利方向的抗外力余量纳入轨迹优化。它与 Sleiman 等 2023 的接触顺序搜索、Guided RL 的执行期恢复解决不同决策环节；已在 [技术脉络](lineages.md)写清比较关系。

综述的引用还提示三篇值得进一步查原文的邻接工作：[37 自由度双臂四足的实时 whole-body MPC](https://doi.org/10.1109/HUMANOIDS57100.2023.10375215)（*Humanoids* 2023；高冗余模型控制）、[无臂四足全身推重物](https://doi.org/10.1109/LRA.2023.3335777)（*RA-L* 2023；非抓取操作）、[轮足四足的直接六维末端追踪 RL](https://doi.org/10.1109/LRA.2024.3519856)（*RA-L* 2024；邻接平台）。目前只核对了出版元数据与摘要，**不把它们画成已确认的继承链，也不据此改写当前逐篇结论**。

使用顺序：以 Gu 和 Gong 确定“方法层＋操作形态”，用 Rahman 检查四足任务组合是否漏检；遇到接触、规划或 VLA 的具体问题，再读对应专题综述，然后追其参考文献和后续引用，最后核对候选原论文的接口、实验与局限。[交互式时间与关系图](../literature-map.html)可按方法、平台、年份查看现有主线与这些综述的覆盖位置。

2026-10-24补查的十篇原文已用于校准上述分类：不平地形站立位姿、行走时动态抓放、动态对象视觉抓取、释放窗口鲁棒性及导航臂推物分别登记。此轮不是给旧综述添加新的引用数；原文关系与证据见[技术脉络](lineages.md)和[覆盖记录](../literature/papers.md)。
