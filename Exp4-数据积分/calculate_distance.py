import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
import os


def main():
    try:
        # 获取当前文件所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 构建数据文件相对路径，假设数据文件和此脚本在同一目录
        data_file = os.path.join(current_dir, 'Velocities.txt')
        # 读取数据
        data = np.loadtxt(data_file)
        t = data[:, 0]  # 时间列
        v = data[:, 1]  # 速度列
        # 计算总距离，使用np.trapezoid替代np.trapz
        total_distance = np.trapezoid(v, t)
        print(f"总运行距离: {total_distance:.2f} 米")
        # 计算累积距离
        distance = cumulative_trapezoid(v, t, initial=0)
        # 绘制图表
        plt.figure(figsize=(10, 6))
        plt.plot(t, v, 'b-', label='Velocity (m/s)')
        plt.plot(t, distance, 'r--', label='Distance (m)')
        plt.title('Velocity and Distance vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s) / Distance (m)')
        plt.legend()
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print(f"错误：找不到数据文件 {data_file}")
        print("请确保数据文件存在于项目目录中")


if __name__ == '__main__':
    main()

