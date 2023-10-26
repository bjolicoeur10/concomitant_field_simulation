B0 = 3000; % 3000 mT = 3T
Bmax = 0.2; % mT/mm
ele = 22;
ni = ele/2;
t = 1:120; %1t = 0.01ms -> 1000t = 10 ms
for ti = 1:numel(t)
    ti
    for xi = -ni:ni
        for yi = -ni:ni
            for zi = -ni:ni
                Bc(xi+ni+1, yi+ni+1, zi+ni+1, ti) = (1/2*B0) * (((Gx(ti) * zi - Gz(ti) * ...
                    zi/2)^2 + (Gy(ti) * zi - Gz(ti) * yi/2)^2));
            end
        end
    end
end

save('Bc.mat','Bc','-v7.3')
clear all
close all
