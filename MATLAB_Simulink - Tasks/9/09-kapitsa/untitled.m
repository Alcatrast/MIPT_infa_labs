figure(1)
plot(dtheta,theta)
grid on
xlabel('dtheta')
ylabel('theta')
figure(2)
plot(x,y)
grid on
xlabel('x')
ylabel('y')
%%
freq_m = [0.1 0.5 10 50];
len = length(freq_m);
dtheta1 = zeros(len,1800);
theta1 = zeros(len,1800);
x1 = zeros(len,1800);
y1 = zeros(len,1800);

for i = 1:len+1
    Freq = freq_m(i);
    sim('Kapitsa0x2Dpendulum.slx')
    
    dtheta1(i,:) = paddata(dtheta,1800);
    theta1(i,:) = paddata(theta,1800);
    x1(i,:) = paddata(x,1800);
    y1(i,:) = paddata(y,1800);

    subplot(len,2,i*2-1)
    plot(x,y)
    title(['Частота: ', num2str(freq_m(i)),' График XY'])
    grid on
    xlabel('x')
    ylabel('y')
    subplot(len,2,i*2)
    plot(theta,dtheta)
    title(['Частота: ', num2str(freq_m(i)),' График theta dtheta'])
    grid on
    xlabel('theta')
    ylabel('dtheta')
end



% sinFreqsHz = (1 : 5);
% 
% close all;
% fig1 = figure();
% set(fig1,'Visible','on');
% hold all;
% grid('minor');
% title('Запуск модели c разными параметрами колебаний');
% for i = 1 : length(sinFreqsHz)
%     A = 1/i;
%     sinFreq = sinFreqsHz(i) * 2 * pi;
% 
%     % Запуск модели. В первом параметере имя файла,  во втором время исполнения модели.
%     out = sim('simple_model.slx',2); 
% 
%     % В структуре out доступны по имени все переменные, которые выведены
%     % через блок ToWorkspace. Также в ней содержится поле tout, в котором
%     % содержится сетка по времени для расчётной модели
%     plot(out.tout, out.sinValues,'DisplayName',['F = ', num2str(sinFreqsHz(i)), ' Гц'],'LineWidth',1);
% end
% legend();