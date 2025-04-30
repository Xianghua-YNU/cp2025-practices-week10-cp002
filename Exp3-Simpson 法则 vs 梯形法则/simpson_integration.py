import numpy as np
import matplotlib



# 待积分函数
def f(x):
    return x ** 4 - 2 * x + 1


# 梯形法则积分函数
def trapezoidal(f, a, b, N):
    """
    梯形法数值积分
    :param f: 被积函数
    :param a: 积分下限
    :param b: 积分上限
    :param N: 子区间数
    :return: 积分近似值
    """
    h = (b - a) / N
    result = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        result += f(a + i * h)
    return result * h


# Simpson法则积分函数
def simpson(f, a, b, N):
    """
    Simpson法数值积分
    :param f: 被积函数
    :param a: 积分下限
    :param b: 积分上限
    :param N: 子区间数（必须为偶数）
    :return: 积分近似值
    """
    if N % 2 != 0:
        raise ValueError("N 必须为偶数")
    h = (b - a) / N
    result = f(a) + f(b)
    for i in range(1, N, 2):
        result += 4 * f(a + i * h)
    for i in range(2, N - 1, 2):
        result += 2 * f(a + i * h)
    return result * h / 3


def main():
    a, b = 0, 2  # 积分区间
    exact_integral = 4.4  # 精确解

    results = {"N": [], "Trapezoidal": [], "Simpson": [], "Trapezoidal Error": [], "Simpson Error": []}

    for N in [100, 1000]:  # 不同子区间数
        trapezoidal_result = trapezoidal(f, a, b, N)
        simpson_result = simpson(f, a, b, N)

        trapezoidal_error = abs(trapezoidal_result - exact_integral) / exact_integral
        simpson_error = abs(simpson_result - exact_integral) / exact_integral

        results["N"].append(N)
        results["Trapezoidal"].append(trapezoidal_result)
        results["Simpson"].append(simpson_result)
        results["Trapezoidal Error"].append(trapezoidal_error)
        results["Simpson Error"].append(simpson_error)

        print(f"N = {N}")
        print(f"梯形法则结果: {trapezoidal_result:.8f}, 相对误差: {trapezoidal_error:.2e}")
        print(f"Simpson法则结果: {simpson_result:.8f}, 相对误差: {simpson_error:.2e}")
        print("-" * 40)

    # 绘制误差图并保存
    plt.figure()
    plt.loglog(results["N"], results["Trapezoidal Error"], label="Trapezoidal Error", marker='o')
    plt.loglog(results["N"], results["Simpson Error"], label="Simpson Error", marker='s')
    plt.xlabel("Number of Subintervals (N)")
    plt.ylabel("Relative Error")
    plt.title("Error Comparison: Trapezoidal vs Simpson")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.savefig(r"C:\Users\31025\OneDrive\桌面\t\integration_error.png")
    print("图像已保存到 C:\\Users\\31025\\OneDrive\\桌面\\t\\integration_error.png")
    # plt.show()  # 如果需要显示图像，请取消注释此行


if __name__ == '__main__':
    main()
