clear all
close all
base_width = 10;
top_width = 2;

% Specify the start points for the gradients for each TR
all_start = 5;
start_point_x = all_start;
start_point_y = all_start;
start_point_z = all_start;
height = .1; % 100 mT/cm gradinet amplitude 
array_length = 30;


reference_matrix = [-1, -1, -1;  
                     1,-1, -1;   
                    -1, 1, -1;
                    -1,-1,  1;
                   ];

balanced_matrix = [0, 0, 0;  % For i = 1
                    2, 0, 0;   % For i = 2
                     0, 2, 0;
                     0, 0, 2;
                   ];

current_matrix = reference_matrix;

num_encodes = size(current_matrix, 1);

% Initialize empty arrays to store Gx, Gy, and Gz
Gx = zeros(num_encodes, array_length);
Gy = zeros(num_encodes, array_length);
Gz = zeros(num_encodes, array_length);

for i = 1:num_encodes
    % Set start_enc_x, start_enc_y, and start_enc_z from the reference matrix
    start_enc_x = current_matrix(i, 1);
    start_enc_y = current_matrix(i, 2);
    start_enc_z = current_matrix(i, 3);

    Gx(i, :) = generate_trapezoid(base_width, top_width, start_point_x, height, array_length, start_enc_x);
    Gy(i, :) = generate_trapezoid(base_width, top_width, start_point_y, height, array_length, start_enc_y);
    Gz(i, :) = generate_trapezoid(base_width, top_width, start_point_z, height, array_length, start_enc_z);
end

% Concatenate the arrays
Gx_combined = reshape(Gx.', 1, []);
Gy_combined = reshape(Gy.', 1, []);
Gz_combined = reshape(Gz.', 1, []);

% Plot the trapezoid
figure
subplot(3,1,1)
plot(1:numel(Gx_combined), Gx_combined);
title('Gx')

subplot(3,1,2)
plot(1:numel(Gy_combined), Gy_combined);
title('Gy')
ylabel('gradient amplitude (mT/m)','FontSize',10,'FontWeight','bold')
subplot(3,1,3)
plot(1:numel(Gz_combined), Gz_combined);
title('Gz')
xlabel('time (ms)','FontSize',10,'FontWeight','bold')

Gx = Gx_combined;
Gy = Gy_combined;
Gz = Gz_combined;
clear Gz_combined;
clear Gx_combined;
clear Gy_combined;
getgrads
