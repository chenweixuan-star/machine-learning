import random
data = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10)
]

def compute_loss(data, w, b):
    """计算整个数据集上的总损失（平方和）"""
    loss = 0.0
    for x, y in data:
        pred = w * x + b
        loss += (pred - y) ** 2
    return loss

def gradient_descent(data, w_init=0.0, b_init=0.0, lr=0.1, steps=5, batch_size=3):
    """
        data:list of (x, y) 样本
        w_init: 初始权重 w
        b_init: 初始偏置 b
        lr: 学习率
        steps: 迭代次数
        batch_size: 每个 mini-batch 的大小
        返回: 最终 w, b
    """
    w, b = w_init, b_init
    n = len(data)
    
    print(f"Mini-batch 梯度下降")
    print(f"初始参数: w = {w}, b = {b}")
    print(f"学习率: {lr}, 批次大小: {batch_size}, 总迭代: {steps}")
    print(f"{'Step':<4} {'w':<10} {'b':<10} {'Loss':<10}")
    print("-" * 40)
    
    for step in range(steps):
        batch = random.sample(data, batch_size)  
        
        grad_w = 0.0
        grad_b = 0.0
        
        for x, y in batch:
            pred = w * x + b
            error = pred - y
            grad_w += 2 * error * x   
            grad_b += 2 * error * 1   
        
        w -= lr * grad_w
        b -= lr * grad_b
        
        loss = compute_loss(data, w, b)
        
        print(f"{step+1:<4} {w:<10.4f} {b:<10.4f} {loss:<10.4f}")
    
    return w, b