def bfs(start, end, obstacle, map_size):
    # 先起点放入对列，和将起点放入已访问集合
    if start == end:
        return [start]
    queue = []  # 队列
    parent = {start: None}  # 父节点记录
    visited = set()
    queue.append(start)
    visited.add(start)
    # 已访问集合
    directions = [
        (0, -1),  # 上
        (0, 1),  # 下
        (-1, 0),  # 左
        (1, 0)  # 右
    ]  # 方向
    while queue:
        compare = queue.pop(0)
        # 判断合法坐标
        for dx, dy in directions:
            # 上下左右的坐标
            tmep_x = compare[0] + dx
            tmep_y = compare[1] + dy
            if (0 <= tmep_x <= map_size[0]
                    and  # 判断边界
                    0 <= tmep_y <= map_size[1]
                    and  # 判断障碍
                    (tmep_x, tmep_y) not in obstacle
                    and  # 判断已访问集合
                    (tmep_x, tmep_y) not in visited
            ):
                parent[tmep_x, tmep_y] = compare
                queue.append((tmep_x, tmep_y))
                visited.add((tmep_x, tmep_y))
                if (tmep_x, tmep_y) == end:
                    # 逆向坐标
                    endpoint = end
                    route = []
                    while endpoint is not None:
                        route.append(endpoint)  # 先要把终点坐标记录下来
                        endpoint = parent[endpoint]  # 从终点逆推起点坐标
                    route.reverse()  # 翻转列表
                    return route
    return None


if __name__ == "__main__":
    r = bfs(
        start=(0, 0),  # 开始位置
        end=(2, 0),  # 结束位置
        obstacle=[[1, 0]],  # 障碍位置
        map_size=(2, 2)  # 地图位置
    )
    if r == [(0, 0)]:
        print("开始位置是终点")
    elif r is not None:
        print(f"路线:{r}")
    elif r is None:
        print("找不到路线")

"""
    r = bfs(
        start=(0, 0),#开始位置
        end=(2, 0),#结束位置
        obstacle=[[1, 0]],#障碍位置
        map_size=(2, 2) #地图位置
    )
"""
