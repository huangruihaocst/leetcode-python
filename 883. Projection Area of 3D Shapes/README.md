# 883. Projection Area of 3D Shapes

## Solution

俯视图：所有非零元素的个数。

正视图：数组中每个子数组中最大值之和。（`grid[0][1], grid[0][1], grid[0][2]...`）

侧视图：数组中每个子数组中相同位置的数最大值之和。（`grid[0][0], grid[1][0], grid[2][0]...`）