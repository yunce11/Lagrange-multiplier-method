import tensorflow as tf

# 目标函数
def f(x, y):
    return (x - 1)**2 + (y - 2)**2

# 约束函数
def h1(x, y):
    return x**2 + y**2 - 4

def h2(x, y):
    return x + y - 3
# 参数初始化
x = tf.Variable(0.0, name='x')  # 使用tf.Variable来自动跟踪梯度
y = tf.Variable(0.0, name='y')
s = tf.Variable(1.0, name='s')  # 松弛变量，保证非负
lambd1 = tf.Variable(0.0, name='lambda1')
lambd2 = tf.Variable(0.0, name='lambda2')
mu1 = 1.0  # 初始惩罚系数
mu2 = 1.0

optimizer = tf.optimizers.SGD(learning_rate=0.01)  # 使用SGD优化器

# 迭代优化
for i in range(1000):
    with tf.GradientTape() as tape:
        # 确保松弛变量s非负
        s.assign(tf.maximum(0.0, s))
        # 增广拉格朗日函数
        L_A = (f(x, y) + lambd1 * h1(x, y) + (mu1 / 2) * (h1(x, y)**2) +
               lambd2 * (h2(x, y) + s**2) + (mu2 / 2) * (h2(x, y) + s**2)**2)
    # 自动计算梯度
    grads = tape.gradient(L_A, [x, y, s, lambd1, lambd2])
    # 应用梯度更新
    optimizer.apply_gradients(zip(grads, [x, y, s, lambd1, lambd2]))

    # 手动更新拉格朗日乘子和松弛变量
    lambd1.assign(lambd1 + mu1 * h1(x, y))
    lambd2.assign(lambd2 + mu2 * (h2(x, y) + s**2))

    if i % 10 == 0:
        print(f"Iteration {i}: x = {x.numpy()}, y = {y.numpy()}, s = {s.numpy()}, lambda1 = {lambd1.numpy()}, lambda2 = {lambd2.numpy()}")

print(f"Optimized x = {x.numpy()}, y = {y.numpy()}")
print(f"Lambda1 = {lambd1.numpy()}, Lambda2 = {lambd2.numpy()}")
print(f"Constraint1 satisfaction (should be close to 0): {h1(x, y).numpy()}")
print(f"Constraint2 satisfaction (should be less than or equal to 0): {h2(x, y).numpy()}")
