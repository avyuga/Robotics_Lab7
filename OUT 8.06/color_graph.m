results=dlmread('C:\Users\Anastasia\PycharmProjects\Robotics_Lab7\OUT 8.06\code_color2.txt'); %считываем файл
time = results(:, 1);
red = results(:, 5);
green = results(:, 6);
blue = results(:, 7);
hold on;
plot(time, red, 'r');
plot(time, green, 'g');
plot(time, blue, 'b');
