results=dlmread('C:\Users\Anastasia\PycharmProjects\Robotics_Lab7\OUT 25.05\square2\square2_4___-90_90_0.txt'); %считываем файл
theta1=results(:,1);
theta2=results(:,2);
theta3=results(:,3);


theta1 = theta1*pi/180/5;
theta2 = theta2*pi/180/(-5);
theta3 = theta3*pi/180/(-5/3);
theta3 = theta2-theta3;

a = [ 0.007, 0.128, 0.128];
d = [ 0.18, 0, 0];
for i = 1:size(results)
    x(i)=(a(2)*cos(theta2(i)) + a(3)*cos(theta3(i)))*(cos(theta1(i)));
    y(i) = (a(2) * cos(theta2(i)) + a(3) * cos(theta3(i)))*(sin(theta1(i)));
    z(i) = d(1) + a(2) * sin(theta2(i)) + a(3) * sin(theta3(i));
end 

hold on; 
line = plot3(x,y,z, 'magenta');
line.LineWidth = 2.5;
grid on;
