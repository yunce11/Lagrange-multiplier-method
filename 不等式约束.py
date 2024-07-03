#引入库文件
import sympy
from sympy import *

#设置变量，mu为拉格朗日乘子μ
x1,x2,mu=symbols('x1 x2 mu')

#设置函数f、约束条件g
f = x1**2 + x2**2
g = x1+x2+2

#构建拉格朗日方程L
L = f + mu * g

#求各个偏导
diffs=[diff(L, var) for var in [x1, x2, mu]]

#偏导取零，求解
m=solve(diffs, (x1, x2, mu), dict=True,real=True)

#用KKT条件筛选可行解
m_valid = []
for sol in m:
    if g.subs(sol) <= 0 and mu.subs(sol) >= 0 and g.subs(sol)*mu==0:
#KKT条件：1、g(x)小于等于0； 2、u大于等于零； 3、g(x)·μ等于0
        m_valid.append(sol)

#赋值并输出结果
f_min= [f.subs(sol) for sol in m_valid]
if f_min:
    print("f最小值:",f_min[0])
    print("此时x1、x2的值为:")
    for sol in m_valid:
        print("x1 =", sol[x1], ", x2 =", sol[x2])
else:
    print("限制条件中无解.")
#{f最小值: 2
#此时x1、x2的值为:
#x1 = -1 , x2 = -1}
