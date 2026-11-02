# 移动操作知识网络

本稿按共同机制组织移动操作知识，不按论文题名逐篇排序。共 107 篇研究／方法论文，其中 103 篇有正文或定向方法／实验核读记录；具体深度逐篇登记。另 4 篇尚未取得可核对全文，仅保留既有检索卡片，不作为新机制结论的全文证据。7篇综述提供分类与定义，性能结论回到原论文。核读日期：2026-10-29。

知识节点的“前置”表示学习依赖；论文之间的直接继承只在有原文依据时登记。每个节点合并共同机制，来源说明谁在何处怎样使用；这不声明所列作者首先发明该机制。Walk These Ways与另22篇技术基础单列；loco-manipulation、跨平台邻接与通用方法分别标明。当前是可继续补写的领域知识稿，不声称文献穷尽或未经独立验证的稳定性证明。

[交互阅读页](../knowledge-network.html) · [论文贡献与审读依据](../literature/papers.md) · [原论文关系图](../literature-map.html)


## 从问题进入

### R1 身体移动时，怎样保持手端操作？
从运动学补偿到动态可行与接触响应，分开判断误差来自哪里。

[K01 浮动基、足接触与手端运动的耦合](#k01) → [K02 参考坐标系决定控制器究竟在保持什么](#k02) → [K03 冗余运动：同一个手端目标不只一个全身姿态](#k03) → [K20 未来末端轨迹预览与时间一致性](#k20) → [K12 运动学可达、动力学可行与策略能力](#k12) → [K37 训练可预测的步态，再辨识闭环响应](#k37) → [K07 位置准确、保持接触与力准确分别是什么](#k07) → [K08 柔顺控制规定受力后怎样运动](#k08) → [K39 触觉、握力与接触释放](#k39)
### R2 到达物体附近后，怎样开始并完成操作？
从视觉目标、站位可达性到机构与接触步骤，区分准备与执行。

[K21 视觉策略可以学控制，也可以只学操作参考](#k21) → [K40 视觉表示要丢掉什么、保留什么](#k40) → [K22 可操作区域、接触目标与动作参数](#k22) → [K23 导航终点应满足后续操作条件](#k23) → [K24 机构约束与在线交互辨识](#k24) → [K10 离散接触模式与连续运动需要共同安排](#k10) → [K36 物体反作用力的预测与反馈](#k36) → [K18 跟踪示范、调节进度与任务优化](#k18) → [K30 执行过、完成了与记忆可观测性](#k30)


### R3 怎样给低成本臂使用力或触觉信息？
先判断信号可辨识什么，再确定它应该进入控制还是动作模型。

[K04 关节角度、速度与力矩是不同的动作接口](#k04) → [K07 位置准确、保持接触与力准确分别是什么](#k07) → [K09 无力传感器时，估计到的到底是什么](#k09) → [K08 柔顺控制规定受力后怎样运动](#k08) → [K39 触觉、握力与接触释放](#k39) → [K31 力信息进入 VLA 的位置决定它能改什么](#k31)
### R4 RL 与 VLA 各自负责哪些变量？
把控制结构、训练先验、视觉动作与执行调度接成可实现接口。

[K43 策略、回报、评价网络与信用分配](#k43) → [K13 统一策略、协作策略与模型分工](#k13) → [K14 分层接口把学习任务限制在某个动作空间](#k14) → [K15 特权训练、历史估计与视觉学生](#k15) → [K44 示范监督与闭环数据分布](#k44) → [K16 多目标奖励与多评价网络不等于多个物理机制](#k16) → [K17 首次成功、接触探索与奖励塑形](#k17) → [K19 域随机化、模型校准与在线补偿](#k19) → [K26 语言规划、技能选择与 VLA 动作生成](#k26) → [K28 示范迁移必须处理坐标、形态与动作差异](#k28) → [K41 物体相对示范扩增与接触阶段的锚点](#k41) → [K27 动作块、重规划与平滑的精度—效率取舍](#k27) → [K29 世界模型与搜索必须预测实际闭环执行](#k29) → [K47 高层只给手端目标，还是同时指定身体动作？](#k47)


### R5 按过按钮后，怎样知道该停下还是重试？
区分动作历史、程序阶段和真实物理成功，不把所有 memory 合并。

[K15 特权训练、历史估计与视觉学生](#k15) → [K18 跟踪示范、调节进度与任务优化](#k18) → [K24 机构约束与在线交互辨识](#k24) → [K30 执行过、完成了与记忆可观测性](#k30) →  →
## 本质相似与实质差别

### 相同运动学，目标附着位置不同
**共同机制。** 都利用身体位姿与臂正运动学计算手端。

**不同部分。** Deep WBC参考部分不随height/roll/pitch；UMI使用任务轨迹；Multi-Terrain保持身体位置与重力朝向；ReCo预测身体运动再协调臂。不能据各自误差直接排名。

**怎样区分。** 把同一世界中的固定点／轨迹给四种接口，并明确哪些方法必须改目标定义才能执行。

论文：[Deep WBC](../literature-map.html#paper=2210.10044)；[UMI on Legs](../literature-map.html#paper=2407.10353)；[Reinforcement Learning Based](../literature-map.html#paper=2610.23548)；[ReCo](../literature-map.html#paper=2610.01612)
知识：[K02 参考坐标系决定控制器究竟在保持什么](#k02)；[K20 未来末端轨迹预览与时间一致性](#k20)；[K37 训练可预测的步态，再辨识闭环响应](#k37)

### 都叫residual，修改的变量不同
**共同机制。** 保留已有模型或行为，再学习修正。

**不同部分。** RAMBO修正执行加速度及关节参考；Guided RL修正参考与phase；Athletic在仿真中校准执行器；CAIMAN修正对象转移预测。前两类是部署时的闭环执行反馈，后两类修改仿真或预测模型。

**怎样区分。** 先写残差单位、加入位置和是否经过约束，再判断能否替换或组合。

论文：[RAMBO](../literature-map.html#paper=2504.06662)；[Guided RL](../literature-map.html#paper=2410.13817)；[Athletic Loco-Manipulation](../literature-map.html#paper=paper-63)；[CAIMAN](../literature-map.html#paper=2502.00835)
知识：[K04 关节角度、速度与力矩是不同的动作接口](#k04)；[K18 跟踪示范、调节进度与任务优化](#k18)；[K19 域随机化、模型校准与在线补偿](#k19)

### 都有历史，保存的状态不同
**共同机制。** 当前观测不足，增加过去信息。

**不同部分。** 步态历史适应物理变化；SOMA隐式编码推物响应；POT保留对象角色并验证几何结果；投球timer只标记阶段执行。历史长度相同也不是相同方法。

**怎样区分。** 分别制造隐藏载荷、短遮挡、对象混淆与视觉相同的成功／失败，检验保存的信息。

论文：[Deep WBC](../literature-map.html#paper=2210.10044)；[SOMA](../literature-map.html#paper=2610.20968)；[POT-VLA](../literature-map.html#paper=2607.18016)；[Athletic Loco-Manipulation](../literature-map.html#paper=paper-63)
知识：[K15 特权训练、历史估计与视觉学生](#k15)；[K30 执行过、完成了与记忆可观测性](#k30)

### 都有力信息，信号、目标和执行层不同
**共同机制。** 视觉或位置不足以描述物理接触。

**不同部分。** 力估计输入、期望力输出、触觉区域目标、握力控制和身体补偿可独立存在。FWBC的残差tokens不等于标定的六维力；Opt2VLA显式给目标力；TAC主要控制已抓住后的握持。

**怎样区分。** 固定动作权限，分开消融输入／目标／快反馈，并使用参考传感器测物理量。

论文：[Force Control](../literature-map.html#paper=2405.01402)；[Position + Force RL](../literature-map.html#paper=2505.20829)；[FWBC-VLA](../literature-map.html#paper=2609.03889)；[Opt2VLA](../literature-map.html#paper=2609.23968)；[TAC-LOCO](../literature-map.html#paper=2607.10132)
知识：[K07 位置准确、保持接触与力准确分别是什么](#k07)；[K09 无力传感器时，估计到的到底是什么](#k09)；[K31 力信息进入 VLA 的位置决定它能改什么](#k31)；[K39 触觉、握力与接触释放](#k39)

### 都有预测，预测对象和使用方式不同
**共同机制。** 用未来信息减少只追当前误差的问题。

**不同部分。** Sumo在仿真预测内执行低层；ReCo使用辨识闭环模型做MPC；DECOWAM联合视频与动作生成而非在线搜索；DiPLO生成全身及物体轨迹交给跟踪器。

**怎样区分。** 写清预测量、在线是否搜索、是否含低层、未来对象状态来自何处。

论文：[Sumo](../literature-map.html#paper=2604.08508)；[ReCo](../literature-map.html#paper=2610.01612)；[DECOWAM](../literature-map.html#paper=2608.20114)；[DiPLO](../literature-map.html#paper=2610.24847)
知识：[K20 未来末端轨迹预览与时间一致性](#k20)；[K29 世界模型与搜索必须预测实际闭环执行](#k29)；[K37 训练可预测的步态，再辨识闭环响应](#k37)

### 都叫全身，决策权限不同
**共同机制。** 身体和操作端共同完成任务。

**不同部分。** RoboDuet分工并交换姿态请求；Terrain-aware腿RL臂IK；PAKE用部分运动学多解；ReLIC接受上层指定肢体角色。不能仅凭WBC标题视为所有关节联合RL。

**怎样区分。** 对相同目标列可控制自由度、共享状态、能否换角色、底层冻结情况。

论文：[RoboDuet](../literature-map.html#paper=2403.17367)；[Terrain-Aware WBC](../literature-map.html#paper=2605.31343)；[PAKE](../literature-map.html#paper=2607.11041)；[ReLIC](../literature-map.html#paper=2506.07876)
知识：[K13 统一策略、协作策略与模型分工](#k13)；[K14 分层接口把学习任务限制在某个动作空间](#k14)；[K38 肢体角色分配与给定角色的执行](#k38)

### 同叫动态抓取，运动主体和观测条件不同
**共同机制。** 相对运动使末端对齐和接触时机困难，需要视觉或状态历史配合执行。

**不同部分。** DQ-Net移动对象、仿真视觉学生；Dynamic Pick-and-Place机器人移动、真机动捕对象；Badminton高速飞行对象、机载视觉EKF且任务是击球。不能把它们的成功率并排排名。

**怎样区分。** 固定对象轨迹、相机延迟与底盘速度，再评末端相对速度、实际接触与全任务成功；真实观测与特权状态单独消融。

论文：[DQ-Net / DQ-Bench](../literature-map.html#paper=2508.08328)；[Dynamic Pick-and-Place](../literature-map.html#paper=2605.15713)；[Badminton](../literature-map.html#paper=2505.22974)
知识：[K14 分层接口把学习任务限制在某个动作空间](#k14)；[K20 未来末端轨迹预览与时间一致性](#k20)；[K25 低频观测、高频反馈与时间戳](#k25)；[K38 肢体角色分配与给定角色的执行](#k38)；[K40 视觉表示要丢掉什么、保留什么](#k40)

### 行为条件、环境适应与腿臂协作分别改变什么
**共同机制。** 都在策略中加入额外信息，使同一机器人能根据条件改变动作。

**不同部分。** Walk These Ways的b是外部指定的运动方式；Deep WBC的z由特权参数或部署历史产生；RoboDuet由臂产生pitch／roll请求。参数来源、训练目的和控制权限不同，不能统称为“加个latent”。

**怎样区分。** 固定任务、网络权重和环境，分别改变行为指令、历史及臂目标，检查哪一输入引起哪类身体响应；再单独评估外部选择者。

论文：[Walk These Ways](../literature-map.html#paper=2212.03238)；[Deep WBC](../literature-map.html#paper=2210.10044)；[RoboDuet](../literature-map.html#paper=2403.17367)
知识：[K13 统一策略、协作策略与模型分工](#k13)；[K15 特权训练、历史估计与视觉学生](#k15)；[K46 用可调行为保留同一任务的多种运动解](#k46)

### 把方法基础与移动操作系统拆开
**共同机制。** 后作可能复用同一个底层工具、数据接口或动作模型，同时另行设计机器人全身执行。

**不同部分。** UMI on Legs用原始UMI示范和Diffusion Policy生成高层轨迹，用自己的四足全身跟踪执行；Visual WBC用DAgger蒸馏视觉学生，不能称DAgger本身完成了视觉四足操作；Deep WBC对照RMA并修改适应训练，不能把RMA说成背载臂控制器。

**怎样区分。** 逐项查后作正文中的训练数据来源、输入输出、复用的代码／权重、重新训练的模块，以及各自单独的消融实验。

论文：[Original UMI](../literature-map.html#paper=2402.10329)；[Diffusion Policy](../literature-map.html#paper=2303.04137)；[UMI on Legs](../literature-map.html#paper=2407.10353)；[DAgger](../literature-map.html#paper=1011.0686)；[Visual WBC](../literature-map.html#paper=2403.16967)；[RMA](../literature-map.html#paper=2107.04034)；[Deep WBC](../literature-map.html#paper=2210.10044)
知识：[K15 特权训练、历史估计与视觉学生](#k15)；[K20 未来末端轨迹预览与时间一致性](#k20)；[K28 示范迁移必须处理坐标、形态与动作差异](#k28)；[K44 示范监督与闭环数据分布](#k44)

### 高层输出末端路径，还是同时输出身体命令？
**共同机制。** 都要把视觉任务意图变成可执行的移动操作，并由更快的控制层响应机器人状态。

**不同部分。** UMI on Legs 是非语言扩散策略＋四足 RL 全身跟踪；MoManipVLA 是轮式 VLA 路径点＋优化；Whole-Body UMI 是人形非 VLA 轨迹＋运动生成；Go2＋Piper 初步工作是 VLA 显式底盘／身体／臂命令。CMP 提醒末端请求可能越过低层能力。

**怎样区分。** 同机器人、同观测、同示教预算、同任务与成功定义比较动作空间，再测可行性、足移动、跟踪误差和接触安全；现有跨论文数字不可直接排名。

论文：[UMI on Legs](../literature-map.html#paper=2407.10353)；[MoManipVLA](../literature-map.html#paper=2503.13446)；[Whole-Body UMI](../literature-map.html#paper=2609.22829)；[Walking Bot VLA](../literature-map.html#paper=2610.32271)；[CMP](../literature-map.html#paper=2604.07457)
知识：[K03 冗余运动：同一个手端目标不只一个全身姿态](#k03)；[K12 运动学可达、动力学可行与策略能力](#k12)；[K14 分层接口把学习任务限制在某个动作空间](#k14)；[K47 高层只给手端目标，还是同时指定身体动作？](#k47)

## 问题与贡献链

### 参考轨迹在移动身体上怎样执行
UMI→CMP为原文复用；其余按共同接口作问题比较，不声明算法继承。

| 工作 | 在这一子问题中做了什么 | 尚需处理的条件 |
|---|---|---|
| [Deep WBC](../literature-map.html#paper=2210.10044) | 统一策略协调关节，参考部分不随身体姿态。 | 目标仍随水平位置与yaw，难直接复现固定对象轨迹。 |
| [UMI on Legs](../literature-map.html#paper=2407.10353) | 任务坐标轨迹与未来目标让全身提前协调。 | 高层仍可能请求超出低层能力的轨迹，闭环响应也存在误差。 |
| [CMP](../literature-map.html#paper=2604.07457) | 对请求作经验能力投影。 | 投影改变原目标；学习边界有估计误差，不能当无条件安全。 |
| [ReCo](../literature-map.html#paper=2610.01612) | 训练并辨识可预测步态，MPC补偿身体响应。 | 没有完整物体接触力模型，需接上力与柔顺评价。 |

### 给定接触计划怎样应对执行偏差
ETH→Guided RL为明确直接承接；RoLoMa与ETH按接触决策范围比较。

| 工作 | 在这一子问题中做了什么 | 尚需处理的条件 |
|---|---|---|
| [RoLoMa](../literature-map.html#paper=2203.01446) | 给定接触阶段，优化足位与抗扰力裕量。 | 接触顺序预设；离线计划仍需真实反馈。 |
| [ETH Multi-Contact](../literature-map.html#paper=2308.09179) | 搜索对象接触序列，再优化全身／物体轨迹。 | 在线主要沿已有序列执行，偏离计划时恢复有限。 |
| [Guided RL](../literature-map.html#paper=2410.13817) | 用规划单示范训练反馈；进度可暂停或倒退。 | 恢复仍围绕参考，部署需对象状态，锁扣机制没有完整覆盖。 |

### 动作指令怎样表达接触需求
按力信息／力命令接口比较；Opt2VLA明确引用FWBC-VLA并区分目标力，其他箭头不表示已核实直接继承。

| 工作 | 在这一子问题中做了什么 | 尚需处理的条件 |
|---|---|---|
| [Force Control](../literature-map.html#paper=2405.01402) | 学习力目标，外层位置反馈构造柔顺行为。 | 位置与力模式切换，精度有限。 |
| [Position + Force RL](../literature-map.html#paper=2505.20829) | 统一自由位置／接触力目标，接上力条件操作策略。 | 准静态近似；整pipeline消融未隔离输入与输出贡献。 |
| [FWBC-VLA](../literature-map.html#paper=2609.03889) | 关节残差影响VLA，另用快速身体补偿。 | 接触代理不等于准确物理力；低层安全仍需验证。 |
| [Opt2VLA](../literature-map.html#paper=2609.23968) | VLA显式预测目标力，TO力矩监督训练执行器。 | 人形邻接、任务专用控制器；真机力偏差与四足换步仍待检验。 |

### 少量示范怎样覆盖新状态
三者是数据与部署条件的并行选择，不是统一实验中的逐年替代；DemoHLM明确复用MimicGen，DiPLO明确复用DynaRetarget。

| 工作 | 在这一子问题中做了什么 | 尚需处理的条件 |
|---|---|---|
| [UMI on Legs](../literature-map.html#paper=2407.10353) | 末端示范绕开关节形态差异，低层执行轨迹。 | 需要任务覆盖、准确空间与时间对齐。 |
| [DemoHLM](../literature-map.html#paper=2510.11258) | 分段物体相对重定向，仿真执行过滤新数据。 | 几何／机构改变、生成失败与代理任务定义限制覆盖。 |
| [DiPLO](../literature-map.html#paper=2610.24847) | 动态优化扩增并蒸馏强参考教师，再微调规划。 | 仍依赖模型和动捕；跨任务统一模型尚待验证。 |

### 从静态抓取接口到动态任务：复用和差别
Visual WBC→DQ-Net／Interactive Navigation／Deployment Framework是正文明确的低层或实现复用。Dynamic Pick-and-Place把Visual WBC低层重训为对照，任务和观测不同；不是整个系统的线性排名。

| 工作 | 在这一子问题中做了什么 | 尚需处理的条件 |
|---|---|---|
| [Visual WBC](../literature-map.html#paper=2403.16967) | 视觉高层给身体／末端命令，腿RL与臂IK执行。 | 原任务主要静态物体；部署接口不等于所有新任务通用。 |
| [DQ-Net / DQ-Bench](../literature-map.html#paper=2508.08328) | 复用低层，动态教师用候选融合，学生从双视角时间序列模仿。 | 只有仿真；L4教师74.3%、学生41.0%。 |
| [Interactive Arm-Pushing](../literature-map.html#paper=2503.01474) | 臂推物动作可经全身跟踪器执行，并接导航重规划。 | 动捕和已知可移动障碍；不是力安全评测。 |
| [Deployment Framework](../literature-map.html#paper=2512.18938) | 复现训练／模拟器／ROS实机接口并分析接触差异。 | 遥操作小样本；原文代码仍计划公开。 |
| [Dynamic Pick-and-Place](../literature-map.html#paper=2605.15713) | 抗随机臂运动低层加完整抓放任务回报和质量估计。 | 真机动捕，主要抓取接触失败；跨论文十倍速度不是公平基线。 |

### 示范动作生成与四足执行是分开的贡献
原始UMI与Diffusion Policy均被UMI on Legs正文明确采用；CMP继承UMI on Legs设置。阶段分工比单纯按发表时间排序更准确。

| 工作 | 在这一子问题中做了什么 | 尚需处理的条件 |
|---|---|---|
| [Original UMI](../literature-map.html#paper=2402.10329) | 手持夹爪数据与相对末端动作降低采集及形态门槛。 | 默认机器人能追踪末端目标；无足端运动。 |
| [Diffusion Policy](../literature-map.html#paper=2303.04137) | 视觉条件扩散策略表示未来多种可能动作。 | 原作低层执行在固定臂操作上验证。 |
| [UMI on Legs](../literature-map.html#paper=2407.10353) | 把高层末端轨迹交给带未来预览的四足全身策略。 | 高层轨迹仍可能超出足支撑与手端能力范围。 |
| [CMP](../literature-map.html#paper=2604.07457) | 在低层能力范围内约束高层要求。 | 经验能力边界不是物理安全证明。 |

### 手端目标怎样落到全身动作上
UMI on Legs→CMP 有原文数据／训练设置复用；其余为动作权限与执行器的对照，不表示互相继承或时间上的必然替代。

| 工作 | 在这一子问题中做了什么 | 尚需处理的条件 |
|---|---|---|
| [UMI on Legs](../literature-map.html#paper=2407.10353) | 手持示范训练手端轨迹策略，四足 RL 全身控制器自主协调腿臂。 | 请求可能超出低层能力；高层没有力目标。 |
| [MoManipVLA](../literature-map.html#paper=2503.13446) | VLA 给末端路径点，轮式底盘与臂双层轨迹优化检查可达／平滑／碰撞。 | 非四足；真机任务成功率较低，且先经单独导航。 |
| [CMP](../literature-map.html#paper=2604.07457) | 在类似 UMI 的轨迹接口上修正低层能力外的请求。 | 投影可能改变任务目标，并不等同于显式身体决策。 |
| [Whole-Body UMI](../literature-map.html#paper=2609.22829) | 保留手端轨迹，在人形下层加入身体／落脚运动先验。 | 高层不是 VLA；先验需适配形态，移动任务仍较难。 |
| [Walking Bot VLA](../literature-map.html#paper=2610.32271) | Go2＋Piper 的 VLA 直接给底盘速度、身体俯仰与臂关节目标。 | 仅初步真机定性展示；没有与末端接口同平台消融。 |

## 知识正文

### 1. 身体与控制接口
先确定哪些变量可以控制、身体运动怎样传到手端。

<a id="k01"></a>
#### K01 浮动基、足接触与手端运动的耦合
类型：领域基础。

**问题。** 四足的身体不能像固定机械臂的底座那样被当作静止参考。手端碰到物体时，反作用力经过机械臂传到身体，再由足接触承担；抬腿也会改变可用的支撑。

‘浮动基’指身体没有被固定在地面上：电机直接驱动腿和臂的关节，身体的位置和朝向则要靠这些关节以及地面接触来改变。例如机械臂向前顶住面板，面板会反过来推机器人；身体要靠足底与地面的作用力承受它。抬起一只脚后，能承担这部分作用力的接触也会改变。

全身动力学把身体、腿和臂放在同一个受力与运动关系中。‘广义配置’是把身体位姿和所有关节位置组成一个状态；‘广义力’是与这些运动对应的作用量，其中既有推动身体平移的力，也有使身体或关节转动的力矩。下面的式子记录电机和环境接触如何共同产生这些作用。

四足通常不能直接套用差速轮式底盘的‘不能横移’非完整约束。它能靠不同步态横移；在某一足接触阶段，其运动受足不滑移和支撑力约束。连续身体运动与离散抬落脚共同决定操作能力。对于轻操作，关键不是机器人重就必然不准，而是身体运动、接触切换和闭环误差怎样传到手端。

**数学表达与变量。**

这条式子是全身的受力与运动关系：实际运动所需的总作用，由关节电机与环境接触共同提供。先按各项的物理含义阅读，不必先掌握矩阵推导。

$$
M(q)/dot v+h(q,v)=S^{/top}/tau+/sum_{i/in/mathcal C}J_i(q)^{/top}/lambda_i
$$

$q$ 描述身体位置、朝向和各关节角度；$v$ 是身体与关节的速度，$/dot v$ 是相应加速度。$M(q)$ 是把加速度换算成所需作用的惯量矩阵；$h(q,v)$ 汇总重力以及随运动产生的科氏、离心项。因此左边是模型根据当前运动计算出的所需广义力。

$/tau$ 是各电机的关节力矩。$S^/top/tau$ 把这些力矩放到全身变量对应的位置；身体没有直接驱动自身六个自由度的电机，所以不能给它直接填入一组独立电机力矩。

$/lambda_i$ 是第 $i$ 个接触处环境作用在机器人上的力。例如左前足的 $/lambda_i$ 可以包含地面的向上支撑和两个切向摩擦分量，点接触时通常是一个三维向量，单位是牛顿；它不是算法的权重或超参数。手接触面板时，面板的反作用也属于接触力。

$J_i$ 是第 $i$ 个接触处的 Jacobian，描述身体和关节运动怎样传到接触点。$J_i^/top/lambda_i$ 则把这个接触力换算成对身体和关节的作用；对一个转动关节，这相当于根据力臂计算力矩。$/mathcal C$ 是当前接触集合，求和把各处接触的作用加起来。

广义力向量的平移分量是力，转动分量是力矩，单位并不全相同。有些接触模型还允许接触处传递力矩，这时 $/lambda_i$ 使用六维力旋量：包含三个力分量和三个力矩分量，相应 $J_i$ 也必须匹配。

身体朝向可用四元数等坐标表示，因此配置坐标与速度坐标不一定同维，不能一律写成 $v=/dot q$。各力与 Jacobian 需使用相容坐标系。这条动力学关系本身不提供稳定性或安全保证。


**成立条件。** 这是标准刚体动力学建模。实际接触刚度、摩擦、执行器响应和状态估计是否准确，需要另外处理。

**相似与差别。** 挂载臂、用腿操作、固定夹爪、人形都可能有全身耦合，但自由度、足支撑和执行器能力不同。不能把一个形态的控制结果直接当成另一个形态的性能。

**可区分实验。** 在相同手端参考下改变身体运动和抬腿阶段，同时记录世界坐标下的手端误差、足接触、身体姿态和接触力。

**来源与用途。**

- [ETH Multi-Contact](../literature-map.html#paper=2308.09179) · [PDF](../papers/2308.09179_Versatile_Multi-Contact_Planning_and_Control_for_Legged_Loco-Manipulation.pdf)：§III 的机器人—物体动力学与接触建模；基础模型的应用。
- [Arm-dynamics NMPC](../literature-map.html#paper=2507.22042) · [PDF](../papers/2507.22042_A_Nonlinear_MPC_Framework_for_Loco-Manipulation_of_Quadrupedal_Robots_with_Non-Negligible_Manipulator_Dynamics.pdf)：NMPC framework 的模型推导；臂动力学近似的实例。

前置：无。
关联／后续：[K02 参考坐标系决定控制器究竟在保持什么](#k02)；[K03 冗余运动：同一个手端目标不只一个全身姿态](#k03)；[K04 关节角度、速度与力矩是不同的动作接口](#k04)；[K05 轨迹规划、MPC 与 WBC 的决策范围](#k05)；[K07 位置准确、保持接触与力准确分别是什么](#k07)；[K10 离散接触模式与连续运动需要共同安排](#k10)；[K36 物体反作用力的预测与反馈](#k36)

<a id="k02"></a>
#### K02 参考坐标系决定控制器究竟在保持什么
类型：领域基础。

**问题。** 同一个‘手端位置不变’，可能指相对身体不变，也可能指相对柜门或世界不变。身体开始俯仰或迈步时，这些要求不再等价。

手端在世界中的位置由身体位置、身体旋转以及臂的正运动学共同决定。若目标固定在身体坐标系，控制器可以正确跟踪这个目标，同时让手端在世界中移动。若物体固定在世界，则应把物体参考经当前身体位姿转换后交给控制器，或直接采用世界／任务坐标的跟踪误差。

改变坐标表示本身不改变物理任务；但如果目标随身体重置、变换有延迟或误差定义随身体姿态改变，训练和反馈就会改变。Deep WBC 的高度／roll／pitch 不随动参考仍随水平位置与 yaw；UMI on Legs 的任务坐标轨迹有不同的保持要求，不能统称‘固定坐标系’。

Multi-Terrain WBC把位置目标留在身体坐标，只使朝向对齐重力；因此适合端物体过坡，不能将其身体坐标位置误差当成固定面板上的世界接触误差。此时看起来都是“task-consistent”，任务定义却不同。

**数学表达与变量。**

$$
p_E^{W}=p_B^{W}+R_{WB}p_E^{B}(q_a)
$$

$$
T_{WE}=T_{WB}T_{BE}(q_a)
$$

$W,B,E$ 分别表示世界、身体和末端坐标系；$q_a$ 是臂关节配置。$R_{WB}$ 将身体坐标的向量旋转到世界坐标；$T_{AB}$ 是把 $B$ 坐标变换到 $A$ 坐标的齐次位姿变换。

第一式描述位置，第二式同时描述位置与朝向。目标附着在世界、身体或物体上，是任务要求的区别；改变同一目标的坐标表示不改变物理要求。

变换需使用一致的时间戳与外参；世界坐标表示不能自动消除世界定位的漂移。


**成立条件。** 需要变换的时间戳、相机外参和身体状态一致。世界参考并不会自动消除定位漂移。

**相似与差别。** 球坐标、笛卡尔坐标和位姿矩阵可表示同一目标；‘目标附着在哪里’和‘有哪些信息被控制器观测到’才是应比较的区别。

**可区分实验。** 冻结同一世界目标，依次只改变身体高度、俯仰、yaw 和平移，检查各方法究竟保持了哪个参考。

**来源与用途。**

- [Deep WBC](../literature-map.html#paper=2210.10044) · [PDF](../papers/2210.10044_Deep_Whole-Body_Control_Learning_a_Unified_Policy_for_Manipulation_and_Locomotion.pdf)：Unified policy 的 command frame；部分不随身体姿态的参考。
- [UMI on Legs](../literature-map.html#paper=2407.10353) · [PDF](../papers/2407.10353_UMI_on_Legs_Making_Manipulation_Policies_Mobile_with_Manipulation-Centric_Whole-body_Controllers.pdf)：§3 Task-space WBC 与附录；任务坐标轨迹。
- [Learning Visual Quadrupedal ](../literature-map.html#paper=2403.20328) · [PDF](../papers/2403.20328_Learning_Visual_Quadrupedal_Loco-Manipulation_from_Demonstrations.pdf)：§III-B(d)；视觉规划与低层使用不同参考系。
- [Reinforcement Learning Based](../literature-map.html#paper=2610.23548) · [PDF](../papers/2610.23548_Reinforcement_Learning_Based_Multi-Terrain_Adaptive_Whole-Body_Control_for_a_Quadruped_Manipulator.pdf)：§II-B；§IV-B2/3；身体位置＋重力朝向的混合参考。
- [Whole-body Pose Tracking](../literature-map.html#paper=2409.16048) · [PDF](../papers/2409.16048_Whole-body_End-Effector_Pose_Tracking.pdf)：§III-C/D；工具上三个不共线点统一位置与朝向误差。

前置：[K01 浮动基、足接触与手端运动的耦合](#k01)
关联／后续：[K03 冗余运动：同一个手端目标不只一个全身姿态](#k03)；[K37 训练可预测的步态，再辨识闭环响应](#k37)；[K45 释放时刻不确定时，怎样仍命中目标](#k45)；[K20 未来末端轨迹预览与时间一致性](#k20)；[K25 低频观测、高频反馈与时间戳](#k25)；[K28 示范迁移必须处理坐标、形态与动作差异](#k28)；[K41 物体相对示范扩增与接触阶段的锚点](#k41)；[K47 高层只给手端目标，还是同时指定身体动作？](#k47)

<a id="k07"></a>
#### K07 位置准确、保持接触与力准确分别是什么
类型：领域基础。

**问题。** 手端误差很小，仍可能向刚性面板施加过大力；受到未知外力时还能走稳，也不表示能按给定数值施力。

自由空间主要关心位姿；接触建立后，误差与环境刚度共同产生作用力。对于刚性环境，小幅过冲也可能带来大力。‘接触适应’还可能只是承受未知外力并保持姿态，和期望力跟踪是不同目标。

位置目标和力目标在同一约束方向可能冲突。混合位置／力控制会在自由方向跟踪位移，在受约束方向调节力；也有方法用虚拟刚度把位置与力需求联系起来。应写出哪个方向受约束、谁给期望力，以及真实反馈来自哪里。

**数学表达与变量。**

$$
F_n/simeq k_{/mathrm{env}}/delta,/qquad /delta=x_E-x_{/mathrm{surface}}/geq 0
$$

这是已经建立接触的一维线性弹性近似。$/delta$ 定义为沿选定法向的压入量，$k_{/mathrm{env}}$ 是环境刚度，$F_n$ 是机器人对环境的压缩力大小；机器人受到反向作用。

未接触时不能把负压入量直接解释成拉力。位置误差、稳态力误差、峰值力与接触丢失是不同指标；该近似未包含摩擦、碰撞冲击或迟滞。


**成立条件。** 必须明确传感器、力的方向与符号，以及接触状态。稳态力误差、峰值力和滑脱是不同评价量。

**相似与差别。** Force Control 2024、统一位置／力 RL 2025、FALCON 的未知外力适应与触觉区域预测并非同一知识点；有时任务表现相似，控制目标仍不同。

**可区分实验。** 在不同环境刚度和摩擦下同时画位置误差与力误差，记录首次接触峰值、接触丢失、任务完成率。

**来源与用途。**

- [Force Control](../literature-map.html#paper=2405.01402) · [PDF](../papers/2405.01402_Learning_Force_Control_for_Legged_Manipulation.pdf)：force tracking 与 position baseline；力目标控制。
- [Position + Force RL](../literature-map.html#paper=2505.20829) · [PDF](../papers/2505.20829_Learning_a_Unified_Policy_for_Position_and_Force_Control_in_Legged_Loco-Manipulation.pdf)：准静态目标构造与实验；统一位置／力目标。
- [FALCON](../literature-map.html#paper=2505.06776) · [PDF](../papers/2505.06776_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation.pdf)：§3、§4；未知外力适应。
- [Whole-Body ID-MPC](../literature-map.html#paper=2511.19709) · [PDF](../papers/2511.19709_Whole-Body_Inverse_Dynamics_MPC_for_Legged_Loco-Manipulation.pdf)：§VI-C；有力目标和接触案例，但无独立施力测量。

前置：[K01 浮动基、足接触与手端运动的耦合](#k01)；[K04 关节角度、速度与力矩是不同的动作接口](#k04)
关联／后续：[K08 柔顺控制规定受力后怎样运动](#k08)；[K09 无力传感器时，估计到的到底是什么](#k09)；[K11 抗扰裕量是在扰动发生前保留余地](#k11)；[K36 物体反作用力的预测与反馈](#k36)；[K39 触觉、握力与接触释放](#k39)；[K24 机构约束与在线交互辨识](#k24)

### 2. 接触与可行性
区分跟踪目标、维持接触、调节作用力和满足约束。

<a id="k07"></a>
#### K07 位置准确、保持接触与力准确分别是什么
类型：领域基础。

**问题。** 手端误差很小，仍可能向刚性面板施加过大力；受到未知外力时还能走稳，也不表示能按给定数值施力。

自由空间主要关心位姿；接触建立后，误差与环境刚度共同产生作用力。对于刚性环境，小幅过冲也可能带来大力。‘接触适应’还可能只是承受未知外力并保持姿态，和期望力跟踪是不同目标。

位置目标和力目标在同一约束方向可能冲突。混合位置／力控制会在自由方向跟踪位移，在受约束方向调节力；也有方法用虚拟刚度把位置与力需求联系起来。应写出哪个方向受约束、谁给期望力，以及真实反馈来自哪里。

**数学表达与变量。**

$$
F_n/simeq k_{/mathrm{env}}/delta,/qquad /delta=x_E-x_{/mathrm{surface}}/geq 0
$$

这是已经建立接触的一维线性弹性近似。$/delta$ 定义为沿选定法向的压入量，$k_{/mathrm{env}}$ 是环境刚度，$F_n$ 是机器人对环境的压缩力大小；机器人受到反向作用。

未接触时不能把负压入量直接解释成拉力。位置误差、稳态力误差、峰值力与接触丢失是不同指标；该近似未包含摩擦、碰撞冲击或迟滞。


**成立条件。** 必须明确传感器、力的方向与符号，以及接触状态。稳态力误差、峰值力和滑脱是不同评价量。

**相似与差别。** Force Control 2024、统一位置／力 RL 2025、FALCON 的未知外力适应与触觉区域预测并非同一知识点；有时任务表现相似，控制目标仍不同。

**可区分实验。** 在不同环境刚度和摩擦下同时画位置误差与力误差，记录首次接触峰值、接触丢失、任务完成率。

**来源与用途。**

- [Force Control](../literature-map.html#paper=2405.01402) · [PDF](../papers/2405.01402_Learning_Force_Control_for_Legged_Manipulation.pdf)：force tracking 与 position baseline；力目标控制。
- [Position + Force RL](../literature-map.html#paper=2505.20829) · [PDF](../papers/2505.20829_Learning_a_Unified_Policy_for_Position_and_Force_Control_in_Legged_Loco-Manipulation.pdf)：准静态目标构造与实验；统一位置／力目标。
- [FALCON](../literature-map.html#paper=2505.06776) · [PDF](../papers/2505.06776_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation.pdf)：§3、§4；未知外力适应。
- [Whole-Body ID-MPC](../literature-map.html#paper=2511.19709) · [PDF](../papers/2511.19709_Whole-Body_Inverse_Dynamics_MPC_for_Legged_Loco-Manipulation.pdf)：§VI-C；有力目标和接触案例，但无独立施力测量。

前置：[K01 浮动基、足接触与手端运动的耦合](#k01)；[K04 关节角度、速度与力矩是不同的动作接口](#k04)
关联／后续：[K08 柔顺控制规定受力后怎样运动](#k08)；[K09 无力传感器时，估计到的到底是什么](#k09)；[K11 抗扰裕量是在扰动发生前保留余地](#k11)；[K36 物体反作用力的预测与反馈](#k36)；[K39 触觉、握力与接触释放](#k39)；[K24 机构约束与在线交互辨识](#k24)

### 3. 控制策略怎样学到
把结构、训练信号与部署信息分别讨论。

<a id="k43"></a>
#### K43 策略、回报、评价网络与信用分配
类型：领域基础。

**问题。** 论文都写PPO、critic和reward时，应知道这些是训练工具，不能把用了同一种算法当成相同控制方法，也不能把回报更高直接当成任务更可靠。

策略π把可得观测与任务条件映射为动作分布。强化学习用交互后的回报改进策略；评价网络估计在当前状态后还能取得多少回报。优势表示一个动作相对当前基准有多好，用于决定提高还是降低其概率。PPO限制一次更新的概率比变化，以减少训练突变；这种限制作用于策略更新，不是机器人接触力的硬约束。

不同论文可共享PPO，却改变动作空间、观测、奖励、先验和状态分布。critic是训练期的价值估计器，不一定部署；多个critic、多个动作头与多个独立策略是不同结构。奖励中的力矩／动作平滑惩罚表达偏好，不保证每一步满足上限。

**数学表达与变量。**

$$
J(/pi)=/mathbb E_{/pi}/!/left[/sum_{t=0}^{/infty}/gamma^tr_t/right],/qquad A^/pi(s,a)=Q^/pi(s,a)-V^/pi(s)
$$

$$
/rho_t(/theta)=/frac{/pi_/theta(a_t/mid o_t)}{/pi_{/theta_{/mathrm{old}}}(a_t/mid o_t)}
$$

$$
L^{/mathrm{CLIP}}(/theta)=/widehat{/mathbb E}_t/!/left[/min/!/left(/rho_t(/theta)/widehat A_t,/operatorname{clip}/!/left(/rho_t(/theta),1-/epsilon,1+/epsilon/right)/widehat A_t/right)/right]
$$

$r_t$ 是奖励，$0/leq/gamma<1$ 是折扣，$Q^/pi,V^/pi$ 是动作与状态价值，$A^/pi$ 是优势。有限回合可使用对应有限时域和终端定义。

$/rho_t$ 是新旧策略对采样动作的概率比，$/widehat A_t$ 是优势估计，$/epsilon>0$ 是裁剪参数；$/widehat{/mathbb E}_t$ 表示批次样本平均。PPO 最大化该裁剪代理目标，完整训练还可含价值与熵项。

裁剪代理目标不严格保证概率比始终处于 $[1-/epsilon,1+/epsilon]$，更不约束实机每步接触力或力矩。策略可用观测与评价网络可用状态仍需分别记录。


**成立条件。** 回报的目标、量纲、权重、终止条件和训练预算决定学到的行为。动作概率裁剪不能替代物理约束。

**相似与差别。** 方法贡献通常在任务接口、控制结构或训练信息，而非首次使用PPO。论文给出的critic特权状态不等于部署策略也能读到。

**可区分实验。** 固定接口、任务与预算，再比较训练改动；分别报告回报和实际成功、跟踪、力、效率指标，并保留多种子。

**来源与用途。**

- [Deep WBC](../literature-map.html#paper=2210.10044) · [PDF](../papers/2210.10044_Deep_Whole-Body_Control_Learning_a_Unified_Policy_for_Manipulation_and_Locomotion.pdf)：§2.1/2.2；动作组优势和非对称训练。
- [Pedipulate](../literature-map.html#paper=2402.10837) · [PDF](../papers/2402.10837_Pedipulate_Enabling_Manipulation_Skills_using_a_Quadruped_Robots_Leg.pdf)：§III；足端任务用标准策略优化。
- [Multi-critic Learning for Wh](../literature-map.html#paper=2507.08656) · [PDF](../papers/2507.08656_Multi-critic_Learning_for_Whole-body_End-effector_Twist_Tracking.pdf)：Method；多回报评价。
- [PPO](../literature-map.html#paper=1707.06347) · [PDF](../papers/1707.06347_Proximal_Policy_Optimization_Algorithms.pdf)：§2–6；PPO裁剪概率比与多轮更新原始算法。
- [Learning to Walk in Minutes](../literature-map.html#paper=2109.11978) · [PDF](../papers/2109.11978_Learning_to_Walk_in_Minutes_Using_Massively_Parallel_Deep_Reinforcement_Learning.pdf)：训练设置／消融；大规模并行PPO与任务课程。
- [Asymmetric Actor-Critic](../literature-map.html#paper=1710.06542) · [PDF](../papers/1710.06542_Asymmetric_Actor_Critic_for_Image-Based_Robot_Learning.pdf)：方法；非对称actor／critic的训练信息分配。

前置：[K04 关节角度、速度与力矩是不同的动作接口](#k04)
关联／后续：[K13 统一策略、协作策略与模型分工](#k13)；[K44 示范监督与闭环数据分布](#k44)；[K15 特权训练、历史估计与视觉学生](#k15)；[K48 可微动力学代理用于训练全身跟踪策略](#k48)

<a id="k13"></a>
#### K13 统一策略、协作策略与模型分工
类型：方法机制。

**问题。** 腿和臂的动作互相影响，但未必必须由一个网络直接输出全部关节。策略结构要解决的是信息与控制权限怎样分配。

统一策略共同接收目标并输出所有动作；协作策略分别输出腿和臂动作，同时交换身体姿态请求或共享全身观测；模型分工则可让腿由 RL 控制、臂由逆运动学或模型控制。一个网络与两个网络的区别本身并不确定协调效果，关键是每一方能看到什么、请求什么、改变什么。

RoboDuet 允许臂请求身体 roll／pitch；FALCON 的上下身策略共享观测但采用不同奖励；Terrain-aware WBC 的臂仍通过 IK 执行。它们都处理分工，但不是同一个学习结构。冻结步态后，操作层只能通过该步态已有的条件接口调节身体，不能通过重新训练扩展低层已有能力；冻结的条件策略仍可按mask／目标产生已有接触行为。

**数学表达与变量。**

$$
a=/pi(o,c_B,c_E)
$$

$$
/begin{aligned}(a_a,c_{/mathrm{posture}})&=/pi_a(o_a,g),//a_{/mathrm{legs}}&=/pi_{/mathrm{legs}}(o_{/mathrm{legs}},c_{/mathrm{posture}})./end{aligned}
$$

第一式表示统一动作接口，$o$ 是观测，$c_B,c_E$ 是身体与末端条件。第二式仅示意带姿态请求的协作接口：臂策略输出臂动作 $a_a$ 与姿态请求，腿策略根据请求输出腿动作。

这是结构记号，不是统一策略与协作策略等价的证明，也不表示所有双策略论文都交换姿态请求。模型分工还可以让操作肢体由逆运动学或模型控制执行。

应另外记录各模块的观测、奖励、训练是否联合，以及冻结低层后仍可调用的条件接口。


**成立条件。** 需要记录是否联合训练、共享奖励／观测、冻结哪些模块，以及部署动作维度。

**相似与差别。** 把不同网络命名为 agent、expert 或 policy 不构成独立知识；若决策变量、信息和训练目标一致，应放进同一结构类别，再比较实现。

**可区分实验。** 在同一机器人、目标和训练预算下比较联合、协作与分工；报告学习速度、腿／臂各自误差和受扰动后的行为。

**来源与用途。**

- [Deep WBC](../literature-map.html#paper=2210.10044) · [PDF](../papers/2210.10044_Deep_Whole-Body_Control_Learning_a_Unified_Policy_for_Manipulation_and_Locomotion.pdf)：Unified policy；全关节策略。
- [RoboDuet](../literature-map.html#paper=2403.17367) · [PDF](../papers/2403.17367_RoboDuet_Learning_a_Cooperative_Policy_for_Whole-body_Legged_Loco-Manipulation.pdf)：§III-A/B；姿态请求协作。
- [FALCON](../literature-map.html#paper=2505.06776) · [PDF](../papers/2505.06776_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation.pdf)：§3.1；共享观测、独立目标。
- [Terrain-Aware WBC](../literature-map.html#paper=2605.31343) · [PDF](../papers/2605.31343_Learning_Terrain-Aware_Whole-Body_Control_for_Perceptive_Legged_Loco-Manipulation.pdf)：controller architecture；腿 RL 与臂 IK。
- [FALCON (quadruped)](../literature-map.html#paper=2512.04381) · [PDF](../papers/2512.04381_FALCON_Actively_Decoupled_Visuomotor_Policies_for_Loco-Manipulation_with_Foundation-Model-Based_Coordination.pdf)：§IV-A/D；双专用动作流由共享语义与阶段条件协调。
- [Walk These Ways](../literature-map.html#paper=2212.03238) · [PDF](../papers/2212.03238_Walk_These_Ways_Tuning_Robot_Control_for_Generalization_with_Multiplicity_of_Behavior.pdf)：§3.1/3.2；可解释行为条件作为高层／低层接口。

前置：[K03 冗余运动：同一个手端目标不只一个全身姿态](#k03)；[K04 关节角度、速度与力矩是不同的动作接口](#k04)；[K43 策略、回报、评价网络与信用分配](#k43)
关联／后续：[K38 肢体角色分配与给定角色的执行](#k38)；[K14 分层接口把学习任务限制在某个动作空间](#k14)；[K15 特权训练、历史估计与视觉学生](#k15)；[K16 多目标奖励与多评价网络不等于多个物理机制](#k16)；[K46 用可调行为保留同一任务的多种运动解](#k46)

### 4. 从观测到操作目标
理解视觉、导航、机构模型怎样连接动作。

<a id="k20"></a>
#### K20 未来末端轨迹预览与时间一致性
类型：方法机制。

**问题。** 只看到当前目标，控制器要等误差出现才调整身体。手端即将离开当前工作范围时，可能已经来不及迈步或改变姿态。

给低层未来若干末端目标可让它提前分配身体和臂动作。预览长度、轨迹采样频率与目标所在参考系共同构成接口。它不是无条件的‘记忆’：预览描述未来计划，历史描述过去观测。

如果高层慢、低层快，未来轨迹必须按时间戳一致地执行。预测轨迹被替换时，旧动作和新动作的连续性也要处理。UMI on Legs 的预览、视觉足端示范的后续点、MLM 缺少未来目标时的训练设计都属于这个接口问题，具体信息供给不同。

Accurate Throwing将100 Hz全身名义策略冻结，再用400 Hz臂关节残差补偿短释放窗口中的误差。高频有助于更及时使用反馈，但需匹配训练、状态估计和执行器；作者实机改善明显弱于仿真，并指出残差可能过拟合模型。

**数学表达与变量。**

$$
/Xi_t=/bigl(/xi(t),/xi(t+/Delta t),/ldots,/xi(t+H/Delta t)/bigr)
$$

$/Xi_t$ 是低层可读取的未来参考序列，$/xi$ 是任务轨迹，$H$ 是预览步数，$/Delta t$ 是参考采样间隔。

预览描述未来计划，历史描述过去观测，二者不能互称记忆。轨迹替换、时间戳、参考坐标和错误预览都影响执行。


**成立条件。** 预览通常来自高层模型或示范，在实时随机目标下不一定可得；错误预览会导致提前做错。

**相似与差别。** 位置＋速度监督改善局部轨迹一致性；未来目标预览改善提前决策；低通滤波改变输入频谱。应分别消融。 TONAV的速度监督并不自动意味着部署速度头控制了真实关节；原文执行用途需与训练损失分别记录。

**可区分实验。** 用相同轨迹比较零预览、正确预览和错误预览，测相位滞后、身体提前动作与接触误差。

**来源与用途。**

- [UMI on Legs](../literature-map.html#paper=2407.10353) · [PDF](../papers/2407.10353_UMI_on_Legs_Making_Manipulation_Policies_Mobile_with_Manipulation-Centric_Whole-body_Controllers.pdf)：look-ahead tracking／ablation；未来轨迹条件。
- [Learning Visual Quadrupedal ](../literature-map.html#paper=2403.20328) · [PDF](../papers/2403.20328_Learning_Visual_Quadrupedal_Loco-Manipulation_from_Demonstrations.pdf)：§III-D；未来足端点。
- [MLM](../literature-map.html#paper=2508.10538) · [PDF](../papers/2508.10538_MLM_Learning_Multi-task_Loco-Manipulation_Whole-Body_Control_for_Quadruped_Robot_with_Arm.pdf)：multi-task tracking design；轨迹供给条件。
- [Accurate Throwing](../literature-map.html#paper=2506.16986) · [PDF](../papers/2506.16986_Learning_Accurate_Whole-body_Throwing_with_High-frequency_Residual_Policy_and_Pullback_Tube_Acceleration.pdf)：§III-A/B；§IV-F/G；100 Hz名义全身策略＋400 Hz臂残差。
- [Diffusion Policy](../literature-map.html#paper=2303.04137) · [PDF](../papers/2303.04137_Diffusion_Policy_Visuomotor_Policy_Learning_via_Action_Diffusion.pdf)：方法／滚动执行；条件扩散生成未来动作序列。
- [Original UMI](../literature-map.html#paper=2402.10329) · [PDF](../papers/2402.10329_Universal_Manipulation_Interface_In-The-Wild_Robot_Teaching_Without_In-The-Wild_Robots.pdf)：动作表示／延迟匹配；手持示范到相对末端轨迹。

前置：[K02 参考坐标系决定控制器究竟在保持什么](#k02)；[K14 分层接口把学习任务限制在某个动作空间](#k14)
关联／后续：[K45 释放时刻不确定时，怎样仍命中目标](#k45)；[K21 视觉策略可以学控制，也可以只学操作参考](#k21)；[K27 动作块、重规划与平滑的精度—效率取舍](#k27)

### 5. VLA、数据与闭环执行
确定动作模型负责什么，以及何时根据结果更新。

<a id="k26"></a>
#### K26 语言规划、技能选择与 VLA 动作生成
类型：领域基础。

**问题。** 带语言指令的系统可能只是在已有技能里选一个，也可能直接生成动作。二者训练数据、失败类型和控制权限不同。

VLM／语言规划器可根据图像和指令输出目标、步骤或技能编号，技能内部动作由其他模块产生。VLA 将视觉、语言等观测映射到动作表示，例如关节目标、末端轨迹或全身潜动作；潜动作仍需一个解码器或快速控制器执行。

WildLMa 主要把示教技能与语言任务规划组合；KINO 选择关键姿态给控制器；WholeBodyVLA 学全身潜动作。把高层规划器改成大模型不自动改变低层接触能力。VLA 输出是否包含底盘动作、是否真正参与移动物体，必须从运行接口与实验核查。

SayCan在离散技能层选择可执行步骤；RT-1以真实机器人多任务数据训练动作token模型，RT-2把互联网视觉语言任务和机器人动作token联合微调；Open X-Embodiment整合跨机器人轨迹，Octo和OpenVLA从这些数据训练不同通用策略；π0用流匹配产生连续动作块。数据来源、动作格式和底层执行权限不同，原始模型的实机实验不能直接当作四足足接触证据。

**结构与说明。**

语言规划器或 VLM 可以选择技能、关键姿态或步骤，连续动作由已有模块产生；VLA 则根据视觉、语言等条件生成动作表示，再由执行器或低层控制器执行。

这是模型权限与运行接口的区别。不能用同一个抽象箭头把技能选择和连续全身动作生成写成同一方法。


**成立条件。** 模型名称不说明动作空间。应列出语言在哪里进入、动作频率、输出维度和复用低层。

**相似与差别。** 语言分解能力、动作策略泛化和低层控制准确性是不同贡献；不同平台的任务成功率不能直接排名。 DECOWAM联合建模未来视频与动作，但没有据预测视频作显式在线MPC搜索；生成模型和预测规划应按实际执行图区分。

**可区分实验。** 固定技能库和低层比较任务规划；固定任务指令与动作空间比较 VLA；对新对象、新组合、新动作分别测试。

**来源与用途。**

- [WildLMa](../literature-map.html#paper=2411.15131) · [PDF](../papers/2411.15131_WildLMa_Long_Horizon_Loco-Manipulation_in_the_Wild.pdf)：task planner／skill library；语言规划。
- [KINO](../literature-map.html#paper=2609.18869) · [PDF](../papers/2609.18869_KINO_A_Keyframe_Interface_for_VLM_Planning_and_Whole-Body_Control_in_Humanoid_Loco-Manipulation.pdf)：keyframe interface；VLM 选择姿态。
- [WholeBodyVLA](../literature-map.html#paper=2512.11047) · [PDF](../papers/2512.11047_WholeBodyVLA_Towards_Unified_Latent_VLA_for_Whole-Body_Loco-Manipulation_Control.pdf)：latent action architecture；VLA 全身动作。
- [VLA 综述](../literature-map.html#paper=survey-vla) · [PDF](../papers/2405.14093_A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI.pdf)：模型与动作接口分类；定义依据。
- [FALCON (quadruped)](../literature-map.html#paper=2512.04381) · [PDF](../papers/2512.04381_FALCON_Actively_Decoupled_Visuomotor_Policies_for_Loco-Manipulation_with_Foundation-Model-Based_Coordination.pdf)：§IV-D；CLIP条件扩散动作流，区别于语义技能选择。
- [SayCan](../literature-map.html#paper=2204.01691) · [PDF](../papers/2204.01691_Do_As_I_Can_Not_As_I_Say_Grounding_Language_in_Robotic_Affordances.pdf)：方法／真机长程任务；语言相关性与技能可行性联合选择。
- [RT-1](../literature-map.html#paper=2212.06817) · [PDF](../papers/2212.06817_RT-1_Robotics_Transformer_for_Real-World_Control_at_Scale.pdf)：方法／实机多任务；视觉语言条件下动作token的机器人Transformer。
- [RT-2](../literature-map.html#paper=2307.15818) · [PDF](../papers/2307.15818_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control.pdf)：方法／实机语义泛化；图文与机器人动作token联合微调的VLA。
- [Open X-Embodiment](../literature-map.html#paper=2310.08864) · [PDF](../papers/2310.08864_Open_X-Embodiment_Robotic_Learning_Datasets_and_RT-X_Models.pdf)：数据集／RT-X评估；跨机器人统一数据与模型。
- [Octo](../literature-map.html#paper=2405.12213) · [PDF](../papers/2405.12213_Octo_An_Open-Source_Generalist_Robot_Policy.pdf)：方法／九平台适配；开放通用策略的目标图像／语言条件。
- [OpenVLA](../literature-map.html#paper=2406.09246) · [PDF](../papers/2406.09246_OpenVLA_An_Open-Source_Vision-Language-Action_Model.pdf)：方法／实机评估；视觉语言到离散动作token。
- [π0](../literature-map.html#paper=2410.24164) · [PDF](../papers/2410.24164_Pi0_A_Vision-Language-Action_Flow_Model_for_General_Robot_Control.pdf)：方法／真机评估；视觉语言条件下连续动作流匹配。

前置：[K14 分层接口把学习任务限制在某个动作空间](#k14)；[K21 视觉策略可以学控制，也可以只学操作参考](#k21)
关联／后续：[K27 动作块、重规划与平滑的精度—效率取舍](#k27)；[K28 示范迁移必须处理坐标、形态与动作差异](#k28)；[K30 执行过、完成了与记忆可观测性](#k30)；[K31 力信息进入 VLA 的位置决定它能改什么](#k31)；[K47 高层只给手端目标，还是同时指定身体动作？](#k47)

<a id="k27"></a>
#### K27 动作块、重规划与平滑的精度—效率取舍
类型：方法机制。

**问题。** 一次生成未来一段动作可减少推理负担并改善连续性；但新接触或失败发生后，继续执行旧动作会延迟反应。

动作块包含未来 H 个动作，只执行前 M 个再更新；H、M 与推理／通信延迟一起决定反馈频率。相邻块可以插值、融合或重新计时，减少速度跳变，但平滑会改变轨迹和接触建立时间。

TONAV 在位置块之外监督速度，以改善动作的时间一致性；UMI on Legs 做块间插值；DECOWAM采用联合世界—动作生成；它未单独证明动作块平滑机制。这些设计影响执行效率的环节不同，但更少推理次数、更平滑输出和更高任务成功不必同时成立。TONAV 平台是 Go2-W＋Piper，每任务五次真机；不能据此断言换步接触安全已解决。

Ψ₀的RTC在训练时给模型已承诺动作前缀，部署时对齐异步推理；这与普通低通／块间插值不同。其最后一步RTC消融成功仍9/10，主要改善平顺性，未证明成功率进一步提高。

**数学表达与变量。**

$$
A_t=/bigl(a_{t/mid t},a_{t+1/mid t},/ldots,a_{t+H-1/mid t}/bigr)
$$

$$
u_{t+j}=a_{t+j/mid t},/qquad j=0,/ldots,M-1,/qquad 1/leq M/leq H
$$

$A_t$ 是在时刻 $t$ 生成的长度为 $H$ 的动作块，$a_{k/mid t}$ 表示当时预测的第 $k$ 步动作；$u$ 是实际执行输入，仅执行前 $M$ 步后再更新。

上式描述同步块执行的基本接口。异步推理还需对齐已承诺前缀与时间戳；平滑、插值和速度监督是另外的改动，不能从动作块记号推出。


**成立条件。** 平滑需在正确参考坐标和时间基准上进行。动作被取消、重启和延迟时，应有一致的执行状态。

**相似与差别。** 增加速度监督是训练信号改动；降低执行 M 是调度改动；力反馈在低层修正是闭环改动。不能合并成‘轨迹更丝滑’。

**可区分实验。** 固定模型比较 H／M、平滑、异步推理和反馈通道，测动作 jerk、延迟、峰值力、任务时间和成功率。

**来源与用途。**

- [TONAV](../literature-map.html#paper=2608.22296) · [PDF](../papers/2608.22296_TONAV_Task-Oriented_Navigation_and_Action-Velocity_Chunk_Learning_for_Articulated_Object_Quadrupedal_Mobile_Manipulation.pdf)：action-velocity chunk loss／real experiments；轮足速度监督。
- [UMI on Legs](../literature-map.html#paper=2407.10353) · [PDF](../papers/2407.10353_UMI_on_Legs_Making_Manipulation_Policies_Mobile_with_Manipulation-Centric_Whole-body_Controllers.pdf)：App §9；动作块衔接。
- [Ψ₀](../literature-map.html#paper=paper-66) · [PDF](../papers/RSS_2026_Psi0_An_Open_Foundation_Model_Towards_Universal_Humanoid_Loco-Manipulation.pdf)：RTC implementation／ablation；异步动作前缀对齐；承诺前缀与异步块对齐。
- [ACT / ALOHA](../literature-map.html#paper=2304.13705) · [PDF](../papers/2304.13705_Learning_Fine-Grained_Bimanual_Manipulation_with_Low-Cost_Hardware.pdf)：§III／实机任务；ACT动作块与时间集成。
- [Diffusion Policy](../literature-map.html#paper=2303.04137) · [PDF](../papers/2303.04137_Diffusion_Policy_Visuomotor_Policy_Learning_via_Action_Diffusion.pdf)：方法／实机任务；扩散动作序列滚动执行。
- [RT-1](../literature-map.html#paper=2212.06817) · [PDF](../papers/2212.06817_RT-1_Robotics_Transformer_for_Real-World_Control_at_Scale.pdf)：方法；序列模型预测离散动作。
- [RT-2](../literature-map.html#paper=2307.15818) · [PDF](../papers/2307.15818_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control.pdf)：方法；图文／动作文本token统一预测。
- [OpenVLA](../literature-map.html#paper=2406.09246) · [PDF](../papers/2406.09246_OpenVLA_An_Open-Source_Vision-Language-Action_Model.pdf)：动作token接口；离散动作预测对照。
- [π0](../literature-map.html#paper=2410.24164) · [PDF](../papers/2410.24164_Pi0_A_Vision-Language-Action_Flow_Model_for_General_Robot_Control.pdf)：动作专家；连续动作块对照。

前置：[K20 未来末端轨迹预览与时间一致性](#k20)；[K25 低频观测、高频反馈与时间戳](#k25)；[K26 语言规划、技能选择与 VLA 动作生成](#k26)
关联／后续：[K31 力信息进入 VLA 的位置决定它能改什么](#k31)

