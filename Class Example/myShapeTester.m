clc
clear
close all

xlim([0, 10])
ylim([0, 10])

tri = MyShape([1, 3, 5], [1, 4, 1], 'y');
rect = MyShape([6, 9, 9, 6], [1, 1, 3, 3], 'r');

pause(1)

while true
    for k = 1:100
        tri.move(0, 0.03)
        rect.move(-0.01, 0.01)
        pause(0.01)
    end
    
    for k = 1:100
        tri.move(0, -0.03)
        rect.move(0.01, -0.01)
        pause(0.01)
    end
end