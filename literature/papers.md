# 论文阅读：问题、方法、实验与贡献

每篇论文在同一处记录问题、接口、方法、实验与贡献核查；共用机制可由链接回到知识网络。共 107 篇研究／方法论文，其中 103 篇有正文或定向方法／实验核读记录；具体深度逐篇登记。另 4 篇尚未取得可核对全文，仅保留既有检索卡片，不作为新机制结论的全文证据。7篇综述提供分类与定义，性能结论回到原论文。核读日期：2026-10-29。

知识节点的“前置”表示学习依赖；论文之间的直接继承只在有原文依据时登记。每个节点合并共同机制，来源说明谁在何处怎样使用；这不声明所列作者首先发明该机制。Walk These Ways与另22篇技术基础单列；loco-manipulation、跨平台邻接与通用方法分别标明。当前是可继续补写的领域知识稿，不声称文献穷尽或未经独立验证的稳定性证明。

本表将一篇论文拆成复用部分、实际改动、证据和限制。共用同一知识标签表示机制相关，不表示直接引用／继承。依赖PDF文件是否存在不能判断是否已读；下面的阅读范围是实际正文核读登记。

[知识网络](../knowledge/network.md) · [交互阅读页](../knowledge-network.html#view=papers)

## 研究与方法论文索引

| 工作 | 平台 | 本次核读 | 对应知识 |
|---|---|---|---|
| [RoLoMa](#2203-01446) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K01, K10, K11, K36 |
| [ETH Multi-Contact](#2308-09179) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K01, K05, K10, K24, K36 |
| [Guided RL](#2410-13817) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K10, K17, K18, K24, K30 |
| [RAMBO](#2504-06662) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K04, K05, K08, K13, K19, K38 |
| [Arm-dynamics NMPC](#2507-22042) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K01, K05, K06, K36 |
| [Safe Whole-Body Loco-Manipul](#2603-02443) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K02, K08, K09, K12, K15 |
| [Sumo](#2604-08508) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K05, K14, K29, K38, K37 |
| [Learning Loco-Manipulation F](#2608-12063) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K14, K17, K18, K29 |
| [Contact-Guided Exploration f](#2608-28140) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K14, K16, K17, K22 |
| [Deep WBC](#2210-10044) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K02, K04, K13, K15, K16, K43 |
| [RoboDuet](#2403-17367) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K02, K03, K04, K13, K46 |
| [UMI on Legs](#2407-10353) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K02, K14, K19, K20, K25, K27, K28, K47, K44 |
| [Multi-critic Learning for Wh](#2507-08656) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K04, K15, K16, K43 |
| [MLM](#2508-10538) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K15, K16, K17, K20, K21 |
| [Force Control](#2405-01402) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K07, K08, K09, K15 |
| [Position + Force RL](#2505-20829) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K07, K08, K09, K31 |
| [Learning Tactile-Aware Quadr](#2604-27224) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K14, K20, K31, K39 |
| [TAC-LOCO](#2607-10132) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K07, K13, K16, K39 |
| [FWBC-VLA](#2609-03889) | 轮足 | 正文／方法与实验定向核读；范围见下 | K09, K26, K31 |
| [Force-Aware Reinforcement Le](#2609-13779) | 轮足 | 正文／方法与实验定向核读；范围见下 | K07, K09, K15, K31 |
| [Visual WBC](#2403-16967) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K13, K15, K21, K40 |
| [QuadWBG](#2411-06782) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K03, K12, K15, K21, K22, K23 |
| [WildLMa](#2411-15131) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K14, K21, K23, K26, K42, K40 |
| [SLIM](#2501-09905) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K14, K15, K17, K21, K27, K40, K42, K44 |
| [ODYSSEY](#2508-08240) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K13, K15, K23, K26 |
| [SigLoMa](#2605-03846) | 四足＋固定夹爪 | 正文／方法与实验定向核读；范围见下 | K22, K25, K38, K40 |
| [DECOWAM](#2608-20114) | 轮足 | 正文／方法与实验定向核读；范围见下 | K14, K26, K29, K13, K15 |
| [CMP](#2604-07457) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K03, K12, K47 |
| [Terrain-Aware WBC](#2605-31343) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K02, K12, K13, K15 |
| [FT-WBC](#2606-24466) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K12, K13, K15, K38 |
| [Reinforcement Learning Based](#2610-23548) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K12, K13, K15, K16, K02 |
| [Hierarchical Optimization-ba](#2311-00112) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K01, K05, K06, K36 |
| [Design and Control Co-Optimi](#paper-32) | 四足＋臂 | 未取得可核对全文 | K01, K03, K06 |
| [LocoMan](#2403-18197) | 四足＋腿部小臂 | 正文／方法与实验定向核读；范围见下 | K03, K05, K38 |
| [Learning Visual Quadrupedal ](#2403-20328) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K02, K14, K15, K20, K21 |
| [Pedipulate](#2402-10837) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K13, K17, K38, K43 |
| [HiLMa-Res](#2407-06584) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K14, K17, K19, K38 |
| [Learning Multi-Agent Loco-Ma](#2411-07104) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K14, K15, K17, K29 |
| [Env-Mani](#paper-38) | 四足＋臂 | 未取得可核对全文 | K11, K38 |
| [HMC](#2511-14756) | 人形 | 正文／方法与实验定向核读；范围见下 | K04, K08, K13, K31 |
| [HANDO](#2510-09221) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K14, K23, K26 |
| [Calf-Integrated Arms for Bim](#2607-06186) | 四足＋腿部小臂 | 正文／方法与实验定向核读；范围见下 | K03, K22, K26, K30, K38 |
| [PAKE](#2607-11041) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K03, K12, K13 |
| [TONAV](#2608-22296) | 轮足 | 正文／方法与实验定向核读；范围见下 | K23, K24, K27 |
| [DeViGrasp](#2609-22278) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K15, K21, K25 |
| [Contact as a Decision Variab](#2609-30140) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K10, K11, K12, K36, K38 |
| [SOMA](#2610-20968) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K14, K17, K29, K38, K03, K15 |
| [KINO](#2609-18869) | 人形 | 正文／方法与实验定向核读；范围见下 | K14, K26, K28 |
| [Opt2VLA](#2609-23968) | 人形 | 正文／方法与实验定向核读；范围见下 | K08, K26, K31, K36, K47 |
| [DiPLO](#2610-24847) | 人形 | 正文／方法与实验定向核读；范围见下 | K05, K14, K18, K29, K15, K41, K44 |
| [Learning to Open and Travers](#2409-04882) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K13, K15, K17, K24 |
| [Human2LocoMan](#2506-16475) | 四足＋腿部小臂 | 正文／方法与实验定向核读；范围见下 | K14, K28, K38 |
| [RAKOMO](#2507-19652) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K03, K05, K12 |
| [GeCCo](#2509-17582) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K04, K10, K20, K38 |
| [WholeBodyVLA](#2512-11047) | 人形 | 正文／方法与实验定向核读；范围见下 | K14, K26, K28 |
| [OpenHEART](#2603-05830) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K15, K24, K40 |
| [ReCo](#2610-01612) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K02, K06, K29, K37, K19 |
| [Adaptive-MHE](#2609-17832) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K09, K15, K29, K36 |
| [QLIMB](#paper-58) | 四足＋臂 | 未取得可核对全文 | K12, K13 |
| [From Policy Actions to Whole](#paper-59) | 四足＋臂 | 未取得可核对全文 | K04, K05, K13 |
| [Arm-Constrained Curriculum L](#2403-16535) | 轮足 | 正文／方法与实验定向核读；范围见下 | K04, K13, K17 |
| [CAIMAN](#2502-00835) | 四足足端／无臂 | 正文／方法与实验定向核读；范围见下 | K14, K17, K29 |
| [ReLIC](#2506-07876) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K13, K19, K26, K38 |
| [Athletic Loco-Manipulation](#paper-63) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K06, K14, K18, K19, K30, K38 |
| [DemoHLM](#2510-11258) | 人形 | 正文／方法与实验定向核读；范围见下 | K14, K15, K17, K21, K28, K41 |
| [EgoHumanoid](#2602-10106) | 人形 | 正文／方法与实验定向核读；范围见下 | K14, K26, K28 |
| [Ψ₀](#paper-66) | 人形 | 正文／方法与实验定向核读；范围见下 | K14, K26, K28, K27 |
| [POT-VLA](#2607-18016) | 人形 | 正文／方法与实验定向核读；范围见下 | K25, K26, K30 |
| [HoMMI](#paper-68) | 轮式双臂 | 正文／方法与实验定向核读；范围见下 | K02, K14, K20, K28, K42 |
| [FALCON](#2505-06776) | 人形 | 正文／方法与实验定向核读；范围见下 | K06, K07, K13, K17, K19, K38, K09, K16 |
| [Whole-body Pose Tracking](#2409-16048) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K02, K03, K12, K13, K17, K20, K38 |
| [PFG Unified Policy](#2507-04229) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K02, K03, K12, K13, K16, K17, K20 |
| [Badminton](#2505-22974) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K06, K15, K19, K20, K25, K37, K38, K43 |
| [Accurate Throwing](#2506-16986) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K04, K06, K14, K18, K19, K20, K29, K37, K38, K45 |
| [Interactive Arm-Pushing](#2503-01474) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K10, K14, K15, K17, K23, K29, K30, K36 |
| [DQ-Net / DQ-Bench](#2508-08328) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K14, K15, K20, K21, K22, K25, K40, K42, K44, K38 |
| [FALCON (quadruped)](#2512-04381) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K13, K14, K20, K25, K26, K27, K30, K42, K44 |
| [Whole-Body ID-MPC](#2511-19709) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K01, K04, K05, K06, K07, K08, K10, K11, K19, K37, K36 |
| [Deployment Framework](#2512-18938) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K04, K09, K13, K15, K19, K27, K37, K38 |
| [Dynamic Pick-and-Place](#2605-15713) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K03, K06, K13, K14, K15, K17, K18, K30, K38 |
| [Walk These Ways](#2212-03238) | 四足行走（无臂） | 正文／方法与实验定向核读；范围见下 | K04, K13, K14, K15, K17, K19, K46 |
| [PPO](#1707-06347) | 通用方法 | 正文／方法与实验定向核读；范围见下 | K43 |
| [DAgger](#1011-0686) | 通用方法 | 正文／方法与实验定向核读；范围见下 | K44, K15 |
| [Isaac Gym](#2108-10470) | 跨平台仿真工具 | 正文／方法与实验定向核读；范围见下 | K19, K43 |
| [RMA](#2107-04034) | 四足行走（无臂） | 正文／方法与实验定向核读；范围见下 | K15, K19 |
| [Learning to Walk in Minutes](#2109-11978) | 四足行走（无臂） | 正文／方法与实验定向核读；范围见下 | K19, K43 |
| [Challenging Terrain](#2010-11251) | 四足行走（无臂） | 正文／方法与实验定向核读；范围见下 | K19 |
| [Perceptive Locomotion](#2201-08117) | 四足行走（无臂） | 正文／方法与实验定向核读；范围见下 | K15, K40 |
| [Unified MPC 2021](#2103-00946) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K01, K05, K10 |
| [Original UMI](#2402-10329) | 固定臂操作／数据接口 | 正文／方法与实验定向核读；范围见下 | K02, K20, K28 |
| [Diffusion Policy](#2303-04137) | 固定臂操作／动作生成 | 正文／方法与实验定向核读；范围见下 | K20, K27, K44 |
| [ACT / ALOHA](#2304-13705) | 固定双臂操作 | 正文／方法与实验定向核读；范围见下 | K27, K44 |
| [Mobile ALOHA](#2401-02117) | 轮式双臂 | 正文／方法与实验定向核读；范围见下 | K13, K28, K44 |
| [SayCan](#2204-01691) | 轮式移动机械臂 | 正文／方法与实验定向核读；范围见下 | K26 |
| [Contact-GraspNet](#2103-14127) | 通用机械臂 | 正文／方法与实验定向核读；范围见下 | K22 |
| [OpenVLA](#2406-09246) | 固定臂操作／通用模型 | 正文／方法与实验定向核读；范围见下 | K26, K27 |
| [π0](#2410-24164) | 多形态机械臂／移动机械臂 | 正文／方法与实验定向核读；范围见下 | K26, K27 |
| [CLIP](#2103-00020) | 通用视觉语言模型 | 正文／方法与实验定向核读；范围见下 | K22, K40 |
| [Asymmetric Actor-Critic](#1710-06542) | 通用方法／机械臂 | 正文／方法与实验定向核读；范围见下 | K15, K43 |
| [RT-1](#2212-06817) | 固定／移动机械臂数据 | 正文／方法与实验定向核读；范围见下 | K26, K27 |
| [RT-2](#2307-15818) | 固定／移动机械臂数据 | 正文／方法与实验定向核读；范围见下 | K26, K27 |
| [Open X-Embodiment](#2310-08864) | 跨机器人数据／模型 | 正文／方法与实验定向核读；范围见下 | K28, K26 |
| [Octo](#2405-12213) | 跨机器人策略 | 正文／方法与实验定向核读；范围见下 | K26, K28 |
| [MoManipVLA](#2503-13446) | 轮式＋臂 | 正文／方法与实验定向核读；范围见下 | K03, K12, K14, K26, K47 |
| [Whole-Body UMI](#2609-22829) | 人形 | 正文／方法与实验定向核读；范围见下 | K03, K14, K20, K28, K47 |
| [Walking Bot VLA](#2610-32271) | 四足＋臂 | 正文／方法与实验定向核读；范围见下 | K14, K26, K27, K28, K47 |
| [SuperMimic](#2610-28480) | 人形（移动操作邻接训练方法） | 正文／方法与实验定向核读；范围见下 | K19, K43, K48 |

<a id="2203-01446"></a>
## 2203.01446 RoLoMa: Robust Loco-Manipulation for Quadruped Robots with Arms

[RoLoMa](../literature-map.html#paper=2203.01446) · [PDF](../papers/2203.01446_RoLoMa_Robust_Loco-Manipulation_for_Quadruped_Robots_with_Arms.pdf) · [原文](https://doi.org/10.1007/s10514-023-10146-0)

**原问题与接口。** 全身控制器能纠正一定的执行偏差，但如果规划的姿态本来就几乎承受不了额外作用力，执行时再补救的余地很小。 输入机器人、手臂及接触的模型，给定操作任务和预设的接触切换顺序；输出身体、关节、手端与足端的整段运动轨迹，交给现有控制器同步执行。

**对应／相邻机制。** [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)；[K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)；[K11 抗扰裕量是在扰动发生前保留余地](../knowledge/network.md#k11)；[K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)

**来源与版本。** *Autonomous Robots* 2023；首次预印本：2022-03。由高相关综述的参考文献回溯补入

**方法。** 从动力学、关节力矩和摩擦等约束计算轨迹在最不利方向上还能承受多大外力，用这个抗扰裕量作为轨迹优化目标；允许足接触位置在给定阶段内调整。接触何时建立或断开仍需预先指定。

**实验设置。** ANYmal＋Kinova 真机在工业平台模拟环境转手轮、拉杆、推门，并在后退迈步时拉绳提桶；比较不同轨迹承受外力的能力。论文报告其优化轨迹在所测方向上的最小不可抵抗外力约 60 N，比对照轨迹高约 33%。

**阅读定位：重要对照。** 较早将抗外力余量写进四足＋臂轨迹优化，建立模型分支的重要参照；当前没有核到多支后作默认采用该特定目标／求解器，和ETH多接触规划也不是直接继承。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)：预设阶段的轨迹优化
- [K11 抗扰裕量是在扰动发生前保留余地](../knowledge/network.md#k11)：规划抗扰裕量

**平台与执行。** ANYmal＋Kinova 六自由度臂；真机实验。

**相对已有方法的具体改动。** 将作者此前站立情况下的最小不可抵抗外力（SUF）优化扩展到预设接触切换的全身轨迹，同时优化落足位置，主动保留抗外力余量。

**复用部分。** SUF、剩余力多面体和站立抗扰优化来自作者 2020／2021 年工作；逆动力学和直接离散轨迹优化是已有工具。

**实验能支持什么。** 真机操作手轮、拉杆与绳索提桶，并在迈步时提起未知载荷。三个施力方向的测力计实验中，测得最小抗扰余量约 60 N，名义／基线约 45 N；另有 30 分钟重复执行演示。

**未覆盖条件与比较限制。** 离线规划；含抗扰目标的阀门轨迹求解约 26–38 秒。接触顺序和时间由外部给定，没有物体动力学或接触力反馈。模型余量比实测失效阈值高 21–22%，施力方向测试有限。

**阅读范围。** 已核对 PDF 题名与版本；阅读主要动力学、抗扰能力定义、接触切换、全部实验、接触位置优化和讨论；用参考文献核对 SUF 的前序来源。

**原文定位。** §1.1；§3.1–3.6；§4.1–4.6；§5；§6.1–6.4

**核读订正。** 不能把 SUF 写成 2023 年首次提出的方法，也不能把该规划器写成在线 MPC；抗扰力余量不构成任意碰撞安全保证。

<a id="2308-09179"></a>
## 2308.09179 Versatile Multi-Contact Planning and Control for Legged Loco-Manipulation

[ETH Multi-Contact](../literature-map.html#paper=2308.09179) · [PDF](../papers/2308.09179_Versatile_Multi-Contact_Planning_and_Control_for_Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2308.09179)

**原问题与接口。** 打开带回弹力的门时，不能只规划手臂；还要决定站在哪里、用手还是脚顶住、何时松开。 输入：机器人和物体的几何、动力学模型，允许接触的部位，初始状态和任务目标，例如把门打开并通过。 输出：先生成身体、关节、物体的运动计划，以及接触位置、接触顺序和作用力；执行时由两层控制器跟踪计划。

**对应／相邻机制。** [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)；[K24 机构约束与在线交互辨识](../knowledge/network.md#k24)；[K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)

**来源与版本。** 首次预印本：2023-08-17

**方法。** 在接触状态树中搜索候选接触切换，每次扩展都用短期轨迹优化检查几何和动力学可行性；交替使用目标方向与随机方向扩展。找到接触序列后固定它，重新优化整段连续运动。

**实验设置。** 真机开关重洗碗机、通过弹簧门；也有阀门等仿真任务。

**阅读定位：核心主线。** 把手、足和环境接触的选择与连续全身轨迹统一起来，是模型规划分支的基础参照；Guided RL明确使用其规划器生成训练示范。因此它同时是完整系统和可以被后作提取使用的规划基础。

**主线判断的证据范围。** Guided RL引言“build upon ... framework from Sleiman et al.”；T-Mech综述[84]。已核实直接算法复用主要是Guided RL，不能说全领域默认使用此规划器。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)：基础模型的应用
- [K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)：多层优化
- [K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)：联合决策
- [K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)：联合预测
- [K24 机构约束与在线交互辨识](../knowledge/network.md#k24)：已知机构模型

**平台与执行。** ANYmal＋自制六自由度臂；仿真场景及真机门／洗碗机任务。

**相对已有方法的具体改动。** 逻辑引导的离散物体接触搜索与短时连续最优控制问题（OCP）交错进行，结合随机探索及长时域细化，从少量任务目标求出多接触模式的全身计划。

**复用部分。** 使用作者 2021 年质心动力学＋全身运动学＋物体动力学的 OCP；借鉴任务与运动规划／逻辑几何规划、ANA* 和 RRT 式探索，执行层使用 MPC 与分层 QP。

**实验能支持什么。** 改变肢体可操作区域／关节限位会产生不同接触计划；真机穿过弹簧闭门器门、操作高静摩擦洗碗机，接触力最高约 125 N。消融分别检验采样、逻辑规则、后处理、MPC 和接触力前馈。

**未覆盖条件与比较限制。** 依赖预建几何／可操作区域及名义物体动力学；在线追踪器不重搜完整接触序列，丢失物体接触可能使离线计划失效。步态模板和接触建立／解除的简单时序结构仍预设。

**阅读范围。** 已阅读主要方法、结果、讨论和控制器；核对补充材料中的动力学／约束、代价／参考构造、剪枝实现、算法消融和 WBC 优先级表。

**原文定位。** Materials and Methods；Results；Discussion；Supplement S2–S7；Table S7

**核读订正。** 离线规划包含物体状态，在线追踪 MPC 为提速删去物体状态；不能写成无先验地自动发现步态的所有细节。

<a id="2410-13817"></a>
## 2410.13817 Guided Reinforcement Learning for Robust Multi-Contact Loco-Manipulation

[Guided RL](../literature-map.html#paper=2410.13817) · [PDF](../papers/2410.13817_Guided_Reinforcement_Learning_for_Robust_Multi-Contact_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2410.13817)

**原问题与接口。** 上一类规划算出的动作可行，但物体参数不准、手滑或机器人被推时，照着原计划执行容易失败。 输入：机器人和物体的当前状态、与示范的偏差、抓取端的位置和速度、当前动作进度。训练另需每个任务的一条规划示范。 输出：全身关节角度目标，以及示范进度的调整量；可以放慢、加快或倒退到前面的阶段。

**对应／相邻机制。** [K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)；[K24 机构约束与在线交互辨识](../knowledge/network.md#k24)；[K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)

**来源与版本。** 首次预印本：2024-10-17

**方法。** 跟踪偏差大时自动降低示范进度的推进速度，让策略先追赶；另由策略输出进度残差，必要时倒退重抓。训练改变摩擦、门的弹簧参数等，按当前接触模式启用身体、物体和抓取关系的跟踪目标。

**实验设置。** 四种门／洗碗机任务，各 4096 个仿真测试，比较固定时钟、最近参考搜索、自适应进度及消融。拉门任务的固定时钟与完整方法成功率为 15.38%／96.33%，定义为完成示范进度超过 95%；主要增益来自自适应推进，进度残差的平均增益较小。ANYmal 真机每项任务完成六次连续测试。

**阅读定位：重要对照。** 已证实承接ETH规划器，把示范执行变成可反馈、可恢复的RL；是清楚的发展步骤，但尚无已核实的多支下游采用其自适应进度模块。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)：执行反馈
- [K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)：参考进度反馈
- [K24 机构约束与在线交互辨识](../knowledge/network.md#k24)：锁扣建模边界
- [K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)：示范阶段

**平台与执行。** ANYmal-D＋六自由度臂；四种门／洗碗机任务均有仿真与实机验证。

**相对已有方法的具体改动。** 根据当前状态／追踪奖励推进示范相位，执行落后时放慢或暂停；学到的相位残差可在接触丢失后回退。按接触模式构造追踪，使单条规划示范成为反馈执行参考。

**复用部分。** 直接采用 ETH 2023 年多接触规划器，结合 PPO、参考状态初始化（RSI）、关节残差追踪与域随机化。

**实验能支持什么。** 每任务 4096 个仿真回合；比较名义执行、近邻参考、自适应相位，并消融相位残差／课程／关节参考。拉门名义执行 15.38%，自适应相位＋残差 96.33%，成功定义为完成超过 95% 的示范进度；每任务另有连续六次实机测试。

**未覆盖条件与比较限制。** 物体／手柄状态由动捕提供，初始状态仅覆盖参考附近，每任务一条示范。附录 D.1 将手柄建为固定连杆，加入锁止机构后成功率较低；不是完整在线任务与运动规划，也不是仅凭机载视觉完成任务。

**阅读范围。** 已阅读主要方法和全部实验；核对附录 B 的示范来源、C 的观测／奖励／随机化／训练细节，以及 D 的限制。

**原文定位。** §3.1–3.5；§4；§5.1–5.3；Appendix B/C/D

**核读订正。** 主要成功率收益来自自适应相位，相位残差的平均额外收益较小；不能认为已解决门锁解锁。示范进度判据与应用任务的完成判据不同。

<a id="2504-06662"></a>
## 2504.06662 RAMBO: RL-Augmented Model-Based Whole-Body Control for Loco-Manipulation

[RAMBO](../literature-map.html#paper=2504.06662) · [PDF](../papers/2504.06662_RAMBO_RL-Augmented_Model-Based_Whole-Body_Control_for_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2504.06662)

**原问题与接口。** 模型控制能明确计算施力，但怕模型不准；单靠学习又不容易精确控制接触力。 输入：期望身体速度、操作足端的位置和施力，机器人自身状态、步态信息及近期历史。 输出：最终关节力矩。其中模型计算基础力矩，学习模块修正身体加速度和关节角度目标，再形成反馈力矩。

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** 首次预印本：2025-04-09。**Go2 无外挂臂，以前腿操作。**

**方法。** 用单刚体模型解接触力分配 QP，再通过足端 Jacobian 得到前馈力矩；强化学习分别纠正身体加速度参考和关节位置参考。它的 QP 不等同于完整关节逆动力学的全身控制器。

**实验设置。** Go2 真机用前腿推购物车、保持托盘平衡、持软物体，包含三腿支撑行走和后两腿行走；仿真比较无前馈、不同残差通道等设置。力目标训练施加反向虚拟外力，主要量化末端位置误差，不能把该表直接当作腕部力传感器的力跟踪误差。

**阅读定位：重要对照。** 模型WBC加RL纠错是重要混合控制对照；残差学习的大类早已存在，尚未核实本文特定接口在多个后作中成为标准组件。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)：模型前馈加反馈
- [K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)：当前力矩生成
- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：执行链残差

**平台与执行。** Unitree Go2，无外挂机械臂；以前腿操作，其他三腿支撑，或用后两腿行走。

**相对已有方法的具体改动。** 接触力分配 QP 计算前馈力矩，RL 同时修正期望身体加速度和逆运动学关节目标；前馈与 PD 反馈分离，使较低反馈增益下仍可支撑并柔顺交互。

**复用部分。** 使用 SRB 接触力分配、逆运动学、启发式步态、PD、PPO 与 QP 求解器。

**实验能支持什么。** 三个训练种子，每个 1000 个仿真回合；消融仅前馈、仅身体残差、仅关节残差以及去掉 QP。实机包括推车、托盘／柔软物体、地形与推扰、低增益握手。

**未覆盖条件与比较限制。** 力追踪训练施加反向虚拟力，主要报告末端位置误差，没有经标定的直接 F/T 力追踪误差表。机载状态会漂移，因操作表面不确定而省略操作接触摩擦检查；最终关节 PD 残差力矩也不由 QP 保证可行。

**阅读范围。** 已阅读单刚体（SRB）和步态预备知识、全部方法小节、定量／真机对比、柔顺实验、结论和表格。

**原文定位。** §III；§IV-A/B/C；§V-A/B/C/D；§VI；Tables I–V

**核读订正。** 平台无外挂臂。QP 是 SRB 接触力分配，不是完整逆动力学分层 QP；低增益柔顺演示不构成任意安全证明。

<a id="2507-22042"></a>
## 2507.22042 A Nonlinear MPC Framework for Loco-Manipulation of Quadrupedal Robots with Non-Negligible Manipulator Dynamics

[Arm-dynamics NMPC](../literature-map.html#paper=2507.22042) · [PDF](../papers/2507.22042_A_Nonlinear_MPC_Framework_for_Loco-Manipulation_of_Quadrupedal_Robots_with_Non-Negligible_Manipulator_Dynamics.pdf) · [原文](https://arxiv.org/abs/2507.22042)

**原问题与接口。** 小机器狗背上较重的臂时，把臂当成固定附加重量，会漏掉臂运动对身体平衡的影响。 输入：身体和臂的状态、模型、接触条件，以及操作者给出的身体速度、朝向和臂关节目标。 输出：规划层输出未来身体运动和机械臂力矩；腿的下层控制器把身体运动计划转成腿部力矩，臂力矩直接执行。

**对应／相邻机制。** [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)

**来源与版本。** 首次预印本：2025-07-29

**方法。** 将身体单刚体模型与浮动机械臂模型分开，以安装点刚性约束和交互力／力矩保持动态一致性；同时优化身体运动、足底力和臂力矩。实际求解每个预测时域内冻结臂惯量、忽略臂的科里奥利项，每周期更新惯量，仍有计算近似。

**实验设置。** Go2 约 15 kg、Kinova 臂约 4.4 kg；规划约 60 Hz，腿部控制约 500 Hz。真机验证负载、扰动、地形及开门／抽屉等遥操作；200 个随机地形中走完 10 m 的仿真稳定通过率为 86%／28%，这是移动稳定性，非操作任务成功率。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)：臂动力学近似的实例
- [K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)：保留臂动力学的取舍

**平台与执行。** Go2 约 15 kg＋Kinova Gen2 四自由度臂 4.4 kg；真机与仿真。

**相对已有方法的具体改动。** 通过刚性安装加速度约束与隐式相互作用力，将身体 SRB 动力学和浮基臂动力学耦合，联合优化臂力矩与身体地面接触力，不预先消去耦合变量。

**复用部分。** 使用 SRB 行走模型、非线性 WBC、力矩控制、CasADi／IPOPT 和 Raibert 落足启发式。

**实验能支持什么。** 遥操作冰箱／抽屉／门／推车／抓放，另测粗糙地形、载荷及外推扰动。仿真 200 个随机地形中走完 10 m 的稳定通过率为 86%，运动学—质心基线为 28%；身体 WBC 相同，但臂力矩／PD 实现也不同。

**未覆盖条件与比较限制。** 实际求解省略臂科氏项，在预测窗口内冻结惯量、每周期更新。计算在外部 i9 电脑上，操作员提供身体／臂／夹爪命令；未验证自主任务规划或详细接触安全指标。

**阅读范围。** 已阅读动力学分解、刚性安装约束、分层控制器、设置／实现、真机任务和定量对比。

**原文定位。** §II；§III-A/B；§IV-A/B/C；§V

**核读订正。** 86／28 是行走稳定通过率，不是操作成功率。质心基线保留全身运动学，不能等同于完全没有臂影响；数值实现也不是毫无简化的完整臂动力学。

<a id="2603-02443"></a>
## 2603.02443 Safe Whole-Body Loco-Manipulation via Combined Model and Learning-based Control

[Safe Whole-Body Loco-Manipul](../literature-map.html#paper=2603.02443) · [PDF](../papers/2603.02443_Safe_Whole-Body_Loco-Manipulation_via_Combined_Model_and_Learning-based_Control.pdf) · [原文](https://arxiv.org/abs/2603.02443)

**原问题与接口。** 人推拉夹爪时，既要顺着作用力移动，也要避免身体或臂进入不允许的状态。 输入：腕部力和力矩测量，机器人状态、估计的身体速度、允许的运动约束。 输出：先把外力换算成末端移动速度，再分配给臂和身体；臂由模型控制，腿由学习控制器输出关节角度。

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)；[K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)

**来源与版本。** 首次预印本：2026-03-02

**方法。** 以设定的刚度、阻尼把测得外力转换为末端速度，并扣除身体运动来计算臂速度；参考管理器调整可能违反位置、速度、力及运动学边界的目标，另用状态估计改善身体速度反馈。

**实验设置。** Go2＋六自由度臂和腕部六维力传感器，仿真与真机验证人与机器人共同搬运等受力交互。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)：导纳与约束参考

**平台与执行。** Go2＋D1 六自由度舵机臂＋BOTA 腕部力／力矩传感器。

**相对已有方法的具体改动。** 模型式臂导纳提供快速局部修正，RL 行走器响应末端速度要求；改进身体速度估计并过滤参考，使共同搬运中可以柔顺协调。

**复用部分。** 使用导纳、卡尔曼滤波、神经网络残差模型、参考调节器／最大输出容许集（MOAS）理论和 PPO。

**实验能支持什么。** 真机共同搬运木板，测外力驱动的六维速度追踪；参考调节器有／无的阶跃参考对比测位置／速度约束违反，并报告动捕下状态估计误差。

**未覆盖条件与比较限制。** 需要腕部 F/T。实际 MOAS 为各轴独立离散采样并通过 KD-tree 近邻查询，不能推出全身耦合混合系统安全；状态估计表未分别消融神经网络／滤波器／低通滤波。

**阅读范围。** 已阅读导纳／身体补偿、RL 控制器、神经网络辅助卡尔曼估计、参考调节器、全部实机验证及讨论。

**原文定位。** §III-A–E；§IV；§V

**核读订正。** 不是无力传感器控制。神经网络预测平均误差的外积并不自动是经标定的条件协方差；参考调节器证据限于建模／采样约束，不能推广到所有碰撞。

<a id="2604-08508"></a>
## 2604.08508 Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation

[Sumo](../literature-map.html#paper=2604.08508) · [PDF](../papers/2604.08508_Sumo_Dynamic_and_Generalizable_Whole-Body_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2604.08508)

**原问题与接口。** 重物抬不起来时，要推、拖或翻转；每换一种物体就重新训练完整任务策略，成本很高。 输入：机器人和物体的状态估计、物体模型、任务评分规则，例如轮胎离直立状态还有多远。 输出：短期身体速度、臂关节目标等命令；已有的低层控制器把这些命令转成全身关节目标。

**对应／相邻机制。** [K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** 首次预印本：2026-04-09

**方法。** 运行时在仿真里尝试多组候选命令，每组都经过低层控制器执行预测；选评分好的方案，执行一小段后重算。

**实验设置。** Spot 真机八种任务各十次，包括扶正／叠放重轮胎、拖围栏等；使用已有 ReLIC 控制器，部分任务借助脚和身体接触。G1 人形任务只在仿真中验证；对照中的通用三项成本用于受控仿真，完整真机任务另有任务专用成本。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)：预测内含低层策略
- [K37 训练可预测的步态，再辨识闭环响应](../knowledge/network.md#k37)：仿真闭环预测对照
- [K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)：仿真内运行低层策略

**平台与执行。** Spot＋臂有实机，Unitree G1 仅仿真。

**相对已有方法的具体改动。** 在线在命令空间做采样 MPC，将冻结的预训练 ReLIC 放进完整接触物理仿真展开，用较低维命令搜索稳定动作，同时允许测试时更换物体／目标。

**复用部分。** 使用 ReLIC、CEM／MPPI 系列、MuJoCo 与样条参数化搜索；没有提出新的低层控制策略。

**实验能支持什么。** 在受控仿真的五种物体中共用代价，比较端到端 MPC／RL 和分层 RL；Spot 实机八种任务各十次，包括轮胎扶正／堆叠、拖障碍。G1 只有仿真。

**未覆盖条件与比较限制。** 需要物体模型／状态；真机用动捕与外部 Threadripper。完整任务演示还使用任务专用代价和固定物体坐标系接近／抓取点，试验次数少。高层学习基线没有显式新模型参数，而 MPC 获得新物理模型。

**阅读范围。** 已阅读分层结构、策略嵌入动力学、采样规划器／接口、全部分析／真机章节、限制，以及附录真机任务代价。

**原文定位。** §III-A–E；§IV-A–D；§V-A/B/C；§VI；Appendix A

**核读订正。** 不是 VLA，也不是未知环境自主操作。三项通用代价对应受控仿真分析，并非覆盖所有真机任务；实机物体上的站位／抓取点不是在线接触点优化得到的。

<a id="2608-12063"></a>
## 2608.12063 Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL

[Learning Loco-Manipulation F](../literature-map.html#paper=2608.12063) · [PDF](../papers/2608.12063_Learning_Loco-Manipulation_From_SMPC_Demonstrations_With_Sparse_Offline-to-Online_RL.pdf) · [原文](https://arxiv.org/abs/2608.12063)

**原问题与接口。** 只在任务完成时给奖励，机器人随机练习很难碰巧成功；手工设计很多中间奖励又费时。 输入：有噪声的机器人和物体状态及任务目标；真机结合机载传感与外部运动捕捉获得状态。训练时先用仿真规划器生成成功经验。 输出：上层输出身体速度和臂关节目标的变化量；已有低层策略生成全身关节角度。Spot 实验不额外调整身体高度和俯仰。

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)

**来源与版本。** 首次预印本：2026-08-12

**方法。** 以采样式 MPC 自动生成经验，早期 TD3 训练约一半批数据来自规划器；达到成功率阈值后逐步去掉旧数据，用稀疏任务奖励继续学习。动作以命令增量表示，评价网络输出被限制在理论回报范围；数据规划器仍使用需调节的稠密成本。

**实验设置。** Spot 推箱子、轮胎扶正／滚动及 G1 推箱子均有真机演示；完成时间、数据量／质量及多模态示范消融主要在仿真中量化。Spot 推理离机，G1 推理机载；两者使用外部动捕辅助状态估计。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)：成功示范初始化
- [K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)：经验初始化后优化

**平台与执行。** Spot＋臂与 Unitree G1 均有真机；OptiTrack 观测物体／机器人，Spot 外部计算，G1 机载计算。

**相对已有方法的具体改动。** 以采样 MPC 的分块示范经验初始化稀疏奖励 TD3，策略改善后逐渐退出专家样本；限制 critic 值范围并采用增量命令，提高训练／执行稳定性。

**复用部分。** 使用 ReLIC、TD3／FastTD3、采样 MPC 与向量化 MuJoCo Warp。

**实验能支持什么。** 五种任务策略部署，仿真比较相对教师的任务时长，消融数据量／质量和多峰示范。最难的滚轮胎任务需约 400 万样本；在仿真评测中改善时长和一致性。

**未覆盖条件与比较限制。** 教师仍需设计稠密代价；冻结低层策略限制任务适应。状态来自外部动捕，最优行为局限于数据支持；单峰 TD3 和有限历史使其难处理某些多峰示范。

**阅读范围。** 已阅读稀疏 RL、教师数据收集、实验 Q1–Q4、限制，以及附录示范退出／训练／critic 界限／SMPC／真机实现。

**原文定位。** §3.1–3.3；§4 Q1–Q4；§6；Appendix A/B/B.1/C/D

**核读订正。** 稀疏奖励仅用于学到的高层任务策略，不用于示范生成器或低层控制器。多峰数据失败是特定任务／算法结果；真机演示不等于全面成功率基准。

<a id="2608-28140"></a>
## 2608.28140 Contact-Guided Exploration for Non-Prehensile Locomanipulation with Multi-Critic RL

[Contact-Guided Exploration f](../literature-map.html#paper=2608.28140) · [PDF](../papers/2608.28140_Contact-Guided_Exploration_for_Non-Prehensile_Locomanipulation_with_Multi-Critic_RL.pdf) · [原文](https://arxiv.org/abs/2608.28140)

**原问题与接口。** 推椅子时，如果一直碰不到合适位置，学习几乎收不到有用奖励；一直奖励靠近某个点又会妨碍真正移动椅子。 输入：身体和臂的关节状态、重力方向、身体速度，以及物体位置、朝向和到目标的误差。接触候选点和物体速度是训练评价网络的额外信息。 输出：上层输出臂关节角度、身体高度和身体速度；固定的行走策略输出腿部关节角度。

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)

**来源与版本。** 首次预印本：2026-08-28

**方法。** 用三个价值估计头分别评价任务完成、接近接触点和动作规范程度，再按权重合并各组优势来更新动作策略。接触探索权重按训练迭代从 0.1 降到 0.01，动作规范权重从 0.15 升到 0.24；它不是每次碰到物体就触发的在线切换。

**实验设置。** 推箱子、移椅子仿真比较单价值网络／多价值网络与有无权重调度；主要对照均使用接触引导奖励。真机四种未见 IKEA 物体合计 40/58 次成功（约 69%），其中两种是少量边界案例。另有洗碗机门的接触切换分析。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)：探索权重变化
- [K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)：接触提示

**平台与执行。** ALMA quadruped+arm;frozenbasevelocity/heightRL;objectmocap

**相对已有方法的具体改动。** grasp-derivedcandidatepoint exploration；task/explore/regmultiheadcritics+weightedadvantageschedules；frozenlegcontroller+HLarm/baseheight

**复用部分。** PPO/LSTM、graspingalgorithm、domainrandomization、pretrainedlocomotion

**实验能支持什么。** singlePPO/scheduledPPO/fixedmulti/scheduledmultiallhavecontactreward；sim5seeds94.1%；unseenIKEAreal40/58=69%;dishwasherbranchcontactswitchandjointlimits

**未覆盖条件与比较限制。** mocapobject;realsharpturnodometryfailures；chairgeometrytrialcountsunequal；dishwashersection未明确truehardware

**阅读范围。** 正文 §III/IV核心方法所有仿真/硬件/接触分支审读；无另附录

**原文定位。** §III-A/B/C; §IV-A/B/C/D; TableII

**核读订正。** regularizationweight实际增加0.15→0.24，不是decay；overviewword与正文不一致；noexplorationrewardextra0%不是主要baseline设定；dishwashercontactswitch不要无证写真机

<a id="2210-10044"></a>
## 2210.10044 Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion

[Deep WBC](../literature-map.html#paper=2210.10044) · [PDF](../papers/2210.10044_Deep_Whole-Body_Control_Learning_a_Unified_Policy_for_Manipulation_and_Locomotion.pdf) · [原文](https://arxiv.org/abs/2210.10044)

**原问题与接口。** 腿和臂分别控制时，臂够不到地面目标，身体也不知道应该蹲下或倾斜来帮忙。 输入：身体姿态与角速度、腿和臂的关节状态、脚接触信息、上一动作、期望身体速度和末端位置／朝向。 输出：腿和臂的关节角度目标；每个关节的底层控制器再把角度误差变成力矩。

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)

**来源与版本。** 首次预印本：2022-10-18

**方法。** 在仿真里联合训练腿和臂；初期将操作优势主要用于臂动作、移动优势主要用于腿动作，再逐渐混入交叉影响。历史网络拟合环境编码，环境编码也被约束到历史可预测的表示，降低训练时特权信息与部署观测之间的差距。

**实验设置。** 低成本 Go1＋臂，展示擦白板、取放、按按钮和抛物等；目标可来自遥控、视觉模块或示范回放。

**阅读定位：核心主线。** 后续实际采用的不只是“腿和臂一起动”：Visual WBC明确采用ROA，Terrain-Aware WBC §III的ROA引用[6]指向本文，TAC-LOCO §4的advantage mixing引用[10]指向本文。不同作者、不同任务重复使用可辨识的训练模块。

**主线判断的证据范围。** Visual WBC附录的Regularized online adaptation；Terrain-Aware WBC ROA小节；TAC-LOCO §4。ROA和AM的继承不意味着照搬整套控制器。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)：部分不随身体姿态的参考
- [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)：角度目标接口
- [K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)：动作组优势和非对称训练
- [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)：全关节策略
- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：历史推断
- [K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)：按动作组混合优势

**平台与执行。** Unitree Go1 + Interbotix WidowX 250s; 12 leg + 6 arm joint PD targets; gripper separate

**相对已有方法的具体改动。** 共享全身状态与策略；按动作组混合操作/移动优势；同时学习并约束 privileged encoder 与 history adapter

**复用部分。** PPO、关节 PD、domain randomization、球坐标任务、AprilTag 目标外环

**实验能支持什么。** 3 seeds ×1000 simulation episodes；独立/统一/无交叉优势等；RMA/DR/teacher 比较；真实抓取 easy 3 点/hard 5 点，每任务10次

**未覆盖条件与比较限制。** 目标随 base xy/yaw，height/roll/pitch 部分解耦；无显式末端 force 目标；机器人任务由遥操作/AprilTag/重放提供

**阅读范围。** 正文控制方法/仿真与真机实验审读；附录 B–E、部署/轨迹部分审读；未观看视频/运行代码

**原文定位。** §2; §2.1; §2.2; §3.2; §3.3; Appendix B–E

**核读订正。** 并非完整固定 world/task frame；共享网络含 separate action heads，不能用“一个网络”排除分工；任务演示非全面自主任务判断

<a id="2403-17367"></a>
## 2403.17367 RoboDuet: Learning a Cooperative Policy for Whole-body Legged Loco-Manipulation

[RoboDuet](../literature-map.html#paper=2403.17367) · [PDF](../papers/2403.17367_RoboDuet_Learning_a_Cooperative_Policy_for_Whole-body_Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2403.17367)

**原问题与接口。** 联合策略的精确末端姿态跟踪仍困难；又希望保留已经练好的走路能力。 输入：期望身体速度、末端位置和朝向，身体和关节状态、近期动作；两策略共享必要状态。 输出：臂策略输出臂关节角度，以及期望身体俯仰／侧倾；腿策略执行身体速度和姿态，输出腿关节角度。

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)

**来源与版本。** 首次预印本：2024-03-26

**方法。** 先训练稳定行走，再启用臂与操作目标，让两策略协作。臂不只管自己的关节，还能请求身体改变姿态。

**实验设置。** 仿真和真机比较跟踪、工作空间与任务表现，并测试相近 Go1／Go2 平台之间的迁移。

**阅读定位：重要对照。** 两阶段、腿臂协作是统一策略之外的重要替代架构，有正式发表和对照；被引用、被当基线与后作实际沿用协作接口是不同证据，目前后者不足以称为默认范式。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)：学习姿态请求
- [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)：姿态请求协作
- [K46 用可调行为保留同一任务的多种运动解](../knowledge/network.md#k46)：步态条件基础的受限继承
- ：相似目标、不同分工

**平台与执行。** Unitree Go1 + ARX5; also sim A1/Go2 and real Go2 policy transfer

**相对已有方法的具体改动。** arm policy 6 joint offsets + 2 base posture guidance；leg policy 确保 locomotion；stage1 fixed arm pretraining、stage2 cooperation 和 reward 调整

**复用部分。** PPO、asymmetric actor critic、locomotion gait prior、Deep WBC式球坐标和 joint PD

**实验能支持什么。** 200000 pose targets，包括结构不可达；Unified/Two-Stage/Cooperative/Full 3 seeds；真实 extreme poses 8次，跨高度每设置15次

**未覆盖条件与比较限制。** 站立与移动下workspace按精度/碰撞/时间定义；真实大部分teleoperation；target不是完整world fixed

**阅读范围。** 正文 §III–V 完整方法、训练和实验审读；无另附录；intro/related work未逐段登记全文精读

**原文定位。** §III-A/B; §IV-A–E; §V-A/B; Tables III–VI

**核读订正。** 两阶段主要改善survival；cooperation主要改善pose error；“0.87 m³”是performance workspace，不是理论几何容量

<a id="2407-10353"></a>
## 2407.10353 UMI on Legs: Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers

[UMI on Legs](../literature-map.html#paper=2407.10353) · [PDF](../papers/2407.10353_UMI_on_Legs_Making_Manipulation_Policies_Mobile_with_Manipulation-Centric_Whole-body_Controllers.pdf) · [原文](https://arxiv.org/abs/2407.10353)

**原问题与接口。** 用真机器狗收集示范贵且危险；固定臂上学到的操作动作也难直接用于会移动的身体。 输入：上层看腕部图像；下层看身体和关节状态，以及上层预测的一小段未来末端轨迹。 输出：上层输出夹爪未来的位置、朝向和开合；下层输出腿和臂的关节角度目标。

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；[K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)

**来源与版本。** 首次预印本：2024-07-14

**方法。** 人拿手持夹爪收集示范，训练图像到轨迹的策略；另外在仿真中只练习全身跟踪轨迹。轨迹在不随身体晃动的任务坐标中表达，下层提前看到后续动作。

**实验设置。** 真机杯子重排、推壶铃和投球，每种主要条件 20 次；投球从人工放入球的预抓取状态开始。仿真分别移除预览、任务坐标和真实操作轨迹；文中 Deep WBC 风格基线由同时移除这三个组件构造。原固定臂的杯子操作策略直接部署到四足上。

**阅读定位：核心主线。** 将高层操作与机器人本体动作解耦，用带未来预览的末端轨迹连接示范和全身控制。CMP实际沿用数据／训练设置并研究能力边界；Tactile-aware沿用部分低层设置。这是可以更换高层任务而继续使用的接口。

**主线判断的证据范围。** CMP正文训练／基线设置；Tactile-aware低层训练节。原始UMI采集和diffusion policy是外部前作，不是UMI on Legs首次发明。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)：任务坐标轨迹
- [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)：轨迹接口
- [K44 示范监督与闭环数据分布](../knowledge/network.md#k44)：示范动作分布与任务轨迹
- [K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)：未来轨迹条件
- [K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)：位姿延迟与定时限制
- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：动作块衔接
- [K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)：四足轨迹驱动全身 RL
- ：轨迹执行条件

**平台与执行。** Unitree Go2 + ARX5; iPhone ARKit or OptiTrack; RL onboard 50 Hz, DP offboard RTX4090

**相对已有方法的具体改动。** 固定任务frame末端轨迹和preview作为层间接口；UMI真实数据学任务DP、sim无需物体资产学WBC；异步频率实现

**复用部分。** UMI、Diffusion Policy/CLIP、PPO、DR、joint PD

**实验能支持什么。** 500 simulated tossing episodes；remove preview/frame/UMI trajectories；20 real trials/task；cup checkpoint zero-shot 85/80%; toss 75/70%; 10 lb push 95/90% OptiTrack/iPhone

**未覆盖条件与比较限制。** 投球从手工预抓球开始；操作policy zero-shot不等于WBC不训练；明确无人从sim force task训练；未collision/force feedback；140 ms odometry、抖动、URDF误差、overheat

**阅读范围。** 正文 §1–5 与完整附录 §7–10审读，cost misc浏览；未看视频和代码

**原文定位。** §3.1–3.3; §4.1–4.4; Table 1; Appendix §7–10

**核读订正。** DeepWBC 比較由同时去掉3个接口组件构造；task-frame真机测量依赖定位；无 force modeling 不代表已经精确 force control

<a id="2507-08656"></a>
## 2507.08656 Multi-critic Learning for Whole-body End-effector Twist Tracking

[Multi-critic Learning for Wh](../literature-map.html#paper=2507.08656) · [PDF](../papers/2507.08656_Multi-critic_Learning_for_Whole-body_End-effector_Twist_Tracking.pdf) · [原文](https://arxiv.org/abs/2507.08656)

**原问题与接口。** 只给一连串末端位置，不能直接要求移动速度；走路希望身体平稳，伸手又可能需要倾斜，两者训练目标冲突。 输入：身体运动命令、末端终点位姿和线速度／转动速度、抬脚高度，以及近期机器人状态。 输出：相对当前腿和臂关节角度的修正量，经截断后交给底层关节控制器执行。

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)

**来源与版本。** 首次预印本：2025-07-11

**方法。** 一个动作网络控制全身，走路、操作和脚接触时序各有价值估计网络；各组优势分别归一化后求和，用于更新同一策略。训练混合局部与全局参考轨迹，目标不是只在最后时刻到达终点。

**实验设置。** ANYmal D＋Dynaarm 真机跟踪多速度直线、圆和半圆，记录位置与速度误差；仿真比较不同腿部策略和全身控制器。站立比较中的 Portela [8] 是 2025 年末端姿态跟踪论文，与 2024 年力控制论文不是同一篇；部分对照复用本文臂动作再替换腿策略。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)：多回报评价
- [K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)：评价分解
- ：训练结构与执行结构之别

**平台与执行。** ANYmal D + Dynaarm; 50 Hz policy /400 Hz motion; joint increments relative current q

**相对已有方法的具体改动。** twist+final pose接口；local/global trajectory training；locomotion/manipulation/contact schedule 三critic，优势各自归一化后求和

**复用部分。** PPO、teacher-student、DR、joint PD、gait phase

**实验能支持什么。** 真机直线/圆/半圆多速度误差；sim替换不同leg controller、pose controller、MPC；扩展trajectory velocity errors

**未覆盖条件与比较限制。** 主要末端运动而非精细接触力；某些baseline混合本文arm action和其他leg action；难完全归因critic

**阅读范围。** 正文 §3、§4实验与结论审读；附录 §7.1 observation/reward/train 及相关训练细节审读；未逐项复算全部扩展表

**原文定位。** §3.1–3.3; §4; Tables1–3; Appendix §7.1

**核读订正。** §4 stationary Portela [8] 是2025 Whole-body end-effector pose tracking，不是2024 Learning Force Control（[11]）；应按题名/引用号区分同一作者的不同方法。部分比较复用本文 arm control 并替换 leg controller，不代表完整原系统直接比较。

<a id="2508-10538"></a>
## 2508.10538 MLM: Learning Multi-task Loco-Manipulation Whole-Body Control for Quadruped Robot with Arm

[MLM](../literature-map.html#paper=2508.10538) · [PDF](../papers/2508.10538_MLM_Learning_Multi-task_Loco-Manipulation_Whole-Body_Control_for_Quadruped_Robot_with_Arm.pdf) · [原文](https://arxiv.org/abs/2508.10538)

**原问题与接口。** 控制器在某类轨迹上练得好，换空间范围不同的操作就变差；遥控时也拿不到未来轨迹。 输入：身体和臂的近期状态、上一动作、末端轨迹历史；自动操作时也可以直接输入未来轨迹。 输出：十二个腿关节和六个臂关节的角度修正量。

**对应／相邻机制。** [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)

**来源与版本。** 首次预印本：2025-08-14

**方法。** 建立真实轨迹库，按各任务的学习情况调整抽样难度；用轨迹历史预测未来目标，用自身状态历史估计身体速度，再训练全身跟踪。

**实验设置。** Go2＋AIRBOT 真机演示遥控和图像扩散策略驱动的操作；轨迹抽样、预测网络及误差比较主要在仿真中完成。文中的 DeepWBC 式基线同时移除了未来轨迹预测、轨迹输入和任务坐标系，差异不能只归于网络结构。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)：轨迹供给条件

**平台与执行。** Unitree Go2 + Airbot Play; Livox Mid360 odometry; onboard RL50 Hz/offboard teleop or DP

**相对已有方法的具体改动。** task轨迹库、adaptive sampling/precision curriculum；past trajectory→future prediction NAE；proprioceptive history→velocity estimation

**复用部分。** PPO、AMP locomotion prior、DP/CLIP、DR、joint PD

**实验能支持什么。** TVP/noNAE/sMLP/多接口移除DeepWBC；sim torque MSD、7轨迹误差、uniform sampling；real teleop/DP

**未覆盖条件与比较限制。** 仿真核心是重放任务轨迹；七条轨迹不等于七任务自主语义；轨迹预测对突然改变上游存在假设

**阅读范围。** 正文 §III–V 方法与结果审读；表格误差及架构核查；无完整参考文献推导审读

**原文定位。** §III-A–C; §IV-B/C; TablesIII–V

**核读订正。** DeepWBC baseline由该架构删目标frame/preview/NAE构造；低层multi-task是轨迹tracking，不是直接7任务RL策略

<a id="2405-01402"></a>
## 2405.01402 Learning Force Control for Legged Manipulation

[Force Control](../literature-map.html#paper=2405.01402) · [PDF](../papers/2405.01402_Learning_Force_Control_for_Legged_Manipulation.pdf) · [原文](https://arxiv.org/abs/2405.01402)

**原问题与接口。** 强化学习机器人能推东西，但通常只是碰巧用了足够的力，不能明确要求“保持某个力”。 输入：近期身体和关节状态、动作历史，以及期望移动／末端目标或施力命令；不输入实测腕部力。 输出：腿和臂的关节角度目标；同时估计夹爪外力等状态供控制使用。

**对应／相邻机制。** [K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)；[K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)；[K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)

**来源与版本。** 首次预印本：2024-05-02

**方法。** 仿真中用虚拟弹簧／阻尼产生接触力，以真实仿真力计算力跟踪奖励，并监督从自身状态历史估计外力的网络。位置和力模式交替训练；部署时用位置误差与速度反馈生成力命令，实现可调柔顺交互。

**实验设置。** B1＋Z1 真机在五个末端位置测量施力，误差约 5–10 N；展示柔顺示教、拉物体及移动中操作。控制器明确接收身体速度命令，包含行走能力，并非仅固定底盘的力控制。

**阅读定位：重要对照。** 较早的四足RL力目标控制，适合建立接触操作对照；力控制这一大类并非本文首创，当前库中的直接模块复用证据不足。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)：力目标控制
- [K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)：力策略外层位置反馈
- ：力跟踪与精度边界
- ：位置／力精度边界

**平台与执行。** Unitree B1 + Z1; first5 arm joint position targets +12legs; direct control last arm roll/gripper

**相对已有方法的具体改动。** 位置/力mode alternation；virtual spring contact/force reward；history estimator；forcepolicy外包位置误差反馈构成impedance

**复用部分。** DeepWBC目标定义、PPO/PD/DR、concurrent state estimation

**实验能支持什么。** 1000 simulated force setpoints；force0–70N、5workspace positions真机dynamometer；force约5–10N误差；pull90N；position4–7cm

**未覆盖条件与比较限制。** force和position二选一，不能同轴独立同时跟踪；低频policy及模糊force估计；大量interaction teleoperation

**阅读范围。** 正文 §II–VI（核心§IV/V逐段）审读；无另附录；力与位置定量表和discussion核查

**原文定位。** §IV-A–E; §V-A–D; §VI; TablesI/Figs3–5

**核读订正。** 无 force-torque sensor 作为控制输入，但真机评估有 dynamometer；有walking/locomotion command；不能说这篇仅固定底盘/没有locomotion

<a id="2505-20829"></a>
## 2505.20829 Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation

[Position + Force RL](../literature-map.html#paper=2505.20829) · [PDF](../papers/2505.20829_Learning_a_Unified_Policy_for_Position_and_Force_Control_in_Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2505.20829)

**原问题与接口。** 接触操作不能只追位置，或只追力；操作策略也需要知道是否已经碰上、推紧或受阻。 输入：身体和关节历史、动作、步态时序，以及身体速度、末端位置、末端／身体力命令；不依赖实测腕部力。 输出：全身关节角度目标，以及外力、末端位置和身体速度的估计。另一个模仿学习模块使用估计力生成操作动作。

**对应／相邻机制。** [K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)；[K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)；[K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)；[K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)

**来源与版本。** 首次预印本：2025-05-27

**方法。** 仿真中同时改变位置、力命令和外部扰动，依据准静态阻抗关系将净力转成目标位移补偿，再奖励控制器跟踪补偿后的目标。示教时记录估计力，把它与视觉／运动信息一起用于后续操作学习。

**实验设置。** B2＋Z1 上擦白板、开／关按压式柜门和遮挡下拉抽屉四任务，每个设置 50 次，比较带力信息的操作学习与位置基线。G1 人形实验只验证身体力交互和移动，不包含这四个臂操作任务。

**阅读定位：重要对照。** 同一策略兼顾位置、力和柔顺行为，跨四足／人形实验，是力控制分支的重要方法对照；触觉后作讨论它不等于采用其统一公式／训练方案。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)：统一位置／力目标
- [K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)：准静态补偿位置
- ：同名目标的不同监督

**平台与执行。** Unitree B2 + Z1 for manipulation; Unitree G1 for base force/locomotion only

**相对已有方法的具体改动。** 准静态impedance由位置/力/外力生成xtarget与basevelocity target；学习unifiedpolicy；estimatedforce加入DP数据/输入/输出

**复用部分。** PPO、history estimator、DP、PD、两阶段训练

**实验能支持什么。** 五点force测量5–10N级；四真实tasks每50 trials；wipe/push-to-open 3mm cabinet/drawer occlusion；G1baseforce行为

**未覆盖条件与比较限制。** 假设末端slow/quasi-static，去掉M,D；rough force误差；human forcing/teleop；position约0.1m

**阅读范围。** 正文 §3–4完整核心与discussion审读；附录 A 完整公式、C训练、D任务、E估计部分审读

**原文定位。** §3.1–3.3; §4.1–4.4; Appendix A/C/D/E

**核读订正。** 约39.5% improvement对应force-aware整个pipeline；baseline同时去force observation和force command，非独立force estimator消融；G1不是手臂接触任务证据

<a id="2604-27224"></a>
## 2604.27224 Learning Tactile-Aware Quadrupedal Loco-Manipulation Policies

[Learning Tactile-Aware Quadr](../literature-map.html#paper=2604.27224) · [PDF](../papers/2604.27224_Learning_Tactile-Aware_Quadrupedal_Loco-Manipulation_Policies.pdf) · [原文](https://arxiv.org/abs/2604.27224)

**原问题与接口。** 视觉看不清夹持是否稳定、是否已经插入或夹得过紧；只复制夹爪路径容易损伤或操作失败。 输入：上层看图像、夹爪姿态／开口和触觉历史；下层看机器人状态、触觉反馈以及期望运动与触觉目标。 输出：上层预测末端轨迹、夹爪开口和接触面积／方向／质心目标。第一阶段臂跟踪采用逆运动学；部署的低层策略输出腿和臂关节目标，分别降采样到 50 Hz 和 10 Hz 执行。

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)；[K39 触觉、握力与接触释放](../knowledge/network.md#k39)

**来源与版本。** 首次预印本：2026-04-29

**方法。** 用带触觉的手持夹爪收集示范，训练上层同时预测运动和接触变化；下层先练稳定行走，再在接触任务仿真中练配合这些目标。

**实验设置。** 真机物体重定向与插入、拧紧阀门、轻柔抓取，每个任务设置 20 次。对照分别增加触觉观测、触觉预测和低层触觉跟踪；薯片任务的三个触觉版本均 100% 成功，不能据它单独证明低层触觉目标必要。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K39 触觉、握力与接触释放](../knowledge/network.md#k39)：触觉目标与执行范围

**平台与执行。** Unitree Go2 + D1 position-command arm + FlexiTac arrays; offboard RTX4070Ti

**相对已有方法的具体改动。** DP条件化接触面积/方向/centroid并预测这些触觉目标；lowlevel在task-specific contact scene学目标tracking

**复用部分。** UMI、DP/CLIP、PPO/DR、关节servo控制

**实验能支持什么。** 每task20rollouts；P1vision/P2tactileobs/P3tactileprediction但低层不用/P4 lowlevel tracking；insertion70→85%、whole60→80%；valve80→85%；chip100% tactile variants

**未覆盖条件与比较限制。** 精细contact阶段base forward/lateral velocity设0，约束base稳；多数position chart arm-base frame不含tilt；fruit bruising没有仪器只定性

**阅读范围。** 正文 §III/IV/V方法与结果审读；TableIII/IV reward、V/VI ablation核查；未运行 tactile simulator

**原文定位。** §III-A/B; §IV-A/B; §V; TablesIII–VI

**核读订正。** 不能写已保证持续跨步精细接触安全；chip任务不区分P2/P3/P4；28.54% summary并非每个新增模块独立收益

<a id="2607-10132"></a>
## 2607.10132 TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation

[TAC-LOCO](../literature-map.html#paper=2607.10132) · [PDF](../papers/2607.10132_TAC-LOCO_Unified_Whole-Body_Control_for_Quadrupedal_TACtile-Informed_LOCO-Manipulation.pdf) · [原文](https://arxiv.org/abs/2607.10132)

**原问题与接口。** 手里物体被外力拉扯时，一直夹得很紧会损伤物体；夹得太松又会滑落。外部负载突然消失也会扰乱身体。 输入：身体和关节状态、动作历史、身体速度和末端轨迹命令，以及两指触觉阵列测量。 输出：同一个策略输出腿、臂和夹爪的关节角度目标，在线调整夹持程度。

**对应／相邻机制。** [K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)；[K39 触觉、握力与接触释放](../knowledge/network.md#k39)

**来源与版本。** 首次预印本：2026-07-11

**方法。** 把各触觉点压缩成少量接触特征；仿真中随机改变物体负载，包含突然释放，奖励稳定抓持和不过度用力。

**实验设置。** Go2＋WidowX 和触觉夹爪，真机用弹簧与磁铁制造负载变化／突然释放，动态移动操作成功 9/10 次。约 47% 的夹持力降低来自仿真奖励消融；低于 1% 的掉落率也来自大规模仿真，不能当成真机统计。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K39 触觉、握力与接触释放](../knowledge/network.md#k39)：握力与突然释放
- ：抓取与峰值力

**平台与执行。** Unitree Go2 + Interbotix WidowX250 + FlexiTac TPU fingers; offboard50Hz

**相对已有方法的具体改动。** 两指tactile latent联合腿臂gripper；load ramp/suddenrelease；graspforce/slip/retention reward

**复用部分。** DeepWBC advantage mixing/ROA、PPO、TacSL/DR、PD

**实验能支持什么。** 8000 simrollouts99.9%retain vs46.4%; rewardforce13.11vs24.76N；真实spring/magnets两setting各10、walking9/10、baseline5/10

**未覆盖条件与比较限制。** 已建立抓取，非navigation/reach/grasp；归一化tactile不能保证绝对graspforce threshold；servoarm限制动态范围

**阅读范围。** 正文 §3–7审读；附录 B/C reward/obs/hardware与tactile sim normalization读；未复算全部hyperparam

**原文定位。** §3; §4.1–4.3; §5.1–5.4; §6.1–6.5; §7; AppendixB/C

**核读订正。** 47%force reduction来自sim rewardablation，不是全面真机损伤测量；hardware baseline同时固定gripper、无tactile、不同interactiontraining，不能单独归因sensor

<a id="2609-03889"></a>
## 2609.03889 FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation（轮足邻接）

[FWBC-VLA](../literature-map.html#paper=2609.03889) · [PDF](../papers/2609.03889_FWBC-VLA_Force-Aware_Whole-Body_Compensation_for_Contact-Rich_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2609.03889)

**原问题与接口。** 视觉语言动作模型不易知道手是否受阻；底层稳住身体，也未必知道该抵消什么接触影响。 M20S 轮足＋CM1 臂。输入图像、语言、本体状态及 200 Hz 实测臂关节力矩；π0.5 动作专家生成操作／基座指令，较快的小型残差网络另修正基座速度。无腕部力传感器仍需要实际关节力矩测量。

**对应／相邻机制。** [K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)

**来源与版本。** 首次预印本：2026-09-03

**方法。** 两个自由运动力矩预测器分别使用历史和当前状态；历史较低噪但可能吸收持续接触，状态分支较保留负载变化，由 gate 混合残差。六关节残差的强度／变化编码成 force tokens 输入动作专家；残差经阻尼 Jacobian 逆和力臂变换形成机身负载线索，供限幅／低通的速度补偿。

**实验设置。** 超过 5,000 段示范；真机擦白板、开带闭门器的门各 25 次，最终 64%／52%，F/T 对照 60%／48%，各只差一次成功。已知 0.36／0.72 kg 负载主要验证重力大小，不能代替任意六维接触力标定。

**阅读定位：新路线代表。** 轮足四足接触VLA的相关新接口：力代理进入动作模型与身体补偿；新预印本，尚无已核实的下游采用。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)：接触代理
- [K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)：VLA 条件与独立反馈
- ：信号与补偿分界

**平台与执行。** M20S 轮足底盘＋CM1 六自由度臂；需实测关节力矩，轮足邻接

**相对已有方法的具体改动。** 用历史/当前状态两预测器估自由运动力矩，以gate减少历史吸收持续接触的问题；六维关节残差短历史作为force tokens条件化π0.5 action expert，另由较快小型MLP根据估计负载与姿态修正基座速度。

**复用部分。** π0.5 action expert 为直接复用VLA基础；残差观测、阻尼Jacobian逆、wrench坐标变换和低通/限幅控制是基础组件；未给被动性/耦合稳定性证明

**实验能支持什么。** 力矩200 Hz，policy示范15 Hz，>5000 episodes；teleop force intent仅作元数据，不作为部署输入；0.36/0.72kg已知payload主要验证标量重力负载，不等于任意六维接触wrench标定；wiping64%、doorcloser52%，每任务25次；F/T对照60%/48%各仅差一个成功；消融force接口与body补偿均有收益，但 Table 3 与正文的35/65%及59.5%等数值不一致；具体引用须按表位置注明；残差经杠杆臂变换到机身原点并对base velocity做bounded residual，而不是直接joint torque residual

**未覆盖条件与比较限制。** 无腕传感器但有实际关节力矩测量；没有该接口的廉价伺服臂不可直接复用；残差含摩擦/模型误差，force tokens是load proxy而非精确标定外力；轮足执行与步行换步不同；峰值力与稳定性结论仍受接口/延迟限制

**阅读范围。** 本地 PDF 标题核对；主文完整，包括HSR、force tokens、机身残差补偿、数据、F/T对照和消融。未执行实现；正文内部数字冲突保留并说明。

**原文定位。** HSR 两自由运动力矩预测器与gate；force-token late cross-attention；arm residual→EE wrench→body-origin wrench 与速度补偿；§5结果表及F/T对照；已知payload实验

**核读订正。** 不能将sensorless解释成不需要任何力相关测量；cross-attention不是Bayesian力融合，残差范数不是calibrated6Dwrench；64/52对60/48不能证明估计比F/T更准确；论文正文/表数值有内部冲突，应避免挑较好数字合成新结果

<a id="2609-13779"></a>
## 2609.13779 Force-Aware Reinforcement Learning with Hybrid Sensorless Force Estimation for Wheeled-Legged Loco-Manipulation（轮足邻接）

[Force-Aware Reinforcement Le](../literature-map.html#paper=2609.13779) · [PDF](../papers/2609.13779_Force-Aware_Reinforcement_Learning_with_Hybrid_Sensorless_Force_Estimation_for_Wheeled-Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2609.13779)

**原问题与接口。** 机器人运动造成的力矩变化里，混有地面支撑、手部接触和模型误差，直接把它当手部外力会控制错。 输入：关节和身体状态、关节力矩命令、模型及支撑接触条件；控制器还接收位置／力目标和每个方向的控制选择。 输出：估计末端作用力；策略输出腿和臂的关节角度、轮子速度。

**对应／相邻机制。** [K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)；[K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)

**来源与版本。** 首次预印本：2026-09-12

**方法。** 先用动力学估计总扰动，再利用支撑接触约束分出末端力，网络纠正剩余时变误差；学习策略按方向选择跟踪位置或力。

**实验设置。** 仿真在相同轨迹上比较无约束分解、接触约束分解、单独时序网络与组合估计器，并比较箱子拖动的力误差和实际位移。轮足真机转阀门、擦拭使用仅用于评价的 F/T 传感器作定量参照，开门和人拖动引导提供整套系统的行为验证。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)：估计方法

**平台与执行。** Wheeled-legged platform +6DoF arm;22D leg/arm position + wheel velocity; policy50Hz/observerQP500Hz

**相对已有方法的具体改动。** momentum observer总扰动→contactfeasibleQP wrenchallocation→TCN residual；axiswise position/force selector与force-observedRL

**复用部分。** GMO、QP、TCN、PPO、多critic、virtual spring力训练

**实验能支持什么。** PI/CQP/TCN/hybrid same rollout10trials eachinertiasetting；matched/unmatchedmass含train；drag10trials；realvalve和wipe定量F/T reference、door/guidance系统演示

**未覆盖条件与比较限制。** 估计λcontact和we空间可能重叠；torque command≠true delivered torque；wheeled support/rollingresidual assumptions；hardware全系统验证不隔离每个组件

**阅读范围。** 正文 §II/III/IV方法、仿真、硬件全文核心审读；§I摘要背景与§V结论核查；无另附录

**原文定位。** §II-A–E; §III-A–D; §IV-A–D; TablesI/II

**核读订正。** sensorless指FT不作policyinput，评估装有FT；±20%inertiamismatch在train pooleddataset，不能说unseen OODmass泛化；控制比较还改变训练objective和估计器，别全归TCN

<a id="2403-16967"></a>
## 2403.16967 Visual Whole-Body Control for Legged Loco-Manipulation

[Visual WBC](../literature-map.html#paper=2403.16967) · [PDF](../papers/2403.16967_Visual_Whole-Body_Control_for_Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2403.16967)

**原问题与接口。** 给定末端目标的控制器不会自己找物体，也不会决定应该走近还是倾斜身体来抓取。 输入：上层看分割后的深度图和自身状态；下层接收身体速度、末端姿态目标及机器人状态。 输出：上层给身体速度和末端目标；下层学习策略输出腿关节角度，臂关节角度由几何求解得到。

**对应／相邻机制。** [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)；；[K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)

**来源与版本。** 首次预印本：2024-03-25

**方法。** 先用物体形状／姿态教师训练抓取，再通过 DAgger 把双分割深度学生带到其实际访问状态纠正。腿部策略看臂状态和末端目标，臂用 Jacobian 逆运动学；目标参考系随身体水平位置和 yaw 变化，但固定高度及 roll/pitch，使身体升降能扩展可操作空间。

**实验设置。** 真机 14 个物体×3 高度×5 次重置，每轮允许连续五次尝试，因此不是 one-shot 成功率。附录 E 行走位置误差 0.029 m 对 Deep WBC 0.414 m 来自仿真，不是真机接触精度。

**阅读定位：核心主线。** 后作明确把其低层控制、奖励或实现作为基础：Interactive Navigation、DQ-Net、Deployment Framework。三者分别研究推物导航、动态对象抓取和部署，说明执行器能跨任务复用。

**主线判断的证据范围。** Interactive Navigation §III-B.6；DQ-Net正文和Appendix B；Deployment Framework §3.1。腿RL＋臂IK本身并非本文首次提出。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：视觉策略蒸馏
- [K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)：视觉目标接口
- [K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)：分割深度瓶颈

**平台与执行。** Unitree B1＋Z1，四足＋机械臂

**相对已有方法的具体改动。** 上层先用物体形状/姿态训练 9 维抓取策略，再通过 DAgger 蒸馏为双视角分割深度策略；低层腿 RL 接收臂状态与末端目标，臂以 Jacobian IK 执行 SE(3) 指令。固定高度/roll/pitch、随水平位置/yaw 变化的目标系使身体姿态能够扩展臂可用空间。

**复用部分。** 明确以既有全身 RL 及 teacher–student 范式为基础；PPO、PointNet、IK、DAgger 和 TrackingSAM 各承担独立职责；下游 WildLMa 明确复用本工作低层；其 ACT 与任务规划不是本篇贡献

**实验能支持什么。** 附录 E 仿真 standing/walking 位置误差分别为 0.047/0.029 m，对 Deep WBC 对照 0.236/0.414 m；支持该低层参数化与配方的目标跟踪收益，非真机接触精度测量；真机 14 个对象×3 高度×5 resets；每轮允许连续五次尝试，指标不是单次动作 one-shot 成功率；不分层的文内配置成功为零，支持该配置训练困难，不证明所有端到端系统不可能；视觉 6–8 Hz、腿 50 Hz、臂 IK 800 Hz；任务低/高频分工在部署中实际存在

**未覆盖条件与比较限制。** 每次真机试验开始人工点击目标，至少一个相机需要看见目标；分割深度去掉很多颜色语义；训练约束夹爪闭合时基座速度为零；没有证明持续接触中换步的安全；固定高度/yaw 参考系不是完整世界锁定的接触目标；低层跟踪不提供接触力上界

**阅读范围。** 本地 PDF 标题核对；完整主文的问题、方法、实验、讨论已读。附录 C–J 中训练接口、跟踪、对象实验和消融已核对；长附录的个别参数段未逐项覆盖。未运行代码或观看补充视频。

**原文定位。** 主文 §3.1–3.3，p.3–5；主文 §4，p.6–8；附录 C 的任务与观测接口；附录 E，Table 4 的低层跟踪比较；附录 G/I 的真机与泛化协议

**核读订正。** 不能写成 RL 直接输出所有腿臂关节：腿输出关节目标，臂由 IK；不能把 0.029 m 写成真机结果，也不能将该任务系描述为完整 world frame；目标不依赖颜色的泛化不等于颜色/语义按钮选择已解决；重试不是显式已成功事件记忆

<a id="2411-06782"></a>
## 2411.06782 QuadWBG: Generalizable Quadrupedal Whole-Body Grasping

[QuadWBG](../literature-map.html#paper=2411.06782) · [PDF](../papers/2411.06782_QuadWBG_Generalizable_Quadrupedal_Whole-Body_Grasping.pdf) · [原文](https://arxiv.org/abs/2411.06782)

**原问题与接口。** 相机看到了物体，也算出了抓取点，但机器人当前站位可能够不到或朝向不合适。 输入：相机得到的候选抓取姿态、自身状态，以及预计算的可达信息；低层接收身体平面速度、高度和俯仰命令。 输出：上层选择身体移动／姿态命令，臂执行抓取姿态；行走策略输出腿部关节动作。

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)；[K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)；[K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)

**来源与版本。** 首次预印本：2024-11-11

**方法。** 离线计算不同臂目标下哪些身体站位可达、哪些更好；训练上层朝较好的站位移动，再用现有抓取求解和底层策略执行。

**实验设置。** 真机透明等多类物体抓取，作者报告一次抓取准确率 89%；比较可达信息有无带来的差别。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)：站位可达图
- [K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)：几何站位筛选
- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：latent 与动作联合蒸馏
- [K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)：检测＋站位＋规划
- [K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)：从感知到可抓取目标
- [K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)：可达站位
- ：系统与 GORM 消融

**平台与执行。** Go1＋外挂机械臂；四足＋臂

**相对已有方法的具体改动。** 把目标条件化的视觉策略、抓取检测和广义可达图 GORM 组合：站位筛选考虑臂与身体姿态，低层执行抓取轨迹；教师动作与潜变量同时蒸馏到学生。

**复用部分。** 特权教师／视觉学生、现成抓取检测、PPO、逆运动学和轨迹规划。

**实验能支持什么。** 仿真与真机抓取、身体位姿补偿；GORM／站位处理的消融；整系统与视觉基线比较。

**未覆盖条件与比较限制。** 系统比较还包含感知和执行差异。到达可抓取站位，不等于全段柜门接触轨迹可行；不提供持续换步时的接触力安全证明。

**阅读范围。** 正文问题、方法、实验、讨论完整审读；回查参考文献；未观看补充视频

**原文定位。** §III-A–D；§IV；结论与参考文献

<a id="2411-15131"></a>
## 2411.15131 WildLMa: Long Horizon Loco-Manipulation in the Wild

[WildLMa](../literature-map.html#paper=2411.15131) · [PDF](../papers/2411.15131_WildLMa_Long_Horizon_Loco-Manipulation_in_the_Wild.pdf) · [原文](https://arxiv.org/abs/2411.15131)

**原问题与接口。** 单次抓取不能解决清理走廊、操作柜子再摆放物品等多步骤任务，也难覆盖真实环境变化。 输入：语言任务、头部／腕部图像、机器人状态；训练时由人用 VR 遥控机器狗收集全身示范。 输出：任务规划器输出技能顺序；各技能策略产生末端等控制目标，下层生成身体和臂的关节命令。

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)；[K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)

**来源与版本。** 首次预印本：2024-11-22

**方法。** 明确复用 VBC 全身低层收集 VR 示范，每技能单独训练 ACT；加入 CLIP 文本／像素余弦相关图提供目标定位。演示末尾监督技能终止，部署连续十次终止预测超过 0.8 后结束；LLM 通过人工导航 waypoint／连通关系调用技能。

**实验设置。** 技能均值 71.2%，ACT 40.8%，OpenTV 64.4%；垃圾长任务 7/10、货架 3/10。开门双相机 70% 对头／腕单视角 30%／10%，按钮单腕 85% 略高于双相机 80%，视角收益依任务而定。

**阅读定位：重要对照。** 有真机长程任务，技能库＋语言规划提供完整系统参照；系统广度与学术质量值得读，但尚未核实多支后作沿用其技能接口／cross-attention模块。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)：长程技能组合
- [K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)：CLIP目标相关图
- [K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)：任务相关视角互补
- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：语言规划

**平台与执行。** Unitree B1＋Z1，四足＋机械臂

**相对已有方法的具体改动。** 明确复用 VBC 全身控制以简化 VR 示范采集；用 CLIP 像素特征与任务文本的余弦相关图给独立 ACT 技能提供目标位置，再由 LLM、人工 waypoint 导航和学习终止信号组合长任务。

**复用部分。** VBC 是直接复用的低层执行器；ACT、CLIP/MaskCLIP、LiDAR FAST-LIO/DLO 和语言模型分别来自已有模块；每个技能有独立 ACT 权重

**实验能支持什么。** 技能均值 71.2%，对 ACT 40.8%、OpenTV 64.4%；系统与表征存在多项差异，不能只归因 LLM；开门 head+wrist 70%，head 30%，wrist 10%；按钮 wrist 85%，双相机 80%，支持视角选择与任务有关；普通 DinoV2 83.3% 高于普通 CLIP 76.4%，相关图 CLIP 84.7%；不支持 CLIP 天生优于其他视觉编码；长任务垃圾收集 7/10、货架 3/10，direct ACT 为零；技能分解、终止和系统结构同时变化；四名操作员遥操作地面抓取 21.87 s 对 37.35 s，支持 WBC 在数据采集中的协调收益

**未覆盖条件与比较限制。** 导航 waypoint 与连通关系由人提供；不是从任意场景完全自主建立动作地图；终止标签为演示最后十帧，部署连续十个预测超过 0.8 才终止；不等于物理成功传感验证；30–60 条示范/技能，独立权重，跨技能扩展仍需采集与训练

**阅读范围。** 本地 PDF 标题核对；主文完整，包括数据采集、策略表示、任务/导航系统、全部结果及讨论。未核查项目代码与视频。

**原文定位。** §III，p.3–4：遥操作、特征与 ACT；§IV，p.5–6：技能、多相机和长任务实验；导航/LLM 规划与 skill termination 描述

**核读订正。** LLM 选择技能不等于连续动作 VLA；文中所谓 cross-attention 相关图实质为文本/像素余弦相关定位，不能当 Bayesian confidence 融合；不能把所有多相机改善概括成相机越多越好，或把 termination 描述成按钮成功事件确认

<a id="2501-09905"></a>
## 2501.09905 SLIM: Sim-to-Real Legged Instructive Manipulation via Long-Horizon Visuomotor Learning

[SLIM](../literature-map.html#paper=2501.09905) · [PDF](../papers/2501.09905_SLIM_Sim-to-Real_Legged_Instructive_Manipulation_via_Long-Horizon_Visuomotor_Learning.pdf) · [原文](https://arxiv.org/abs/2501.09905)

**原问题与接口。** 真机示教长任务费时；直接从相机图像练习长任务，学习很难找到成功动作。 输入：部署时输入腕部 RGB 图像、任务指令和关节等自身状态；仿真老师额外知道物体位置和当前子任务。 输出：高层输出臂／夹爪动作及身体速度；固定的低层行走策略输出腿关节动作。

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)；[K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)；[K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)

**来源与版本。** 首次预印本：2025-01-17

**方法。** 分阶段 SAC 教师解决长任务探索，教师物体信息限制在相机视场内；学生不观察阶段真值，以蒸馏＋RL 学单一策略。学生由 RGB／语言预测任务相关 mask/depth 作视觉瓶颈，部署无需深度输入；另学 stationary bit 在抓取／放置时强制基座速度为零。

**实验设置。** Go1＋WidowX＋单腕 RGB，相机观察颜色方块／篮子。360 次主比较＋40 次新场景，完整 78.3% ±5.8%，仅蒸馏 50% ±35.5%；低层十个种子中选最稳定三个实机部署。仿真为 MuJoCo，学生训练约四 GPU 两周。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K44 示范监督与闭环数据分布](../knowledge/network.md#k44)：教师、学生与闭环RL
- [K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)：RGB预测任务表征
- [K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)：视野与停步阶段选择

**平台与执行。** Unitree Go1＋WidowX 250S，四足＋机械臂

**相对已有方法的具体改动。** 以分阶段教师解决长序列探索，再把部署时不可见阶段压进单个视觉学生；学生同时做蒸馏与 RL。RGB/语言/本体先预测任务相关 mask/depth，StopGrad 分隔视觉监督与策略损失；学生 stationary bit 在操作时精确停止基座移动。

**复用部分。** SAC、教师蒸馏、KL 模仿、分层行走控制与 U-Net 视觉瓶颈基于已有方法；低层本体不含臂状态/目标；实机为抑制晃动进一步去掉臂信息，并非末端感知的全身力控制

**实验能支持什么。** 真机主比较 360 episodes＝6 方法×3 seeds×20，另有 40 新场景，共 400；完整方法 78.3% ±5.8%，distillation-only 50% ±35.5%；完整方法完成时间 43.8 s，对人 65.5 s；适用于该颜色方块/篮子任务配置；教师仅在相机视场内提供目标信息，学生输入五帧腕相机 RGB 而非 depth sensor；作者从十个低层 seeds 中选择最稳定三个部署，因此三种子统计不能当无筛选策略重复性；低层 4B steps 约三日，学生四 GPU 两周、40M steps；方法有显著训练成本

**未覆盖条件与比较限制。** 彩色方块与篮子，并非通用开放词汇操纵；抓取/放置时基座速度强制为零，低层需零速度时不抬脚；回避而非解决持续接触中换步；关节 PID 追踪不是显式柔顺/接触力控制；视角与执行延迟条件重要

**阅读范围。** 本地 PDF 标题核对；主文方法、全部核心实验和局限已读；附录 A–J 的教师/学生、仿真、实机、消融和训练规模大部分已核对。少量附录超参数连续段未逐项读完。

**原文定位。** §III-B/C：分层接口与教师学生框架；§IV：渐进式教师训练；§V：学生蒸馏＋RL及预测mask/depth；§VIII-B/D/E：真机消融、结果与场景泛化；附录 B-A/B-B：教师视场限制、stationary bit和动作分布处理；附录 E：低层种子选择及实机配置；附录 C/D：训练规模与MuJoCo

**核读订正。** 仿真平台是 MuJoCo，不能写 Isaac Gym；部署使用 RGB 学出的 mask/depth，不需外部 SAM 点击或物理深度输入；不要把多阶段教师等同于部署显式阶段 FSM；学生不观察教师 stage index；不要把速度精确停零带来的稳定归为移动接触安全已解决

<a id="2508-08240"></a>
## 2508.08240 ODYSSEY: Open-World Quadrupeds Exploration and Manipulation for Long-Horizon Tasks

[ODYSSEY](../literature-map.html#paper=2508.08240) · [PDF](../papers/2508.08240_ODYSSEY_Open-World_Quadrupeds_Exploration_and_Manipulation_for_Long-Horizon_Tasks.pdf) · [原文](https://arxiv.org/abs/2508.08240)

**原问题与接口。** 长程指令需要先找目标、走到附近，再完成操作；仅看桌面图像的规划难处理移动中的视野和地形。 输入：语言、头部 RGB、激光雷达及地图、腕部深度图；低层接收身体速度、末端目标、地形高度和自身状态。 输出：全局规划输出子任务和导航目标；局部模块输出末端姿态；全身策略输出腿和臂关节角度。

**对应／相邻机制。** [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)

**来源与版本。** 首次预印本：2025-08-11

**方法。** GPT-4.1 以语义实例图拆原子任务，Qwen2.5-VL 以腕 RGB-D 生成接触点／姿态并加几何约束。Go2＋Arx5 统一策略输出 18 关节目标：先固定臂训练行走，再训练全身；末端采样高度在世界固定后转到机身坐标，加入地形高度图。

**实验设置。** 8 类长期任务 41.0%–69.8% 是仿真，304 种室内外变化；真机为两个任务、五对象定性展示。Table 3 主要改善基座速度，末端位置／姿态与 RoboDuet 大体相当；不能写末端精度显著领先。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** Unitree Go2＋Arx5，四足＋机械臂，RGB-D＋LiDAR

**相对已有方法的具体改动。** LiDAR/RGB instance graph 支持 GPT-4.1 拆解导航和操作，局部 Qwen2.5-VL 从腕 RGB-D 提出接触点和带几何约束的末端姿态；统一 18 关节 RL 以地形高度图和末端目标协调腿/臂。先静态臂训练行走，再全身训练，采样目标高度不随机身/地形倾斜而变。

**复用部分。** 语义图与对象匹配借鉴现有场景图方法，使用 RAM++、GroundedSAM、MaskCLIP 等模块；RoboDuet 为文中低层比较对象；共用两阶段思路不等于每项训练/网络均直接继承；ARNOLD 短任务定义/场景用于迁移评估，局部操作含预定义执行结构

**实验能支持什么。** 8 类长任务总体 41.0%–69.8%，均为仿真 benchmark；304 个长任务变化，室内246/室外58；Table 3 基座速度跟踪改善，但末端位置/姿态误差大体与 RoboDuet 相当；站立 x/y 指标也非逐项胜出；Table 1 seen pickup 60.45% 低于 PerAct 94.03%，novel pickup 45.24% 高于25.70%；不能泛称所有指标超越；真机仅 navigate-to-pick 与 pick-and-place 两种任务、五个对象定性展示，未提供大样本长期 task success table；Appendix C.1 固定 Observe/Plan→Pre-alignment→linear grasp→task-specific motion，以隔离高层规划方差

**未覆盖条件与比较限制。** 仿真总体成功率不能外推真机；末端对准和小物体抓取仍失败；局部 Qwen 生成姿态仍需几何约束、深度和任务运动规则；论文 Table 3 单位/缩放未清晰说明，不能未经核对将数字解释为米或厘米；地图中无碰撞 waypoint 不保证后续臂工作空间与接触路径可行

**阅读范围。** 本地 PDF 标题核对；主文完整，附录 A 感知/地图、B 训练、C 任务与 D 核心协议已读；prompt 图未独立逐字转录，图中无法解析的内容不作实现结论。

**原文定位。** §3.1：语义地图规划与接触点/姿态 grounding；§3.2：18 关节统一 RL 与两阶段训练；§4，Tables 1–4：仿真与实机区分；Appendix C.1：固定短技能序列；Appendix E/Figure 10：原子任务规划 prompt

**核读订正。** 不是以末端显著更精准为主要定量增量：控制收益主要在基座跟踪；不能把8类41%–70%写为真机结果；'no scripted policies' 泛称与 Appendix C.1 固定执行序列不一致，应按具体阶段描述；统一网络输出 18 个关节目标是真实接口，不能混成仅腿 RL＋臂 IK

<a id="2605-03846"></a>
## 2605.03846 SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision

[SigLoMa](../literature-map.html#paper=2605.03846) · [PDF](../papers/2605.03846_SigLoMa_Learning_Open-World_Quadrupedal_Loco-Manipulation_from_Ego-Centric_Vision.pdf) · [原文](https://arxiv.org/abs/2605.03846)

**原问题与接口。** 相机识别物体慢且会丢失目标，身体却一直在动；直接使用旧位置，容易走错站位或抓空。 Go2 身体直接固定低成本夹爪，没有机械臂。上游 VLM 提供语义 pick/place 锚点；策略以目标几何、本体与历史输入，输出前后／侧向速度、yaw 和 body pitch，通过整个身体对准夹爪。

**对应／相邻机制。** [K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)；[K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)；[K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)

**来源与版本。** 首次预印本：2026-05-05

**方法。** 加权 PCA 中心＋三轴正负端点共七点表示目标；各点的 Kalman filter 结合视觉里程计更新 ego-motion，遮挡历史训练模拟视野外漂移。这里的 sigma points 是几何点，不是 UKF 的统计传播点。

**实验设置。** 真机三类 pick/place 各十次，检测约 5 Hz／200 ms；比较 KF、遮挡噪声训练和人工。仿真成功判据主要是身体到理想对准姿态并停下，与物理夹取需区分。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)：固定夹爪的稀疏几何预测
- [K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)：稀疏几何

**平台与执行。** Unitree Go2 身体直接安装低成本夹爪，没有机械臂；四足无臂相邻机制

**相对已有方法的具体改动。** 把目标点云压成加权 PCA 中心＋三轴正负端点七个点，用 ego-motion Kalman filter 保持短期目标；上游 VLM 选择 pick/place 语义锚点，RL 以基座平移/yaw/body pitch 对准身体夹爪，遮挡噪声训练模拟脱离视野后的估计漂移。

**复用部分。** VLM 提供语义而非直接输出低层动作；Cutie 跟踪、视觉里程计、常速度 Kalman filtering 为已有组件；七点 PCA 是几何压缩，与 UKF 的 unscented transform sigma points 无直接等同关系

**实验能支持什么。** 真机三类 pick/place、每类十次，比较 NoKF、NoBSnoise 与人工；图中每个数未逐项复算；仿真主要成功定义为到达理想姿态并停下，非物理抓取成功；真机另做实际夹取；控制50 Hz、VO60 Hz、目标跟踪约5 Hz/200 ms，上游 Qwen API 使用离板算力；附录 A 先遥控扫描记录目标全局坐标，再转朝目标进入视野触发局部 servo；不是从零长距离自主探索

**未覆盖条件与比较限制。** 平台没有臂，无法直接论证移动时臂末端接触补偿；平地、预扫描目标；无通用长距离导航；滤波依赖 VO/深度，无世界不漂移或接触力保证；对称物体 PCA 轴的稳定性不能仅凭低维表示推定

**阅读范围。** 本地 PDF 标题核对；主文完整，附录 A 硬件/目标扫描与 B 主要训练配置已读；附录 C–G 未全部逐项覆盖。

**原文定位。** §2/§3.4：平台与四维动作接口；§3：Sigma Points、EgoKF、遮挡训练、课程；主文实验与局限；Appendix A：预扫描全局目标坐标

**核读订正。** 必须从四足＋臂主类移到四足无臂邻接：<$20 gripper 直接固定在身体；输出 vx/vy/yaw/bodypitch，不是机械臂关节或末端动作；sigma points 不应解释为 unscented Kalman filter；主文 open-world claim 需附上预扫描与平地范围

<a id="2608-20114"></a>
## 2608.20114 DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation（轮足邻接）

[DECOWAM](../literature-map.html#paper=2608.20114) · [PDF](../papers/2608.20114_DECOWAM_Decoupled_Whole-Body_World-Action_Model_for_Legged_Mobile_Manipulation.pdf) · [原文](https://arxiv.org/abs/2608.20114)

**原问题与接口。** 身体移动会改变相机画面；把画面变化都当成臂操作效果，会使动作和未来画面预测混淆。 输入：当前图像、语言和机器人状态，包括身体速度；训练时另用真实后续图像作监督，部署不读取未来图像。 输出：一段未来动作和未来图像；动作的有效部分是六个臂目标、夹爪开口和三个身体速度，另四个维度只是数据接口补位。

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)；；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)

**来源与版本。** 首次预印本：2026-08-20

**方法。** 复用 FastWAM 的视频／动作模型；未来视频教师监督只看当前状态的因果学生，base／arm 两个 latent 用自己的预测头保留动作、交叉梯度反转减少混杂。基座速度 token 帮视频分支解释镜头运动，不是显式 KF 或 SE(3) 对齐。

**实验设置。** 23 episodes replay 中动作 MSE 较 FastWAM 改善 21.7%，X-VLA 的动作误差仍更低。真机每方法 79 次，本方法 46/79、FastWAM 45/79，仅差一次成功；其他协调指标改善不能代替任务率的统计显著性。

**阅读定位：专题／应用。** 轮足world-action模型的近期完整系统；尚未核实分解接口被后续多篇沿用。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)：学习分解预测
- ：整体成功与效率之别

**平台与执行。** 轮足四足＋六自由度臂，轮足邻接

**相对已有方法的具体改动。** 在 FastWAM 的视频/动作联合模型上，教师看未来视频 latent、学生仅看当前输入，蒸馏可由当前状态预测的 action-equivalent representation；将 base/arm 分成两个16维 latent，用自己的预测头保留动作信息、交叉梯度反转抑制另一组信息，并给视频分支当前基座速度。

**复用部分。** WAN video backbone、Action DiT 与 FastWAM 主框架直接复用；第1阶段全量适配，第2阶段冻结主体训练约25.95M adapters；不是从零构造全部模型；语义/表示因子分离不消除机器人本体物理耦合

**实验能支持什么。** 23 episodes×16 replay batches 中 action MSE 较 FastWAM 改善21.7%；X-VLA 的绝对 action error 仍低于本方法；真机每方法79次，本方法46/79＝58.2%，FastWAM45/79＝57.0%，差一个成功；不证明统计显著 task success 提升；报告协调/位移指标44.3/30.4对34.2/12.7，但指标操作定义不足以将其直接等价精确控制或接触安全；结构消融固定 adapter 配置，有助分离因子设计在 replay 的影响；小样本离线收益不等于所有场景任务优胜

**未覆盖条件与比较限制。** 没有显式通过未来视频做在线 MPC/action search 的实验；数据统计在 abstract217/27tasks、stage214/26tasks、审计集合1487等之间有不同范围；不能忽略子集区分；轮足执行与步行四足接触动力学不同；所谓14维动作中包含padding

**阅读范围。** 本地 PDF 标题核对；主文完整，包括模型、蒸馏、数据统计、离线比较、真机与消融。未复算录像指标或运行作者实现。

**原文定位。** 方法：未来条件教师与因果学生蒸馏；方法：base/arm latent 对抗解耦与 ego-motion token；实验：replay action errors、真机79 trials、结构消融；数据审计与训练分阶段描述

**核读订正。** 14维动作＝臂6＋gripper1＋base velocity3＋padding4，不是14个全身关节；速度 token 是学习 ego-motion 条件，不是显式 KF/SE(3) 注册；不能将58.2%对57.0%描述为显著突破任务成功率；world-action joint model 不等于已实施视觉预测规划

<a id="2604-07457"></a>
## 2604.07457 CMP: Robust Whole-Body Tracking for Loco-Manipulation via Competence Manifold Projection

[CMP](../literature-map.html#paper=2604.07457) · [PDF](../papers/2604.07457_CMP_Robust_Whole-Body_Tracking_for_Loco-Manipulation_via_Competence_Manifold_Projection.pdf) · [原文](https://arxiv.org/abs/2604.07457)

**原问题与接口。** 传感器漂移或用户给出极端轨迹时，原本稳定的全身控制器可能做出危险动作。 输入：机器人状态和期望的一段末端轨迹。先编码为任务意图，再限制编码向量的长度，最后由全身策略输出关节动作。安全估计器用于训练时塑造编码空间，部署投影不需要再调用估计器。

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；；[K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)

**来源与版本。** 首次预印本：2026-04-08

**方法。** 用训练经验学习哪些目标在当前状态下较可靠；把复杂轨迹压缩成少量数值，遇到高风险目标时把这些数值拉回较可靠区域，再继续跟踪。

**实验设置。** 极端目标和定位噪声下的仿真、真机跟踪，显著提高文中定义的存活率，同时保留大部分跟踪表现。

**阅读定位：专题／应用。** 明确继承UMI on Legs，能力边界投影的针对性改进；研究问题清楚，但不是已被多支后作采用的基础层。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)：经验控制能力
- [K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)：末端轨迹的能力边界

**平台与执行。** Unitree Go2 + Hexfellow Saber; T265VIO, tasktrajectory;RL jointcontroller

**相对已有方法的具体改动。** safeprobabilityTD学习；KL塑造latent半径与生存对应；normtruncation best-effort意图投影

**复用部分。** UMItrajectoryRL、PPO、CVAElatent、VIO

**实验能支持什么。** 7000traj ID/OODgeom/OODsensor；CVAE/SCVAE/ILS；45hardwaretrials3failure；neuralCBF/latentshield

**未覆盖条件与比较限制。** training timeout target1、maxfuture approximatedlatent0、statisticalradius、安全predictor可过估；survival不是任务完成

**阅读范围。** 正文 §3–6完整审读；附录A–C latentgeometry/proof逐段、部分experiment/baseline补充；未全面独立验证proof适用性

**原文定位。** §3.1–3.4; §4.1–4.3; §6; AppendixA–C

**核读订正。** theory在真值max/准确geometry等条件下，learnedestimator不继承严格guarantee；真实标明3failures；不应写无条件perpetualsafety或forcecontact安全认证

<a id="2605-31343"></a>
## 2605.31343 Learning Terrain-Aware Whole-Body Control for Perceptive Legged Loco-Manipulation

[Terrain-Aware WBC](../literature-map.html#paper=2605.31343) · [PDF](../papers/2605.31343_Learning_Terrain-Aware_Whole-Body_Control_for_Perceptive_Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2605.31343)

**原问题与接口。** 身体会随坡面和台阶改变高度、俯仰；目标若只跟着身体坐标采样，容易把地形变化错误传给手的任务。 输入：身体和关节历史、身体速度／末端目标，以及机载感知得到的脚周和局部地形高度。 输出：学习策略仅输出十二个腿关节的角度目标；六个臂关节目标由末端目标经过逆运动学求解。

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)

**来源与版本。** 首次预印本：2026-05-29

**方法。** 从脚边地形提取信息，按脚的支撑面生成训练目标；合并擅长大范围身体动作和擅长地形适应的两个训练策略。

**实验设置。** 仿真比较地形通过、工作空间、跟踪及模块消融；明确报告走动时可达范围小于站立时。B2＋Z1 真机由 VR 遥控，在操作手臂的同时登上五级、每级 17 cm 的台阶，并连续完成五次组合任务；该演示不等于自主长程任务，也不是各基线的真机对照。

**阅读定位：专题／应用。** 地形条件和末端工作空间的重要扩展，并实际复用Deep WBC的ROA；作为继承实例保留，不因应用环境更复杂就自动成为方法基础。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)：地形条件
- [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)：腿 RL 与臂 IK

**平台与执行。** Unitree B2 + Z1; D455+Mid360 terrain, VRcommands;legsRL50Hz/armIK

**相对已有方法的具体改动。** perfootrings terrainencoding；footcontactplane targetframe；quasilevelWBC +complexterrainlocomotionexpert distillation

**复用部分。** ROA、PPO、DR、DLSIK、terrainmapping

**实验能支持什么。** 五组件独立替换；各terrain workspace/error/footcollision；VRbottle/stairs sequence5times5steps17cm

**未覆盖条件与比较限制。** 高度图依赖传感/4脚有效contactframeupdate；armjoint不是RL；真实长任务由teleop；walkingworkspace小于standing

**阅读范围。** 正文 §III/IV/V方法、reward、ablation、hardware审读；无另附录

**原文定位。** §III-A/B1–6; §IV-A/B/C; TablesII/III

**核读订正。** unified wholebody标题不等于alljointRL；real5consecutive成功不等于largebenchmark success probability；orientationIK精度非learnedarm策略

<a id="2606-24466"></a>
## 2606.24466 FT-WBC: Learning Fault-Tolerant Whole-Body Control for Legged Loco-Manipulation

[FT-WBC](../literature-map.html#paper=2606.24466) · [PDF](../papers/2606.24466_FT-WBC_Learning_Fault-Tolerant_Whole-Body_Control_for_Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2606.24466)

**原问题与接口。** 臂希望身体倾斜以够到目标，但某条腿已无力，继续执行同样姿态会让机器人倒下。 输入：腿和臂的自身状态历史、期望速度／末端姿态，以及从腿状态估计出的关节故障信息。 输出：臂关节目标和期望身体姿态；姿态调整模块根据故障修正身体要求，腿策略输出补偿步态的关节目标。

**对应／相邻机制。** [K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** 首次预印本：2026-06-23

**方法。** 在仿真中降低执行器可用力矩，学习故障识别；将臂提出的身体姿态改成更适合当前支撑能力的姿态，再联合执行。附录规定训练主要削弱同一条腿的三个关节，单关节削弱与锁止是后续评价条件。

**实验设置。** 仿真比较故障下的跟踪与工作空间；真机从地面取物，放到 50、75、90 cm 高的桌面，每个高度、每种故障做 20 次。最难的 90 cm 锁止条件下存活 14/20 次、放置成功 9/20 次，表明维持稳定与完成原任务确有取舍。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)：故障条件与真机范围

**平台与执行。** Unitree Go2 + Airbot Play; fault softwaretorqueweakening/locked command;onboard50Hz

**相对已有方法的具体改动。** fault12vectorfrom5step history；PAM remaparmbasepitch/roll；faultawarelegpolicy

**复用部分。** RoboDuet分支/两stage、RMAstyleadaptation、PD/PPO、DR

**实验能支持什么。** 1000simtrials；partial/completeweakening；height50/75/90×faultmode20realtrial每case；unmodeledlock

**未覆盖条件与比较限制。** §6真实sequentialmove/standingmanipulation；单/同腿faultsupport，不涵盖多腿同时故障；worst90cmlock14/20survive9/20success

**阅读范围。** 正文 §3/4/6全文核心审读；附录A policyinputs/adaptation、C faultdefinition/curriculum、D部分hyperparameters

**原文定位。** §3.1–3.3; §4.1–4.3; §6; AppendixA/C

**核读订正。** §4说w/oFE用groundtruthlabels，却§4.2解释为cannotperceivedamage，消融因果叙述矛盾；AppendixC训练整腿3jointsweakening，§6single-actuator措辞需区分；不是完成walkingforce任务

<a id="2610-23548"></a>
## 2610.23548 Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator

[Reinforcement Learning Based](../literature-map.html#paper=2610.23548) · [PDF](../papers/2610.23548_Reinforcement_Learning_Based_Multi-Terrain_Adaptive_Whole-Body_Control_for_a_Quadruped_Manipulator.pdf) · [原文](https://arxiv.org/abs/2610.23548)

**原问题与接口。** 小机器狗走坡面、台阶或软地面时，追求手的精度与维持身体稳定容易冲突。 输入：身体和关节状态、上一动作、身体速度和末端目标。局部地形高度图仅用于训练的评价网络，不输入部署动作网络。 输出：同一个学习策略输出十二个腿关节和六个臂关节的角度目标。

**对应／相邻机制。** [K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)

**来源与版本。** 首次预印本：2026-10-16

**方法。** 位置目标附着身体，末端朝向保持重力方向；身体状态／速度跟踪表现门控低优先级操作奖励。无需actor读取地形，高度图仅训练critic。

**实验设置。** 仿真每条件1024，模型／质量／速度／载荷比较；真机坡与台阶跟踪，40次完整粗糙地形导航抓取32次成功。分开8次失败原因。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)：身体位置＋重力朝向的混合参考
- [K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)：状态门控奖励与目标冲突

**平台与执行。** Go1＋自制1.5kg Lite Arm；18关节统一 RL

**相对已有方法的具体改动。** 位置目标附着身体，末端朝向保持重力方向；身体状态／速度跟踪表现门控低优先级操作奖励。无需actor读取地形，高度图仅训练critic。

**复用部分。** 非对称 PPO、关节 PD、粗细跟踪奖励、地形课程与域随机化；现成 VLM／检测导航链。

**实验能支持什么。** 仿真每条件1024，模型／质量／速度／载荷比较；真机坡与台阶跟踪，40次完整粗糙地形导航抓取32次成功。分开8次失败原因。

**未覆盖条件与比较限制。** 抓取进入工作空间后速度设零。台阶1.6cm位置误差为身体坐标FK，不是固定世界接触误差；奖励门控是软优先级。

**阅读范围。** 正文 §II–IV 方法、训练、全部主要实验与结论审读；未逐项审读参考文献／观看视频

**原文定位。** §II-A–C；§III-A–C；§IV-A/B；Fig.5/6；Table I

**核读订正。** Table I 定性标签不替代前作全文；总体32/40不能归为独立奖励门控收益。

<a id="2311-00112"></a>
## 2311.00112 Hierarchical Optimization-based Control for Whole-body Loco-manipulation of Heavy Objects

[Hierarchical Optimization-ba](../literature-map.html#paper=2311.00112) · [PDF](../papers/2311.00112_Hierarchical_Optimization-based_Control_for_Whole-body_Loco-manipulation_of_Heavy_Objects.pdf) · [原文](https://arxiv.org/abs/2311.00112)

**原问题与接口。** 搬重物、开门时臂给身体的反作用力不能再当小扰动。输入是物体任务、机器人状态及接触估计；输出是物体运动、机械臂力与身体运动参考，再交给低层控制。 

**对应／相邻机制。** [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)

**来源与版本。** ICRA 2024；2023 预印本，因重载接触是后来模型控制的重要参照而保留。**四足＋背载臂，真机。**

**方法。** 在线操作规划先算物体轨迹和所需力；姿态优化检查机器人能否到达；线性 MPC 将臂施加的力写进身体预测模型。这比仅让走路 MPC 抵抗未知扰动更早考虑操作任务。

**实验设置。** Aliengo＋自制一自由度臂真机举起／搬运最高 8 kg 载荷；门任务及 10 kg 物体快速起升测试为仿真。对照分别移除操作力预测或改变姿态优化，适合重载分支，不宜拿其结果推断轻触电气面板性能。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)：对象与底盘的力序列接口

**平台与执行。** Unitree Aliengo＋自制单自由度臂；真机举起／搬运，门任务与快速起升在仿真中验证。

**相对已有方法的具体改动。** 将物体作用力规划、机器人姿态可行性和考虑操作力的行走 MPC 拆成层级子问题，以便在线执行。

**复用部分。** 组合已有线性行走 MPC、非线性姿态优化、步态／摆腿控制器与物体动力学。

**实验能支持什么。** 真机 3 kg 起升与忽略操作力的 MPC 对比，真机载荷最高 8 kg。仿真 10 kg 起升逐渐缩短动作时间，检验固定力与规划时变力的差别；门操作也在仿真中。

**未覆盖条件与比较限制。** 依赖单自由度专用臂、任务模型／约束、分层参数与近似腿约束。只与忽略物体操作力的简单基线比较，不能建立相对所有统一 MPC 的优势。

**阅读范围。** 已阅读控制总览、物体规划器、身体姿态优化、考虑操作力的行走 MPC、全部实验小节和结论。

**原文定位。** §II–V；§VI-A/B/C/D；§VII

**核读订正。** 门演示不是实机；0.25 秒起升 10 kg 是仿真结果，报告的真机最大载荷为 8 kg。

<a id="paper-32"></a>
## paper-32 Design and Control Co-Optimization for Dynamic Loco-Manipulation With a Robotic Arm on a Quadruped Robot

[Design and Control Co-Optimi](../literature-map.html#paper=paper-32) · [原文](https://doi.org/10.1115/1.4066852)

**原问题与接口。** 背载六自由度臂增加重量、挤占负载；若身体本身会移动，某些任务不一定需要完整的六个臂自由度。 

**对应／相邻机制。** [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)；[K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)

**来源与版本。** *Journal of Mechanisms and Robotics*, 2024。**Aliengo＋臂；目前只核对出版摘要。**

**方法。** 把机械臂结构选择与全身控制一起设计，研究少自由度臂如何利用四足底盘移动补足工作空间，而不只在固定六自由度硬件上调控制参数。

**实验设置。** 出版摘要称 Aliengo 上比较其一自由度臂与六自由度臂，最大载荷为 8 kg 对 2 kg；具体任务、重复次数和控制消融尚待全文核对。对当前 Piper 臂不能直接类推为“自由度越少越好”。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**未取得全文。** 保留旧卡片与候选机制标签，不作独立全文判断。新方法细节和效果须待全文回查。



<a id="2403-18197"></a>
## 2403.18197 LocoMan: Advancing Versatile Quadrupedal Dexterity with Lightweight Loco-Manipulators

[LocoMan](../literature-map.html#paper=2403.18197) · [PDF](../papers/2403.18197_LocoMan_Advancing_Versatile_Quadrupedal_Dexterity_with_Lightweight_Loco-Manipulators.pdf) · [原文](https://arxiv.org/abs/2403.18197)

**原问题与接口。** 背载单臂难进窄空间，直接用腿操作又损失支撑。Go1 两前小腿各加 3 自由度／147 g 操纵模块，与腿三关节合成 6DoF 操作肢；输入身体／手目标，由模式化 WBC 输出关节／力指令。 

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** IROS 2024。**四足＋小腿装臂，真机。**

**方法。** 运动学 nullspace 优先级与动力学 QP 按单手、双手、行走和移动操作切换；切换含停稳、移开机身等规则。贡献首先是形态、可达性及模式执行，控制不是从零训练的全身 RL。

**实验设置。** 真机遥操作充电器插入、柜门／抽屉、倒饮料、狭窄取物和双手提物。单／双 workspace 0.34→0.68、0.38→0.83 m³ 来自运动学采样；原地五组任务的8秒末端轨迹平均 1.89 mm／0.047 rad 由自身估计与运动学计算，没有独立世界测量。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** Go1两前小腿各装3DoF/147g操纵模块；每条腿＋模块形成6DoF操作肢

**相对已有方法的具体改动。** 通过极轻3DoF末端模块复用腿的3DoF形成操作肢；按standing single/bimanual/locomotion/locomanipulation切换运动学任务优先级，再由现有式样的dynamicQP实现支撑与操作。硬件可达空间与统一模式执行是主要贡献。

**复用部分。** 运动学nullspace任务优先级与动力学QP基于Kim whole-body impulse control等既有控制思想；Human2LocoMan直接承接硬件/控制；学习人示范是后者的新上层，不是本篇

**实验能支持什么。** 每模块147g、约$370；单/双工作空间0.34→0.68m3、0.38→0.83m3来自碰撞约束运动学配置采样；五组原地任务各以四个中间位姿生成8秒轨迹；Table IV的gripper-with-torso-motion平均1.89mm/0.047rad，由关节/状态估计运动学计算，没有独立worldgroundtruth；真机charger/cabinet/ropehoisting/pouring与.25m床/.09m柜下操作均遥操作示范，非自主成功率评估；行走模式手电筒在worldframe跟踪orientation，前行.15m/s、侧移.05m/s；不等于完整六维接触位置跟踪

**未覆盖条件与比较限制。** 固定站立/坐姿与模式切换；换模式含停稳/shiftbody规则；运动学workspace不代表带力矩/摩擦/速度限制的动态contactworkspace；真机毫米误差含自身估计，不能排除base/world漂移

**阅读范围。** 本地 PDF 标题核对；主文完整至结论；附录控制/状态估计主要段核对，硬件/参数附录未全逐项复算。

**原文定位。** §III：硬件设计与6DoF组合；§IV与Table III：FSM/各模式任务优先级及WBC；§V，Table IV：末端轨迹误差；§V：双手任务、狭窄空间与手电筒行走；附录：state estimation

**核读订正。** 不是在背部安装两个六轴臂，而是两个小腿3DoF模块＋腿关节；1.89mm不是walkingcontactworldgroundtruthaccuracy；loco-manipulation主要维持gripperorientation，不要写任意完整EEposition在行走中精确控制；FSMmotionmode不是自主任务成功事件记忆

<a id="2403-20328"></a>
## 2403.20328 Learning Visual Quadrupedal Loco-Manipulation from Demonstrations

[Learning Visual Quadrupedal ](../literature-map.html#paper=2403.20328) · [PDF](../papers/2403.20328_Learning_Visual_Quadrupedal_Loco-Manipulation_from_Demonstrations.pdf) · [原文](https://arxiv.org/abs/2403.20328)

**原问题与接口。** 单纯位置指令难把远距离移动与可变场景中的腿部操作串起。方法从人示范和图像学习任务策略，下层用 RL 全身控制把目标足端动作落实到步态和身体。 

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)

**来源与版本。** **四足以前腿为手，真机。**

**方法。** 视觉扩散策略生成参数化 Bézier 足端轨迹／身体指令，低层接收当前及未来足端目标执行；分层使少量视觉示范不用学全部关节反馈。

**实验设置。** 真机足端交互与轨迹跟踪；视觉规划、未来点及策略接口的实验。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)：视觉规划与低层使用不同参考系
- [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)：参数化轨迹接口
- [K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)：未来足端点
- [K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)：视觉轨迹规划

**平台与执行。** 四足，无外挂臂；使用前足操作

**相对已有方法的具体改动。** 视觉扩散策略生成参数化 Bézier 足端轨迹／身体指令，低层接收当前及未来足端目标执行；分层使少量视觉示范不用学全部关节反馈。

**复用部分。** 特权信息训练、历史适应、扩散模仿、参数化轨迹、PD 执行。

**实验能支持什么。** 真机足端交互与轨迹跟踪；视觉规划、未来点及策略接口的实验。

**未覆盖条件与比较限制。** 轨迹接口和任务示范给出较强先验；视觉与低层参考系不完全相同，不能仅写端到端视觉全身策略。

**阅读范围。** 正文方法、训练、主要实验与结论审读；提取的双栏段落逐项核对；未逐项复核所有补充图

**原文定位。** §III-A–D；§IV；§V-A；结论

<a id="2402-10837"></a>
## 2402.10837 Pedipulate: Enabling Manipulation Skills using a Quadruped Robot’s Leg

[Pedipulate](../literature-map.html#paper=2402.10837) · [PDF](../papers/2402.10837_Pedipulate_Enabling_Manipulation_Skills_using_a_Quadruped_Robots_Leg.pdf) · [原文](https://arxiv.org/abs/2402.10837)

**原问题与接口。** 不加专用机械臂，能否让一条前腿既准确触物又在目标远离时主动迈步扩大工作空间？输入足端目标位置，RL 控制器输出全身运动；走步从追踪远端目标的策略中出现。 

**对应／相邻机制。** [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** ICRA 2024。**四足以前腿操作，真机。**

**方法。** 训练面向单足末端位置目标的策略，要求同时抵抗足端相互作用力、身体扰动和滑动接触。与普通抬腿触物相比，任务空间指令可持续驱动机器人移动到目标附近。

**实验设置。** 真机遥操作开门、按按钮、取样、推障碍，并用足端悬挂搬运 2.0 kg 背包；论文还测了可达空间、跟踪及扰动。它训练时施加交互扰动，但原文明确说没有显式建模或跟踪操作力；不能把抗扰能力写成受控施力能力。其工作空间与支撑也不同于背载 Piper 臂。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)：固定前腿操作
- [K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)：足端任务用标准策略优化

**平台与执行。** ANYmalD;fixedrightfrontfootmanipulator,optionalfootgripper,SLAMcontrolframe

**相对已有方法的具体改动。** largeworkspacefoottrackingcurriculum让3leglocomotionemerge；inertialtasktarget transformbaseobs

**复用部分。** PPO/MLP、actuatornetwork、DR、jointPD

**实验能支持什么。** near3.7cmsim/5.7cmreal、IK4.1cmsim；far4.3cmsim；upto132Nbaseperturb；realdoors/backpack/button1.25m

**未覆盖条件与比较限制。** foottracking/teleop，operator视线到robot；onefixedlimb，不autonomousmask；noarm

**阅读范围。** 正文 §III/IV/V方法结果完整审读；没有arm，无另附录

**原文定位。** §III-A–E; §IV-A/B/C

**核读订正。** bodyframeobs不意味bodyfixedtarget；SLAMfixedlocalframe；demo带gripper不改变controllerabstracttask，不能作为quadruped-armcorepaper

<a id="2407-06584"></a>
## 2407.06584 HiLMa-Res: A General Hierarchical Framework via Residual RL for Combining Quadrupedal Locomotion and Manipulation

[HiLMa-Res](../literature-map.html#paper=2407.06584) · [PDF](../papers/2407.06584_HiLMa-Res_A_General_Hierarchical_Framework_via_Residual_RL_for_Combining_Quadrupedal_Locomotion_and_Manipulation.pdf) · [原文](https://arxiv.org/abs/2407.06584)

**原问题与接口。** 持续走动时，能否利用摆动腿操作，而不为每个任务重新训练全部走路能力？底层输入身体移动指令和摆动足轨迹参数，输出关节角度目标；高层根据任务状态或视觉决定这些指令与参数。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** IROS 2024。**四足以足端操作，真机。**

**方法。** 固定采用对角小跑，先训练底层跟踪由步态发生器生成的正常足轨迹与 Bézier 残差之和；残差只加在摆动足，支撑足参考不变。高层任务策略再选择残差曲线的控制点。这里的残差是足端轨迹修正，并非关节力矩补偿，也非任意支撑模式下的足端控制。

**实验设置。** 真机运送载荷、踢／带球和避开散布石块，涵盖仿真训练与实机学习，并与单层、轨迹跟踪及其他分层方法比较。石块任务主要验证走路避障；论文没有专用机械臂，适合理解分层轨迹接口，非柜门轻接触的直接基线。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** Quadruped robot no arm;footCPG+Bézierresidual;taskplanner;UWB/depthcameras

**相对已有方法的具体改动。** task-independentoperationalspacefootcontroller；taskhighlevel选swingfootresidual＋basecommand；sim/realpolicyreuse

**复用部分。** CPG/Bézier/PPO、DroQ/RLPD、DR、GRUdepthencoder

**实验能支持什么。** NavLoadGazebosimbenchmark4goals×2attempts；real9min1000steptraining；ballUturn、4stonepassruns87.5%avoidance

**未覆盖条件与比较限制。** fixedtrot/swinglegsnotarbitrarymask；loadlearnedrealdata；stonebranch纯障碍规避，不是物体操作；小量trials

**阅读范围。** 正文 §III–VI完整方法任务和结果审读；无另附录

**原文定位。** §III; §IV-A/B/C; §V-A/B; §VI-A/B/C

**核读订正。** 无mountedarm；residual指swingtrajectory，不是additivetorquecorrection；87.5%是stonesavoided比率而非complete-task-success

<a id="2411-07104"></a>
## 2411.07104 Learning Multi-Agent Loco-Manipulation for Long-Horizon Quadrupedal Pushing

[Learning Multi-Agent Loco-Ma](../literature-map.html#paper=2411.07104) · [PDF](../papers/2411.07104_Learning_Multi-Agent_Loco-Manipulation_for_Long-Horizon_Quadrupedal_Pushing.pdf) · [原文](https://arxiv.org/abs/2411.07104)

**原问题与接口。** 多个四足推大物体绕障时，单个机器人局部推进会相互妨碍。输入地图、物体目标和各机器人状态；输出子目标与每台机器人的移动指令。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)

**来源与版本。** ICRA 2025。**多四足以身体推物，真机。**

**方法。** RRT提供物体路径，中央高层调物体子目标，去中心中层策略各自输出速度，底层走路；凸包内法向与子目标方向的奖励帮助找推物侧。

**实验设置。** 仿真中相对最优基线成功率高 36 个百分点、时间少 24.5%；真机展示不同形状物体的协同推送。无机械臂，纳入是为覆盖非抓取式四足操作，不是用户当前设备的主路线。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** 多台 Go1，无臂；机身共同推物，外部动捕

**相对已有方法的具体改动。** RRT提供物体路径，中央高层调物体子目标，去中心中层策略各自输出速度，底层走路；凸包内法向与子目标方向的奖励帮助找推物侧。

**复用部分。** MAPPO／PPO、RRT、WTW 步态；仿真底层拟合 Unitree 真机内置控制器响应。

**实验能支持什么。** 三种物体长程障碍推送，多种分层／奖励消融，1–4机器人规模比较；两台真机推方箱和T块。

**未覆盖条件与比较限制。** 仿真≥10m任务终点容差1m，与轻操作精度不同；动捕对象状态；真机与仿真底层不同，但作者专门拟合其行为。

**阅读范围。** 正文分层方法、奖励、仿真与真机设置／结果审读；主要表格核对；未观看视频

**原文定位。** §III-A–E；§IV-A–D；Tables II/III

**核读订正。** 四台不优于三台，接触面积与机器人干扰限制收益；遮挡奖励是几何提示，不是视觉遮挡感知算法。

<a id="paper-38"></a>
## paper-38 Env-Mani: Quadrupedal Robot Loco-Manipulation with Environment-in-the-Loop

[Env-Mani](../literature-map.html#paper=paper-38) · [原文](https://doi.org/10.1109/IROS60139.2025.11246108)

**原问题与接口。** 四足若只靠地面四点支撑，够不到较高目标。方法让机器人利用桌沿等外部环境承重，扩展操作工作空间。 

**对应／相邻机制。** [K11 抗扰裕量是在扰动发生前保留余地](../knowledge/network.md#k11)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** IROS 2025。**四足以环境作支撑；目前仅核对出版摘要。**

**方法。** 统一策略以有限机载传感和自身状态生成全身动作，用奖励处理感知误差与重心转移，并以课程训练教师和学生策略。与多接触规划分支讨论相同物理机会，但不能由此断言继承了 ETH 的算法。

**实验设置。** 摘要称仿真训练和扩展实验，未明确说明真机与数量；全文 PDF 未取得，因此仅保留摘要层面的判断。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**未取得全文。** 保留旧卡片与候选机制标签，不作独立全文判断。新方法细节和效果须待全文回查。



<a id="2511-14756"></a>
## 2511.14756 HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation

[HMC](../literature-map.html#paper=2511.14756) · [PDF](../papers/2511.14756_HMC_Learning_Heterogeneous_Meta-Control_for_Contact-Rich_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2511.14756)

**原问题与接口。** 同一任务的靠近、插入、拉出需要不同刚度；固定位置控制会碰撞，始终柔顺又拉不动。输入视觉和自身状态，策略同时给出运动与控制模式权重，控制器在力矩层连续混合位置、阻抗和力／位混合控制。 

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)

**来源与版本。** ICRA 2026。**人形，真机；移动成分较弱，列为接触控制邻接参考。**

**方法。** 先用大量只有位置标签的数据训练共同表征，再用较少的带力感示范学习模式路由；软混合避免模式硬切换引起的力突变。这是“学习策略怎样调用柔顺控制”的有价值接口例子，不是四足 VLA。

**实验设置。** Unitree G1 真机擦拭、拿瓶、开抽屉，每种设置 15 次；表中擦拭成功率 93% 对位置基线 33%。实验主要是接触操作，未把持续行走接触作为核心量化结果，故不放严格的四足核心短名单。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)：多控制器的力矩接口
- [K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)：控制模式混合
- [K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)：控制模式与参数学习

**平台与执行。** G1人形；全身接触操作、关节力矩混合执行

**相对已有方法的具体改动。** 让异构策略学习位置、阻抗与混合控制器的参数和组合权重，最终混合力矩，处理自由运动／接触需求变化。

**复用部分。** 位置／阻抗／混合控制器、Transformer行为克隆、既有全身执行结构。

**实验能支持什么。** 三类真机任务；seen／unseen 条件每类15次；控制模式组合及异构策略消融。

**未覆盖条件与比较限制。** 软权重切换没有整体稳定性证明；基准策略不是 VLA；无专门 F/T 的粗力信息和物理力标定需区别。

**阅读范围。** 正文方法、实验、消融和结论审读；控制器公式与真机试验数回查

**原文定位。** §III 控制与示教；§IV-A/B 学习；§V 实验

<a id="2510-09221"></a>
## 2510.09221 HANDO: Hierarchical Autonomous Navigation and Dexterous Omni-loco-manipulation

[HANDO](../literature-map.html#paper=2510.09221) · [PDF](../papers/2510.09221_HANDO_Hierarchical_Autonomous_Navigation_and_Dexterous_Omni-loco-manipulation.pdf) · [原文](https://arxiv.org/abs/2510.09221)

**原问题与接口。** 未知环境里先找到目标、再在操作位完成接触。方法将目标条件自主探索与全身操作策略分层；接口上导航给目标区域，操作层协调臂和腿。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)

**来源与版本。** **Go1＋Piper，早期预印本。**

**方法。** 方法将目标条件自主探索与全身操作策略分层；接口上导航给目标区域，操作层协调臂和腿。

**实验设置。** 作者只报告导航模块的初步真机部署；精细实机操作仍是后续工作。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** HANDO：Unitree 四足＋Piper 系列臂，导航系统原型

**相对已有方法的具体改动。** 提出把语义导航、分层任务和四足操作接成系统的架构。

**复用部分。** 现成导航与视觉语言组件、预设任务分解。

**实验能支持什么。** 目前只报告导航模块的初步真机部署。

**未覆盖条件与比较限制。** §IV 明确操控仍在开发，不能用整系统目标描述充当已验证自主操作结果。

**阅读范围。** 本地4页全文审读，逐项核对实现与当前结果

**原文定位。** §III；§IV；结论

**核读订正。** 摘要／架构与实验状态不一致；已实现范围按实验段落记录。

<a id="2607-06186"></a>
## 2607.06186 Calf-Integrated Arms for Bimanual Quadruped Loco-Manipulation

[Calf-Integrated Arms for Bim](../literature-map.html#paper=2607.06186) · [PDF](../papers/2607.06186_Calf-Integrated_Arms_for_Bimanual_Quadruped_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2607.06186)

**原问题与接口。** 四足双手操作通常要立起身体或牺牲前腿支撑。每条前小腿嵌入滑动关节、旋转关节和夹爪，四足着地时即可双臂操作。 

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **Go2 小腿内置双臂，仅仿真。**

**方法。** 底层全身控制按技能执行，VLM 仅在技能边界依据图像／任务状态选择预定义技能；它不是连续输出全身动作的 VLA。

**实验设置。** 仿真柜门任务、双手举起与两手交接。缺真机验证，价值主要在形态方案和“语言选技能／控制器执行”的分层接口。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)：腿上小臂形态，仅仿真
- [K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)：区域中心不是把手接触点

**平台与执行。** 仿真四足，腿部安装小臂；无真机

**相对已有方法的具体改动。** 腿上小臂通过预定义 FSM 和动作库执行；VLM 选择语义目标／步骤，模块化验证特定形态。

**复用部分。** 刚体仿真、固定技能库／FSM、VLM 任务分解。

**实验能支持什么。** 仅仿真；区域定位与操作案例，部分目标用红色标记；报告16–40秒推理。

**未覆盖条件与比较限制。** 区域中心不等于把手接触点；VLM 不生成未定义技能；执行延迟与无真机验证限制结论。

**阅读范围。** 正文结构、控制架构、VLM、任务与限制审读；未运行系统

**原文定位。** §III–V；§V-F；结论

<a id="2607-11041"></a>
## 2607.11041 PAKE: Learning Whole-Body Loco-Manipulation with Partial Kinematic Embeddings

[PAKE](../literature-map.html#paper=2607.11041) · [PDF](../papers/2607.11041_PAKE_Learning_Whole-Body_Loco-Manipulation_with_Partial_Kinematic_Embeddings.pdf) · [原文](https://arxiv.org/abs/2607.11041)

**原问题与接口。** 给定手的目标位置和移动速度，常有许多可行身体／臂姿态；直接 RL 在高维关节空间寻找精确解很难。输入手六维目标和底盘速度，输出连续关节控制。 

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)

**来源与版本。** RA-L 接收稿，2026-10。**RAION Robotics RAIBO2＋Unitree Z1，真机。**

**方法。** 采样身体高度、横滚、俯仰和六个臂关节，用正运动学生成训练数据；条件流模型据此生成同一末端目标对应的多种身体／臂参考。高层策略选择流模型的潜变量，低层 RL 控制腿去实现身体参考，臂由 PD 控制跟踪关节参考；完整 PAKE 还加入教师引导的高层优化以减小参考突变。运动学采样省略腿的约束，因此生成参考不自动保证动态可行。

**实验设置。** RaiSim 中用 4000 个目标比较精度与工作空间；真机实际部署简化版 PAKE-S，8 类任务共 24 次，含拉车、扫地、插充电器、挂衣架。动捕测得平均末端位置误差约 4.5 cm、姿态误差约 0.14 rad；完整 PAKE 相对 PAKE-S 的进一步增益来自仿真。UMI on Legs 基线改用随机轨迹和身体坐标跟踪，不能当作原方法完整接口的直接排名。它仍是任务空间跟踪器，不直接解决语义决策或接触力安全。

**阅读定位：新路线代表。** 学习末端目标对应的多种可行全身姿态，并选择执行；新的分层接口值得观察，尚无已核实的多支复用。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)：多配置建模
- ：真机版本边界

**平台与执行。** RAIBO2 from RAION Robotics + Unitree Z1; RaiSim; heading-frame partial torso–arm reference; LLC100Hz/armPD

**相对已有方法的具体改动。** conditionalNF学partialtorso–arm多解，HLC选择latent、LLC动态腿执行；laterteacher-guidedHLCoptimization改善平滑

**复用部分。** NormalizingFlows/Glow/PPO、jointPD、asymmetriccritic、DR

**实验能支持什么。** 4000targets+latentzero/shuffle/randomintervention；200targets×6torsoforces；PAKE-S24episodes8realtasks

**未覆盖条件与比较限制。** partialFK省略legconstraints，无动态保证；优化highlevel不是freehandtaskplanner；硬件usedPAKE-S；基线来自IsaacGym而PAKE来自RaiSim，多平台/训练处理差异

**阅读范围。** 正文 §III完整方法；§IV-A/B完整平台/基线与部分扩展数据；§IV-C/D/E完整ablation/hardware；无另附录

**原文定位。** §III-A–D; §IV-B/C/D/E; TablesIII–VII

**核读订正。** 强化teacher-guided额外training onlysim，hardware不支持全部completePAKE独立效益；samplingfullpartialchain≠全身接触可行；§IV-A平台是RAIBO2+Z1，非ANYmal；§IV-B的UMI-on-Legs基线使用随机轨迹且body-frame tracking，已经改变其核心task-frame接口，不能无条件视为原方法比较

<a id="2608-22296"></a>
## 2608.22296 TONAV: Task-Oriented Navigation and Action-Velocity Chunk Learning for Articulated Object Quadrupedal Mobile Manipulation

[TONAV](../literature-map.html#paper=2608.22296) · [PDF](../papers/2608.22296_TONAV_Task-Oriented_Navigation_and_Action-Velocity_Chunk_Learning_for_Articulated_Object_Quadrupedal_Mobile_Manipulation.pdf) · [原文](https://arxiv.org/abs/2608.22296)

**原问题与接口。** 导航到物体附近还需调整朝向／距离才能进入操作策略的起始分布；示范又会因主从伺服延迟及动作块跳变产生误差。输入语言、RGB-D、本体与示范，输出导航目标、近场对齐及臂动作块。 

**对应／相邻机制。** [K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)；[K24 机构约束与在线交互辨识](../knowledge/network.md#k24)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)

**来源与版本。** **Go2-W 轮足＋Piper 臂，真机预印本；轮足邻接。**

**方法。** 语言拆子目标后用 SAM2 mask／深度反投影和 ego-motion KF 更新目标，AAM 使目标居中并维持工作空间 stand-off。220 Hz 主从 MIT 控制记录从臂目标轨迹／速度；ACT 同时预测位置、速度，加入有限差分一致性损失。

**实验设置。** 关抽屉、开灯、放马桶盖，各五次导航共 9/15＝60%。操作从统一准备姿态单独开始，12/15＝80%；这是条件操作率，不是完整导航后操作的端到端成功。相同小样本下，position+velocity ACT 46.67%，完整80%。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)：轮足操作导向终点
- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：轮足速度监督

**平台与执行。** Unitree Go2-W 轮足底盘＋Piper 主从臂遥操作，轮足邻接

**相对已有方法的具体改动。** 远场语义导航后，AAM 用目标 mask 深度及 ego-motion KF 做近场朝向/距离对齐，使起始姿态接近操作示范；主从遥操作记录从臂跟随目标，同步关节速度，再在 ACT 加速度监督与有限差分一致性损失减少块内不连续。

**复用部分。** Qwen、SAM2、既有导航器、ACT/CVAE 与关节 MIT PD 为复用组件；主从控制220 Hz、相机30 Hz同步；它是关节目标/数据质量路线，不是提出新动力学 WBC

**实验能支持什么。** 3任务×5导航试验，9/15成功＝60%；操作均从统一 manipulation-ready pose 开始，12/15＝80%是条件操作率；ACT position+velocity 为46.67%，完整80%，without improved data 为53.33%，小样本消融支持数据采集与对齐贡献；AAM 为目标居中与工作空间 stand-off，未完整优化操纵度/接触未来路径；数据标签使用 follower target trajectory，可避免直接 master pose 标签的伺服时间差

**未覆盖条件与比较限制。** 导航与操作分阶段，非接触中持续移动/换步实验；每任务五次，统计方差大；80%不是全链路表现；velocity head 是否实际进入部署低层控制描述不充分；无校准峰值接触力或触觉安全实验

**阅读范围。** 本地 PDF 标题核对；主文完整，包括数据/控制接口、导航、AAM、ACT 损失、全部结果及讨论。

**原文定位。** PP-CoT 与 AAM 方法；主从 MIT 控制及数据同步；ACT position/velocity/consistency loss；结果：导航15次与条件操作15次

**核读订正。** 是 Go2-W 轮足＋Piper，不是普通步行四足；把导航60%与操作80%分开，不能将后者写为端到端，也不能把二者相乘当实测；position-velocity consistency loss 不是已证明柔顺/力控制；近场对齐不是完整可操作 base pose optimization

<a id="2609-22278"></a>
## 2609.22278 DeViGrasp: Robust Visual Mobile Grasping for Quadruped Manipulators under Degraded Perception

[DeViGrasp](../literature-map.html#paper=2609.22278) · [PDF](../papers/2609.22278_DeViGrasp_Robust_Visual_Mobile_Grasping_for_Quadruped_Manipulators_under_Degraded_Perception.pdf) · [原文](https://arxiv.org/abs/2609.22278)

**原问题与接口。** 遮挡、深度噪声和目标抖动使学生难以复制物体真值教师；用双视角的有效帧与时间可靠性信息形成较稳定的抓取动作。 

**对应／相邻机制。** [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)；[K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)

**来源与版本。** **四足＋臂，仅仿真定量。**

**方法。** 教师聚合候选抓取特征，学生以双相机缓存、时间／来源编码、可靠性与 GRU 保存近期目标；输出 9 维末端／基座／夹爪目标，低层为腿 RL＋臂 IK。它记近期感知，不记录“按钮已按成功”等任务事件。

**实验设置。** 主文定量为 Isaac Gym 中 B1＋Z1，33 已见／6 未见物体、四级退化、500 episodes×3 seeds。Difficult 62.3% 对 VBC46.2%、DQ58%；DQ 在成功 episode 上更快。Go2 补充示范不能替代定量真机证据；descriptor 融合也不是两个相机三维测量注册后的物理平均。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)：感知退化与特征级融合

**平台与执行。** 仿真 B1＋Z1；四足＋机械臂。补充 Go2 示范的真实硬件属性未完整核实

**相对已有方法的具体改动。** 教师从候选抓取特征形成动作相关 latent，学生在双分割深度流中保存有效历史，用时间、来源、可靠性和退化程度选择近期信息，并通过 GRU 输出 9 维移动/末端/夹爪指令。

**复用部分。** PPO/teacher distillation 与 RL腿＋IK臂接口属 VBC 同族；共享结构不独立推断作者直接继承关系；主要增量是退化观测处理及教师抓取特征，而非发现新的机械臂动力学

**实验能支持什么。** 全部主文定量在 Isaac Gym，33 seen/6 unseen objects，500 episodes×3 seeds，遮挡/dropout/noise/jitter四级；Difficult 成功62.3%，VBC46.2%、DQ58%；Hard54.8%对DQ44.3%；成功动作平滑性 ASL1 0.289 对0.370；DQ在已经成功的episodes上更快，故效率非各项统优；固定EMA没有稳定收益，选择性可靠性/时间记忆优于该简单平滑基线；不同相机descriptor各自归一化像素/深度，策略融合的是特征，不是注册后的物理三维点平均

**未覆盖条件与比较限制。** 仿真退化分布与真机相关噪声、标定误差、光照等未充分等价验证；手动/既有分割接口和高层目标语义限制仍在；没有按钮成功事件记忆，也没有校准接触力/换步安全指标

**阅读范围。** 本地 PDF 标题核对；主文完整，教师抓取聚合、双视角时间记忆、训练和全部定量实验已读。未观看补充视频，因此不登记未核实的真机定量结果。

**原文定位。** 教师 grasp candidate attention；学生 THM/TMA/recovery descriptor 与 GRU；controlled degradation levels、seen/unseen objects；结果表：success、smoothness 与成功episode耗时

**核读订正。** 不能把62.3%写成真机结果；补充视频不能替代定量hardware证据；TMA是感知历史，不是已操作/失败事件记忆；attention聚合抓取特征不是平均6D抓取姿态；可靠性descriptor融合不是Bayesian几何sensor fusion

<a id="2609-30140"></a>
## 2609.30140 Contact as a Decision Variable: Capability-Tradeoff Contact Selection for Legged Loco-Manipulation

[Contact as a Decision Variab](../literature-map.html#paper=2609.30140) · [PDF](../papers/2609.30140_Contact_as_a_Decision_Variable_Capability-Tradeoff_Contact_Selection_for_Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2609.30140)

**原问题与接口。** 机器人可把身体靠住环境增加承受外力能力，但靠错地方会挡住手或妨碍走路。输入候选环境接触和任务所需末端位姿／力，输出支撑接触点及身体配置。 

**对应／相邻机制。** [K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)；[K11 抗扰裕量是在扰动发生前保留余地](../knowledge/network.md#k11)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **Go2＋臂，真机预印本。**

**方法。** 以剩余可承受力、末端可达性、底盘移动能力与建立接触成本来评估候选；先筛不可行项，再用相近接触分组及局部敏感度近似减少反复优化。它把“要不要靠、靠哪里”作为显式决策，与预设额外接触的控制方法有区别。

**实验设置。** 仿真大规模候选比较；Go2＋NERO 臂另装身体侧面平面支撑架，真机持续支持接触并行走承载，5 次行走试验的末端位置 RMSE 为 14.97 mm。候选选择约需 39／62 秒，执行控制器为 10 Hz；不能称为实时完整接触序列规划。场景几何及摩擦需预建模，具体约束还引用 PDF 外的补充材料。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K11 抗扰裕量是在扰动发生前保留余地](../knowledge/network.md#k11)：额外接触选择

**平台与执行。** Go2＋AgileX NERO 七自由度臂＋专用平面侧向支撑架。

**相对已有方法的具体改动。** 依据任务剩余施力／可达／移动能力和接触获取成本，联合选择环境支撑与身体配置；用 LP 值敏感度、锚点分组、验证及候选缩减降低评估成本。

**复用部分。** 使用全身动力学／接触约束、能力多面体、LP 值敏感度、聚类与滚动时域控制。

**实验能支持什么。** Gazebo 包含 392 种任务条件及 45000 个接触／配置候选，比较穷举、只用地面、固定支撑及消融；真机分别五次固定支撑和五次行走试验，借助额外接触保持载荷。

**未覆盖条件与比较限制。** 选择约需 39／62 秒，执行控制器 10 Hz；有限采样候选不代表全局最优。能力是局部的，且指定了 trot 阶段；需要专用支撑硬件。完整约束／控制器细节依赖本地缺失的外链补充材料。

**阅读范围。** 已阅读全文的能力定义／接触选择算法／实验；补充约束细节通过外部链接提供，不在本地 PDF 中，未读取。

**原文定位。** §III-A/B/C；§IV-A/B/C；§V-A/B/C/D；§VI

**核读订正。** 不是实时任意接触序列规划。其操作可达余量不同于 RAKOMO 的腿运动学可达余量；固定支撑也可能损失移动性或降低某些能力。

<a id="2610-20968"></a>
## 2610.20968 SOMA: Stack-of-Objects Manipulation using a Quadruped Robot

[SOMA](../literature-map.html#paper=2610.20968) · [PDF](../papers/2610.20968_SOMA_Stack-of-Objects_Manipulation_using_a_Quadruped_Robot.pdf) · [原文](https://arxiv.org/abs/2610.20968)

**原问题与接口。** 推叠放的箱子时，上层可能滑落；底盘高度也是影响施力位置的变量。高层用时间历史预测物体推进目标，低层步行策略按目标调节身体高度和步态。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)；[K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)

**来源与版本。** **四足无臂推物，真机预印本。**

**方法。** 给高层速度接口增加身体高度，改变推力作用点；S5历史编码、Beta有界命令、单箱→双箱课程及堆物滑移／倾倒惩罚。

**实验设置。** 125形状／质量网格仿真；MLP/GRU/S5、单形状／多形状训练比较；双箱九条件，最优90.1%；真机五配置，图4四次轨迹。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：历史编码与显式辨识的区分

**平台与执行。** Go1，无臂；机身推双层堆物；动捕底层物体

**相对已有方法的具体改动。** 给高层速度接口增加身体高度，改变推力作用点；S5历史编码、Beta有界命令、单箱→双箱课程及堆物滑移／倾倒惩罚。

**复用部分。** 冻结的PPO步态、分层推物、非对称critic、域随机化；历史估计思想不是新提出。

**实验能支持什么。** 125形状／质量网格仿真；MLP/GRU/S5、单形状／多形状训练比较；双箱九条件，最优90.1%；真机五配置，图4四次轨迹。

**未覆盖条件与比较限制。** 90.1%是最佳条件，不是全部堆物平均。真机姿态容差5°，仿真部分1°；Fig.2正文0.1m、摘要／其他部分0.05m，需按各实验区分。

**阅读范围。** 正文 §II–III 方法、训练、全部主要实验与结论审读；部分参考追踪

**原文定位。** §II-A–D；§III-A–D；Tables II/III；Fig.4

**核读订正。** 没有height通道独立消融，不能将全部收益归给高度；S5历史有用不证明物理参数被显式准确估计。

<a id="2609-18869"></a>
## 2609.18869 KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation

[KINO](../literature-map.html#paper=2609.18869) · [PDF](../papers/2609.18869_KINO_A_Keyframe_Interface_for_VLM_Planning_and_Whole-Body_Control_in_Humanoid_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2609.18869)

**原问题与接口。** 抽象任务步骤缺少动态控制目标；VLM 从人工关键帧库选标签，再按现场物体重定位，由 RL 控制器追踪，形成有限目标空间的高低层接口。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)

**来源与版本。** **人形，真机预印本；VLM＋RL 而非端到端 VLA。**

**方法。** 物体相对重定位加 IK 修正全身姿态，tracker 以关键帧历史和多 critic 训练；提高抓取／释放等稀疏事件的 goal sampling，使训练目标更符合规划器部署分布。规划器接收目标误差与停稳反馈重新选目标。

**实验设置。** 仿真 100 trials 的消融 44%→92%；Unitree G1 真机取放主要定性，物体位姿用 MoCap。放置容差约 0.3 m，不能作精细面板操作的精度证据。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：VLM 选择姿态

**平台与执行。** Unitree G1；真机objectpose使用MoCap，人形邻接

**相对已有方法的具体改动。** VLM从人工库选择稀疏关键帧标签，按场景重定位全身/物体参考并用IK修正；低层RL以关键帧历史追踪、分别处理goal/tracking/regularization，训练增加抓取等关键事件采样，缩小部署稀疏目标与训练分布的差异。

**复用部分。** keyframe/motionretargeting、IK、multi-criticPPO与VLMplanner为已有机制结合；作者库限定任务动作；VLM不是自由生成continuousjointactions；物体相对目标与数据扩增的共同坐标思想不等于直接承接DemoHLM/MimicGen

**实验能支持什么。** 仿真100trials整体44→92%，不是hardware92%；硬件主要qualitative且mocapobjectpose；placeobjectgoalerror本方法.227比uniform.082差，但最终task成功高，说明referenceerror与goalquality不总同向；planner根据goalerror/停稳等反馈重请求，可恢复在库内的目标错误；place容差约.3m、thirdpersoncamera给VLM，不是精密面板任务

**未覆盖条件与比较限制。** 人工库、已知动作和posegrounding；不能外推无库任意任务规划；路径arc/Dubins型限制是设计接口，不证明humanoid本体必有wheel式nonholonomicconstraint；关键帧筛选用加速度峰，不能视为一般语义压缩定理

**阅读范围。** 本地 PDF 标题核对；完整主文至结论，keyframelibrary、retargeting、multi-critic、planner和所有sim/real结果已读。

**原文定位。** keyframe提取/库与object-relative重定位；RLtracking、关键事件goalsampling；plannerfeedback/arcwaypoints；simulation100trials与objectgoalerror；hardwarecamera/MoCap及limitations

**核读订正。** 归VLMplanning＋RLtracking，而非continuousactionVLA；92%定量是仿真，真实物体定位不是纯onboardvision；少量关键帧不是自动证明policy学到全部动态技能；更高任务成功可能伴随较大referenceerror，不能用其中一个指标替代另一个

<a id="2609-23968"></a>
## 2609.23968 Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation

[Opt2VLA](../literature-map.html#paper=2609.23968) · [PDF](../papers/2609.23968_Opt2VLA_Force-Aware_Vision-Language-Action_for_Contact-Rich_Humanoid_Whole-Body_Manipulation.pdf) · [原文](https://arxiv.org/abs/2609.23968)

**原问题与接口。** 只输出位姿的 VLA 无法表达“轻擦”或“用力推”的期望力。模型联合输出运动和接触力目标，底层力控执行；语言指令可以指定力级别。 

**对应／相邻机制。** [K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)；[K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)；[K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)

**来源与版本。** **人形，真机预印本；接触力 VLA 邻接。**

**方法。** GR00T-N1.7输出手／足几何目标和独立法向力命令；TO提供关节力矩监督训练任务专用RL力控制器，再用rollout训练VLA。独立力矩token与未来力矩辅助损失。

**实验设置。** MO/FC/FCT对照；9种VLA消融，每任务30次仿真，整体joint成功82.2%；真机低层每任务30次，端到端45次。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K31 力信息进入 VLA 的位置决定它能改什么](../knowledge/network.md#k31)：邻接训练接口；力命令、训练力矩与部署反馈分离
- [K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)：手足目标和力目标的邻接接口

**平台与执行。** Digit人形，20驱动关节；邻接全身接触操作

**相对已有方法的具体改动。** GR00T-N1.7输出手／足几何目标和独立法向力命令；TO提供关节力矩监督训练任务专用RL力控制器，再用rollout训练VLA。独立力矩token与未来力矩辅助损失。

**复用部分。** Opt2Skill的全阶轨迹优化、PPO/PD、预训练GR00T、非对称训练；力反馈参考FWBC-VLA／TA-VLA。

**实验能支持什么。** MO/FC/FCT对照；9种VLA消融，每任务30次仿真，整体joint成功82.2%；真机低层每任务30次，端到端45次。

**未覆盖条件与比较限制。** 82.2%为仿真完成＋力指令＋测得力联合标准；真机报告趋势与误差，擦拭MAE7N，不是力目标精确实现。示例不能证明持续行走接触；三任务使用各自FCT。

**阅读范围。** 正文 §III–V 完整方法、结果、结论；附录标题/评价说明部分核对，未完整精读所有附录

**原文定位。** §III-A–C；§IV-B–D；Tables I–III；Appendix VI-D 对应正文评价定义

**核读订正。** 未来力矩头只作训练辅助，不是部署力矩输出；力输入、期望力输出、TO力矩监督应分别归类。

<a id="2610-24847"></a>
## 2610.24847 DiPLO: Self-distilled Diffusion Planning for Loco-manipulation

[DiPLO](../literature-map.html#paper=2610.24847) · [PDF](../papers/2610.24847_DiPLO_Self-distilled_Diffusion_Planning_for_Loco-manipulation.pdf) · [原文](https://arxiv.org/abs/2610.24847)

**原问题与接口。** 全身接触行为样本少，直接从头 RL 难学。先用人类动作重定向训练扩散规划器，RL 训练低层追踪；再用自蒸馏与策略优化减少规划器对强任务条件的依赖。 

**对应／相邻机制。** [K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K41 物体相对示范扩增与接触阶段的锚点](../knowledge/network.md#k41)

**来源与版本。** **人形，真机预印本。**

**方法。** SBTO生成可动态执行示范；扩散生成全身＋物体轨迹，参考条件教师在闭环上下文指导无参考学生；冻结RL跟踪器，用DA:PPO优化扩散规划。旋转单独用SO(3)扩散。

**实验设置。** 数据扩增、SO(3)、直接动作扩散、教师条件移除、规划／跟踪器微调消融；pick/place、kick、push/pull仿真；真机搬运同目标10/10、不同目标5/5。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K44 示范监督与闭环数据分布](../knowledge/network.md#k44)：闭环蒸馏与任务优化
- [K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)：移除参考条件与任务优化
- [K41 物体相对示范扩增与接触阶段的锚点](../knowledge/network.md#k41)：动态可行扩增
- ：存活与条件任务成功率

**平台与执行。** G1人形；动捕身体及物体；状态输入而非视觉VLA

**相对已有方法的具体改动。** SBTO生成可动态执行示范；扩散生成全身＋物体轨迹，参考条件教师在闭环上下文指导无参考学生；冻结RL跟踪器，用DA:PPO优化扩散规划。旋转单独用SO(3)扩散。

**复用部分。** DynaRetarget、PPO跟踪、扩散模型、SDPO自蒸馏启发、DA-MDP最大熵方法、对称数据扩增。

**实验能支持什么。** 数据扩增、SO(3)、直接动作扩散、教师条件移除、规划／跟踪器微调消融；pick/place、kick、push/pull仿真；真机搬运同目标10/10、不同目标5/5。

**未覆盖条件与比较限制。** Task success 在存活轨迹上计算，必须与survival同时看。DPPO-style删去部分原算法技巧，非完整公平复现；真机只15次且动捕；多技能主要分任务训练。

**阅读范围。** 正文 §III–VI 方法和主要实验完整审读；附录D/E/G训练与评价定位核查，未全面逐式复算SO(3)推导与全部附录

**原文定位。** §III-A–C；§IV-B–D；§V-A–I；Tables I–VII；Appendix E

**核读订正。** 保留原生旋转扩散与一般6D旋转表示的区别；不把生成物体未来状态直接归为视觉世界模型。

<a id="2409-04882"></a>
## 2409.04882 Learning to Open and Traverse Doors with a Legged Manipulator

[Learning to Open and Travers](../literature-map.html#paper=2409.04882) · [PDF](../papers/2409.04882_Learning_to_Open_and_Traverse_Doors_with_a_Legged_Manipulator.pdf) · [原文](https://arxiv.org/abs/2409.04882)

**原问题与接口。** 门可能推开或拉开，铰链、闭门力和开门方向事先不全知道，机器人还得在门打开后穿过狭窄门口。 

**对应／相邻机制。** [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K24 机构约束与在线交互辨识](../knowledge/network.md#k24)

**来源与版本。** **ANYmal＋臂，真机。**

**方法。** 仿真教师知道四种推拉／左右门真值，循环学生只从本体历史与门／把手位置推断响应，输出臂关节目标与基座速度，复用已有行走低层。去掉 recurrence 无法有效模仿，去掉辅助门类型分类损失影响很小，应把历史机制与显式分类分开评价。

**实验设置。** 40 真机 trials，拉门20/20、推门18/20＝95%；所有门都打开，失败在突出门口通过。MoCap 或外部相机 AprilTag 提供门／把手位置，95% 不代表纯机载自然视觉结果。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** ANYmal＋机械臂＋hook；部署门状态来自MoCap或外部相机AprilTag

**相对已有方法的具体改动。** 在四种推/拉左/右门模拟训练知道物体真值的教师，蒸馏为本体历史RNN学生，使其根据接触响应适应未直接给出的门机构；高层产生臂关节目标与基座速度，已有低层执行。

**复用部分。** 明确复用Ma等2022低层行走策略；高层输出不是全身torque；阶段奖励与door task shaping为人工设计；循环估计与teacher–student为既有技术的任务结合

**实验能支持什么。** 40真机trials：pull20/20、push18/20＝95%；门都成功打开，失败主要在突出doorway通过；门/handle位置依赖MoCap或外部cameraAprilTag，不是纯机载自然视觉门检测；去掉recurrence无法有效imitation，去辅助door type loss对模仿loss几乎无影响；不支持分类头性能关键；未unlock时push/pull循环可把自身转动误认为handle已转，直接暴露操作效果不可观测问题；PD目标裁剪currentq±0.7τlimit/Kp以限制名义关节作用，不是实际接触力上界

**未覆盖条件与比较限制。** 手工门角度30/70deg阶段与pull分区奖励；外部定位延迟影响实机；历史学生可适应门响应，但未得到未知任意机构/视觉建模能力；95%含mocap条件，不应外推纯视觉场景

**阅读范围。** 本地 PDF 标题核对；完整主文与附录 reward/观测主要段已读，附录参数表未全部逐字覆盖。

**原文定位。** §3.1/3.2：教师/循环学生、门类型与历史；§3：PD目标裁剪与部署观测；§4.3：门类型分类与recurrence消融；§4.2：真机40trials；§5.2：失败分析；附录A：阶段奖励与推拉路径

**核读订正。** 不是视觉VLA，主要是具接触历史的taskRL；RNN必要性与aux分类必要性需分别描述；UMAP可分只是投影解释，非latent因果结构证明；到达/开门与真正unlock成功确认不能混为一项

<a id="2506-16475"></a>
## 2506.16475 Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining

[Human2LocoMan](../literature-map.html#paper=2506.16475) · [PDF](../papers/2506.16475_Human2LocoMan_Learning_Versatile_Quadrupedal_Manipulation_with_Human_Pretraining.pdf) · [原文](https://arxiv.org/abs/2506.16475)

**原问题与接口。** 四足双手技能的机器人数据少，人类操作示范量大但动作结构不同。输入人类示范和少量全身机器人遥操作数据，输出视觉条件的四足操作策略。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **四足小腿装臂，真机预印本。**

**方法。** 明确复用 LocoMan 小腿操纵模块及 nullspace IK／动力学 QP。人 VR 示范先映射到共享头／腕任务空间，身体、末端与夹爪用独立 stems 编解码，共享 Transformer；换机器人时重建形态特定 stems 并 mask 缺失模态，迁移的是表征结构而非人关节控制。

**实验设置。** 单／双手玩具、鞋、scoop 和 pour 六任务，ID 每条件24次、OOD12次；人预训练改善20–40条机器人示范的条件。41.9%／79.7% 为相对增益，不是成功率百分点差。对 HPT 还同时改变视觉微调，MXT-Agg 消融更能分离模块化收益。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)：特定四足形态迁移

**平台与执行。** Go1前小腿安装两个3DoF操纵模块/夹爪；腿兼操作，非背部独立长臂

**相对已有方法的具体改动。** 将身体、末端、夹爪等可对应模态独立tokenize，共享策略主干，用人VR示范预训练，换机器人时重建形态特定stems并mask缺失模态；model-based LocoMan负责执行，使结构知识迁移与motor执行分开。

**复用部分。** LocoMan的nullspace IK/dynamicQP是明确复用执行器；human VR头/腕→共享camera/groundframe的动作对齐为数据基础；并非人关节直接复制机器人；HPT与模块Transformer为相关基线，不以作者/标题自动建立继承

**实验能支持什么。** 六实机任务：单/双手玩具、鞋、scoop、pour，ID每条件24次/OOD12次；20–40 robot示范＋200–340 human可改善较少robotdata条件，对比robot40–80示范；headline41.9/79.7为相对增益，不是percentage-point差；HPT聚合特征且冻结ResNet，而MXT还finetune视觉，直接比较有配置混杂；MXT-Agg同family更能分离modularity；作者说明validationL1与实际policy表现不总一致

**未覆盖条件与比较限制。** humanpretraining不是任意互联网视频，需VR位姿/动作格式；前腿操作与坐姿双手任务，不证明行走同时持续接触全域能力；一些模态不存在需mask，视觉/接触与机器人数据仍必要

**阅读范围。** 本地 PDF 标题核对；引言、完整核心方法、六任务与消融/泛化实验及讨论已读；背景的部分连续段与长附录未逐项覆盖。

**原文定位。** §III：sharedframe、modality stems/MXT与mask；§IV：六任务real-ID/OOD；HPT/MXT-Agg比较；控制引用LocoMan

**核读订正。** 平台不是Go1背部双臂，硬件来自calf-mounted LocoMan；head/hand representation迁移与robotmotorpolicy直接转移应区分；不能把对HPT改进全部归因modalitytokenization；relative improvement不能写成成功率提升相同percentagepoints

<a id="2507-19652"></a>
## 2507.19652 RAKOMO: Reachability-Aware K-Order Markov Path Optimization for Quadrupedal Loco-Manipulation

[RAKOMO](../literature-map.html#paper=2507.19652) · [PDF](../papers/2507.19652_RAKOMO_Reachability-Aware_K-Order_Markov_Path_Optimization_for_Quadrupedal_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2507.19652)

**原问题与接口。** 简化成身体＋臂的轨迹优化可能忽略腿关节极限，使机身抬得过高或压得过低；显式纳入全部腿关节会增加求解开销。 

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)

**来源与版本。** **四足＋臂，仅仿真。**

**方法。** 学习给定足端与机身姿态下，到腿可达区域边界的距离及其梯度，作为 KOMO 的约束／成本；规划机身和臂轨迹后由完整动力学 WBC 跟踪。

**实验设置。** HyQReal＋Kinova 臂在 Gazebo 中低处抓取、高架放置，并与普通 KOMO 比较；全程四脚固定接触，动态步态和接触序列优化留作后续。它验证姿态的腿运动学可行性，不验证行走时的臂操作精度；与 CMP 无已核实直接承接。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** HyQReal＋Kinova Gen3；仅 Gazebo 仿真，四足全程固定在地面。

**相对已有方法的具体改动。** 用多层感知机近似各腿耦合的运动学可达余量，在只显式优化身体＋臂的 KOMO 中使用其值／梯度，不加入腿变量也能保留腿运动学限制。

**复用部分。** 使用 K 阶马尔可夫路径优化（KOMO）、可达区域射线投射、神经网络近似和逆动力学 WBC。

**实验能支持什么。** 低位瓶子和高架罐子任务与不含腿余量的 KOMO 对比，展示关节限位余量和可执行末端路径。规划时间由基线 104／120 ms 增至 270／285 ms。

**未覆盖条件与比较限制。** 不优化步态／接触序列，无真机。神经网络近似没有全局保守可行性证明；文中提出可兼容商业速度接口，但未在这些商业机器人上验证。

**阅读范围。** 已阅读腿可达区域／余量与神经网络近似、KOMO 目标／约束、控制器、两个实验和结论。

**原文定位。** §II-A/B；§III；§IV-A/B；§V

**核读订正。** 这是固定站立时的腿运动学可行性，不是真实行走实验，也不是剩余施力能力指标。

<a id="2509-17582"></a>
## 2509.17582 GeCCo: A Generalist Contact-Conditioned Policy for Loco-Manipulation Skills on Legged Robots

[GeCCo](../literature-map.html#paper=2509.17582) · [PDF](../papers/2509.17582_GeCCo_--_a_Generalist_Contact-Conditioned_Policy_for_Loco-Manipulation_Skills_on_Legged_Robots.pdf) · [原文](https://arxiv.org/abs/2509.17582)

**原问题与接口。** 每换一种地形或足端操作都从头定义奖励训练策略，效率低。输入规划器指定的接触位置和机器人自身状态，输出跟踪接触计划的腿关节动作。 

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **ANYmal-D 无外挂臂，以足端接触／操作，真机预印本。**

**方法。** 随机采样足端目标区域、持续时间及步态组合，训练跟踪给定接触计划的策略；通过接触事件奖励和对称数据增强提高复用性。上层仍负责给出计划，策略本身不发现完整物体操作序列。

**实验设置。** 多地形仿真统计；真机演示步态、地形通过、足按按钮／翻箱／推桶。操作目标容差半径为 0.1 m，且其操作目标满足判据不要求实际物体接触；主要量化结果是地形通过率，不足以作为精确按钮或背载臂控制证据。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** ANYmal-D，无外挂臂，以足端操作。

**相对已有方法的具体改动。** 单个 RL 策略以足接触区域／持续时间为条件，执行多种步态和足端操作；随机接触采样与对称增广扩展固定速度追踪步态的能力。

**复用部分。** 组合 PPO／非对称 actor-critic、地形课程、对称增广以及已有接触计划／高程地图。

**实验能支持什么。** 真机包括多种步态、台阶／窄梁、足端按按钮／翻箱／推桶；仿真地形测试为 3×500 次，另消融采样／对称性／高度观测。

**未覆盖条件与比较限制。** 操作目标区域半径 0.1 m，判定操作目标满足时不要求真的地面接触；未验证精确臂操作或完整接触序列规划。除 AprilTag 按钮外，目标主要人工给定／遥操作。

**阅读范围。** 已阅读接触目标空间、采样、actor／critic、奖励、课程／对称性、全部结果和消融。

**原文定位。** §III-A–F；§IV-A–E；§V；Tables I–II

**核读订正。** 无外挂臂。定量成功率主要是地形通过率，不能当作操作任务成功率；足端追踪目标点也不等于力追踪或确认物体接触。

<a id="2512-11047"></a>
## 2512.11047 WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control

[WholeBodyVLA](../literature-map.html#paper=2512.11047) · [PDF](../papers/2512.11047_WholeBodyVLA_Towards_Unified_Latent_VLA_for_Whole-Body_Loco-Manipulation_Control.pdf) · [原文](https://arxiv.org/abs/2512.11047)

**原问题与接口。** 上身操作策略与下身走路控制分开，语言视觉任务难驱动全身移动。输入图像、文字和机器人状态；模型用全身潜动作表示生成运动与操作指令。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)

**来源与版本。** **人形，真机；Agibot 相关。**

**方法。** 机器人操作视频与人移动视频分别训练两套 VQ-VAE latent action models，VLM 预测两种 codes 后由机器人 decoder 输出双臂目标、离散移动及高度。低层 LMO 先学行走，再以臂运动扰动、精准停止及站稳要求适配操作。

**实验设置。** Agibot X2 真机搬袋／箱与推 50 kg 车。Table 2 的78%为六个子目标均值；最终袋13/25、箱17/25、车22/25，不能混成整体78%端到端成功率。连续速度对照还改变课程／奖励，不能只归因离散动作。

**阅读定位：新路线代表。** ICLR2026全身VLA代表：视觉语言到全身潜动作；人形邻接。提供明确架构，但尚不足以判断其动作接口已被广泛沿用。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：VLA 全身动作

**平台与执行。** AGIBOT X2 人形；复用低层行走策略，非四足

**相对已有方法的具体改动。** 分别从机器人操作视频和人移动视频学习两套VQ-VAE潜动作，VLM预测两种codes再用robot decoder输出双臂动作与离散行走/高度；低层LMO先训练基本行走，再在结构化臂运动扰动及精准停止要求下适配操作。

**复用部分。** DINO特征、VQ-VAE LAM、VLA/robot action decoder与低层RL行走是基础框架；潜操作与潜移动分开表示不意味着实际腿臂物理独立；低层专门训练臂扰动响应

**实验能支持什么。** Table2平均78%为六个子目标的平均；最终 bag13/25、box17/25、cart22/25，与整体78%端到端有区别；离散动作/LMO整体比默认连续速度基线平均54%更好，但接口、课程和奖励同时改变；人移动视频减轻机器人移动示范需求；机器人操作数据仍必须存在；真机推50kgcart展示全身负载执行，但无F/T峰值力/安全指标

**未覆盖条件与比较限制。** 有限离散速度指令及任务集合，不是任意连续全身运动；潜动作视觉歧义、机器人精细接触误差及停止精度仍在；印刷Eq2的tanh差分滤波对恒定指令趋零，不能未经代码核对直接当可靠实现公式

**阅读范围。** 本地 PDF 标题核对；主文完整核心方法与实验已读；附录 A/B/C 部分配置核对，未逐项覆盖全部长附录。

**原文定位。** §3.1：two LAMs、统一latent VLA与机器人decoder；§3.2 LMO：离散移动/高度、两阶段训练及smooth expression；§4.2，Table 2：子目标与终任务区分；§4.2 cart pushing真机实验及§4.4 LMO消融

**核读订正。** 不能把78%平均子目标成功写为全部任务端到端成功；不能把LMO结果仅归为离散动作本身天然更好；VLA不是直接输出全部腿关节；低层50Hz承担行走执行；潜动作同名不等同Psi0的分阶段表征训练

<a id="2603-05830"></a>
## 2603.05830 OpenHEART: Opening Heterogeneous Articulated Objects with a Legged Manipulator

[OpenHEART](../literature-map.html#paper=2603.05830) · [PDF](../papers/2603.05830_OpenHEART_Opening_Heterogeneous_Articulated_Objects_with_a_Legged_Manipulator.pdf) · [原文](https://arxiv.org/abs/2603.05830)

**原问题与接口。** 门、抽屉和柜体机构不同，直接把大图像送入 RL 难以充分利用少量数据。输入把手与面板的简化几何、自身状态和交互历史；输出全身开门／拉抽屉动作。 

**对应／相邻机制。** [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K24 机构约束与在线交互辨识](../knowledge/network.md#k24)；[K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)

**来源与版本。** **四足＋臂，真机预印本。**

**方法。** Go2＋ViperX300＋hook。SAFE 在把手／面板包围盒内部采样保留尺寸关系；ArtIEst 视觉几何分支预测把手到铰链方向，本体历史分支仅在对象已运动时监督，再按交互历史 gate 融合。初始世界包围盒由外部提供、LiDAR 更新相对位姿，不是已验证的自主视觉识别。

**实验设置。** 41 异构资产仿真 train79.35%、test79.02%；真机柜门／抽屉为定性展示，无41对象真机成功统计。全程方向误差融合较好，contact-only 本体单支 0.0606 反低于完整 0.0687，不是各阶段统一胜出。

**阅读定位：专题／应用。** 异构机构的状态／参数估计有独立价值，但以机构操作为中心，尚无跨任务下游采用证据。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K24 机构约束与在线交互辨识](../knowledge/network.md#k24)：机构特征与交互估计
- [K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)：数据处理与几何表示

**平台与执行。** Unitree Go2＋ViperX300 六自由度臂＋hook，四足＋臂

**相对已有方法的具体改动。** 将 handle/panel 包围盒内部采样点作为低维结构表示；视觉分支估计把手到铰链轴的 articulation vector，本体历史分支仅在门运动后监督，gate 融合接触前/后的信息，供高层臂/基座策略操作异构铰链/滑轨对象。

**复用部分。** PartManip资产、teacher–student RL、历史估计与分层行走控制为基础；降域差的几何表示与条件交互估计是可分离机制；不把模块名视为新的理论定理

**实验能支持什么。** 41 heterogeneous assets，仿真 train79.35%/test79.02%；no sampling test70.23%、pointcloud41.39%；全程方向误差完整0.1701对本体单支0.1827、视觉单支0.2482；contact-only本体0.0606优于完整0.0687；实机多柜门/抽屉及重新抓取主要定性，无大规模真机统计success table；初始 handle/panel world-frame包围盒由外部提供，LiDAR odometry更新robot-relative几何；未证明全自主视觉估计包围盒

**未覆盖条件与比较限制。** KL 数据处理不等式不保证任务信息保留或泛化必然提高；接触中不同机构参数可能不可辨识，使用人为统一 articulation vector 而非完整参数；系统不使用腕部力传感器，历史本体是接触相关信号而非实测外力

**阅读范围。** 本地 PDF 标题核对；主文完整，包括几何表示、机构估计、gate、策略、仿真与定性真机。

**原文定位。** §III-A SAFE；其中Remark 3.1与Eq.(1)为KL数据处理论证；§III-B ArtIEst：视觉/本体分支与belief gate；§IV，Tables II/III：阶段误差与泛化消融；§IV实机设置与cabinet/drawer示例

**核读订正。** 机械臂是 ViperX300，不是Piper；79%为仿真，不能写为跨41对象真机泛化率；融合不是每个阶段误差都最好；不能把KL下降解释成理论证明泛化改善

<a id="2610-01612"></a>
## 2610.01612 ReCo: Response-Consistent Locomotion with Policy-Aware MPC for Legged Manipulation

[ReCo](../literature-map.html#paper=2610.01612) · [PDF](../papers/2610.01612_ReCo_Response-Consistent_Locomotion_with_Policy-Aware_MPC_for_Legged_Manipulation.pdf) · [原文](https://arxiv.org/abs/2610.01612)

**原问题与接口。** MPC 假设下层走路策略会按指令移动，但真实响应随步态相位、足接触和载荷而变；即使规划器同时算底盘与手，手的世界坐标仍会偏。 

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)；[K37 训练可预测的步态，再辨识闭环响应](../knowledge/network.md#k37)

**来源与版本。** **Go2＋ARX X5 臂，真机预印本；与“走动中末端精度”直接相关。**

**方法。** 训练时让走路策略对相同指令有更一致的响应；对固定策略辨识闭环指令响应模型；MPC 再用这个模型共同规划移动指令和臂轨迹。关键不是给臂加更强的跟踪增益，而是让底盘成为规划器可预测的受控对象。

**实验设置。** 仿真末端位置／姿态 RMSE 比相应最佳基线低 28.7%／27.4%，另有响应训练／模型辨识的 2×2 消融及留出命令的预测测试。真机 8 条动捕轨迹的位置 RMSE 为 7.60 cm、姿态为 9.93°；无动捕任务的误差由机载里程计重建，未独立测量世界坐标漂移。部分基线另配外部底盘路径跟踪器，接口不同；论文未量化接触力或安全事件。

**阅读定位：新路线代表。** 步态闭环响应建模与MPC联动，针对移动时末端误差提出可检验方法；很新，不能从问题相关性推断长期影响。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)：闭环模型
- [K37 训练可预测的步态，再辨识闭环响应](../knowledge/network.md#k37)：训练响应＋辨识＋相位消融
- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：步态闭环辨识
- [K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)：低阶闭环模型
- ：预测和跟踪协议

**平台与执行。** Go2＋六自由度 X5 臂；仿真与机载实机。

**相对已有方法的具体改动。** 训练行走策略，使速度命令的瞬态与步态相位响应较一致；辨识紧凑闭环滞后／谐波模型，再由 MPC 联合优化身体命令与臂速度。

**复用部分。** 使用 PPO、Walk These Ways 步态接口、系统辨识与 OCS2 多重打靶／SQP。

**实验能支持什么。** 100 条基准轨迹，匹配信息条件的参考对比；“响应训练 × 闭环模型”2×2 消融、留出预测与错误相位反例；八条动捕实机轨迹、三种依赖里程计的操作任务。

**未覆盖条件与比较限制。** 基准参考不同于模仿基线训练轨迹；RoboDuet／Visual WBC 的身体路径由外部 pure-pursuit 给定。2×2 中模型辨识改善位置误差，但姿态 RMSE 增加；未量化任意接触力安全，动捕外的里程计误差没有独立测量。

**阅读范围。** 已阅读响应训练／模型公式、策略感知 MPC、完整基准／基线设置、2×2 与预测／相位消融和真机章节。

**原文定位。** §III-A/B/C/D；§IV-A/B/C/D/E/F；§V；Tables II/III/IV

**核读订正。** 不能将比较 RMSE 写成控制器普适排名。动捕外任务误差由机载里程计重建，不能当作独立世界坐标真值；显式力反馈也不是其核心机制。

<a id="2609-17832"></a>
## 2609.17832 Adaptive-MHE: A Sampling-Based Adaptive MPC for Legged Loco-Manipulation via Moving Horizon Estimation

[Adaptive-MHE](../literature-map.html#paper=2609.17832) · [PDF](../papers/2609.17832_Adaptive-MHE_A_Sampling-Based_Adaptive_MPC_for_Legged_Loco-Manipulation_via_Moving_Horizon_Estimation.pdf) · [原文](https://arxiv.org/abs/2609.17832)

**原问题与接口。** 推物过程中物体质量或地面摩擦改变，固定模型的 MPC 预测会偏，可能持续按原力度推而无法到达目标。 

**对应／相邻机制。** [K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)；[K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)

**来源与版本。** **Go1 以身体推箱，真机预印本；非背载臂。**

**方法。** 用近期执行轨迹与并行仿真滚动比较，在线估计未知物理参数，再把估计送回采样式 MPC；它从模型不确定性入手，和 ReCo 的“学习控制器的指令响应”是不同建模对象。

**实验设置。** 仿真比较真实参数、固定先验和在线估计；真机 Go1 无外挂臂，以身体推物，测试篮子从 3 kg 加到 4 kg 及从混凝土地面到草皮垫。它验证在线动力学适应，不验证机械臂接触操作；任务改善也不等于质量和摩擦分别被准确辨识。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)：近期交互参数估计

**平台与执行。** Unitree Go1，无外挂臂，以身体或单腿推物；真机与仿真。

**相对已有方法的具体改动。** 用滑动窗口内的物体／机器人轨迹匹配加先验正则，替代固定离线系统辨识；异步将更新的物体／地形参数送入采样 MPC。

**复用部分。** 使用 MPOPI、SPI、CMA-ES 式参数采样与 MPPI。

**实验能支持什么。** 五种仿真任务比较真实参数／固定先验／自适应估计；摩擦变化实验使用 15 对种子，实机推篮子从 3 增至 4 kg，地面从混凝土变为草坪。

**未覆盖条件与比较限制。** 需要已知／记录的物体和机器人状态，估计器更新慢于控制器；没有独立证明质量与摩擦可辨识。无外挂臂，也没有轻型机构操作证据。

**阅读范围。** 已阅读 MPOPI／SPI 预备知识、完整滑动窗口参数估计目标／控制适应、全部场景、成对消融和实机演示。

**原文定位。** §III-A/B；§IV-A/B/C；§V-A/B/C；Appendix scenario analysis

**核读订正。** 采样协方差是搜索分布协方差，不是已证明的贝叶斯后验；任务表现改善不能证明每个恢复的物理参数分别准确。

<a id="paper-58"></a>
## paper-58 QLIMB: End-to-End Whole-Body Control for Quadruped Loco-Manipulation and Balance on Complex Terrains

[QLIMB](../literature-map.html#paper=paper-58) · [原文](https://doi.org/10.1109/LRA.2026.3712638)

**原问题与接口。** 小型平台力矩余量少，复杂地形晃动使操作策略看到的状态不断扰动；只在平地练手又无法走到任务点。 

**对应／相邻机制。** [K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)

**来源与版本。** *IEEE RA-L*, 2026。**小型四足＋臂，摘要称真机；尚未取得全文。**

**方法。** 摘要称用统一策略及“潜在信念混合”机制，在行走和操作两种状态表征之间自适应融合，使身体、腿与臂在模式转换时共同调整。具体网络输入、动作输出与损失函数未见全文，不作推断。

**实验设置。** 摘要声称在复杂地形上有大量真机试验，但未给出任务种类、次数或量化对照。它是地形＋操作方向不可忽视的 2026 正式发表工作，验证强度须读全文后再判。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**未取得全文。** 保留旧卡片与候选机制标签，不作独立全文判断。新方法细节和效果须待全文回查。



<a id="paper-59"></a>
## paper-59 From Policy Actions to Whole-Body Dynamics: A Unified Projection-Based Framework for Versatile Legged Loco-Manipulation

[From Policy Actions to Whole](../literature-map.html#paper=paper-59) · [原文](https://doi.org/10.1109/LRA.2026.3734869)

**原问题与接口。** 已有 RL 行走策略给的是关节指令，而 WBC 要求的是满足动力学和接触约束的加速度、地面力与力矩；两者难以直接组合。 

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)

**来源与版本。** *IEEE RA-L*, 2026。**点足和轮足四足＋臂，摘要称真机；尚未取得全文。**

**方法。** PADP 用优化将预训练步态策略的关节动作映射到满足动力学／接触条件的全身变量，再通过一个统一 QP 加入操作任务；目标是不重训底层策略也能保留模型控制的显式约束。

**实验设置。** 摘要称点足、轮足四足平台都有仿真和真机，并相较传统 WBC 改善灵活性与精度；没有全文，暂不能核对具体任务、指标及是否边移动边接触物体。对“RL 底盘＋模型操作”接口很相关，待全文优先核实。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**未取得全文。** 保留旧卡片与候选机制标签，不作独立全文判断。新方法细节和效果须待全文回查。



<a id="2403-16535"></a>
## 2403.16535 Arm-Constrained Curriculum Learning for Loco-Manipulation of a Wheel-Legged Robot

[Arm-Constrained Curriculum L](../literature-map.html#paper=2403.16535) · [PDF](../papers/2403.16535_Arm-Constrained_Curriculum_Learning_for_Loco-Manipulation_of_a_Wheel-Legged_Robot.pdf) · [原文](https://arxiv.org/abs/2403.16535)

**原问题与接口。** 轮足底盘移动较快，臂的动作会影响平衡；把腿／轮和臂的奖励简单合在一起，训练时容易只顾其中一端。输入自身状态和任务目标，输出六个底盘关节力矩与六个臂关节位置目标，后者再由低层控制器转成力矩。 

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)

**来源与版本。** **轮足＋臂，真机；作为平台邻接方法。**

**方法。** 先行为克隆模型式全身控制器以初始化策略，再用带约束评价网络的 P3O 训练，惩罚臂关节越界、臂与底盘质心间距及碰撞。课程从接近目标的初始状态开始，随跟踪奖励改善扩大初始距离；不是先后分别训练走路、抓取两种技能。

**实验设置。** Isaac Gym 中比较课程与约束模块，真机演示开门、触碰风扇、接取移动物体等。约束降低了多数臂关节的越界次数，但 J6 反而增加，因此不是硬约束安全保证。轮足底盘结果也不能直接移到抬腿行走的四足。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**平台与执行。** Two-wheel-legchassis +AirbotPlay;6chassistorque +6armpositionactions

**相对已有方法的具体改动。** armjoint/centroid/collisioncostconstraintcritic；BCinitfromWBC；rewardawarestartergoal curriculum

**复用部分。** P3Oexistingalgorithm、PPO、WBCdemonstrations、PD/IsaacGym

**实验能支持什么。** 3basecommandscases×2024repeat simdynamictraj；curriculumandconstraintablations；realteleopdoor/fan、visionbatongrasp

**未覆盖条件与比较限制。** 轮腿自由度及contactsupport不同；costconstraints不等于hard瞬时安全；real统计较少

**阅读范围。** 正文 §III/IV/V method、CMDP前提、全部experimentablation审读；无另附录

**原文定位。** §III-A/B; §IV-A–D; §V-A–D

**核读订正。** 直出torque是chassis，arm仍position；J6violationincrease原文承认；不能写strictguarantee或所有jointsafer

<a id="2502-00835"></a>
## 2502.00835 CAIMAN: Causal Action Influence Detection for Sample-Efficient Loco-Manipulation

[CAIMAN](../literature-map.html#paper=2502.00835) · [PDF](../papers/2502.00835_CAIMAN_Causal_Action_Influence_Detection_for_Sample-Efficient_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2502.00835)

**原问题与接口。** 只给“把箱子推到目标”的稀疏奖励，机器人很难先探索出碰箱子的有效动作。上层策略输出底盘速度目标，下层已训练走路策略负责执行。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)

**来源与版本。** **无臂四足以身体推物，真机。**

**方法。** 训练一个带简化运动学先验的物体动力学模型，再从“机器人动作能否明显改变物体后续状态”形成内在探索奖励；学习到的数据继续修正这个模型。与人为设计靠近／推箱奖励相比，奖励来自物体受到动作影响的程度。

**实验设置。** 仿真单箱、绕一面墙、绕多面墙三类任务，在相同稀疏任务奖励下比较物体状态新颖度、整体状态新颖度、人工接近提示及不同动力学模型构造的探索奖励；Go2 真机推 5.5 kg 箱子，展示直推和绕障。真机物体位置来自外部动捕，论文未报告系统化的真机成功率，不能把仿真曲线当成现场鲁棒性证据。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)：非抓取探索

**平台与执行。** UnitreeGo2 bodypushing, no arm;robot/objectmocap;HL5Hz+LL50Hz

**相对已有方法的具体改动。** conditionalmutualinformationobject-action exploration；kinematicprior+learnedresidualtransitionmodel；timecorrelatednoise

**复用部分。** existingLL locomotionpolicy、PPO、CAIexistingtheory、DR

**实验能支持什么。** singleobject/wall/multiwall800eval×3seeds；heuristic,RNDfull/object,kin/learned/hybrid；cart/transferdynamics；realmocappushdemo

**未覆盖条件与比较限制。** singleobjectentity focus；groundtruthobjectstate，notvisualautonomy；simpleobjectheuristiccomparable；highlevelforce/contactselectionlimitedbybasecommand

**阅读范围。** 正文 §III/IV/V/VI完整核心方法实验审读；relatedwork因果前提阅读；无另附录

**原文定位。** §III; §IV-A/B/C; §V-A/B/C/D

**核读订正。** 因果作用度并非Bayesposterior/attention；learnedresidual不是控制torqueresidual；无arm但physicalobjloco-manipulation有可迁移探索知识

<a id="2506-07876"></a>
## 2506.07876 ReLIC: Versatile Loco-Manipulation through Flexible Interlimb Coordination

[ReLIC](../literature-map.html#paper=2506.07876) · [PDF](../papers/2506.07876_ReLIC_Versatile_Loco-Manipulation_through_Flexible_Interlimb_Coordination.pdf) · [原文](https://arxiv.org/abs/2506.07876)

**原问题与接口。** 臂够不到或推不稳时，有时应让一条前腿临时触物，其他腿维持走动；预先固定“腿只走、臂只操作”限制了能力。输入任务目标及各肢体当前分工，输出所有腿与臂关节动作。 

**对应／相邻机制。** [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **Spot＋背载臂，12 类真机任务；截至本次核查按预印本标注。**

**方法。** 任务层指定各肢体的操作／走路掩码，模型控制模块追踪操作肢体目标，RL 控制其余肢体保持移动与稳定，再按掩码合成动作。论文框架允许逆运动学或阻抗控制，但实际真机实现使用逆运动学。接触接口由用户指定接触点、方向与分工；语言接口用 GPT-4o＋SAM2 选接触点，方向仍按任务预设。肢体分工不是底层策略自主发现的。

**实验设置。** Spot＋Spot Arm 在 12 类真机任务中每类做 10 次随机化试验，论文报告平均 78.9% 成功率，并比较直接目标、接触点、语言接口及 MPC／端到端 RL 基线。任务含用腿辅助抽屉／箱体操作、持续推靠等；外部 PC 参与计算。MPC 基线原本不支持三腿走路和肢体操作，不能将其失败推广为适配这些接触模式的模型控制都无效。该工作提供可指定肢体角色的接口，但不等于 Piper 背载臂系统有同样可行的足端接触点。

**阅读定位：新路线代表。** 肢体角色在支撑／操作间重新分配，是独立控制问题，有多类真机任务；不能仅凭新意推定形成主线。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)：给定角色的混合执行

**平台与执行。** BostonDynamicsSpot+SpotArm;externalPC;IKmanipulation +RLsupportlegs

**相对已有方法的具体改动。** givenrole-mask IK/RLactionmixing；contacttimegaitfor3/4legs；calibration；contact/VLM接口

**复用部分。** IK、PPO/DR、CMAES、SAM2/GPT4o；interface directions人工定义

**实验能支持什么。** 12tasks10trials each；arm/leg10rhombusrepeatswalking；motor/gaitablations；9/12tasks>8/10

**未覆盖条件与比较限制。** 任务层给mask/target；部分语言任务；contactinterface有manualcontact/mask；MPCbaseline不支持interlimb/3leg；未闭环在线finecontact

**阅读范围。** 正文 §3/4/6全核心审读；附录E.2motorcalibration、F所有taskinterfaces、Gablations完整审读；附录reward列表选择性

**原文定位。** §3.1–3.4; §4.1–4.3; §6; AppendixE.2/F/G

**核读订正。** 非直接language-actionVLA；非自主学任意limbrole；§6arm-support-locomotion仍future；MPCfailure不能说明matchingmulticontactMPC无效

<a id="paper-63"></a>
## paper-63 Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation

[Athletic Loco-Manipulation](../literature-map.html#paper=paper-63) · [PDF](../papers/RSS_2025_Bridging_the_Sim-to-Real_Gap_for_Athletic_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2502.10894)

**原问题与接口。** 投掷、举重、拖拽需要动作目标奖励，而只靠末端轨迹模仿限制爆发力；但任务奖励又可能让 RL 利用仿真器的电机误差取巧。 

**对应／相邻机制。** [K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** RSS 2025。**四足＋臂，真机；RSS PDF为图像版；本次已核读作者arXiv 2502.10894 HTML主文与附录A–C。**

**方法。** 用实机状态转移监督仿真执行器残差模型；预训练 WBC 后对任务奖励微调，突破冻结低层的权限。对低质量球重复投掷加计时阶段变量。

**实验设置。** 真机约20m投球、10lb举升、113N拉车10m；230N只拉0.5m。执行器网络、冻结与微调低层比较。

**阅读定位：重要对照。** RSS正式论文，实机执行器辨识／模型修正支持高动态全身任务；方法与证据值得重点读，但当前未核到多支后作采用其执行器模型或训练流程。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)：冻结与微调低层的消融
- [K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)：任务回报微调
- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：从实机转移学执行器模型
- [K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)：重复投掷与计时进度
- ：执行进度与重复动作

**平台与执行。** Unitree B2＋结构加强的 Unitree Z1 Pro；全身动态操作

**相对已有方法的具体改动。** 用实机状态转移监督仿真执行器残差模型；预训练 WBC 后对任务奖励微调，突破冻结低层的权限。对低质量球重复投掷加计时阶段变量。

**复用部分。** 预训练全身 RL、任务空间参考、PPO、域随机化、历史编码。

**实验能支持什么。** 真机约20m投球、10lb举升、113N拉车10m；230N只拉0.5m。执行器网络、冻结与微调低层比较。

**未覆盖条件与比较限制。** 执行器消融固定臂以避免腿失稳，不能作为完整全身所有模块消融；参考与对象任务由人工设计；计时只表示执行过，不验证投球成功。

**阅读范围。** 作者 arXiv 2502.10894 HTML 主文、方法、实验、App A/B/C 审读；原 RSS PDF 图像文本不可提取，全文依据为作者 HTML

**原文定位。** §II-A–C；§IV-A/B；Appendix B-A；Appendix C

**核读订正。** 补充原文入口 https://arxiv.org/html/2502.10894v1；纠正旧“只核摘要”的阅读登记。

<a id="2510-11258"></a>
## 2510.11258 DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation

[DemoHLM](../literature-map.html#paper=2510.11258) · [PDF](../papers/2510.11258_DemoHLM_From_One_Demonstration_to_Generalizable_Humanoid_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2510.11258)

**原问题与接口。** 一次仿真全身示范难覆盖新的起点和物体位姿。输入示范、已知物体模型／位姿与变化的初始场景，生成仿真动作数据，再训练依赖 FoundationPose 位姿与本体的任务策略。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；；[K41 物体相对示范扩增与接触阶段的锚点](../knowledge/network.md#k41)

**来源与版本。** **人形，真机。**

**方法。** 明确扩展 MimicGen：移动／接近段按物体相对位姿变换，接触后改用接触时刻锚点，插值连接，由复用的 AMO 执行并过滤成功轨迹。它增加动态全身数据生成，不是原始 RGB／语言 VLA，也不是首次物体相对示范扩增。

**实验设置。** 10 类仿真任务扩增至5000轨迹；真机 Table 4 实际为7类各5次，成功为 lift5、press5、push4、handover4、grasp3、cabinet2、erase2。正文／结论任务数不一致，不能把10个仿真任务写成10个真机任务。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K41 物体相对示范扩增与接触阶段的锚点](../knowledge/network.md#k41)：物体相对与接触段重定向
- ：代理子任务与应用目标的区别

**平台与执行。** Unitree G1＋两自由度neck＋parallelgrippers；AMO低层

**相对已有方法的具体改动。** 一次仿真示范分成移动、接近和接触段，变换对象相对接近动作，接触后改用接触时刻锚点，插值连接并在模拟由AMO执行过滤成功轨迹；以FoundationPose/本体训练MLP/ACT/DP上层。新增全身动态执行数据，不是首次几何示范生成。

**复用部分。** MimicGen是作者明确承接的数据生成机制；AMO低层和FoundationPose已知objectmesh位姿是直接复用基础；高层taskpolicy不是rawRGB语言VLA

**实验能支持什么。** 仿真10tasks、100→5000traj可改善策略，5000rollouts×3seeds；更广初始空间生成失败增加；真机Table4为7tasks×5：lift5、press5、push4、handover4、grasp3、cabinet2、erase2；正文6/conclusion10real有数字不一致，以表为准；AppendixPressCube=handdistance<.05m，不测电气按钮激活；EraseBoard=抓橡皮左移>.2m，不测擦净面积；PushCart主要gripper抓住crossbar，非cart送到目标；Pourwater也用pose条件而非液体量；生成轨迹须由WBC真实仿真过滤，几何变换本身不保证动力学可行

**未覆盖条件与比较限制。** task名称比终止代理条件更宽；实用任务目标不能由这些success直接推定；已知mesh/pose与小样本5次硬件实验；未知对象/机构泛化未证明；印刷变换矩阵顺序存在不一致，不能未经code核对直接复制公式

**阅读范围。** 本地 PDF 标题核对；完整主文和附录 B 硬件、任务成功定义、超参数/真机表已读；其余长附录未完全逐项覆盖。

**原文定位。** 方法：分阶段object-relative/contact-time锚点；仿真示范生成/过滤与policy输入；Table4真机7tasks×5；AppendixBtasksuccessdefinitions；MimicGen直接lineage说明

**核读订正。** 真机以Table4七任务为准，不将10个仿真任务写为10个真机任务；按钮/擦除/推车演示应按真正测量的子目标描述；几何数据扩增是MimicGen扩展，不是全新generalimitationprinciple；one demonstration是在仿真VR采集，并非一次自然真机视频即可部署

<a id="2602-10106"></a>
## 2602.10106 EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration

[EgoHumanoid](../literature-map.html#paper=2602.10106) · [PDF](../papers/2602.10106_EgoHumanoid_Unlocking_In-the-Wild_Loco-Manipulation_with_Robot-Free_Egocentric_Demonstration.pdf) · [原文](https://doi.org/10.15607/RSS.2026.XXII.204)

**原问题与接口。** 机器人遥操作数据集中在实验室；人类第一视角视频覆盖多场景，却与人形机器人在视点和动作尺度上不一致。输入人类第一视角视频与少量机器人示范，输出视觉语言条件的全身动作块。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)

**来源与版本。** **人形 VLA，真机；非四足。**

**方法。** MoGe 深度将人眼图像重投影到机器人视高，再补缺失图像；以相对末端动作、离散移动和夹爪统一表示，人／机器人数据共同训练 π0.5。移除本体减少域差，但作者同时指出精细朝向变得模糊；补洞也可能产生错误几何。

**实验设置。** 四类真机任务每类100机器人＋300人示范，移动约1–5 m。78 对59、82 对31为子任务归一化分数，不是端到端成功率；所谓新机器人场景在部分人训练数据中覆盖，体现跨数据来源场景迁移。

**阅读定位：新路线代表。** RSS2026跨人类／机器人示范的全身VLA数据路线代表；人形邻接，后续采用情况仍需观察。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)：人机数据对齐

**平台与执行。** Unitree G1，人形邻接，π0.5高层＋低层行走

**相对已有方法的具体改动。** 以人的ego示范补充机器人数据，先将视角变换到机器人高度，再用相对末端动作和离散移动统一动作表述，混合人/机器人数据训练π0.5；去掉本体输入减小域差，但也牺牲精细状态信息。

**复用部分。** π0.5、MoGe重建、图像inpainting与离散行走接口为复用组件；不是人视频直接作为机器人joint action，也不是机器人数据零需求

**实验能支持什么。** 每任务100robot＋300human、四任务，移动1–5m；机器人监督始终存在；ID78对59、新机器人场景82对31是子任务归一化score，而非完整任务success rate；新机器人场景在human训练数据中覆盖，因此是跨数据来源场景迁移，不能叫完全未见全部场景；human-only导航较好但fine cart grasp5对robot15/co60，说明任务层行为与接触几何可迁移程度不同；场景多样性/视角对齐消融固定数量后也改善未见场景，支持实际对齐机制贡献

**未覆盖条件与比较限制。** 补洞可能产生错误几何，无本体输入使精细朝向模糊；全新人对象/所有机器人形态的迁移未证明；无力/触觉闭环，接触执行仍依赖低层和robot data

**阅读范围。** 本地 PDF 标题核对；主文完整方法、四任务实验及讨论；参考文献后的长附录未全部读完。

**原文定位。** 人视角MoGe深度重投影/补洞；相对末端动作＋离散移动/夹爪的共同表示；四任务ID/新机器人场景实验；无本体输入与精细朝向局限

**核读订正。** Robot-Free指人示范采集过程，不是整个训练无robot示范；78/82不能写为端到端成功率；82对31差51percentage points，不是相对提升51%；新robot domain不能不加条件地称全部训练未见domain

<a id="paper-66"></a>
## paper-66 Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

[Ψ₀](../literature-map.html#paper=paper-66) · [PDF](../papers/RSS_2026_Psi0_An_Open_Foundation_Model_Towards_Universal_Humanoid_Loco-Manipulation.pdf) · [原文](https://doi.org/10.15607/RSS.2026.XXII.021)

**原问题与接口。** 人类视频和机器人关节动作差异较大，直接共同训练一个动作模型可能学不好精细控制。与 EgoHumanoid 的对齐后共同训练形成两种并行数据路线；它们同届发表，不能画成前后继承。 

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)

**来源与版本。** **人形全身 VLA，真机。**

**方法。** 先训练 next task-space action 的 VLM 表征，再冻结骨干，以机器人数据训练 joint-space flow action expert，最后任务微调。阶段一实际同时使用 EgoDex 与 Humanoid Everyday，不是仅人数据。复用 AMO 低层，VLA 输出臂／手／torso／height／移动36维命令；RTC 用已提交动作前缀对齐异步推理。

**实验设置。** 约829小时人数据、31小时机器人数据，8类各10次。子任务评价允许失败后人工干预继续，以测后续子目标，overall仍要求全程成功；不可将干预后的子目标均值当完全自主整体率。单任务消融最后 RTC 与前一步同为9/10，主要改善连续性。

**阅读定位：新路线代表。** RSS2026人形基础动作模型代表；人类视频与机器人动作分阶段训练。正式发表支持阅读优先级，不证明已经形成下游范式。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：异步动作前缀对齐；承诺前缀与异步块对齐
- [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)：分阶段数据使用

**平台与执行。** Unitree G1＋双手；AMO低层，人形邻接

**相对已有方法的具体改动。** 先对next task-space action训练VLM表征，再冻结backbone训练500M joint-spaceflow expert，最后任务微调；训练时加入已提交动作前缀，使异步RTC能连续执行。重点是异构数据分阶段目标和部署时间一致性。

**复用部分。** AMO低层直接复用；VLA输出36维臂/手/torso/height/移动目标，而非43joint direct policy；EgoDex和HumanoidEveryday为已有数据集；RTC跟随已有动作块思路，并非首次提出；第一阶段数据同时有829hEgoDex和31hHumanoidEveryday，摘要的人/机器人完全分离叙事须按方法修正

**实验能支持什么。** 8tasks×10trials；子任务评估允许失败后人工干预继续，用于评估后续子目标，overall要求全部子任务成功；单个3subtask任务消融每配置10次：naiveDiT0、MM2、ego6、ego+HE8、post9、RTC9；RTC未额外增加观测成功次数但更连续；zero-shot背景2/10、对象4/10、空间2/10；对一般未见情况的鲁棒性有限；不同基础模型预训练量及GR00T缺少公开RTC而用sequential execution，比较不只改变architecture

**未覆盖条件与比较限制。** 高质量结构化人位姿数据不是任意互联网视频；robot数据和任务微调不可缺；少量零样本测试不能支持universal字面范围；任务动作和低层执行仍分层，未给接触力安全证明

**阅读范围。** RSS2026本地正式PDF标题核对；完整主文的三阶段训练、架构、RTC、所有结果与局限已读。未运行开源实现。

**原文定位。** §III：人/机器人task-space预训练与robot joint-space flow expert；RTC训练/执行前缀；8任务评价及subtask干预协议；ablation及zero-shot tests

**核读订正。** 阶段一不是仅人数据；阶段间是representation迁移，不是直接人joint动作复制；子目标均值及干预后续评估需注明，不能混成完全自主端到端率；RTC smoothness改善不等于该消融成功率提升；对基线的四成泛称提升不能当同数据/同推理接口的纯architecture因果证据

<a id="2607-18016"></a>
## 2607.18016 POT-VLA: Closing the Loop in Humanoid VLA with Persistent 3D Object Tokens

[POT-VLA](../literature-map.html#paper=2607.18016) · [PDF](../papers/2607.18016_POT-VLA_Closing_the_Loop_in_Humanoid_VLA.pdf) · [原文](https://arxiv.org/abs/2607.18016)

**原问题与接口。** 机器人走近、拿起、搬运、放下物体后，短动作块的模型可能忘记“同一个物体现在在哪里”；另一个独立监控器也可能用与动作模型不同的状态判断成功。 

**对应／相邻机制。** [K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)

**来源与版本。** **人形，真机预印本；与“任务状态／重复动作”问题相关。**

**方法。** 从 RGB-D 保存固定角色的8个对象槽，跨动作块刷新位置／尺度／可见性／关系，tokens 输入 GR00T N1.7 action expert。配置的 typed subtask 与稳定窗口几何谓词共享这些对象信息，将状态分为进行、完成、受阻、失败、不确定；不确定时重观察，避免仅凭已尝试认定成功。

**实验设置。** Unitree G1 八类合计80次，直接基线39/80、完整71/80；四任务消融direct15/40、verifier22/40、tokens31/40、both34/40。Being-0来自不同论文suite，不能排名。对象身份保持、短感知记忆与已完成事件应分开；回弹按钮无持久视觉变化时仍需过程／电气等结果证据，几何tokens不能自动确认。

**阅读定位：专题／应用。** 持续物体记录／结果检查的近期人形VLA方法；不是已经建立的四足全身操作范式。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)：对象空间结果验证
- ：结果验证

**平台与执行。** Unitree G1＋Dex3，RGB-D，人形邻接

**相对已有方法的具体改动。** 为当前子任务保存固定语义角色的三维对象槽，跨动作块刷新几何/可见性/关系，再将tokens注入既有action expert；用稳定窗口几何谓词将任务区分为in-progress/done/blocked/failed/uncertain，遇不确定重新观察或重试。

**复用部分。** GR00T N1.7 action expert与SAM3为复用基础；任务schema/条件可人工设置或VLM计划；verifier thresholds需配置，不是由VLA自动发现全部逻辑

**实验能支持什么。** 8任务×10＝80trials，完整71次成功，对直接VLA39次；小样本多任务结论；四任务各十次消融：direct15/40、verifieronly22、tokenonly31、both34，分离对象条件与完成验证贡献；8slots×33features包含role identity、confidence、visibility、geometry及relations，角色跨chunk保持；Being0的44/50对37/50来自另一论文不同suite引用，非同条件复现实验

**未覆盖条件与比较限制。** 几何关系可观察的任务适合验证；短按后回弹的按钮可能没有持久视觉状态；对象身份保持不等于已按成功事件确认，需要额外结果证据；深度标定/分割失误、人工阈值、接触力不可见仍影响可靠性

**阅读范围。** 本地 PDF 标题核对；主文完整，附录 A 部分schema/任务细节核对，剩余附录未逐字覆盖。

**原文定位。** typed subtask/role slots与SAM3几何；object tokens进入GR00T action expert；chunk后几何关系verifier与uncertain处理；主文80trials及40trial分解消融

**核读订正。** persistent object memory、short perception memory与task event memory应分开；不能凭Being0引用数字做跨论文性能排名；verifier是可解释但配置依赖的反馈，不是物理成功全自动oracle；不涉及四足换步的动态安全证明

<a id="paper-68"></a>
## paper-68 HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations

[HoMMI](../literature-map.html#paper=paper-68) · [PDF](../papers/RSS_2026_HoMMI_Learning_Whole-Body_Mobile_Manipulation_from_Human_Demonstrations.pdf) · [原文](https://doi.org/10.15607/RSS.2026.XXII.205)

**原问题与接口。** 腕相机缺全局视野；人的六维头pose又不适合机器人两自由度neck。输入UMI头／腕图像与任务空间示范，输出双手轨迹和3D look-at point，而非要求机器人复制完整人头pose。 

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；[K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)

**来源与版本。** **RB-Y1 双臂移动底盘，真机；非四足、非 VLA。**

**方法。** 明确扩展UMI，以ARKit共享头／腕SE(3)。头图像DINOv3＋深度位置特征转到左夹爪坐标，腕图像保留局部细节；双手由Mink差分IK/QP追踪，头look-at单独控制避免抢占手目标，timestamp对齐并丢弃已过期动作。不是UMI on Legs的直接后续算法。

**实验设置。** RB-Y1全向轮式双臂，laundry／delivery／table各20次成功90%／85%／80%；去neck为75%／55%／55%，单腕或单头更低。示范约200／166／115条、同款夹爪及精确人位姿，支持整体／局部视野与主动观察互补。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)：主动观察接口
- [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)：移动双臂采集

**平台与执行。** RB-Y1全向轮式底盘＋双臂＋6DoFtorso＋2DoFneck，轮式邻接；不是legged humanoid

**相对已有方法的具体改动。** 从机器人自由的头/腕示范学习双手任务空间动作和3D观察目标；头图像三维特征转到左夹爪坐标，腕图像保留局部信息；把人六维头pose改为低自由度neck可实现的look-at并与双手IK分开，减少观察任务抢占手部控制。

**复用部分。** UMI数据采集、ARKit、Diffusion Policy、DINOv3与Mink QP为已有组件；差分IK以手端任务、姿态/速度正则、CoM与碰撞/关节/底盘限制求运动；不是浮动基腿接触动力学WBC

**实验能支持什么。** 真机laundry200demos成功90%/20，delivery166demos85%/20，table115demos80%/20；只wrist20/15/0%，RGBonly0/45/0%，headonly0/5/0，no neck75/55/55；多任务消融支持局部/整体与主动视线互补；使用同款夹爪及ARKit测得的头/腕pose；robot/data的167/182cm高度迁移不等于任意人视频/机器人形态通用；policy10Hz、底层500Hz、IK100Hz；按timestamp对齐图像/本体并丢弃已过去动作

**未覆盖条件与比较限制。** 轮式平台没有抬腿接触切换；运动学QP结论不直接外推四足动态安全；几何对齐依赖深度/位姿准确性，双手taskspace仍需机器人模型；wrist视觉细节不是力/触觉反馈，未测接触力闭环

**阅读范围。** RSS2026本地正式PDF标题核对；完整主文，包括UMI采集、坐标表示、look-at、IK控制、同步与全部实验/消融。

**原文定位。** §IV：UMI三iPhone共享SE(3)示范采集；§V-A/C：head/wrist特征与gripper-centric三维编码；§V-B：look-at point；§VI-B：differential IK/QP；§VI-C：异步timestamp；§VII：实机实验与消融

**核读订正。** 分类应为holonomic wheeled mobile manipulator，不是四足/人形行走；学3D look-at goal，不是硬逼机器人跟完整human6Dheadpose；其对齐/执行机制与一般VLA latent video pretraining不同；成功率属于各20trials小样本，不是任意长期任务普适率

<a id="2505-06776"></a>
## 2505.06776 FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation

[FALCON](../literature-map.html#paper=2505.06776) · [PDF](../papers/2505.06776_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2505.06776)

**原问题与接口。** 开门、拉车、搬重物时，末端受到未知三维外力，臂若一味追位置会把失衡扰动传给腿。输入身体／臂状态及任务运动目标，控制器要同时输出抗扰步态与臂动作。 

**对应／相邻机制。** [K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **人形，真机预印本；大力接触邻接。**

**方法。** 下半身 RL 策略学习外力下稳定行走，上半身策略学习末端位置追踪与隐式施力补偿；联合训练时逐步增加三维末端外力，并检查关节力矩限制。重点在控制策略对未知力的适应，不是语义任务选择。

**实验设置。** 论文在 Unitree G1 与 Booster T1 真机展示负载搬运、拉车与开门，分别标注约 0–20 N、0–100 N、0–40 N 的交互范围；仿真与基线比较臂跟踪和抗扰。力级别、身体形态都与轻型 Piper 不同，不能把其大力性能直接当作轻接触安全保证。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)：真实执行器热限制
- [K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)：未知外力适应
- [K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)：接触点与准静态补偿的限制
- [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)：共享观测、独立目标
- [K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)：动作与目标分解

**平台与执行。** G1与Booster T1人形；上下身联合训练、分别优化策略

**相对已有方法的具体改动。** 上下身分别优化策略，共享全身观测；训练中施加大范围未知操作外力，以逆运动学转换手端目标为上身关节参考。

**复用部分。** PPO、域随机化、角度目标／PD、多目标奖励、任务空间跟踪。

**实验能支持什么。** 仿真负载与外力范围；真机负载行走、站立开门；上下身分工与外力训练消融。

**未覆盖条件与比较限制。** 真机开门为 stance；主要外力训练不含任意外部力矩。接触点／准静态补偿有限制；附录报告执行器热约束。

**阅读范围。** 正文完整方法、实验与结论；附录 A.1–A.6 的奖励、外力、硬件与补偿限制审读

**原文定位。** §3.1；§4；Appendix A.1–A.6

**核读订正。** 未知力适应不等于期望力精确跟踪；负载行走不能证明开门时持续移动。

<a id="2409-16048"></a>
## 2409.16048 Whole-body End-Effector Pose Tracking

[Whole-body Pose Tracking](../literature-map.html#paper=2409.16048) · [PDF](../papers/2409.16048_Whole-body_End-Effector_Pose_Tracking.pdf) · [原文](https://arxiv.org/abs/2409.16048)

**原问题与接口。** 已有末端跟踪方法或只跟踪位置，或主要覆盖身体前方、平地。本文研究如何站在不平地面上，利用身体与臂的冗余运动准确达到较大工作空间内的六维末端位姿。 输入本体状态、上一动作和当前／目标三个末端关键点在身体坐标中的位置差；不读取地形图。输出12腿＋6臂关节位置目标。行走由另一策略执行，操作策略鼓励四足接触和少量足移动。

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **ICRA 2025（作者 arXiv journal reference）；首次公开2024-09。**

**方法。** 先以臂正运动学采集10000个无自碰位姿，再加随机身体变换扩大目标范围，并利用粗地形图排除低于地面的目标。末端位姿用固定在工具上的三个不共线点表示，位置和转动统一成点距离。每4秒换目标，仅最后2秒启用到达奖励，并按超过历史最佳距离的进展补充稀疏奖励；以误差推动地形课程。复用行走策略产生的稳定初始配置，减少切换跳动。

**实验设置。** 【真机＋仿真】ANYmal-D＋DynaArm。真机动捕20个平地目标：平均2.03 cm／2.86°；楼梯测试平均2.64 cm／3.64°。仿真10000目标检验表示与附加载荷，35目标比较MPC。MPC与RL的中位误差相近，MPC均值较差主要来自少数跨身体的卡住情况。

**阅读定位：重要对照。** 位姿关键点与目标采样是可独立理解的方法，Dynamic Pick-and-Place明确借鉴关键点；目前核实的是一条局部表示继承，不是多支全身控制范式继承。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)：工具上三个不共线点统一位置与朝向误差
- [K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)：无碰目标采样、地形课程与稳定行走初态
- [K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)：延迟到达奖励与超过历史最佳距离的进展奖励

**平台与执行。** ANYmal-D＋DynaArm，18关节角度目标／PD；操作策略50 Hz

**相对已有方法的具体改动。** 先以臂正运动学采集10000个无自碰位姿，再加随机身体变换扩大目标范围，并利用粗地形图排除低于地面的目标。末端位姿用固定在工具上的三个不共线点表示，位置和转动统一成点距离。每4秒换目标，仅最后2秒启用到达奖励，并按超过历史最佳距离的进展补充稀疏奖励；以误差推动地形课程。复用行走策略产生的稳定初始配置，减少切换跳动。

**复用部分。** PPO、非对称/本体训练接口、PD、域随机化、腿式地形课程；参考UMI on Legs的位姿跟踪评测。

**实验能支持什么。** 【真机＋仿真】ANYmal-D＋DynaArm。真机动捕20个平地目标：平均2.03 cm／2.86°；楼梯测试平均2.64 cm／3.64°。仿真10000目标检验表示与附加载荷，35目标比较MPC。MPC与RL的中位误差相近，MPC均值较差主要来自少数跨身体的卡住情况。

**未覆盖条件与比较限制。** §III-G明确不包含locomotion，切换到独立行走策略后再换楼梯朝向。不能用楼梯位姿跟踪证明边走边保持物体接触。地形图仅用于训练采样；没做楼梯MPC公平对照。关键点立方体尺寸仍隐含位置／朝向权重；不是完全没有权衡。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；§III-A–H；§IV-A/B；Figs.3–6；Table I；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** §III-A–H；§IV-A/B；Figs.3–6；Table I

**核读订正。** 区分2024首次公开与ICRA2025发表；摘要2.64 cm指楼梯结果。采用作者HTML v2及下载PDF回查，未观看补充视频。

<a id="2507-04229"></a>
## 2507.04229 Efficient Learning of A Unified Policy For Whole-body Manipulation and Locomotion Skills

[PFG Unified Policy](../literature-map.html#paper=2507.04229) · [PDF](../papers/2507.04229_Efficient_Learning_of_A_Unified_Policy_For_Whole-body_Manipulation_and_Locomotion_Skills.pdf) · [原文](https://arxiv.org/abs/2507.04229)

**原问题与接口。** 只奖励最终末端误差时，RL早期难发现身体姿态改变能让臂够到目标；之后行走奖励变强，还可能放弃已学到的身体／臂配合。本文用显式运动学提示这种配合。 输入身体速度和末端位姿目标、本体与臂状态、上一动作；统一输出18关节位置目标。IK求解主要用于训练期可达性奖励及critic信息，不是在部署时替代臂动作头。

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K16 多目标奖励与多评价网络不等于多个物理机制](../knowledge/network.md#k16)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)

**来源与版本。** **IROS 2025（作者 arXiv journal reference）。**

**方法。** 把目标转到当前身体坐标，以带关节限位的阻尼最小二乘IK判断该身体姿态能否让臂达到目标。IK有解时给予可行姿态奖励，并依据解出的臂关节配置提供训练指导，使策略在到达目标之前也能从有利身体姿态获得反馈。再用三次插值生成平滑末端参考，结合速度、位姿和运动正则项训练非对称PPO。

**实验设置。** 【真机＋仿真】仿真比较AAC、AAC＋PFG、ROA、ROA＋AM；5000位姿用第60百分位误差，1000速度指令测速度跟踪。PFG位置误差8.7 cm、转动0.18 rad，不能当平均误差。真机X20＋Z1展示移动时末端升降及身体俯仰补偿，另有拾取与拖车案例。

**阅读定位：专题／应用。** IK可达姿态奖励是清楚、可检验的探索改动；尚无已核实的多支采用，属于方法专题。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)：先奖励身体使目标具有IK解，而不是只奖励末端到达
- [K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)：IK有解率是近似可达性指标，不是工作空间体积

**平台与执行。** DeepRobotics X20＋Unitree Z1；仿真另含Aliengo＋Z1

**相对已有方法的具体改动。** 把目标转到当前身体坐标，以带关节限位的阻尼最小二乘IK判断该身体姿态能否让臂达到目标。IK有解时给予可行姿态奖励，并依据解出的臂关节配置提供训练指导，使策略在到达目标之前也能从有利身体姿态获得反馈。再用三次插值生成平滑末端参考，结合速度、位姿和运动正则项训练非对称PPO。

**复用部分。** PPO、非对称actor–critic、POE运动学、阻尼最小二乘IK、三次参考插值、域随机化。

**实验能支持什么。** 【真机＋仿真】仿真比较AAC、AAC＋PFG、ROA、ROA＋AM；5000位姿用第60百分位误差，1000速度指令测速度跟踪。PFG位置误差8.7 cm、转动0.18 rad，不能当平均误差。真机X20＋Z1展示移动时末端升降及身体俯仰补偿，另有拾取与拖车案例。

**未覆盖条件与比较限制。** 所谓工作空间扩大34%基于IK有解率，不是几何体积增加34%。参考坐标随水平身体移动，不能直接理解为固定世界接触。真机没有大样本接触力／任务成功率；IK数值失败也不严格等于目标不可达。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；§III-A–D；Algorithm 1；§IV-A–C；Tables I–III；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** §III-A–D；Algorithm 1；§IV-A–C；Tables I–III

**核读订正。** AAC＋PFG优于某些末端指标，但ROA＋AM的线速度误差更低；不是全指标胜出。

<a id="2505-22974"></a>
## 2505.22974 Learning coordinated badminton skills for legged manipulators

[Badminton](../literature-map.html#paper=2505.22974) · [PDF](../papers/2505.22974_Learning_coordinated_badminton_skills_for_legged_manipulators.pdf) · [原文](https://arxiv.org/abs/2505.22974)

**原问题与接口。** 打羽毛球要求在有限剩余时间内移动到击球位置、准确挥拍，并在准备动作中持续看清飞行物体。身体转动影响相机测量，感知误差又改变应当执行的击球目标。 输入本体状态及EKF／飞行模型给出的击球位置、速度、时间等目标，统一输出腿和臂的18关节位置命令。策略100 Hz，机载视觉与预测异步60 Hz；不是RGB直接到关节的VLA。

**对应／相邻机制。** [K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)；[K37 训练可预测的步态，再辨识闭环响应](../knowledge/network.md#k37)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)；[K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)

**来源与版本。** **Science Robotics 2025；DOI 10.1126/scirobotics.adu3922。**

**方法。** 从实机移动相机数据拟合检测概率与位置误差对距离、角速度的依赖，在训练中使用该模型并运行与真机相同的EKF。策略奖励准确、按时击球，同时惩罚预测误差，使身体动作既服务击球也服务观测。非对称critic额外读取剩余击球次数等未来信息；N-P3O处理臂总电流预算，执行器模型与CMA-ES辨识改善迁移。

**实验设置。** 【真机＋仿真；强实验】机载系统在实验室、室内大厅及户外与人对打，记录10拍连续回合；真机速度最高12.06 m/s。仿真分开到点、含感知误差的截击、能耗、critic信息和电流约束消融；部分击球成功区域在真机验证。Fig.7主要约束与学习曲线来自仿真，不能全部当真机统计。

**阅读定位：专题／应用。** Science Robotics、高质量真机动态任务，包含主动感知、约束RL与执行器建模；任务特化不代表低质量，但当前无多支采用其关键模块的证据。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：未来击球信息仅给critic，部署actor不可读取
- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：腿执行器网络、臂CMA-ES辨识与预算限制分开
- [K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)：控制动作改变测量质量，EKF复用进入训练

**平台与执行。** ANYmal-D＋DynaArm＋ZED X；18关节100 Hz策略

**相对已有方法的具体改动。** 从实机移动相机数据拟合检测概率与位置误差对距离、角速度的依赖，在训练中使用该模型并运行与真机相同的EKF。策略奖励准确、按时击球，同时惩罚预测误差，使身体动作既服务击球也服务观测。非对称critic额外读取剩余击球次数等未来信息；N-P3O处理臂总电流预算，执行器模型与CMA-ES辨识改善迁移。

**复用部分。** PPO的约束变体N-P3O、非对称critic、EKF、羽毛球阻力动力学、域随机化、执行器辨识。

**实验能支持什么。** 【真机＋仿真；强实验】机载系统在实验室、室内大厅及户外与人对打，记录10拍连续回合；真机速度最高12.06 m/s。仿真分开到点、含感知误差的截击、能耗、critic信息和电流约束消融；部分击球成功区域在真机验证。Fig.7主要约束与学习曲线来自仿真，不能全部当真机统计。

**未覆盖条件与比较限制。** 橙色羽毛球以HSV检测，背景／光照影响感知模型；实测视觉延迟60–160 ms。主要平地与特定球拍／运动模型，不是通用物体操作。电流预算的训练约束和任务中的人身安全保证不同，不能以无超流证实任意接触安全。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；Results；Materials and Methods；Figs.3–7；补充实验定位；未观看视频或完整核全部补充材料；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** Results；Materials and Methods；Figs.3–7；补充实验定位；未观看视频或完整核全部补充材料

**核读订正。** 羽毛球原始HTML主文完整核读；6600/199650等为仿真统计设置，未挪作实机试验数量。

<a id="2506-16986"></a>
## 2506.16986 Learning Accurate Whole-body Throwing with High-frequency Residual Policy and Pullback Tube Acceleration

[Accurate Throwing](../literature-map.html#paper=2506.16986) · [PDF](../papers/2506.16986_Learning_Accurate_Whole-body_Throwing_with_High-frequency_Residual_Policy_and_Pullback_Tube_Acceleration.pdf) · [原文](https://arxiv.org/abs/2506.16986)

**原问题与接口。** 高速投掷不仅需要末端在释放时具有正确位置与速度，还要处理夹爪张开后物体究竟何时脱离的不确定性。单次准确跟踪目标时刻，不能保证整个可能释放窗口都能命中。 输入本体状态、投掷末端位置／速度／朝向、计时与上一动作；100 Hz策略输出18关节参考，400 Hz残差只修正臂关节位置。优化器由当前末端状态计算释放窗口内的竖向加速度参考。

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)；[K37 训练可预测的步态，再辨识闭环响应](../knowledge/network.md#k37)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)；[K45 释放时刻不确定时，怎样仍命中目标](../knowledge/network.md#k45)

**来源与版本。** **IROS 2025（作者 arXiv comments）。**

**方法。** 先学定时全身末端状态跟踪，再冻结名义策略训练高频臂残差。模型模块用抛体落点映射求当前释放状态的落点偏差，并在速度／加速度边界下求修正，让100 ms释放窗口内的末端状态接近能到达目标的状态集合。以CVXPYgen编译参数化求解，部署每2.5 ms更新；不是只在投掷之前离线规划一次。

**实验设置。** 【真机＋仿真；强实验】真机4/6 m各含两种横向偏置、每目标10次，总40次，名义基线另重复；6 m平均落点误差0.276 m，名义基线0.685 m。仿真500次组件消融及1500初态×5种子的释放窗口分析。另与25位学生比较，机器人71/125、人19/125。

**阅读定位：专题／应用。** 释放窗口鲁棒性与高频臂残差是明确贡献，有落点对照；目前针对投掷，未形成已证实的跨任务采用链。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K37 训练可预测的步态，再辨识闭环响应](../knowledge/network.md#k37)：短释放窗口下实时模型修正与高频执行
- [K45 释放时刻不确定时，怎样仍命中目标](../knowledge/network.md#k45)：释放窗口状态集合与闭环加速度修正
- [K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)：100 Hz名义全身策略＋400 Hz臂残差

**平台与执行。** ANYmal＋DynaArm＋Robotiq 2f140；100 Hz全身＋400 Hz臂残差

**相对已有方法的具体改动。** 先学定时全身末端状态跟踪，再冻结名义策略训练高频臂残差。模型模块用抛体落点映射求当前释放状态的落点偏差，并在速度／加速度边界下求修正，让100 ms释放窗口内的末端状态接近能到达目标的状态集合。以CVXPYgen编译参数化求解，部署每2.5 ms更新；不是只在投掷之前离线规划一次。

**复用部分。** 残差RL、PPO、PD、域随机化、执行器网络、已有tube acceleration的释放鲁棒性模型。

**实验能支持什么。** 【真机＋仿真；强实验】真机4/6 m各含两种横向偏置、每目标10次，总40次，名义基线另重复；6 m平均落点误差0.276 m，名义基线0.685 m。仿真500次组件消融及1500初态×5种子的释放窗口分析。另与25位学生比较，机器人71/125、人19/125。

**未覆盖条件与比较限制。** 人对比和雪团测试使用部分实现／较早训练checkpoint，不能当最终全系统消融。实机残差改善弱于仿真，作者指出可能过拟合动力学。只给竖向加速度残差；依赖近似飞行模型与对象相对末端惯量较小的假设。未证明持续行走接触。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；§III-A–D；§IV-A–G；Tables I–V；§V；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** §III-A–D；§IV-A–G；Tables I–V；§V

**核读订正。** 高频残差作用于部署臂关节参考；与Athletic作用于仿真执行器的残差不是同一变量。

<a id="2503-01474"></a>
## 2503.01474 Interactive Navigation for Legged Manipulators with Learned Arm-Pushing Controller

[Interactive Arm-Pushing](../literature-map.html#paper=2503.01474) · [PDF](../papers/2503.01474_Interactive_Navigation_for_Legged_Manipulators_with_Learned_Arm-Pushing_Controller.pdf) · [原文](https://arxiv.org/abs/2503.01474)

**原问题与接口。** 导航遇到可移动障碍时，绕行可能很远；身体推物在狭窄空间里难以找到接触位置。本文让机械臂从身体进不去的位置推开障碍，并将推物成本计入路径选择。 导航输入预建地图、已知可移动障碍及目标位置；推物策略读取物体／目标／末端状态和历史，原始输出6个臂关节增量。扩展全身执行时，由该动作产生末端参考，再交给按Visual WBC训练的低层跟踪器。

**对应／相邻机制。** [K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)；[K29 世界模型与搜索必须预测实际闭环执行](../knowledge/network.md#k29)；[K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)；[K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)

**来源与版本。** **arXiv预印本；本轮未核实正式发表。**

**方法。** Hybrid A*把预计推物时间加入路径代价，QP平滑路径；采样不会继续挡路的物体目标，靠近后调用推物。RL先奖励进入物体相对目标的背侧圆柱区域，再开启向目标推送和防倾倒奖励；分段距离课程与LSTM帮助学习不同质量／摩擦的推物。推不动时把障碍重分类为静态并重规划。

**实验设置。** 【真机＋仿真】Gazebo物体尺寸、摩擦、质量、圆柱迁移，每条件50次，成功率76–92%；两阶段奖励与两个基线比较。B2＋Z1 Pro真机8×6.8 m场景，平均58.20 s／5.42 m，对绕行113.50 s／10.70 m；演示推不动时恢复路径。

**阅读定位：专题／应用。** 复用Visual WBC解决推物导航，可展示低层跨任务使用；不是新的通用全身控制器。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)：先到物体背侧推送区，再启用移物回报
- [K23 导航终点应满足后续操作条件](../knowledge/network.md#k23)：把预计推物时间加入导航路径成本

**平台与执行。** Unitree B2＋Z1 Pro；实机动捕机器人和物体

**相对已有方法的具体改动。** Hybrid A*把预计推物时间加入路径代价，QP平滑路径；采样不会继续挡路的物体目标，靠近后调用推物。RL先奖励进入物体相对目标的背侧圆柱区域，再开启向目标推送和防倾倒奖励；分段距离课程与LSTM帮助学习不同质量／摩擦的推物。推不动时把障碍重分类为静态并重规划。

**复用部分。** Hybrid A*、OSQP、目标条件PPO、LSTM、课程、域随机化；§III-B.6明确following Visual WBC。

**实验能支持什么。** 【真机＋仿真】Gazebo物体尺寸、摩擦、质量、圆柱迁移，每条件50次，成功率76–92%；两阶段奖励与两个基线比较。B2＋Z1 Pro真机8×6.8 m场景，平均58.20 s／5.42 m，对绕行113.50 s／10.70 m；演示推不动时恢复路径。

**未覆盖条件与比较限制。** 预先知道哪些障碍可移动，真机物体与机器人状态来自动捕；不代表开放环境自主识别可推动性。无力峰值安全统计。正文25 Hz、100步与“10秒”时长说明不一致，不据此换算成功速度；全身版本缺单独量化消融。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；§III-A/B，尤其III-B.6；§IV-A/B；Tables III/IV；Fig.7；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** §III-A/B，尤其III-B.6；§IV-A/B；Tables III/IV；Fig.7

**核读订正。** 多接触指臂在推箱过程中多次换接触区域，不等于同时优化四足／臂所有接触模式。

<a id="2508-08328"></a>
## 2508.08328 Whole-Body Coordination for Dynamic Object Grasping with Legged Manipulators

[DQ-Net / DQ-Bench](../literature-map.html#paper=2508.08328) · [PDF](../papers/2508.08328_Whole-Body_Coordination_for_Dynamic_Object_Grasping_with_Legged_Manipulators.pdf) · [原文](https://arxiv.org/abs/2508.08328)

**原问题与接口。** 已有视觉抓取主要针对静止对象。持续移动的目标使当前抓取位姿很快过期，逐帧运行大型抓取网络又有计算与时序代价；需要视觉历史与稳定抓取候选共同指导接近。 特权教师读取对象位姿、速度、点云与抓取候选；部署目标学生只读腕／身体两视角各3帧mask＋depth、本体状态。高层输出末端位置／朝向增量与底盘速度命令；腿低层RL，臂由IK执行。

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)；[K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)；[K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)；[K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)；[K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)；[K44 示范监督与闭环数据分布](../knowledge/network.md#k44)

**来源与版本。** **arXiv预印本；只有仿真。**

**方法。** 先用Contact-GraspNet生成候选，在对象坐标中保存top-30抓取。教师将候选随当前对象位姿变换，并用点云／位姿query与候选key/value注意力生成抓取表示，再以RL学任务动作。冻结教师，在学生自身到达状态上用DAgger取教师标签；两视角共享CNN后分别进行时序Transformer编码，再融合动作。基准用移动小平台承载对象，分速度和2D/3D随机运动4级。

**实验设置。** 【仅仿真】43类YCB：30训练、13未见。共享低层，比较VBC、适应后的VBC-D、去候选融合、去速度、CNN学生。最难L4完整教师74.3%、学生41.0%，VBC-D学生16.0%；完成步数34.32对41.56。附录保留未见对象与学生架构对照。

**阅读定位：专题／应用。** 动态对象抓取与视觉蒸馏的专题，复用Visual WBC低层；只有仿真，尚不能作为新全身执行范式。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)：B1＋Z1仿真形态与真机部署证据不同
- [K44 示范监督与闭环数据分布](../knowledge/network.md#k44)：学生自身状态上DAgger，仍有特权信息差
- [K21 视觉策略可以学控制，也可以只学操作参考](../knowledge/network.md#k21)：特权动态抓取教师到有限视觉学生的性能差距
- [K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)：对象相对候选库、attention融合与固定候选限制
- [K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)：精确对象速度教师和有限视觉学生的可实现性缺口
- [K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)：两视角各三帧的时间模型

**平台与执行。** 仿真Unitree B1＋Z1；腿RL，臂IK

**相对已有方法的具体改动。** 先用Contact-GraspNet生成候选，在对象坐标中保存top-30抓取。教师将候选随当前对象位姿变换，并用点云／位姿query与候选key/value注意力生成抓取表示，再以RL学任务动作。冻结教师，在学生自身到达状态上用DAgger取教师标签；两视角共享CNN后分别进行时序Transformer编码，再融合动作。基准用移动小平台承载对象，分速度和2D/3D随机运动4级。

**复用部分。** Visual WBC低层／奖励、Contact-GraspNet、PointNet、PPO、DAgger、Transformer。

**实验能支持什么。** 【仅仿真】43类YCB：30训练、13未见。共享低层，比较VBC、适应后的VBC-D、去候选融合、去速度、CNN学生。最难L4完整教师74.3%、学生41.0%，VBC-D学生16.0%；完成步数34.32对41.56。附录保留未见对象与学生架构对照。

**未覆盖条件与比较限制。** 结论明确把真机部署列为未来工作，B1＋Z1是仿真形态。74.3%不是可部署视觉学生成功率。固定抓取候选与特权教师到学生的信息缺口明显；附录某些未见物体上去速度更好，不能宣称动态信息总有益。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；Proposed Method；Experiment；Table 1–3；Appendix A–F；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** Proposed Method；Experiment；Table 1–3；Appendix A–F

**核读订正。** 将用户表中Dynamic Object Grasping对应到DQ-Net；明确只有仿真。统计文本写5000 steps，不擅自换成5000独立试验。

<a id="2512-04381"></a>
## 2512.04381 FALCON: Actively Decoupled Visuomotor Policies for Loco-Manipulation with Foundation-Model-Based Coordination

[FALCON (quadruped)](../literature-map.html#paper=2512.04381) · [PDF](../papers/2512.04381_FALCON_Actively_Decoupled_Visuomotor_Policies_for_Loco-Manipulation_with_Foundation-Model-Based_Coordination.pdf) · [原文](https://arxiv.org/abs/2512.04381)

**原问题与接口。** 移动底盘需要全局视野和速度控制，机械臂需要局部视觉与准确位置控制。把这些输入和目标全部交给一个示范策略，可能难以同时学好；拆开后又需要协调身体站位与臂操作。 输入腕／头／身体RGB、本体与任务文字、人工编写的阶段提示。两个扩散策略分别输出底盘速度／高度／pitch与末端目标；低层腿RL、臂IK。动作模型10 Hz离板4090，腿RL50 Hz、内环200 Hz，臂100 Hz。

**对应／相邻机制。** [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K25 低频观测、高频反馈与时间戳](../knowledge/network.md#k25)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)；[K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)；；[K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)；[K44 示范监督与闭环数据分布](../knowledge/network.md#k44)

**来源与版本。** **NUS MARMot Lab arXiv预印本；真机。**

**方法。** 冻结CLIP编码多视角与文字，用可训练投影／浅Transformer融合为两策略共享上下文。ongoing/done阶段文字与图像相似度给出阶段概率及进度，作为动作条件。训练时以匹配示范臂／底盘动作作为正样本，打乱两子系统动作构造负样本，InfoNCE正则使共享表示包含协作关系；高层从同一批遥操作示范学习。

**实验设置。** 【真机】两类抽屉任务：走近→开抽屉→取玩具→放入，以及携物→走近→放入→关抽屉。同50条示范，CDP／ACT／LatentToM及阶段／对比损失消融，每任务15次（3初始区域各5）。正文报告Task2完整15/15，并另有子系统人工接管试验。

**阅读定位：专题／应用。** 四足双扩散策略协调与阶段语义有真机消融；目前两类抽屉任务，不宜把foundation-model命名当成基础范式证据。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)：双专用动作流由共享语义与阶段条件协调
- [K42 观察目标与操作目标可以分别控制](../knowledge/network.md#k42)：三视角为不同子策略和共享语义分别服务
- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：CLIP条件扩散动作流，区别于语义技能选择
- [K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)：ongoing/done文字相似度是阶段估计，不是物理事件证据
- ：到位、总体完成和人工接管指标分开

**平台与执行。** Go2＋AIRBOT（正文未说明型号）；3台RGB相机

**相对已有方法的具体改动。** 冻结CLIP编码多视角与文字，用可训练投影／浅Transformer融合为两策略共享上下文。ongoing/done阶段文字与图像相似度给出阶段概率及进度，作为动作条件。训练时以匹配示范臂／底盘动作作为正样本，打乱两子系统动作构造负样本，InfoNCE正则使共享表示包含协作关系；高层从同一批遥操作示范学习。

**复用部分。** CLIP、扩散行为克隆、PPO步态、IK、InfoNCE；LatentToM的共享协调表征启发。

**实验能支持什么。** 【真机】两类抽屉任务：走近→开抽屉→取玩具→放入，以及携物→走近→放入→关抽屉。同50条示范，CDP／ACT／LatentToM及阶段／对比损失消融，每任务15次（3初始区域各5）。正文报告Task2完整15/15，并另有子系统人工接管试验。

**未覆盖条件与比较限制。** 只有两任务，主要改变初始位置；阶段文字由人工构造，不是无需任务先验。对比损失有时降低OOD导航指标，并非所有环节有益。Task2的到位与整体完成判据不同；human-in-loop正文100%表述与Table III局部80/90%不一致，分开记录，不能统一称全自主100%。无接触力安全统计。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；§IV-A–D，尤其IV-D.1/2；§V-B–E；Table II/III；§VI；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** §IV-A–D，尤其IV-D.1/2；§V-B–E；Table II/III；§VI

**核读订正。** 与人形Force-Adaptive FALCON 2505.06776分开。AIRBOT型号不凭外形认定Play；无阶段标签不等于无人工阶段描述。

<a id="2511-19709"></a>
## 2511.19709 Whole-Body Inverse Dynamics MPC for Legged Loco-Manipulation

[Whole-Body ID-MPC](../literature-map.html#paper=2511.19709) · [PDF](../papers/2511.19709_Whole-Body_Inverse_Dynamics_MPC_for_Legged_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2511.19709)

**原问题与接口。** 简化身体模型规划、再由WBC执行，可能在臂重、施力大或关节接近力矩上限时产生不一致。本文研究能否把关节级动力学与接触力直接放进同一个实时预测优化。 输入估计的配置／速度、底盘速度、末端速度／力与固定步态接触时序。优化全身配置、速度、加速度、接触力及近端关节力矩，输出轨迹经500 Hz插值加PD执行；没有额外QP-WBC，不表示没有关节反馈。

**对应／相邻机制。** [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)；[K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)；[K08 柔顺控制规定受力后怎样运动](../knowledge/network.md#k08)；[K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)；[K11 抗扰裕量是在扰动发生前保留余地](../knowledge/network.md#k11)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K37 训练可预测的步态，再辨识闭环响应](../knowledge/network.md#k37)

**来源与版本。** **作者标注拟发表于RA-L MPC专题；未独立核到正式出版记录。**

**方法。** 用RNEA逆动力学作每个预测节点的路径约束，同时约束浮动基六维受力平衡、足不滑移、摩擦锥与关节运动范围。末端力／速度是给定等式条件；步态时序固定，横向落脚点可优化。Pinocchio＋CasADi建立稀疏符号问题，Fatrop利用阶段结构求解，热启动与编译加速；前细后粗的几何时间网格延长预测。

**实验设置。** 【真机＋仿真；重要边界】15节点0.56 s时域，编译后平均12.5 ms；前向模型34.2 ms，具体求解器与表达匹配不能泛称所有全阶MPC更快。B2＋Z1真机边走边拉10 kg、行走推箱、站立擦白板及低增益人机柔顺。仿真检验0.8 m/s扰动与力矩饱和，非均匀网格漂移0.4对1.2 cm/s。

**阅读定位：新路线代表。** 全阶逆动力学实时MPC是模型接口的近期代表；正式发表状态仍按作者标注记录，未核实多支采用，也未测量实际末端力精度。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)：全阶逆动力学路径约束MPC及稀疏求解
- [K07 位置准确、保持接触与力准确分别是什么](../knowledge/network.md#k07)：有力目标和接触案例，但无独立施力测量
- [K36 物体反作用力的预测与反馈](../knowledge/network.md#k36)：固定步态下接触约束、可变落脚点与行走拉载荷

**平台与执行。** B2＋Z1，末两臂关节锁定；优化80 Hz，执行500 Hz

**相对已有方法的具体改动。** 用RNEA逆动力学作每个预测节点的路径约束，同时约束浮动基六维受力平衡、足不滑移、摩擦锥与关节运动范围。末端力／速度是给定等式条件；步态时序固定，横向落脚点可优化。Pinocchio＋CasADi建立稀疏符号问题，Fatrop利用阶段结构求解，热启动与编译加速；前细后粗的几何时间网格延长预测。

**复用部分。** 刚体逆动力学、直接多重射击、MPC、Fatrop、Pinocchio、CasADi、Kalman状态估计、PD。

**实验能支持什么。** 【真机＋仿真；重要边界】15节点0.56 s时域，编译后平均12.5 ms；前向模型34.2 ms，具体求解器与表达匹配不能泛称所有全阶MPC更快。B2＋Z1真机边走边拉10 kg、行走推箱、站立擦白板及低增益人机柔顺。仿真检验0.8 m/s扰动与力矩饱和，非均匀网格漂移0.4对1.2 cm/s。

**未覆盖条件与比较限制。** 末两臂关节锁定；力矩限位仅约束前两个时间步，远端未同样约束。真机无设备测实际末端力，不能验证力目标精确跟踪。没有对象动力学或碰撞约束；离板计算、实机有20 ms求解尖峰及质量分布／执行器模型偏差。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；§IV-A–C；§V-A/B；§VI-A–D；Table I；§VII；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** §IV-A–C；§V-A/B；§VI-A–D；Table I；§VII

**核读订正。** RA-L状态保留作者原述；10 kg为拉载荷，不是把10 kg物体举起。无F/T不等于已验证无传感器力估计。

<a id="2512-18938"></a>
## 2512.18938 A Framework for Deploying Learning-based Quadruped Loco-Manipulation

[Deployment Framework](../literature-map.html#paper=2512.18938) · [PDF](../papers/2512.18938_A_Framework_for_Deploying_Learning-based_Quadruped_Loco-Manipulation.pdf) · [原文](https://arxiv.org/abs/2512.18938)

**原问题与接口。** 同一个训练策略跨模拟器或部署真机时，观测索引、控制时序和接触模型不同会使表现改变；不少已有框架缺完整可复用部署链。本文重建同一B1＋Z1接口，检查这些差异。 命令是底盘速度与末端位姿；腿RL加ROA式适应，臂阻尼IK。同ROS控制节点通过MujocoHW或QmHW接模拟器／SDK，保持接口与观测排列；遥操作给高层目标。

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)；[K37 训练可预测的步态，再辨识闭环响应](../knowledge/network.md#k37)；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **UCL／Oxford arXiv预印本；实现／复现工作。**

**方法。** 基于Visual WBC的部分开源实现扩展Isaac Gym训练→MuJoCo验证→实机ROS接口。脚接触用关节力矩经Jacobian伪逆转成粗力估计再阈值化；实机与仿真共用FSM、目标管理与PD。显式比较MuJoCo默认与高impratio接触设置，区分画面更平滑与真实抓地鲁棒性。

**实验设置。** 【真机＋仿真】低／中／高末端目标配23秒速度序列，跨模拟器报告vx／yaw RMSE。真机3种YCB物体、4高度，表4每物共10次，合计30次：WBC 26/30、默认15/30（从表计数），是遥操作取物，不是视觉自主成功。

**阅读定位：专题／应用。** 复用Visual WBC的部署工程整理，不以新控制／学习机制为主要贡献；保留作实现资料。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K09 无力传感器时，估计到的到底是什么](../knowledge/network.md#k09)：Jacobian伪逆加阈值的粗足接触信号，非充分标定的末端力估计
- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：模拟器接触阻抗调大后的平滑不等于策略鲁棒

**平台与执行。** B1＋Z1；腿12维RL，臂解析IK；ROS控制500 Hz

**相对已有方法的具体改动。** 基于Visual WBC的部分开源实现扩展Isaac Gym训练→MuJoCo验证→实机ROS接口。脚接触用关节力矩经Jacobian伪逆转成粗力估计再阈值化；实机与仿真共用FSM、目标管理与PD。显式比较MuJoCo默认与高impratio接触设置，区分画面更平滑与真实抓地鲁棒性。

**复用部分。** Visual WBC基线、ROA、PPO、解析IK、ROS/ros_control、Unitree SDK、MuJoCo接口。

**实验能支持什么。** 【真机＋仿真】低／中／高末端目标配23秒速度序列，跨模拟器报告vx／yaw RMSE。真机3种YCB物体、4高度，表4每物共10次，合计30次：WBC 26/30、默认15/30（从表计数），是遥操作取物，不是视觉自主成功。

**未覆盖条件与比较限制。** 原文称代码尚未公开、计划发布，不能仅据题名把它当现成可下载baseline。接触伪逆公式未完整区分重力／惯性偏差，不是精确外力估计证据。高impratio改善可能来自不现实的摩擦阻抗；每条件3次或地面1次，样本小。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；§3.1/3.2；§4.1–4.3；Tables 1–4；§5；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** §3.1/3.2；§4.1–4.3；Tables 1–4；§5

**核读订正。** 开放pipeline是作者目标，不直接等于已公开代码；成功率汇总为本次据表计算，不是作者报告的大样本均值。

<a id="2605-15713"></a>
## 2605.15713 Learning Dynamic Pick-and-Place for a Legged Manipulator

[Dynamic Pick-and-Place](../literature-map.html#paper=2605.15713) · [PDF](../papers/2605.15713_Learning_Dynamic_Pick-and-Place_for_a_Legged_Manipulator.pdf) · [原文](https://arxiv.org/abs/2605.15713)

**原问题与接口。** 分段抓取和搬运会产生停顿，并可能在抓取时选择不利于后续放置的身体／臂配置。本文研究移动不中断时的抓取、搬运、直立放置与撤离，并适应不同对象质量。 输入机器人／对象状态历史、抓取／放置位置、对象尺寸／类型与显式任务阶段。高层输出底盘vx/vy/yaw、height/pitch及6臂关节／二值夹爪；低层腿策略冻结。LSTM估对象质量及夹爪接触状态；真机对象／台面状态由Vicon取得。

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K06 模型精度、算力与执行偏差的取舍](../knowledge/network.md#k06)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)；[K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)；；[K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)

**来源与版本。** **RA-L 2026，11(6):7652–7659；DOI 10.1109/LRA.2026.3688092。**

**方法。** 先以异步随机关节臂运动和负载训练抗扰步态，避免只覆盖平滑末端插值；再把抓取、搬运、放置与撤臂放在单个episode中训练任务策略。六阶段奖励给当前子目标，同时保留后续回报；同步各子任务成功率驱动距离／质量／放置容差课程。历史估计器以仿真质量和接触真值监督，其输出直接给任务actor。

**实验设置。** 【真机＋仿真；强实验】仿真5种子各10000任务：86.05%对无估计81.88%、分段78.40%、潜变量85.82%；完成时间2.071 s对分段2.572 s。真机6条件各10次，总44/60=73.3%，平均4.06 s；质量最高1.3 kg，地面到1.1 m台面条件6/10。真机名义任务换VBC低层为3/10，完整9/10。

**阅读定位：专题／应用。** 完整动态抓放与显式质量／接触估计，有正式RA-L和消融；借鉴位姿关键点不说明其自己的多阶段训练已成为后作默认方案。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K38 肢体角色分配与给定角色的执行](../knowledge/network.md#k38)：同任务消融与跨论文速度宣传分别评估
- [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)：冻结抗臂扰动步态，高层控制body姿态及臂关节
- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：显式质量／接触历史估计与潜变量适应对照
- [K18 跟踪示范、调节进度与任务优化](../knowledge/network.md#k18)：完整任务回报减少分段抓取对后续放置的短视
- [K30 执行过、完成了与记忆可观测性](../knowledge/network.md#k30)：显式phase观测与阶段奖励；并非无任务状态

**平台与执行。** 自研四足＋Unitree Z1；真机Vicon状态；100 Hz腿／50 Hz任务策略

**相对已有方法的具体改动。** 先以异步随机关节臂运动和负载训练抗扰步态，避免只覆盖平滑末端插值；再把抓取、搬运、放置与撤臂放在单个episode中训练任务策略。六阶段奖励给当前子目标，同时保留后续回报；同步各子任务成功率驱动距离／质量／放置容差课程。历史估计器以仿真质量和接触真值监督，其输出直接给任务actor。

**复用部分。** Visual WBC／Walk These Ways等低层接口、PPO、非对称critic、随机臂运动、LSTM历史物理参数估计、分阶段奖励与课程。

**实验能支持什么。** 【真机＋仿真；强实验】仿真5种子各10000任务：86.05%对无估计81.88%、分段78.40%、潜变量85.82%；完成时间2.071 s对分段2.572 s。真机6条件各10次，总44/60=73.3%，平均4.06 s；质量最高1.3 kg，地面到1.1 m台面条件6/10。真机名义任务换VBC低层为3/10，完整9/10。

**未覆盖条件与比较限制。** 所谓比旧方法快10倍跨论文任务／观测／平台不同，不能作严格同条件排名。真机依赖Vicon，物体形态主要盒／圆柱；2.3 kg为训练范围，实机因夹爪安全限制只测到1.3 kg。主要失败是抓取滑落／弹出，二值夹爪不能连续调力，棱角接触仿真差异明显。

**阅读范围。** 作者全文核心方法、主要实验与限制核读；§III-A–C；§IV-A–C；Tables IV–VI；Fig.4/5；§V；未运行代码／观看视频，附录覆盖按定位记录

**原文定位。** §III-A–C；§IV-A–C；Tables IV–VI；Fig.4/5；§V

**核读订正。** 质量估计不能在未接触前从无信息历史精确知道质量；Fig.4示例在抓起后收敛。真机质量估计的独立精度没有完整评估，不能拿仿真曲线当真机标定。

<a id="2212-03238"></a>
## 2212.03238 Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior

[Walk These Ways](../literature-map.html#paper=2212.03238) · [PDF](../papers/2212.03238_Walk_These_Ways_Tuning_Robot_Control_for_Generalization_with_Multiplicity_of_Behavior.pdf) · [原文](https://proceedings.mlr.press/v205/margolis23a.html)

**原问题与接口。** 仅以平地速度跟踪定义任务，存在很多同样有效的行走方式。RL常收敛到其中一种；这种方式在新环境不合适时，往往要修改环境／奖励再训练。本文保留多种受控行为，使部署者能在不更新网络权重的情况下选择更合适的行走方式。 任务指令是身体坐标下vx、vy、yaw速度；行为向量有8维：三组足间相位、步频、身体高度、身体pitch、站宽、抬脚高度。正文§3.2报告30步关节状态、身体重力方向、命令／行为、过去动作和四足时钟历史；另从历史监督估计身体速度与摩擦。输出12关节位置偏移，经PD（kp=20、kd=0.5）执行；Go1 Edu＋Jetson TX2 NX，50 Hz。没有机械臂、末端目标、相机／地形图或接触力操作目标。

**对应／相邻机制。** [K04 关节角度、速度与力矩是不同的动作接口](../knowledge/network.md#k04)；[K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K17 首次成功、接触探索与奖励塑形](../knowledge/network.md#k17)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；；[K46 用可调行为保留同一任务的多种运动解](../knowledge/network.md#k46)

**方法。** 训练一个行为条件PPO策略，同一速度命令下按行为参数跟踪不同接触节律、姿态和抬脚轨迹。奖励分为速度任务、固定稳定／平滑项及依行为参数变化的辅助项；接触时序决定摆动时应少受力、支撑时应少滑动，Raibert启发式让足落点随速度和站宽变化，避免站宽奖励妨碍转弯。训练中途重采样命令和行为以学习切换；用四类对称步态为采样基础和速度网格课程。地形始终平坦，但随机质量、摩擦、执行器等；另用执行器网络和约20 ms动作延迟缩小sim-to-real差距。

**实验设置。** 【真机＋仿真，行走为主】Go1真机切换trot／pace／bound／pronk及2–4 Hz节律；有人调参数通过台阶／路沿、灌木和22 cm低横杆，并提前加宽站姿抗推；身体倾斜倾倒所携球属于简单身体载荷操作。平台地形和能耗对照主要为仿真：最高16 cm随机平台，三种seed，报告episode存活时间比例，trot 0.88、pace 0.87、gait-free 0.83。Table 3在1 m/s时trot机械功率24、gait-free 35，不能当作真机电池续航。Table 5也显示gait-free平地高速组合性能更好。前跳和舞蹈为预设参数序列演示，不是自动规划。

**阅读定位：底层方法基础。** 以一个行为条件策略保留多种速度跟踪解，部署时选择其泛化方式；RoboDuet、Visual WBC、Terrain-Aware WBC明确沿用步态／接触时序部分。原作是行走控制基础，不是四足＋臂操作控制器。

**主线判断的证据范围。** RoboDuet §III-B.1引用[16]的行为参数、时钟和大部分奖励；Visual WBC附录Swing/Stance phase tracking引用[59]；Terrain-Aware WBC §III的步态时序输入引用[19]。三者不等于采用完整MoB方法。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)：可解释行为条件作为高层／低层接口
- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：历史监督估计身体速度／摩擦，与人为行为条件不同
- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：平地动力学随机化＋执行器辨识，与行为选择分别作用
- [K46 用可调行为保留同一任务的多种运动解](../knowledge/network.md#k46)：MoB接口、训练和人工选择的原始方法

**平台与执行。** Go1 Edu，无臂；50 Hz关节位置目标＋PD；机载Jetson TX2 NX

**相对已有方法的具体改动。** 一个速度跟踪任务对应可调的多种行为：用8维行为输入及相应奖励训练单一PPO策略，部署时修改行为参数而不是重新训练。

**复用部分。** PPO、速度网格课程、历史监督估计、执行器网络、PD、动力学随机化、双足接触奖励启发与Raibert足落点启发；不是首次发明这些部件。

**实验能支持什么。** 正文§4／Tables 3–5及Appendix C；真机行为切换、台阶／灌木／低横杆／抗推由人调参，仿真测能耗与平台地形。平地高速表现可能降低；30步历史估计模块没有单独性能消融。

**未覆盖条件与比较限制。** 没有背载臂或末端轨迹控制；主要由人选行为；预设跳跃／舞蹈不等于自主规划。不是未经训练的任意地形或负载保证。机械功率不等于电功率；平台存活时间不是通过成功率。

**阅读范围。** 作者arXiv v1正文全部章节、Tables 1–8、Appendices A–D；PMLR正文／出版记录及作者项目／README已对照。未逐帧观看视频，未运行训练或完成全部代码审计。

**原文定位。** §2–3.4；§4.1/4.2；Tables 3–5；§5；Appendices A–D

**核读订正。** CoRL2022会议与2023论文集日期分别标明。参考论文／附录的8维行为向量；HTML转换表号有错位，定位采用归档PDF的Table 3（功率）、4（平台）、5（平地）、6–8（训练设置）；开源配置可能扩展字段，不把当前代码配置等同于原版论文。

<a id="1707-06347"></a>
## 1707.06347 Proximal Policy Optimization Algorithms

[PPO](../literature-map.html#paper=1707.06347) · [PDF](../papers/1707.06347_Proximal_Policy_Optimization_Algorithms.pdf) · [原文](https://arxiv.org/abs/1707.06347)

**原问题与接口。** 策略梯度每批数据只更新一次，样本利用率低；大步更新又容易破坏已有策略。 输入当前观测及采样动作的概率比、优势估计；输出更新后的策略参数，不规定机器人传感器或动作空间。

**对应／相邻机制。** [K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)

**方法。** 采集当前策略的轨迹后，以新旧策略动作概率比构造替代目标，并把该比值裁剪在邻近1的区间；同一批数据做多轮小批量更新。裁剪是抑制过大的策略变化，并非严格的安全约束。

**实验设置。** 【仿真基准】连续控制和Atari；原论文没有四足＋臂真机。

**阅读定位：技术基础。** Deep WBC、Visual WBC等明确采用PPO；属于优化器复用。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；大量四足论文用PPO优化策略，但其全身协调、奖励和sim-to-real机制不是PPO自带。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)：PPO裁剪概率比与多轮更新原始算法

**平台与执行。** 通用方法

**相对已有方法的具体改动。** 采集当前策略的轨迹后，以新旧策略动作概率比构造替代目标，并把该比值裁剪在邻近1的区间；同一批数据做多轮小批量更新。裁剪是抑制过大的策略变化，并非严格的安全约束。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【仿真基准】连续控制和Atari；原论文没有四足＋臂真机。

**未覆盖条件与比较限制。** 大量四足论文用PPO优化策略，但其全身协调、奖励和sim-to-real机制不是PPO自带。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="1011-0686"></a>
## 1011.0686 A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

[DAgger](../literature-map.html#paper=1011.0686) · [PDF](../papers/1011.0686_A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No-Regret_Online_Learning.pdf) · [原文](https://arxiv.org/abs/1011.0686)

**原问题与接口。** 只在专家轨迹上模仿会遇到分布偏移：学生一次动作失误后进入训练集未覆盖的状态。 学生在环境中运行产生状态；专家给这些状态标注目标动作；输出更新后的学生策略。

**对应／相邻机制。** [K44 示范监督与闭环数据分布](../knowledge/network.md#k44)；[K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)

**方法。** 反复让当前学生运行，把其实际访问的状态及专家纠正动作汇入训练集，再做监督学习。核心是训练状态分布逐步接近部署分布，而非只增加原始示范量。

**实验设置。** 【模拟与结构化预测】原文比较两个模仿学习任务及序列标注；未做四足真机。

**阅读定位：技术基础。** Visual WBC的视觉学生训练明确使用DAgger，在线向状态教师查询纠正动作。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；需要可随时查询的专家，机器人上可能需要昂贵的遥操作或仿真教师；不自动提供安全访问状态的机制。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K44 示范监督与闭环数据分布](../knowledge/network.md#k44)：DAgger学生到达状态上的专家标注
- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：在线状态分布聚合的教师查询方法

**平台与执行。** 通用方法

**相对已有方法的具体改动。** 反复让当前学生运行，把其实际访问的状态及专家纠正动作汇入训练集，再做监督学习。核心是训练状态分布逐步接近部署分布，而非只增加原始示范量。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【模拟与结构化预测】原文比较两个模仿学习任务及序列标注；未做四足真机。

**未覆盖条件与比较限制。** 需要可随时查询的专家，机器人上可能需要昂贵的遥操作或仿真教师；不自动提供安全访问状态的机制。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2108-10470"></a>
## 2108.10470 Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning

[Isaac Gym](../literature-map.html#paper=2108.10470) · [PDF](../papers/2108.10470_Isaac_Gym_High_Performance_GPU-Based_Physics_Simulation_For_Robot_Learning.pdf) · [原文](https://arxiv.org/abs/2108.10470)

**原问题与接口。** CPU物理仿真与GPU神经网络往返传输限制大批量机器人RL训练速度。 并行环境在GPU上推进，直接向GPU策略／优化器提供状态、奖励和训练数据。

**对应／相邻机制。** [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)

**方法。** 把物理仿真、张量表示及RL流水线放在GPU，批量并行模拟机器人；这是训练基础设施，不是步态奖励或操作算法。

**实验设置。** 【仿真基准＋真机迁移例证】大规模并行仿真与训练吞吐；§6.1.4还报告ANYmal崎岖地形行走实机迁移，另有TriFinger迁移。没有四足＋臂操作实机对比。

**阅读定位：技术基础。** UMI on Legs和DQ-Net等原文明确用Isaac Gym；引用它不能证明沿用同一奖励或控制器。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；仿真吞吐提升不保证动力学逼真或实机成功；具体仿真平台和接触模型仍需逐篇核查。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：GPU并行仿真工具与ANYmal迁移例证

**平台与执行。** 跨平台仿真工具

**相对已有方法的具体改动。** 把物理仿真、张量表示及RL流水线放在GPU，批量并行模拟机器人；这是训练基础设施，不是步态奖励或操作算法。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【仿真基准＋真机迁移例证】大规模并行仿真与训练吞吐；§6.1.4还报告ANYmal崎岖地形行走实机迁移，另有TriFinger迁移。没有四足＋臂操作实机对比。

**未覆盖条件与比较限制。** 仿真吞吐提升不保证动力学逼真或实机成功；具体仿真平台和接触模型仍需逐篇核查。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2107-04034"></a>
## 2107.04034 RMA: Rapid Motor Adaptation for Legged Robots

[RMA](../literature-map.html#paper=2107.04034) · [PDF](../papers/2107.04034_RMA_Rapid_Motor_Adaptation_for_Legged_Robots.pdf) · [原文](https://arxiv.org/abs/2107.04034)

**原问题与接口。** 只在仿真训练的腿式策略到真实地形后，摩擦、载荷、地面软硬无法直接观测且会变化。 第一阶段策略输入本体状态、速度指令和由特权环境因素编码的z；第二阶段适应器以机器人近期本体历史预测z，真机只使用历史预测值。策略输出关节目标。

**对应／相邻机制。** [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)

**方法。** 先在随机环境参数和地形中联合训练环境编码器与行走策略；再冻结它们，用仿真标签监督历史适应器模仿z。部署时适应器从过去动作和反馈实时更新潜表示，不再读取特权环境参数。

**实验设置。** 【真机＋仿真】Unitree A1在沙、泥、碎石、草地和楼梯等条件行走；正文报告部分任务的成功率，且无实机微调。

**阅读定位：技术基础。** Deep WBC §2.2/实验将RMA作为两阶段teacher-student对照，并针对潜表示训练方式提出ROA。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；原作没有机械臂或物体操作；两阶段适应训练的目标与后续Deep WBC的联合ROA安排不同。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：两阶段环境编码器和历史适应器原始方法
- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：历史适应处理未知地形／载荷

**平台与执行。** 四足行走（无臂）

**相对已有方法的具体改动。** 先在随机环境参数和地形中联合训练环境编码器与行走策略；再冻结它们，用仿真标签监督历史适应器模仿z。部署时适应器从过去动作和反馈实时更新潜表示，不再读取特权环境参数。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【真机＋仿真】Unitree A1在沙、泥、碎石、草地和楼梯等条件行走；正文报告部分任务的成功率，且无实机微调。

**未覆盖条件与比较限制。** 原作没有机械臂或物体操作；两阶段适应训练的目标与后续Deep WBC的联合ROA安排不同。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2109-11978"></a>
## 2109.11978 Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning

[Learning to Walk in Minutes](../literature-map.html#paper=2109.11978) · [PDF](../papers/2109.11978_Learning_to_Walk_in_Minutes_Using_Massively_Parallel_Deep_Reinforcement_Learning.pdf) · [原文](https://arxiv.org/abs/2109.11978)

**原问题与接口。** 传统CPU串行训练四足RL过慢，地形难度课程与大量并行机器人训练不易配合。 大规模GPU模拟ANYmal环境，PPO学习本体观测和速度指令到关节动作的策略。

**对应／相邻机制。** [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)

**方法。** 把数千环境并行推进，调整PPO在大批量数据下的实现，并引入按机器人表现升降的地形课程；公开legged_gym训练配置。

**实验设置。** 【真机＋仿真】平地约4分钟、复杂地形约20分钟训练ANYmal策略并迁移真机；训练时长是所述硬件和任务设置，不可外推到带臂任务。

**阅读定位：技术基础。** Deep WBC、UMI on Legs、Visual WBC均引用该工作作并行腿式RL基础；具体软件复用要另核代码／设置。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；行走训练速度突破不等于本文设计了loco-manipulation的奖励、接触安排或手端控制。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)：大规模并行PPO与任务课程
- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：大规模并行训练及地形课程

**平台与执行。** 四足行走（无臂）

**相对已有方法的具体改动。** 把数千环境并行推进，调整PPO在大批量数据下的实现，并引入按机器人表现升降的地形课程；公开legged_gym训练配置。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【真机＋仿真】平地约4分钟、复杂地形约20分钟训练ANYmal策略并迁移真机；训练时长是所述硬件和任务设置，不可外推到带臂任务。

**未覆盖条件与比较限制。** 行走训练速度突破不等于本文设计了loco-manipulation的奖励、接触安排或手端控制。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2010-11251"></a>
## 2010.11251 Learning Quadrupedal Locomotion over Challenging Terrain

[Challenging Terrain](../literature-map.html#paper=2010.11251) · [PDF](../papers/2010.11251_Learning_Quadrupedal_Locomotion_over_Challenging_Terrain.pdf) · [原文](https://arxiv.org/abs/2010.11251)

**原问题与接口。** 盲走控制器在真实崎岖、松软地形上既要避免足滑移，也要跨仿真到真实的执行器误差。 ANYmal的关节与惯性本体观测和速度指令进入策略，输出关节动作；原作部署策略不依赖前向视觉图。

**对应／相邻机制。** [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)

**方法。** 用多难度地形课程、执行器模型及动力学随机化训练本体感知策略；课程逐步暴露台阶、斜坡和不规则足支撑。

**实验设置。** 【真机＋仿真】ANYmal在泥、雪、碎石等真实地形行走；Science Robotics 2020。

**阅读定位：技术基础。** Deep WBC及多篇四足操作论文引用其真实地形行走结果；目前库中未核到其完整控制器被操作论文复制。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；经常被后作当作腿式地形背景引用，不能据此画成它们的具体策略、奖励或地形编码直接继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)：执行器模型、课程和域随机的行走例证

**平台与执行。** 四足行走（无臂）

**相对已有方法的具体改动。** 用多难度地形课程、执行器模型及动力学随机化训练本体感知策略；课程逐步暴露台阶、斜坡和不规则足支撑。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【真机＋仿真】ANYmal在泥、雪、碎石等真实地形行走；Science Robotics 2020。

**未覆盖条件与比较限制。** 经常被后作当作腿式地形背景引用，不能据此画成它们的具体策略、奖励或地形编码直接继承。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2201-08117"></a>
## 2201.08117 Learning robust perceptive locomotion for quadrupedal robots in the wild

[Perceptive Locomotion](../literature-map.html#paper=2201.08117) · [PDF](../papers/2201.08117_Learning_robust_perceptive_locomotion_for_quadrupedal_robots_in_the_wild.pdf) · [原文](https://arxiv.org/abs/2201.08117)

**原问题与接口。** 仅靠足接触之后才知道障碍的本体行走，难以提前选择落脚和调整身体；高度图也可能噪声大或过时。 本体历史与外感地形测量进入注意力式循环编码器，再条件化行走策略；输出腿动作，无臂末端操作目标。

**对应／相邻机制。** [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)

**方法。** 端到端训练注意力式循环编码器融合本体与外感地形信息，让策略在地形视觉失准时更多依靠身体反馈，而非手工规定两种传感的固定权重；训练包含感知退化与复杂地形。

**实验设置。** 【真机＋仿真】ANYmal在户外多季节复杂地形行走，并报告阿尔卑斯山区长时徒步；Science Robotics 2022。

**阅读定位：技术基础。** Guided RL、RAMBO及Terrain-aware WBC等引用；当前直接算法继承证据不足。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；高频被四足操作论文引用作地形感知背景，但不等于它们复用了相同视觉融合器。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：注意力式循环融合本体与地形测量
- [K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)：视觉与本体信息融合的行走场景

**平台与执行。** 四足行走（无臂）

**相对已有方法的具体改动。** 端到端训练注意力式循环编码器融合本体与外感地形信息，让策略在地形视觉失准时更多依靠身体反馈，而非手工规定两种传感的固定权重；训练包含感知退化与复杂地形。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【真机＋仿真】ANYmal在户外多季节复杂地形行走，并报告阿尔卑斯山区长时徒步；Science Robotics 2022。

**未覆盖条件与比较限制。** 高频被四足操作论文引用作地形感知背景，但不等于它们复用了相同视觉融合器。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2103-00946"></a>
## 2103.00946 A Unified MPC Framework for Whole-Body Dynamic Locomotion and Manipulation

[Unified MPC 2021](../literature-map.html#paper=2103.00946) · [PDF](../papers/2103.00946_A_Unified_MPC_Framework_for_Whole-Body_Dynamic_Locomotion_and_Manipulation.pdf) · [原文](https://arxiv.org/abs/2103.00946)

**原问题与接口。** 行走与臂操作若分别规划，难同时处理身体、足、手与被操作物体的动力学耦合。 给定步态／手接触时序及操作目标，MPC滚动优化身体、足、手和物体运动；低层全身控制跟踪优化结果。

**对应／相邻机制。** [K01 浮动基、足接触与手端运动的耦合](../knowledge/network.md#k01)；[K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)；[K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)

**方法。** 把机器人质心动力学与被操作物体动力学放入同一多接触最优控制问题，接触时序由预设切换约束编码；在线反复求解有限时域。与2023 ETH工作相比，本文不搜索离散接触顺序。

**实验设置。** 【四足＋臂真机】ANYmal带臂完成身体／手端位姿跟踪和阻力较大的门推拉；RA-L 2021。

**阅读定位：技术基础。** ETH同作者2023多接触工作将接触顺序搜索加入这一路线；2025臂动力学NMPC正文明确以本工作为先例。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；预定义接触模式和物体模型限制新场景；MPC实时性不等于未知机构、摩擦、抓取点均可自动估计。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K05 轨迹规划、MPC 与 WBC 的决策范围](../knowledge/network.md#k05)：预设接触时序的统一机器人—物体MPC
- [K10 离散接触模式与连续运动需要共同安排](../knowledge/network.md#k10)：给定模式的切换系统；与后续接触搜索区分

**平台与执行。** 四足＋臂

**相对已有方法的具体改动。** 把机器人质心动力学与被操作物体动力学放入同一多接触最优控制问题，接触时序由预设切换约束编码；在线反复求解有限时域。与2023 ETH工作相比，本文不搜索离散接触顺序。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【四足＋臂真机】ANYmal带臂完成身体／手端位姿跟踪和阻力较大的门推拉；RA-L 2021。

**未覆盖条件与比较限制。** 预定义接触模式和物体模型限制新场景；MPC实时性不等于未知机构、摩擦、抓取点均可自动估计。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2402-10329"></a>
## 2402.10329 Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots

[Original UMI](../literature-map.html#paper=2402.10329) · [PDF](../papers/2402.10329_Universal_Manipulation_Interface_In-The-Wild_Robot_Teaching_Without_In-The-Wild_Robots.pdf) · [原文](https://arxiv.org/abs/2402.10329)

**原问题与接口。** 在实际机器人上逐任务遥操作采集数据昂贵，纯人类视频与机器人动作空间又不一致。 人手持带相机和夹爪的工具采示范；从图像与追踪估计手端相对轨迹、夹爪动作，部署时给机器人同类相机观察和相对动作接口。

**对应／相邻机制。** [K02 参考坐标系决定控制器究竟在保持什么](../knowledge/network.md#k02)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)

**方法。** 用便携夹爪收集原环境示范，配广角腕视角、姿态追踪和动作过滤；以相对轨迹及推理延迟匹配降低跨本体偏差，训练视觉动作策略。UMI本身是数据／动作接口体系，不是四足全身控制器。

**实验设置。** 【真机】在不同机器人上做动态、双手、精细和长时操作并测试未见环境／物体；RSS 2024。

**阅读定位：技术基础。** UMI on Legs明确采用该手持示范数据与任务坐标轨迹；HoMMI等扩展采集接口。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；部署默认已有可追踪手端目标的机器人；足支撑和身体补偿由后续UMI on Legs处理。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)：手持示范到相对末端轨迹
- [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)：手持示范跨本体相对动作与延迟匹配

**平台与执行。** 固定臂操作／数据接口

**相对已有方法的具体改动。** 用便携夹爪收集原环境示范，配广角腕视角、姿态追踪和动作过滤；以相对轨迹及推理延迟匹配降低跨本体偏差，训练视觉动作策略。UMI本身是数据／动作接口体系，不是四足全身控制器。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【真机】在不同机器人上做动态、双手、精细和长时操作并测试未见环境／物体；RSS 2024。

**未覆盖条件与比较限制。** 部署默认已有可追踪手端目标的机器人；足支撑和身体补偿由后续UMI on Legs处理。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2303-04137"></a>
## 2303.04137 Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

[Diffusion Policy](../literature-map.html#paper=2303.04137) · [PDF](../papers/2303.04137_Diffusion_Policy_Visuomotor_Policy_Learning_via_Action_Diffusion.pdf) · [原文](https://arxiv.org/abs/2303.04137)

**原问题与接口。** 示范数据中同一观察可能对应多种合理动作，单点回归容易给出不合适的平均动作。 视觉与本体观察条件化多步动作序列；推理时迭代去噪生成序列，执行前一段并重新观察。

**对应／相邻机制。** [K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)；[K44 示范监督与闭环数据分布](../knowledge/network.md#k44)

**方法。** 将动作轨迹看成条件扩散生成变量，用示范轨迹训练去噪网络；时间序列动作预测与滚动执行保持闭环。论文比较卷积和Transformer去噪结构。

**实验设置。** 【多任务仿真＋真机操作】15类操作基准，含多模态动作和视觉反馈任务；其汇总提升应保留基线与任务口径。

**阅读定位：技术基础。** UMI on Legs §3.1明确采用U-Net diffusion policy及DDIM，延长未来动作窗口给WBC。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；原论文没有四足运动、足接触和手端跟踪控制；动作生成质量与低层执行能力须分别衡量。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K44 示范监督与闭环数据分布](../knowledge/network.md#k44)：示范动作的条件扩散分布
- [K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)：条件扩散生成未来动作序列
- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：扩散动作序列滚动执行

**平台与执行。** 固定臂操作／动作生成

**相对已有方法的具体改动。** 将动作轨迹看成条件扩散生成变量，用示范轨迹训练去噪网络；时间序列动作预测与滚动执行保持闭环。论文比较卷积和Transformer去噪结构。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【多任务仿真＋真机操作】15类操作基准，含多模态动作和视觉反馈任务；其汇总提升应保留基线与任务口径。

**未覆盖条件与比较限制。** 原论文没有四足运动、足接触和手端跟踪控制；动作生成质量与低层执行能力须分别衡量。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2304-13705"></a>
## 2304.13705 Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

[ACT / ALOHA](../literature-map.html#paper=2304.13705) · [PDF](../papers/2304.13705_Learning_Fine-Grained_Bimanual_Manipulation_with_Low-Cost_Hardware.pdf) · [原文](https://arxiv.org/abs/2304.13705)

**原问题与接口。** 低成本双臂的细操作会因单步模仿误差不断积累，演示中的停顿也使单步监督不稳定。 多相机与关节状态输入Transformer，输出未来一段双臂关节目标；执行时可对相邻动作块做时间集成。

**对应／相邻机制。** [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)；[K44 示范监督与闭环数据分布](../knowledge/network.md#k44)

**方法。** ACT用条件潜变量模型预测动作块而非单步动作，并使用时间集成平滑当前动作；论文同时提供可遥操作的低成本双臂ALOHA硬件。

**实验设置。** 【真机】六类精细双臂任务，含开调味杯和插电池；文中在两个任务报告约80–90%成功率，依各任务训练数据量而异；RSS 2023。

**阅读定位：技术基础。** WildLMa技能部分明确building upon ACT；Mobile ALOHA直接扩展ALOHA硬件与示范范式到轮式底盘。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；原作固定双臂；单独引用ACT不表示已经解决底盘同步移动和接触稳定性。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K44 示范监督与闭环数据分布](../knowledge/network.md#k44)：动作块及时间集成处理模仿执行
- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：ACT动作块与时间集成

**平台与执行。** 固定双臂操作

**相对已有方法的具体改动。** ACT用条件潜变量模型预测动作块而非单步动作，并使用时间集成平滑当前动作；论文同时提供可遥操作的低成本双臂ALOHA硬件。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【真机】六类精细双臂任务，含开调味杯和插电池；文中在两个任务报告约80–90%成功率，依各任务训练数据量而异；RSS 2023。

**未覆盖条件与比较限制。** 原作固定双臂；单独引用ACT不表示已经解决底盘同步移动和接触稳定性。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2401-02117"></a>
## 2401.02117 Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation

[Mobile ALOHA](../literature-map.html#paper=2401.02117) · [PDF](../papers/2401.02117_Mobile_ALOHA_Learning_Bimanual_Mobile_Manipulation_with_Low-Cost_Whole-Body_Teleoperation.pdf) · [原文](https://arxiv.org/abs/2401.02117)

**原问题与接口。** 固定桌面示范不能直接覆盖开柜、进电梯、搬运等需底盘与双臂同时运动的任务。 全身遥操作采相机、双臂状态、底盘运动；模仿策略联合输出双臂关节与底盘线／角速度。

**对应／相邻机制。** [K13 统一策略、协作策略与模型分工](../knowledge/network.md#k13)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；[K44 示范监督与闭环数据分布](../knowledge/network.md#k44)

**方法。** 把ALOHA双臂遥操作装到移动底盘，收集50段／任务左右的全身示范；用静态ALOHA数据协同训练移动任务，检验固定操作数据能否提高数据效率。

**实验设置。** 【轮式真机】开双门壁柜、把锅放入柜中、使用电梯及厨房任务；部分任务协同训练成功率明显改善，原文“up to 90%”是相对具体设置。

**阅读定位：技术基础。** 原作直接承接ALOHA；DECOWAM等拿它作移动示范先例，而非声称继承其控制算法。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；轮式底盘没有四足起步抬腿与足接触切换；多数本库后作将其作系统／数据背景引用，未核到直接沿用其整套训练。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)：轮式底盘＋双臂同步遥操作采集

**平台与执行。** 轮式双臂

**相对已有方法的具体改动。** 把ALOHA双臂遥操作装到移动底盘，收集50段／任务左右的全身示范；用静态ALOHA数据协同训练移动任务，检验固定操作数据能否提高数据效率。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【轮式真机】开双门壁柜、把锅放入柜中、使用电梯及厨房任务；部分任务协同训练成功率明显改善，原文“up to 90%”是相对具体设置。

**未覆盖条件与比较限制。** 轮式底盘没有四足起步抬腿与足接触切换；多数本库后作将其作系统／数据背景引用，未核到直接沿用其整套训练。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2204-01691"></a>
## 2204.01691 Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

[SayCan](../literature-map.html#paper=2204.01691) · [PDF](../papers/2204.01691_Do_As_I_Can_Not_As_I_Say_Grounding_Language_in_Robotic_Affordances.pdf) · [原文](https://arxiv.org/abs/2204.01691)

**原问题与接口。** 语言模型知道步骤名称，却不知道机器人当前是否能实际完成某一步。 输入用户语言命令及当前候选技能；语言模型提供任务相关性，技能价值函数估计可行性，选技能循环执行。

**对应／相邻机制。** [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)

**方法。** 逐步给每个候选技能计算“语言上合理”和“当前可执行”的组合分数，由低层已训练技能执行；失败或状态改变后可重新评分。它是技能选择接口，不输出连续四足关节动作。

**实验设置。** 【移动机械臂真机】长程家居式语言指令，展示可行性评分对任务完成的影响；CoRL 2022论文集2023。

**阅读定位：技术基础。** WildLMa、UMI on Legs等引用作语言／技能背景；不登记直接承接。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；技能库的覆盖范围决定可执行步骤；本库多数引用仅作语言规划背景，WildLMa未证实直接采用SayCan的评分公式。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：语言相关性与技能可行性联合选择

**平台与执行。** 轮式移动机械臂

**相对已有方法的具体改动。** 逐步给每个候选技能计算“语言上合理”和“当前可执行”的组合分数，由低层已训练技能执行；失败或状态改变后可重新评分。它是技能选择接口，不输出连续四足关节动作。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【移动机械臂真机】长程家居式语言指令，展示可行性评分对任务完成的影响；CoRL 2022论文集2023。

**未覆盖条件与比较限制。** 技能库的覆盖范围决定可执行步骤；本库多数引用仅作语言规划背景，WildLMa未证实直接采用SayCan的评分公式。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2103-14127"></a>
## 2103.14127 Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

[Contact-GraspNet](../literature-map.html#paper=2103.14127) · [PDF](../papers/2103.14127_Contact-GraspNet_Efficient_6-DoF_Grasp_Generation_in_Cluttered_Scenes.pdf) · [原文](https://arxiv.org/abs/2103.14127)

**原问题与接口。** 杂乱场景中直接从深度图找有效六自由度抓取姿态，传统逐候选采样和验证较慢。 输入场景深度点云，输出多个候选夹爪抓取位姿和评分；下游再选择与机器人可达性兼容的抓取。

**对应／相邻机制。** [K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)

**方法。** 把局部接触位置和抓取姿态预测结合，在点云中密集产生并筛选6D抓取；它给出候选物体接触位姿，不控制移动底盘。

**实验设置。** 【抓取基准＋真机夹爪】在杂乱物体场景比较抓取候选质量与执行；ICRA 2021。

**阅读定位：技术基础。** DQ-Net正文明确用预训练Contact-GraspNet生成抓取候选，再做全身动态抓取选择。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；检测到好抓取不等于四足全身能在运动中稳定达到；底盘站位和身体姿态须另规划。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)：点云接触点条件的6D候选抓取

**平台与执行。** 通用机械臂

**相对已有方法的具体改动。** 把局部接触位置和抓取姿态预测结合，在点云中密集产生并筛选6D抓取；它给出候选物体接触位姿，不控制移动底盘。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【抓取基准＋真机夹爪】在杂乱物体场景比较抓取候选质量与执行；ICRA 2021。

**未覆盖条件与比较限制。** 检测到好抓取不等于四足全身能在运动中稳定达到；底盘站位和身体姿态须另规划。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2406-09246"></a>
## 2406.09246 OpenVLA: An Open-Source Vision-Language-Action Model

[OpenVLA](../literature-map.html#paper=2406.09246) · [PDF](../papers/2406.09246_OpenVLA_An_Open-Source_Vision-Language-Action_Model.pdf) · [原文](https://arxiv.org/abs/2406.09246)

**原问题与接口。** 操作策略依赖单任务／单机器人的数据，视觉语言模型又不能直接输出可执行动作。 输入图像和语言指令，输出离散化后的机器人动作token；微调后适配不同机械臂。

**对应／相邻机制。** [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)

**方法。** 在预训练视觉语言骨干上用Open X-Embodiment的大量机器人轨迹训练动作预测，公开模型权重／代码与适配流程。动作token化是其接口特点，未解决四足足接触调度。

**实验设置。** 【多机器人实机操作】原论文跨多个操纵平台评测新指令及适配；不是四足＋臂边走边接触实验。

**阅读定位：技术基础。** WholeBodyVLA将OpenVLA-OFT微调到同一高层离散移动指令和双臂动作，用作比较基线。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；本库WholeBodyVLA主要把OpenVLA-OFT作为改造后的基线；背景引用不表示采用原OpenVLA架构。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：视觉语言到离散动作token
- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：离散动作预测对照

**平台与执行。** 固定臂操作／通用模型

**相对已有方法的具体改动。** 在预训练视觉语言骨干上用Open X-Embodiment的大量机器人轨迹训练动作预测，公开模型权重／代码与适配流程。动作token化是其接口特点，未解决四足足接触调度。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【多机器人实机操作】原论文跨多个操纵平台评测新指令及适配；不是四足＋臂边走边接触实验。

**未覆盖条件与比较限制。** 本库WholeBodyVLA主要把OpenVLA-OFT作为改造后的基线；背景引用不表示采用原OpenVLA架构。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2410-24164"></a>
## 2410.24164 π0: A Vision-Language-Action Flow Model for General Robot Control

[π0](../literature-map.html#paper=2410.24164) · [PDF](../papers/2410.24164_Pi0_A_Vision-Language-Action_Flow_Model_for_General_Robot_Control.pdf) · [原文](https://arxiv.org/abs/2410.24164)

**原问题与接口。** 跨任务机器人策略要同时接受语义指令与连续、高维、可能多峰的低层动作。 图像、语言和本体状态条件化未来连续动作块；流匹配模块生成动作，而非逐token输出关节命令。

**对应／相邻机制。** [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)

**方法。** 在视觉语言骨干旁训练连续动作专家，用flow matching预测动作块，并用机器人数据训练／微调跨形态控制。

**实验设置。** 【多平台真机操作】包括单臂、双臂和移动机械臂任务，原作报告折衣等跨任务操作；RSS 2025。需按任务查看每个成功率，不能把泛化概括成四足能力。

**阅读定位：技术基础。** WholeBodyVLA、FWBC-VLA等列为VLA背景；未登记直接模块继承。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；本库若干2026全身VLA只引用π0作模型背景；当前未证实直接采用原论文权重或流动作头。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：视觉语言条件下连续动作流匹配
- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：连续动作块对照

**平台与执行。** 多形态机械臂／移动机械臂

**相对已有方法的具体改动。** 在视觉语言骨干旁训练连续动作专家，用flow matching预测动作块，并用机器人数据训练／微调跨形态控制。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【多平台真机操作】包括单臂、双臂和移动机械臂任务，原作报告折衣等跨任务操作；RSS 2025。需按任务查看每个成功率，不能把泛化概括成四足能力。

**未覆盖条件与比较限制。** 本库若干2026全身VLA只引用π0作模型背景；当前未证实直接采用原论文权重或流动作头。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2103-00020"></a>
## 2103.00020 Learning Transferable Visual Models From Natural Language Supervision

[CLIP](../literature-map.html#paper=2103.00020) · [PDF](../papers/2103.00020_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision.pdf) · [原文](https://arxiv.org/abs/2103.00020)

**原问题与接口。** 封闭标签的视觉分类器难根据自由文本寻找新物体／语义区域。 分别编码图像与文本，用共同向量空间中的相似度关联两者；不直接输出接触位姿、力或关节动作。

**对应／相邻机制。** [K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)；[K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)

**方法。** 以大量图文对做对比学习，将匹配的图像文本向量拉近、非匹配样本分开；下游以文本查询视觉内容。

**实验设置。** 【视觉基准】零样本图像识别等；原作不做四足操作实机。ICML 2021。

**阅读定位：技术基础。** UMI on Legs用预训练CLIP视觉编码器；WildLMa用CLIP计算文本对象条件概率图；四足版FALCON用冻结CLIP特征协调策略。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；语义相似度不等于可抓取性、可达性或接触稳定性。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K22 可操作区域、接触目标与动作参数](../knowledge/network.md#k22)：文本—图像相似度只给语义线索
- [K40 视觉表示要丢掉什么、保留什么](../knowledge/network.md#k40)：图文对比学习的语义表示

**平台与执行。** 通用视觉语言模型

**相对已有方法的具体改动。** 以大量图文对做对比学习，将匹配的图像文本向量拉近、非匹配样本分开；下游以文本查询视觉内容。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【视觉基准】零样本图像识别等；原作不做四足操作实机。ICML 2021。

**未覆盖条件与比较限制。** 语义相似度不等于可抓取性、可达性或接触稳定性。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="1710-06542"></a>
## 1710.06542 Asymmetric Actor Critic for Image-Based Robot Learning

[Asymmetric Actor-Critic](../literature-map.html#paper=1710.06542) · [PDF](../papers/1710.06542_Asymmetric_Actor_Critic_for_Image-Based_Robot_Learning.pdf) · [原文](https://arxiv.org/abs/1710.06542)

**原问题与接口。** 仿真训练能知道完整状态，但真实策略部署时只有图像等局部观测；让策略在训练时依赖完整状态会造成部署信息落差。 训练时actor读取部署可得的RGB-D观察，critic读取仿真的完整状态；只有actor用于真机动作生成。

**对应／相邻机制。** [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)；[K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)

**方法。** 让价值函数利用仿真真值降低强化学习的价值估计难度，同时限制actor仅用真实可获得的观察；再配域随机化缩小视觉和动力学差距。它改变训练信息分配，不决定任务奖励或全身动作接口。

**实验设置。** 【仿真＋机械臂真机】多类模拟任务与实机抓取、推物、移动方块；RSS 2018，没有四足操作。

**阅读定位：技术基础。** RoboDuet §IV-C明确采用该非对称actor-critic框架，另用PPO和Isaac Gym训练其腿臂策略。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；特权critic不能直接部署；仿真真值若与现实偏差太大也未必帮得上忙。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)：非对称actor／critic的训练信息分配
- [K15 特权训练、历史估计与视觉学生](../knowledge/network.md#k15)：critic使用仿真真值、actor只读部署观察

**平台与执行。** 通用方法／机械臂

**相对已有方法的具体改动。** 让价值函数利用仿真真值降低强化学习的价值估计难度，同时限制actor仅用真实可获得的观察；再配域随机化缩小视觉和动力学差距。它改变训练信息分配，不决定任务奖励或全身动作接口。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【仿真＋机械臂真机】多类模拟任务与实机抓取、推物、移动方块；RSS 2018，没有四足操作。

**未覆盖条件与比较限制。** 特权critic不能直接部署；仿真真值若与现实偏差太大也未必帮得上忙。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2212-06817"></a>
## 2212.06817 RT-1: Robotics Transformer for Real-World Control at Scale

[RT-1](../literature-map.html#paper=2212.06817) · [PDF](../papers/2212.06817_RT-1_Robotics_Transformer_for_Real-World_Control_at_Scale.pdf) · [原文](https://arxiv.org/abs/2212.06817)

**原问题与接口。** 机器人技能数据分散，单任务小模型难同时保持多任务覆盖和训练规模效益。 图像历史与语言任务进入Transformer，输出离散化的低层动作token。

**对应／相邻机制。** [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)

**方法。** 以真实机器人多任务数据训练Robotics Transformer，用token化视觉及动作表示和高容量序列模型吸收任务多样性；研究数据量、模型容量与泛化关系。

**实验设置。** 【真实机器人】Google机械臂平台的多任务执行与未见场景泛化；RSS 2023。

**阅读定位：技术基础。** Open X-Embodiment的RT-X模型家族沿RT-1等架构跨机器人训练；RT-2将视觉语言预训练更直接接入动作token。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；原作重点是大规模真实机器人控制，并未直接学习四足足接触或底盘—手臂接触补偿。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：视觉语言条件下动作token的机器人Transformer
- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：序列模型预测离散动作

**平台与执行。** 固定／移动机械臂数据

**相对已有方法的具体改动。** 以真实机器人多任务数据训练Robotics Transformer，用token化视觉及动作表示和高容量序列模型吸收任务多样性；研究数据量、模型容量与泛化关系。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【真实机器人】Google机械臂平台的多任务执行与未见场景泛化；RSS 2023。

**未覆盖条件与比较限制。** 原作重点是大规模真实机器人控制，并未直接学习四足足接触或底盘—手臂接触补偿。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2307-15818"></a>
## 2307.15818 RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

[RT-2](../literature-map.html#paper=2307.15818) · [PDF](../papers/2307.15818_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control.pdf) · [原文](https://arxiv.org/abs/2307.15818)

**原问题与接口。** 机器人轨迹数据量有限，传统动作策略不易利用互联网视觉语言知识识别未见对象和指令。 输入相机图像和语言指令；将机器人动作编码为文本形式token，由视觉语言模型联合预测。

**对应／相邻机制。** [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)

**方法。** 把机器人动作表示成与语言token兼容的序列，将机器人轨迹和互联网视觉问答等任务共同微调预训练视觉语言模型；此处明确提出VLA范式。

**实验设置。** 【真实机器人】约6000次评价试验，检验未见物体与语义指令；CoRL 2023。实验不含四足边走边操作。

**阅读定位：技术基础。** OpenVLA等以RT-2为VLA先例和比较对象；本库四足VLA大多只作背景引用，未核到使用RT-2权重。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；网络知识有助于语义泛化，不直接约束动作可达性、接触力或足支撑安全。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：图文与机器人动作token联合微调的VLA
- [K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)：图文／动作文本token统一预测

**平台与执行。** 固定／移动机械臂数据

**相对已有方法的具体改动。** 把机器人动作表示成与语言token兼容的序列，将机器人轨迹和互联网视觉问答等任务共同微调预训练视觉语言模型；此处明确提出VLA范式。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【真实机器人】约6000次评价试验，检验未见物体与语义指令；CoRL 2023。实验不含四足边走边操作。

**未覆盖条件与比较限制。** 网络知识有助于语义泛化，不直接约束动作可达性、接触力或足支撑安全。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2310-08864"></a>
## 2310.08864 Open X-Embodiment: Robotic Learning Datasets and RT-X Models

[Open X-Embodiment](../literature-map.html#paper=2310.08864) · [PDF](../papers/2310.08864_Open_X-Embodiment_Robotic_Learning_Datasets_and_RT-X_Models.pdf) · [原文](https://arxiv.org/abs/2310.08864)

**原问题与接口。** 每个机器人单独采集、训练策略限制了跨形态知识迁移；异构轨迹格式也妨碍合并训练。 统一多机构机器人轨迹的观察、动作和任务信息，训练RT-X跨机器人策略供下游适配。

**对应／相邻机制。** [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)

**方法。** 21机构汇集22种机器人数据，统一格式并用RT-X模型测试跨机器人训练的正迁移；贡献同时在数据整理和跨本体预训练，不是一个单一的底盘控制器。

**实验设置。** 【多真实机器人数据和评估】论文报告527种技能及跨机器人测试；ICRA 2024。具体机器人与任务分布不等同于四足移动操作覆盖。

**阅读定位：技术基础。** OpenVLA明确在Open X-Embodiment的约970k机器人轨迹上训练；Octo明确使用约800k条该库轨迹。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；多机器人数据集有明显平台与任务偏差；把新四足平台加入后仍需接口适配和实机验证。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：跨机器人统一数据与模型
- [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)：22种机器人轨迹格式整合

**平台与执行。** 跨机器人数据／模型

**相对已有方法的具体改动。** 21机构汇集22种机器人数据，统一格式并用RT-X模型测试跨机器人训练的正迁移；贡献同时在数据整理和跨本体预训练，不是一个单一的底盘控制器。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【多真实机器人数据和评估】论文报告527种技能及跨机器人测试；ICRA 2024。具体机器人与任务分布不等同于四足移动操作覆盖。

**未覆盖条件与比较限制。** 多机器人数据集有明显平台与任务偏差；把新四足平台加入后仍需接口适配和实机验证。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2405-12213"></a>
## 2405.12213 Octo: An Open-Source Generalist Robot Policy

[Octo](../literature-map.html#paper=2405.12213) · [PDF](../papers/2405.12213_Octo_An_Open-Source_Generalist_Robot_Policy.pdf) · [原文](https://arxiv.org/abs/2405.12213)

**原问题与接口。** 大规模机器人策略若绑定固定相机、任务格式和动作维数，很难低成本迁移到新设备。 接受语言或目标图像条件及不同观察token，输出可适配目标机器人的动作序列。

**对应／相邻机制。** [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)

**方法。** 在Open X-Embodiment约800k轨迹上预训练开源Transformer策略，按新相机、动作空间与任务条件微调；重点验证通用初始化和接口可扩展性。

**实验设置。** 【九种机器人平台实机适配】比较少量新域数据微调与模型设计消融；RSS 2024。不是四足全身控制实验。

**阅读定位：技术基础。** 直接沿用Open X-Embodiment数据；UMI on Legs及后续VLA论文引用作通用策略背景。

**主线判断的证据范围。** 实际承接与仅作背景的关系分开登记在literature/foundations.md；跨平台动作适配与身体动力学稳定是不同问题；本库引用多数为背景，未核到四足＋臂论文直接使用Octo权重。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)：开放通用策略的目标图像／语言条件
- [K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)：新相机及动作空间的适配

**平台与执行。** 跨机器人策略

**相对已有方法的具体改动。** 在Open X-Embodiment约800k轨迹上预训练开源Transformer策略，按新相机、动作空间与任务条件微调；重点验证通用初始化和接口可扩展性。

**复用部分。** 作为后作的方法、工具、数据接口或比较基线；具体性质见本卡“本库承接”和literature/foundations.md。

**实验能支持什么。** 【九种机器人平台实机适配】比较少量新域数据微调与模型设计消融；RSS 2024。不是四足全身控制实验。

**未覆盖条件与比较限制。** 跨平台动作适配与身体动力学稳定是不同问题；本库引用多数为背景，未核到四足＋臂论文直接使用Octo权重。

**阅读范围。** PDF摘要、方法接口、实验与结论相关段落的定向核读；未逐项复验所有数据表、附录、代码或视频。

**原文定位。** 摘要；方法与接口节；实验／评价节

**核读订正。** 不因参考文献列表命中而推断方法继承；部分早期原作没有移动操作实验。

<a id="2503-13446"></a>
## 2503.13446 MoManipVLA: Transferring Vision-Language-Action Models for General Mobile Manipulation

[MoManipVLA](../literature-map.html#paper=2503.13446) · [PDF](../papers/2503.13446_MoManipVLA_Transferring_Vision-Language-Action_Models_for_General_Mobile_Manipulation.pdf) · [原文](https://arxiv.org/abs/2503.13446)

**原问题与接口。** 固定底座 VLA 预测的手端路径点移到移动平台后可能不可达、碰撞或使机械臂靠近关节极限；希望沿用预训练模型的视觉语言能力，而由执行层处理底盘站位。 输入图像、语言和当前移动平台状态；OpenVLA 预测末端路径点。后续规划同时输出轮式底盘移动路径和机械臂轨迹；VLA 本身不直接输出底盘速度。

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K12 运动学可达、动力学可行与策略能力](../knowledge/network.md#k12)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)

**来源与版本。** CVPR 2025；**轮式移动臂，是真正的 VLA 末端目标接口对照**

**方法。** 上层优化选择底盘路径点，为手端目标留出可操作空间；下层在连续末端路径点之间选择臂轨迹。目标函数检查逆运动学可达性、关节和底盘轨迹平滑性、碰撞；臂关节用 Pinocchio IK 求解。先有独立导航／注视模块把平台带到目标附近，再执行该移动操作规划。

**实验设置。** OVMM 仿真整体成功率 15.8%，表中最佳对照 11.6%（高 4.2 个百分点）。Hexman Echo Plus 轮式底盘＋RM65 臂真机 Stack Block 3/10、Open Drawer 1/10、Put in Bowl 4/10；实机适配使用 50 条专家示范。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)：轮式 VLA 末端路径点与双层优化

**平台与执行。** 轮式 Hexman Echo Plus＋RM65

**相对已有方法的具体改动。** 上层选择底盘路径点，下层选择末端及臂轨迹，联合考虑逆运动学可达、平滑和碰撞；先独立导航到操作区。

**复用部分。** OpenVLA、Pinocchio IK、独立导航与注视模块；文中未核实复用UMI on Legs控制器。

**实验能支持什么。** OVMM整体成功15.8%对最佳表中基线11.6%；轮式真机三任务分别3/10、1/10、4/10；50条实机适配示范。

**未覆盖条件与比较限制。** 非四足，真机成功率低且样本小；没有同平台对照显式底盘动作接口。

**阅读范围。** §3；§4；OVMM表与真机任务表；已核对正文或完整扩展摘要中的方法和实验。

**原文定位。** §3；§4；OVMM表与真机任务表

**核读订正。** 摘要4.2%据表是15.8%-11.6%=4.2个百分点；不应解读为相对百分比增长。

<a id="2609-22829"></a>
## 2609.22829 Whole-Body UMI: Transferring UMI Manipulation Skills to Humanoid Whole-Body Manipulation via Real-Time Motion Generation

[Whole-Body UMI](../literature-map.html#paper=2609.22829) · [PDF](../papers/2609.22829_Whole-Body_UMI_Transferring_UMI_Manipulation_Skills_to_Humanoid_Whole-Body_Manipulation_via_Real-Time_Motion_Generation.pdf) · [原文](https://arxiv.org/abs/2609.22829)

**原问题与接口。** 单条手端轨迹通常对应多种身体姿态、落脚位置和步态，仅做末端跟踪可能达标却产生不自然或不稳的全身动作。UMI 人手示范没有机器人身体与足轨迹，不能直接监督这些变量。 视觉 Diffusion Policy 给未来手端轨迹；全身运动生成器利用手端目标和已有全身运动先验补足身体、足与关节参考；全身跟踪器执行。高层仍只输出手端轨迹，并未给底盘速度或把 VLA 接入。

**对应／相邻机制。** [K03 冗余运动：同一个手端目标不只一个全身姿态](../knowledge/network.md#k03)；[K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K20 未来末端轨迹预览与时间一致性](../knowledge/network.md#k20)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；[K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)

**来源与版本。** 2026 预印本；**人形，非语言 VLA**

**方法。** 用人体动作捕捉学习自回归的条件全身生成器，并在生成时看手端轨迹的未来窗口；生成的全身参考交由 WBC 跟踪。与直接从手端目标求一个局部逆运动学解相比，增加了数据驱动的身体和足运动先验。

**实验设置。** G1 真机四任务各 10 次：关抽屉 9/10、架上取放 8/10、投球 3/10、移动取放 4/10；另比较有无手端预览和提供真值身体／足参考的 oracle 条件，并评估动作重建、足滑与末端误差。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)：手端目标欠约束与人形运动生成

**平台与执行。** Unitree G1人形

**相对已有方法的具体改动。** 从人体mocap学习手端条件全身运动先验，自回归生成未来全身动作，再交给全身控制器。

**复用部分。** UMI手持示范与视觉Diffusion Policy思路，人体mocap全身先验；不声明复用UMI on Legs代码。

**实验能支持什么。** G1真机四任务每项10次：关抽屉9/10、架上取放8/10、投球3/10、移动取放4/10；另测有无末端预览和身体／足真值oracle。

**未覆盖条件与比较限制。** 人形先验与四足不同；移动取放和投球仍低成功；跨平台数字不能证明接口优劣。

**阅读范围。** 方法运动生成和WBC接口；Table V与真机任务图表；已核对正文或完整扩展摘要中的方法和实验。

**原文定位。** 方法运动生成和WBC接口；Table V与真机任务图表

**核读订正。** 不能把末端欠约束解释为必须扩大VLA动作维度；本文上层并非语言VLA。

<a id="2610-32271"></a>
## 2610.32271 From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot

[Walking Bot VLA](../literature-map.html#paper=2610.32271) · [PDF](../papers/2610.32271_From_Tabletop_to_Walking_Bot_Deploying_a_VLA_Model_on_a_Legged_Manipulator_Robot.pdf) · [原文](https://arxiv.org/abs/2610.32271)

**原问题与接口。** 固定臂 VLA 的动作空间没有底盘移动和身体俯仰；部署到四足时要决定这些动作由模型还是既有控制器负责，并让示教标签和执行命令一致。 VLA 输出 11 维命令：机体坐标底盘速度 vx、vy、yaw 速度、身体 pitch、六个臂关节绝对角目标及夹爪开合。臂感知的 BinWalker 衍生 RL 行走控制器执行底盘命令，关节轨迹控制器执行臂命令；不是 VLA 只给末端轨迹的接口。

**对应／相邻机制。** [K14 分层接口把学习任务限制在某个动作空间](../knowledge/network.md#k14)；[K26 语言规划、技能选择与 VLA 动作生成](../knowledge/network.md#k26)；[K27 动作块、重规划与平滑的精度—效率取舍](../knowledge/network.md#k27)；[K28 示范迁移必须处理坐标、形态与动作差异](../knowledge/network.md#k28)；[K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)

**来源与版本。** 2026-10-23 初步扩展摘要；**Go2＋AgileX Piper L，硬件相关性高，实验仍初步**

**方法。** 同一操作者用领从臂和手持控制器同时示教底盘、姿态、机械臂与夹爪。采集和部署都经过同一机器人侧命令接口，使动作标签直接对应部署量。微调 MolmoAct2 家族的视觉语言骨干和动作头；采用十步动作块，臂作为连续轨迹执行，底盘以较高频线程维持命令。

**实验设置。** Go2＋Piper 真机给出抓取搬运和推物定性片段，**没有真机成功率表**。131、233、258 条示教的离线留出集上，抓取动作预测的末端误差为 68.7、48.2、47.8 mm；这是根据预测关节前向运动学计算的离线误差，不是真机闭环跟踪误差。

**阅读定位：专题／应用。** 完整库中的专题／系统工作；目前没有登记足以支持进入核心主线的跨论文模块采用证据。此标签不等于低质量，方法和实验仍以逐篇核读为准。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K47 高层只给手端目标，还是同时指定身体动作？](../knowledge/network.md#k47)：Go2＋Piper 显式 11 维 VLA 动作

**平台与执行。** Unitree Go2＋AgileX Piper L

**相对已有方法的具体改动。** 单人同步采集底盘和臂示教，训练与部署共用动作接口；十步动作块、臂连续轨迹、底盘命令保持线程。

**复用部分。** MolmoAct2家族、BinWalker衍生arm-aware RL步态、Piper领从示教；未核实采用UMI on Legs全身控制器。

**实验能支持什么。** 131、233、258示教的离线抓取动作预测末端误差68.7、48.2、47.8mm；Go2＋Piper实机仅定性片段，没有成功率统计。

**未覆盖条件与比较限制。** 初步扩展摘要；离线动作预测误差不是实机闭环跟踪精度；无法判断持续接触安全或接口优劣。

**阅读范围。** §II；§III；Table I；§V；已核对正文或完整扩展摘要中的方法和实验。

**原文定位。** §II；§III；Table I；§V

**核读订正。** 真机片段不可当成功率研究；表中末端误差是离线动作预测的FK误差。

<a id="2610-28480"></a>
## 2610.28480 SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model

[SuperMimic](../literature-map.html#paper=2610.28480) · [PDF](../papers/2610.28480_SuperMimic_Scaling_Humanoid_Whole-Body_Control_with_One_Differentiable_World_Model.pdf) · [原文](https://arxiv.org/abs/2610.28480)

**原问题与接口。** 大型人形动作库中的不同参考动作共享同一机器人动力学，逐段训练专门策略再蒸馏，或用 PPO 在仿真中对所有动作反复采样，都很耗算力。作者研究能否用一套共享的动力学模型加速全身跟踪策略训练，而不是设计新的视觉任务策略。 训练时，策略看最近 10 帧关节角／速度、IMU 角速度、重力方向和上一步动作，以及未来 10 帧参考动作；输出归一化关节位置设定值，经低增益 PD 形成力矩。世界模型还看仿真状态、动作和随机化参数，用于**训练时**预测；真机部署运行跟踪策略，不运行在线世界模型规划器。文中只实测了完整动作参考和速度命令两类接口；手端位姿等在附录中作为可扩展接口举例，尚未报告实测。

**对应／相邻机制。** [K19 域随机化、模型校准与在线补偿](../knowledge/network.md#k19)；[K43 策略、回报、评价网络与信用分配](../knowledge/network.md#k43)；[K48 可微动力学代理用于训练全身跟踪策略](../knowledge/network.md#k48)

**来源与版本。** CoRL 2026 Oral；2026-10-20 预印本。**人形全身动作跟踪训练方法；没有物体操作实验，因此放在相邻方法而非 loco-manipulation 主线。**

**方法。** 每轮先由当前策略在 MuJoCo Warp 采集状态转移，存进 replay buffer；以记录动作作八步自回归训练，拟合共享的可微状态转移模型，并计算／拟合观测、奖励与终止。再从真实仿真轨迹的状态起步，在冻结的模型中想象 32 步，通过模型对动作和状态的导数反向传播更新策略；critic 估计 32 步之后的回报，避免短视。模型每轮随新数据更新。它不要求物理仿真器本身可微，也不在推理时对世界模型求解 MPC。

**实验设置。** 【仿真＋G1 真机】共享的 129,514 条 BONES-SEED **训练动作**上，单 H100 训练 3 h 后失败 25 条；双 H100 训练 9.8 h 后失败 0 条；SONIC 公开权重失败 179 条。单 H100 约 3 h 超过 SONIC 公开权重的归一化回报；后者报告 128 张 L40 训练约 168 h。较公平的 LAFAN1 40 条动作控制对照中，SuperMimic 单卡约 1.2 h 达到评估回报 0.82，PPO-Sim 在 18 h／至多 8 卡预算内未达到；PPO-on-world-model 对照支持模型梯度收益，critic／短时域消融支持扰动恢复。真机仅展示跳跃、侧滚和翻转；另有仿真速度阶跃测试，RL 速度编码器在 672 种命令中 650 种稳态误差较小。

**阅读定位：新路线代表。** CoRL 2026 Oral 的高效全身跟踪训练路线；有控制变量的PPO对照和G1真机动作，但主动过滤物体交互。作为相邻训练方法观察，不列四足移动操作核心主线。

**主线判断的证据范围。** 方法、实验、复用部分及证据边界见本节点卡片与论文贡献审读记录；引用出现或基线比较不独自构成模块继承。

**在知识稿中作为哪些来源。**（包含机制实例、问题比较与反例，不声明首次发明。）

- [K48 可微动力学代理用于训练全身跟踪策略](../knowledge/network.md#k48)：共享可微模型、短时回传、效率对照与对象接触边界

**平台与执行。** Unitree G1 人形；训练动作筛掉地形和物体交互

**相对已有方法的具体改动。** 用持续更新的可微动力学模型代替大量仿真 PPO 样本估计，在短时想象轨迹中反向传播训练统一动作跟踪器；部署只运行策略。

**复用部分。** 沿用 BeyondMimic 的跟踪问题和主要奖励；与 SONIC 的大规模 PPO 对照。可微学习动力学本身已有 ControlVAE、SuperTrack、SuperDyno 等先例。

**实验能支持什么。** 完整动作训练集 129514 条：单 H100 3 h 失败25条，双 H100 9.8 h 失败0条，SONIC公开权重失败179条；LAFAN1同条件PPO-Sim对照；G1真机跳跃、侧滚与翻转；速度接口只在仿真测672种阶跃响应。

**未覆盖条件与比较限制。** 论文§6明确无地形／对象交互；训练数据过滤这些动作。没有四足、轮足、机械臂、按钮／柜门或安全接触验证。训练集回放不可当作新任务泛化。SONIC算力对照硬件和数据量不同。

**阅读范围。** 2026-10-29核读19页PDF全文；重点§2–4、§6、附录A/B/E/F/G，核对作者项目页说明及arXiv元数据。

**原文定位。** §2 prior work；§3 training loop and equations；§4.1 controlled PPO comparison；§4.3 critic；§4.4 real G1；§4.5 velocity interface；§6 limits；App A/B/E/F/G

**核读订正。** 世界模型在训练中给策略梯度，不是部署时的视觉世界模型或在线MPC；接触地面做翻滚不等于接触物体操作；附录列手端目标为可能接口，但没有实测该接口。

## 综述索引
综述提供分类与检索线索，不替代原作的实验核查。来源评价与全文范围见[综述导读](surveys.md)。

<a id="survey-contact"></a>
### A Survey of Robot Manipulation in Contact

[接触操作综述](../literature-map.html#paper=survey-contact) · [PDF](../papers/2112.01942_A_Survey_of_Robot_Manipulation_in_Contact.pdf)
把持续接触任务中的力控制、阻抗、导纳、状态表示与学习方法分开。
按接触任务、执行控制、接触表示以及学习／规划组织。
不覆盖四足移动稳定性与足端接触分配。

<a id="survey-legged"></a>
### Legged Robots for Object Manipulation: A Review

[腿式操作综述](../literature-map.html#paper=survey-legged) · [PDF](../papers/2303.16865_Legged_Robots_for_Object_Manipulation_A_Review.pdf)
区分腿式机器人到底用身体、行走腿、专用臂还是多机器人协作来移动物体。
按物体交互形式和机器人形态组织已有工作，并比较被操作物体与机器人的尺寸关系。
发表于 2023 年，缺少大量 2024–2026 工作。

<a id="survey-tamp"></a>
### A Survey of Optimization-Based Task and Motion Planning

[TAMP 综述](../literature-map.html#paper=survey-tamp) · [PDF](../papers/2404.02817_A_Survey_of_Optimization-Based_Task_and_Motion_Planning_From_Classical_to_Learning_Approaches.pdf)
任务步骤和满足动力学／几何约束的运动轨迹怎样一起求解。
分述任务表示、轨迹优化、联合 TAMP 和学习辅助的可行性判断与恢复。
面向通用 TAMP，不给出四足足接触性能结论；预印本 2024 年公开，期刊卷期为 2025 年。

<a id="survey-vla"></a>
### A Survey on Vision–Language–Action Models for Embodied AI

[VLA 综述](../literature-map.html#paper=survey-vla) · [PDF](../papers/2405.14093_A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI.pdf)
厘清视觉语言规划器、动作模型、数据集和评测之间的区别。
按 VLA 组成、低层动作、任务规划及数据基准组织。
桌面操作方法不能自动成为四足 loco-manipulation 证据。

<a id="survey-humanoid"></a>
### Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning

[人形移动操作综述](../literature-map.html#paper=survey-humanoid) · [PDF](../papers/2501.02116_Humanoid_Locomotion_and_Manipulation_Current_Progress_and_Challenges_in_Control_Planning_and_Learning.pdf)
系统比较模型规划、MPC/WBC、RL/IL、触觉与 foundation models 怎样支持移动操作。
正文分多接触规划、模型精度、全身控制、学习技能、数据和基础模型等章节；比较计算速度与模型精度的取舍。
主要是人形；2026 年发表不等于已覆盖所有 2026 年预印本。

<a id="survey-quadruped"></a>
### Loco-Manipulation With Quadruped Robots: Modeling, Task Taxonomy, and Control Methods—A Critical Review

[四足移动操作综述](../literature-map.html#paper=survey-quadruped) · [PDF](../papers/IEEE_Access_2026_Loco-Manipulation_With_Quadruped_Robots_Critical_Review.pdf)
在四足任务中对应建模假设、任务条件和 WBC/MPC/RL/IL 控制方法。
全文按建模、任务分类和控制方法组织，讨论 WBC、MPC、RL/IL 及混合阻抗／力控制，并考虑地形、载荷、接触和感知延迟。
新发表论文引用积累很少；具体性能比较应回原论文验证任务和实验条件。

<a id="survey-affordance"></a>
### From Passive Perception to Active Interaction: A Survey of Affordance Learning for Embodied AI

[可操作性综述（预印本）](../literature-map.html#paper=survey-affordance) · [PDF](../papers/Preprints_202610.0392_v1_From_Passive_Perception_to_Active_Interaction_A_Survey_of_Affordance_Learning_for_Embodied_AI.pdf)
怎样从视觉场景找出可交互位置，结合任务与机器人状态选定目标，再把目标交给可执行动作。
全文以 affordance 感知、任务相关推理、指导动作为三段；把预测结果分成动作类型、目标区域和可选执行参数，再比较交给规划器／技能与融入策略输入、隐式特征或奖励的不同接口。
Preprints.org 2026-10-07，尚未查到同行评审正式版；方法表主要是夹爪、灵巧手和双臂，不提供四足移动操作性能对照。
