#引入库文件
import sympy
from sympy import *

#设置变量，lam为拉格朗日乘子λ
x1,x2,lam=symbols('x1 x2 lam')

#设置函数f、约束条件g
f=x1**2+x2**2
g=x1**2*x2-3

#构建拉格朗日方程L
L=f+lam*g

#求L对x_1 、x_2 、λ的偏导
dx1=diff(L,x1)
dx2=diff(L,x2)
dlam=diff(L,lam)

#令各个偏导等于零，并求解
m=solve([dx1,dx2,dlam],(x1,x2,lam),dict=True)
x1_value=[sol[x1] for sol in m if im(sol[x1])==0]
x2_value=[sol[x2] for sol in m if im(sol[x2])==0]
lam_value=[sol[lam] for sol in m if im(sol[lam])==0]

#输出x_1 、x_2 、λ的解
for i in range(0,len(x1_value)):
    print('\n第',i,'组解：\n','x1    x2    lambda','\n',x1_value[i],',',x2_value[i],',',lam_value[i])
#{第 0 组解：
 #x1    x2    lambda
 #-2**(1/6)*3**(1/3) ,2**(2/3)*3**(1/3)/2 ,-2**(1/3)*3**(2/3)/3

#第 1 组解：
 #x1    x2    lambda
 #2**(1/6)*3**(1/3) ,2**(2/3)*3**(1/3)/2 ,-2**(1/3)*3**(2/3)/3}

#观察发现两组解代入原方程，最终结果一致，所以只需求一组解

#将解代入原式，计算得出结果并输出
min_f=f.subs([(x1,x1_value[0]),(x2,x2_value[0])])
min_f = min_f.evalf()
print("f在限制下的最小值:",min_f)
#{f在限制下的最小值: 3.93111209131335}
