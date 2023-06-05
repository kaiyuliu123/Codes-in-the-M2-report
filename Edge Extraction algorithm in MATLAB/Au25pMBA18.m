filename = 'C:\Users\Louis Althusser\Desktop\Nano Results\Nano Results Avril\4.17 Capillary Experiment\04.17 Overestimation of the Capillary Width.xlsx';
sheetname = 'pMBAPEIperms'
range = ['A3:H306']
data = xlsread(filename, sheetname, range)
x = data(:, 1)
for i=1:5
    y(:, i) = data (:, i+1)
    subplot(4,5,1)
    plot(x, y(:, i))
    hold on
end

xlabel('Distance');
ylabel('Signal/ms');
legend('0mm','1mm','2mm','3mm','4mm','5mm','6mm','Location', 'northeast')
legend('FontSize', 5)


for i=1:5
    ys(:, i) = sgolayfilt(y(:,i), 3, 7)
    subplot(4, 5, 2)
    plot(x, ys(:, i))
    hold on
end
subplot(4,5,2)
xlabel('Distance');
ylabel('Signal/ms');
legend('0mm','1mm','2mm','3mm','4mm','5mm','6mm','Location', 'northeast')
legend('FontSize', 5)

for i=1:5
    dydx(:, i) = diff(ys(:, i))./diff(x)
    subplot(4, 5, 2+i)
    plot(x(1:end-1), dydx(:, i))
    xlabel('Distance');
    ylabel(['First Derivative ' num2str(i-1) 'mm'])
end

x_lower = 70
x_upper = 230

for i = 1:5
    subset = dydx(x >= x_lower & x <= x_upper, i)
    [max_val, max_ind] = max(subset)
    [min_val, min_ind] = min(subset)
    max_x(:,i) = x(find(x >= x_lower & x <= x_upper, 1) + max_ind - 1)
    min_x(:,i) = x(find(x >= x_lower & x <= x_upper, 1) + min_ind - 1)
    dist(:, i) = min_x(:,i) - max_x(:,i)
end
