function Gx = generate_double_trapezoids_no_gap(base_width, top_width, start_point, height, array_length, first_state)
    % Calculate the start and end indices for the first trapezoid
    base_start = round(start_point);
    base_end = round(base_start + base_width - 1);

    top_start = round(start_point + (base_width - top_width) / 2);
    top_end = round(top_start + top_width - 1);

    % Create the first trapezoid
    Gx1 = zeros(1, array_length);

    Gx1(base_start:top_start - 1) = linspace(0, height, top_start - base_start);
    Gx1(top_start:top_end) = height;
    Gx1(top_end + 1:base_end) = linspace(height, 0, base_end - top_end);
    Gx1 = Gx1 * first_state;

    % Calculate the start and end indices for the second trapezoid
    start_point2 = start_point + base_width -1;  % Start the second trapezoid immediately after the first one
    base_start2 = round(start_point2);
    base_end2 = round(base_start2 + base_width - 1);

    top_start2 = round(start_point2 + (base_width - top_width) / 2);
    top_end2 = round(top_start2 + top_width - 1);

    % Create the second trapezoid
    Gx2 = zeros(1, array_length);

    Gx2(base_start2:top_start2 - 1) = linspace(0, height, top_start2 - base_start2);
    Gx2(top_start2:top_end2) = height;
    Gx2(top_end2 + 1:base_end2) = linspace(height, 0, base_end2 - top_end2);
    Gx2 = Gx2 * first_state * -1;

    % Combine the two trapezoids
    Gx = Gx1 + Gx2;
end
