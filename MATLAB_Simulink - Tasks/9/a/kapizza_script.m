%% Запуск модели
m = 1;
L = 1;
g = 9.8;
start_angle = 120;
decrement = 0.3;
Amplitude = 0.1;

F_0 = 1/(2*pi*sqrt(L/g));

Frequency = F_0/5;
sim('kapizza_pendulum.slx')
x1 = X;
y1 = Y;
theta1 = theta;
dtheta1 = dtheta;

Frequency = F_0*1.5;
sim('kapizza_pendulum.slx')
x2 = X;
y2 = Y;
theta2 = theta;
dtheta2 = dtheta;

Frequency = F_0*30;
sim('kapizza_pendulum.slx')
x3 = X;
y3 = Y;
theta3 = theta;
dtheta3 = dtheta;
%% Построение графиков
% Первый график
subplot(2,3,1);
plot(x1, y1);
grid('minor');
xlabel('x, м'); 
ylabel('y, м'); 
title('XY: f < f_0') 

% Второй график
subplot(2,3,2);
plot(x2, y2);
grid('minor');
xlabel('x, м'); 
ylabel('y, м'); 
title('XY: f \approx f_0')

% Третий график
subplot(2,3,3);
plot(x3, y3);
grid('minor');
xlabel('x, м'); 
ylabel('y, м'); 
title('XY: f >> f_0')

% Четвертый график (фазовая диаграмма)
subplot(2,3,4);
plot(theta1, dtheta1);
grid('minor');
xlabel('\theta'); 
ylabel('d\theta'); 
title('Фаз. диаграмма: f < f_0')

% Пятый график (фазовая диаграмма)
subplot(2,3,5);
plot(theta2, dtheta2);
grid('minor');
xlabel('\theta'); 
ylabel('d\theta'); 
title('Фаз. диаграмма: f \approx f_0')

% Шестой график (фазовая диаграмма)
subplot(2,3,6);
plot(theta3, dtheta3);
grid('minor');
xlabel('\theta'); 
ylabel('d\theta'); 
title('Фаз. диаграмма: f >> f_0')