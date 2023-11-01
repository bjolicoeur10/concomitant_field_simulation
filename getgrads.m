B0 = 3000; % 3000 mT = 3T
ele = 220;
ni = ele/2;
t = 1:120; %1t = 0.01ms -> 1000t = 10 ms
index = 1;
for ti = 1:numel(t)
    ti
    for xi = -ni:index:ni
        for yi = -ni:index:ni
            for zi = -ni:index:ni
                Bc(xi+ni+1, yi+ni+1, zi+ni+1, ti) = 267.513 * (1/(2*B0)) * (((Gx(ti) * zi - Gz(ti) * ...
                    zi/2)^2 + (Gy(ti) * zi - Gz(ti) * yi/2)^2));
            end
        end
    end
end
x = ele+1;
y = ele+1;
z = ele+1;
t = numel(t);

% Create a new 4D matrix to store the cumulative sums
[x, y, z, t] = size(Bc);
Bcsum = zeros(x, y, z, t);

% Initialize the first frame of Bcsum with the first frame of Bc
Bcsum(:, :, :, 1) = Bc(:, :, :, 1);

% Compute the cumulative sum for the rest of the frames
for t_idx = 2:t
    Bcsum(:, :, :, t_idx) = Bcsum(:, :, :, t_idx - 1) + Bc(:, :, :, t_idx);
end

% gammabar = 42.576 gamma / 2pi [MHz * T^-1]
% save('Bc.mat','Bc','-v7.3')
% 
% 
% clear all
% close all
