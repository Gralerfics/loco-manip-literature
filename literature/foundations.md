# 技术基础与引用核查

这份附录回答“现有移动操作论文经常引用了哪些先行方法、究竟拿走了什么”。主表仍按移动能力参与物体任务界定；纯行走、固定臂操作和通用学习算法只放在这里。22篇PDF和[逐篇卡片](../literature/papers.md)均可离线阅读。检索日期：2026-10-26。

在81篇既有研究论文中，77篇可提取全文。脚本按标题短语扫描正文，找到高频候选后，回查引用所在正文与原论文；余4篇暂缺可核全文。标题短语命中数包括参考文献表，既不是独立引用次数，也不是实际复用次数。下表只在正文能核对具体使用时标“原文承接”。

## 方法基础怎样进入移动操作

### 模型控制与四足行走

[Unified MPC 2021](../literature-map.html#paper=2103.00946)先把机器人质心与门的动力学写进同一MPC，但接触顺序需事先给定；[ETH多接触规划](../literature-map.html#paper=2308.09179)进一步搜索脚／手接触模式，再优化连续轨迹。2025的臂动力学NMPC以早期统一MPC为先例，但因模型近似与控制架构不同，不能称作直接复制。

[RMA](../literature-map.html#paper=2107.04034)的两阶段特权教师与历史适应器是[Deep WBC](../literature-map.html#paper=2210.10044)的明确对照。后者的ROA解决潜表示训练与部署不一致的问题；这条线是训练方法的比较，不是RMA已做过带臂操作。[Challenging Terrain](../literature-map.html#paper=2010.11251)和[Perceptive Locomotion](../literature-map.html#paper=2201.08117)分别是盲走地形课程、带注意力的视觉／本体融合；很多论文引用它们说明四足地形能力，当前没有证据能把这两套行走策略当成库中所有操作策略的直接祖先。[Learning to Walk in Minutes](../literature-map.html#paper=2109.11978)与[Isaac Gym](../literature-map.html#paper=2108.10470)分别提供并行RL训练方案和GPU仿真工具。[Asymmetric Actor-Critic](../literature-map.html#paper=1710.06542)则解决仿真critic可读完整状态、实机actor只能读局部观察的问题；RoboDuet明确使用这种非对称训练框架。

### 示范、全身动作与视觉

[Original UMI](../literature-map.html#paper=2402.10329)把手持工具数据转成跨机器人可部署的相对末端动作；[UMI on Legs](../literature-map.html#paper=2407.10353)保留其示范与高层动作接口，同时新增四足全身跟踪。高层生成器明写采用[Diffusion Policy](../literature-map.html#paper=2303.04137)的U-Net扩散策略和DDIM，并将预测窗口加长。原始UMI、Diffusion Policy和四足跟踪各解决不同环节。

[DAgger](../literature-map.html#paper=1011.0686)的DAgger解决学生执行时状态分布偏离示范的问题；[Visual WBC](../literature-map.html#paper=2403.16967)训练视觉学生时直接向特权教师请求纠正动作。[ACT / ALOHA](../literature-map.html#paper=2304.13705)的ACT则预测动作块并时间集成；[WildLMa](../literature-map.html#paper=2411.15131)明写以ACT为技能模型基础，又加入[CLIP](../literature-map.html#paper=2103.00020)的文本对象概率图。[Mobile ALOHA](../literature-map.html#paper=2401.02117)把ALOHA硬件和全身遥操作扩展至轮式双臂，说明移动示范可以联合采身体和手部动作，但不能直接推出四足足端接触方案。

[Contact-GraspNet](../literature-map.html#paper=2103.14127)从深度点云产生6D抓取候选；[DQ-Net](../literature-map.html#paper=2508.08328)确实把它接入移动目标抓取候选生成。候选是否能由当前四足身体配置执行，是后作仍须处理的另一问题。

### 语言与VLA

[SayCan](../literature-map.html#paper=2204.01691)以语言模型和技能价值函数共同选择可执行步骤，是技能级长程决策的先例；[WildLMa](../literature-map.html#paper=2411.15131)虽引用它，但未核到直接复用其打分公式。[RT-1](../literature-map.html#paper=2212.06817)用Transformer做真实机器人多任务动作预测；[RT-2](../literature-map.html#paper=2307.15818)进一步把机器人动作编码成文本token与网络图文任务联合微调，是VLA术语的原始工作。[Open X-Embodiment](../literature-map.html#paper=2310.08864)汇集跨机器人数据，[Octo](../literature-map.html#paper=2405.12213)和[OpenVLA](../literature-map.html#paper=2406.09246)分别从这一数据源训练可微调策略与VLA动作模型。[WholeBodyVLA](../literature-map.html#paper=2512.11047)在实验中适配OpenVLA-OFT作为双臂与移动指令基线。[π0](../literature-map.html#paper=2410.24164)用连续动作流匹配替代动作token路线，有真实移动机械臂数据，但本库2026全身VLA主要将其列为背景，不能推断使用了原动作头或权重。

## 已核对的实际复用或基线适配

| 基础 → 后作 | 原文可核对的具体部分 |
|---|---|
| [Original UMI](../literature-map.html#paper=2402.10329) → [UMI on Legs](../literature-map.html#paper=2407.10353) | UMI on Legs §3将原始UMI的手持示范与相对末端轨迹接口接到四足全身跟踪器。 |
| [Diffusion Policy](../literature-map.html#paper=2303.04137) → [UMI on Legs](../literature-map.html#paper=2407.10353) | UMI on Legs §3.1明确按Chi等配置使用U-Net diffusion policy与DDIM，并延长未来轨迹窗口。 |
| [DAgger](../literature-map.html#paper=1011.0686) → [Visual WBC](../literature-map.html#paper=2403.16967) | Visual WBC视觉学生训练节明确采用DAgger，学生访问状态后向特权教师请求纠正动作。 |
| [ACT / ALOHA](../literature-map.html#paper=2304.13705) → [WildLMa](../literature-map.html#paper=2411.15131) | WildLMa方法节明确building upon ACT训练语言条件技能；新增CLIP对象查询与长时技能组合。 |
| [ACT / ALOHA](../literature-map.html#paper=2304.13705) → [Mobile ALOHA](../literature-map.html#paper=2401.02117) | Mobile ALOHA将ALOHA双臂遥操作硬件／示范学习扩展到带轮式底盘的全身遥操作。 |
| [Contact-GraspNet](../literature-map.html#paper=2103.14127) → [DQ-Net / DQ-Bench](../literature-map.html#paper=2508.08328) | DQ-Net正文以预训练Contact-GraspNet产生抓取姿态候选，再结合身体控制和视觉跟踪。 |
| [CLIP](../literature-map.html#paper=2103.00020) → [WildLMa](../literature-map.html#paper=2411.15131) | WildLMa明确使用CLIP文本—图像表示，计算目标物体概率图供技能网络使用。 |
| [CLIP](../literature-map.html#paper=2103.00020) → [UMI on Legs](../literature-map.html#paper=2407.10353) | UMI on Legs §3.1明确使用预训练CLIP视觉编码器。 |
| [CLIP](../literature-map.html#paper=2103.00020) → [FALCON (quadruped)](../literature-map.html#paper=2512.04381) | 四足版FALCON正文明确冻结CLIP特征，协调分离的腿部与机械臂扩散策略。 |
| [OpenVLA](../literature-map.html#paper=2406.09246) → [WholeBodyVLA](../literature-map.html#paper=2512.11047) | WholeBodyVLA实验将公开OpenVLA-OFT模型适配为双臂动作与离散移动指令基线；这是基线复用，不是其方法起源。 |
| [Asymmetric Actor-Critic](../literature-map.html#paper=1710.06542) → [RoboDuet](../literature-map.html#paper=2403.17367) | RoboDuet §IV-C明确采用非对称actor-critic训练框架，actor只读部署观察，critic可读仿真完整状态。 |
| [Open X-Embodiment](../literature-map.html#paper=2310.08864) → [OpenVLA](../literature-map.html#paper=2406.09246) | OpenVLA正文明确以Open X-Embodiment约970k轨迹训练视觉语言到动作模型。 |
| [Open X-Embodiment](../literature-map.html#paper=2310.08864) → [Octo](../literature-map.html#paper=2405.12213) | Octo正文明确在Open X-Embodiment约800k轨迹预训练，并测试跨平台微调。 |
| [RT-1](../literature-map.html#paper=2212.06817) → [RT-2](../literature-map.html#paper=2307.15818) | RT-2 §3明确沿用RT-1提出的机器人动作协议，并与RT-1比较；新增互联网视觉语言预训练及图文任务共同微调。 |
| [Octo](../literature-map.html#paper=2405.12213) → [OpenVLA](../literature-map.html#paper=2406.09246) | OpenVLA数据配比节明确采用Octo对通过初筛的数据集的混合权重启发；未复制Octo的动作架构。 |

## 只有背景引用或问题对照的例子

| 基础 → 后作 | 边界 |
|---|---|
| [RMA](../literature-map.html#paper=2107.04034) → [Deep WBC](../literature-map.html#paper=2210.10044) | Deep WBC §2.2与实验把RMA两阶段教师—学生适应作为对照基线，再提出ROA；不能称原RMA方法被全身操作系统直接采用。 |
| [Unified MPC 2021](../literature-map.html#paper=2103.00946) → [ETH Multi-Contact](../literature-map.html#paper=2308.09179) | ETH同作者方法线：2021统一MPC预设接触时序，2023增加离散接触搜索；已核题目和问题扩展，未证明复用同一求解器代码。 |
| [Unified MPC 2021](../literature-map.html#paper=2103.00946) → [Arm-dynamics NMPC](../literature-map.html#paper=2507.22042) | Arm-dynamics NMPC引言以早期统一MPC为先例，研究臂动力学不可忽略的问题；具体模型与求解已改变。 |
| [Challenging Terrain](../literature-map.html#paper=2010.11251) → [Deep WBC](../literature-map.html#paper=2210.10044) | Deep WBC引用其地形行走结果；未核到操作控制器直接沿用具体算法。 |
| [Perceptive Locomotion](../literature-map.html#paper=2201.08117) → [Terrain-Aware WBC](../literature-map.html#paper=2605.31343) | Terrain-aware WBC引用感知行走先例；其地形与末端工作空间的训练方案另行提出。 |
| [Learning to Walk in Minutes](../literature-map.html#paper=2109.11978) → [UMI on Legs](../literature-map.html#paper=2407.10353) | UMI on Legs参考并行腿式RL工作；不能仅由参考文献推断完全复用legged_gym配置。 |
| [Isaac Gym](../literature-map.html#paper=2108.10470) → [UMI on Legs](../literature-map.html#paper=2407.10353) | UMI on Legs使用Isaac Gym仿真训练低层全身策略；这是工具复用。 |
| [PPO](../literature-map.html#paper=1707.06347) → [Deep WBC](../literature-map.html#paper=2210.10044) | Deep WBC采用PPO优化策略；ROA与优势混合是另加的训练设计。 |
| [SayCan](../literature-map.html#paper=2204.01691) → [WildLMa](../literature-map.html#paper=2411.15131) | WildLMa引用SayCan作为语言规划背景；未证实采用其语言概率乘技能价值的评分公式。 |
| [Mobile ALOHA](../literature-map.html#paper=2401.02117) → [DECOWAM](../literature-map.html#paper=2608.20114) | DECOWAM以Mobile ALOHA作移动全身示范先例；未证实直接复用数据或控制算法。 |
| [π0](../literature-map.html#paper=2410.24164) → [WholeBodyVLA](../literature-map.html#paper=2512.11047) | WholeBodyVLA把π0列为一般VLA先例；没有证据显示使用原动作专家权重。 |
| [RT-2](../literature-map.html#paper=2307.15818) → [WholeBodyVLA](../literature-map.html#paper=2512.11047) | WholeBodyVLA引用RT-2作为VLA先例；自己的全身潜动作模型另行训练。 |
| [Octo](../literature-map.html#paper=2405.12213) → [UMI on Legs](../literature-map.html#paper=2407.10353) | UMI on Legs引用Octo作为通用机器人策略背景；高层实际使用Diffusion Policy。 |

## 哪些值得先学、还有什么没核完

若目标是四足＋臂控制，先读Unified MPC 2021和RMA，再对照ETH多接触、Deep WBC与Visual WBC。若目标是从示范到移动操作，先读原始UMI、Diffusion Policy、DAgger和ACT，再读UMI on Legs与WildLMa。PPO、Isaac Gym、Learning to Walk in Minutes、Asymmetric Actor-Critic是训练基础；不必把它们误当成操作任务本身的idea。VLA支路先看RT-1／RT-2的动作token、Open X的数据整合、Octo与OpenVLA，再比较π0连续动作输出接口，最后看四足／人形论文如何接底层控制器。

本轮优先处理标题／正文出现频繁且与现有研究链条相关的22篇，未把全领域所有被引算法都收进来。ALMA（ICRA 2019，DOI 10.1109/ICRA.2019.8794273）及早期全身逆动力学WBC值得继续取得原文后核读；目前只验证了其正式出版记录和ETH相关论文的参考文献，**不画未经核实的直接承接边**。当前22篇的PDF已取得并进行摘要、方法与实验相关段落定向核读；各篇卡片没有逐项复算全部表格。
