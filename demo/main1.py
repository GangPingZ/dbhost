import random
b = ['三星', '华为', '荣耀']
random.seed(0)
name = b[random.randint(0, 2)]
print(name)


"""题库二-42"""
# import jieba
# s = input("请输入一个字符串")
# n = len(s)
# m = len(jieba.lcut(s))
# print("中文字符数为：{}，中文词语数为：{}。".format(n, m))


"""题库二-43"""
# n = eval(input("请输入购买数数量"))
# if n == 1:
#     cost = n*150
# elif n==2 or n==3:
#     cost = int(n * 150 * 0.9)
# elif n >= 4 and n <= 9:
#     cost = int(n * 150 * 0.8)
# else:
#     cost = int(n * 150 * 0.7)
# print("总金额为：", cost)

"""题库二-44"""







# np.random.seed(0)
# mu, sigma = 100, 20
# a = np.random.normal(mu, sigma, size=100)
#
# plt.hist(a, 20, density=True, histtype='stepfilled', facecolor='b', alpha=0.75)
# plt.title('Histogram')
#
# plt.show()
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)
#
# plt.pie(sizes, explode= explode, labels= labels, autopct='%1.1f%%', shadow=False, startangle=90)
# plt.axis([2, 3, 4, 5])
# plt.show()

# fig = plt.figure(figsize=(12, 6))
# ax = fig.add_subplot(111, projection='3d')
#
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# p1 = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                     linewidth=0, antialiased=False, label='sanwei')
#
# p1._facecolors2d = p1._facecolor3d
# # p1._edgecolors2d = p1._edgecolor3d
# ax.legend()
#
# ax.set_title('World population')
# ax.set_xlabel('Year')
# ax.set_ylabel('Number of people (millions)')
#
# plt.show()

# a = np.arange(0.0, 5.0, 0.02)
# plt.plot(a, np.cos(2*np.pi*a), 'r--')
#
# plt.xlabel('横轴：时间', fontproperties = 'SimHei', fontsize = 15, color = 'green')
# plt.ylabel('纵轴：振幅', fontproperties = 'SimHei', fontsize = 15)
# plt.title(r'正弦波实例$y=cos(2\pi x)$', fontproperties = 'SimHei', fontsize = 25)
# # plt.text(2, 1, r'$\mu=100$', fontsize = 15)
# plt.annotate(r'$\mu=100$', xy = (2, 1), xytext = (3, 1.5), arrowprops=dict(facecolor='black', shrink = 0.1, width = 2))
#
# # plt.axis([-1, 6, -2, 2])
# plt.grid(True)
# plt.show()

# matplotlib.rcParams["font.family"] = 'SimHei'
# plt.plot([3, 1, 4, 5, 2])
# plt.ylabel("纵轴（值）")
# plt.show()
# a = np.arange(10)
# plt.plot((a, a * 1.5, 'go-'), (a, a * 2.5, 'rx'), (a, a * 3.5, '*'), (a, a * 3.5, 'b-'))
# plt.show()

# def f(t):
#     return np.exp(-t)*np.cos(2*np.pi*t)
#
#
# a = np.arange(0.0, 5.0, 0.02)

# plt.subplot(211)
# plt.plot(a, f(a))
# plt.subplot(2, 1, 2)
# plt.plot(a, np.cos(2*np.pi*a), 'r--')
# plt.show()
# av = plt.subplot(3, 2, 4)
# av.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
# av.ylabel("Grade")
# av.axis([-1, 10, 0, 6])
# plt.show()

# plt.plot([3, 1, 4, 5, 2])
# plt.ylabel("Grade")
# plt.savefig("test", dpi = 600)
# plt.show()