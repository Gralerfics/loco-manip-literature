# Deep WBC：ROA 与对偶优化的关系

依据：[Deep Whole-Body Control](../papers/2210.10044_Deep_Whole-Body_Control_Learning_a_Unified_Policy_for_Manipulation_and_Locomotion.pdf) §2.2、参考文献 [27–28]。核查日期：2026-10-24。以下区分原文公式、原文报告的实际训练方式，以及用于理解它的标准优化背景；没有独立运行作者训练代码。

## 先看 ROA 试图解决什么

特权编码器在仿真训练时读取质量、摩擦等环境参数，形成潜变量 $z^/mu$；适应模块根据部署可得的近期传感历史估计 $z^/phi$。如果先自由训练前者，再要求后者模仿，特权编码器可能使用无法从这些历史辨识的信息。ROA 因此既训练适应模块，也反向约束特权编码器，使其表示更容易由部署信息预测。

原文损失为：

$$
/mathcal L(/theta_/pi,/theta_/mu,/theta_/phi)
=-J(/theta_/pi,/theta_/mu)
+/lambda/left/|z^/mu-/operatorname{sg}(z^/phi)/right/|_2
+/left/|/operatorname{sg}(z^/mu)-z^/phi/right/|_2.
$$

$J$ 是策略的强化学习目标；$/theta_/pi,/theta_/mu,/theta_/phi$ 分别是策略、特权编码器、适应模块的参数。$/operatorname{sg}$ 是停止梯度：数值参与计算，但梯度不经过该分支。这里使用二范数，没有平方。

两个距离项的数值相同，但梯度作用不同。第一项距离使特权编码器在有利于控制的同时接近历史网络能预测的表示；第二项距离使历史网络拟合特权编码器当前的输出。$/lambda$ 决定前一种要求的强度，不是物理接触力。

## 标准原始—对偶方法从哪里来

对约束优化 $/min_/theta f(/theta)$，满足 $g(/theta)/leq0$，拉格朗日函数是：

$$
/mathcal L(/theta,/lambda)=f(/theta)+/lambda g(/theta),/qquad/lambda/geq0.
$$

一种标准更新是：

$$
/theta/leftarrow/theta-/eta_/theta/nabla_/theta/mathcal L,
/qquad
/lambda/leftarrow[/lambda+/eta_/lambda g(/theta)]_+.
$$

对参数下降，对乘子上升。违反约束时提高惩罚权重；这是原始—对偶优化的典型思路，常用于资源分配、分布式优化、约束控制和有成本预算的强化学习。ADMM 是相关的变量分裂／乘子方法，不等于任意两个网络的交替训练。

Deep WBC 引用 [27] Levine、Finn、Darrell 与 Abbeel 的 *End-to-End Training of Deep Visuomotor Policies*（JMLR 2016），其中 guided policy search 用 BADMM 形式协调局部控制器与视觉策略；[28] Wang 与 Banerjee 的 *Bregman Alternating Direction Method of Multipliers*（NeurIPS 2014）提供相应优化背景。原文并非声称发明了对偶优化，也没有直接照搬整个 guided policy search 系统。

## 原文实际采用什么

正文先写对策略／特权编码器与适应模块分别最小化，以及对 $/lambda$ 做梯度上升。随后明确报告实际按固定步数交替优化两组网络，并让 $/lambda$ 按固定线性方案从 0 增到 1。因此，实际方式更适合描述为**交替优化，加上逐渐加强的表示一致性正则化**。不是根据当前约束违反程度自动调整乘子的标准实现。

标准约束形式可以要求平均表示误差不超过预算 $/varepsilon$，但这是解释用的重写，原文未明确给出这样的误差预算。若直接对非负距离使用乘子上升，只要距离不为零，乘子就会继续增加。因此不能把原文写的乘子更新式、预定线性权重以及标准凸优化的收敛结论视为完全相同的东西。神经网络和 PPO 的非凸、采样训练也不能自动继承 BADMM 的理论保证。

实际作用是让训练早期先形成可用控制行为，再逐渐要求特权表示能够由部署历史估计。运行时网络权重固定，适应来自历史变化引起的潜变量变化，不是在机器人上继续进行对偶优化或梯度训练。
