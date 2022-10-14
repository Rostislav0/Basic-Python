from pylab import*
x = linspace(-10, 10, 21)
y = x ** 2
fig = plt.figure() # создаем объект фигура и на него наносим график.
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.2, 0.4, 0.3])
axes1.plot(x, y, 'b') # Передаются массивы значение и стиль построения графиков
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

axes2.plot(y, x, 'g') # Передаются массивы значение и стиль построения графиков
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title')
savefig('1.png')