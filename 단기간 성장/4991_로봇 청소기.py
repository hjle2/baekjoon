# 유저가 경로를 설정하는 로봇 청소기
# 모두 깨끗한 칸으로 만드는 데 필요한 이동 횟수의 최솟 값
# 로봇의 위치 + 먼지들의 위치 각 거리 중 최솟 값이 되는 경우를 구하면 되는 거 아닌가 ㅎ
def getDistance(pt1, pt2):
    ox, oy = pt1
    ex, ey = pt2
    que = [(ox, oy, 0)]
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False]*w for _ in range(h)]
    visited[pt1[0]][pt1[1]] = True
    while que:
        ox, oy, d = que.pop(0)
        if ox == ex and oy == ey:
            return d
        for i, j in dxy:
            x, y = ox + i, oy + j
            if 0<=x<h and 0<=y<w and ar[x][y] != 'x' and not visited[x][y]:
                visited[x][y] = True
                que.append((x, y, d + 1))


def getDistanceList(pt):
    dist = [[0]*len(pt) for _ in range(len(pt))]
    for i in range(len(pt)):
        for j in range(i+1, len(pt)):
            d = getDistance(pt[i], pt[j])
            dist[i][j] = d
            dist[j][i] = d
            if d == None:
                return False
    return dist

def solve(now, sum, dirty):
    global total
    if dirty == 0:
        total = min(total, sum)
        return
    for i in range(len(pt)):
        if not chk[i]:
            chk[i] = True
            solve(i, sum + dist[now][i], dirty-1)
            chk[i] = False


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    ar = []
    pt = []
    cnt = 0
    robot = 0
    for i in range(h):
        tmp = [*input()]
        for j in range(w):
            if tmp[j] == '*' or tmp[j] == 'o':
                cnt += 1
                if tmp[j] == 'o':
                    robot = len(pt)
                pt.append((i, j))
        ar.append(tmp)
    dist = getDistanceList(pt)
    if not dist:
        print(-1)
        continue
    chk = [False] * len(pt)
    total = 1e9
    chk[robot] = True
    solve(robot, 0, cnt-1)
    print(total if total != 1e9 else -1)

# 2 2

# 15 7
# *.o.*..........
# .........**....
# .*.............
# ...............
# ...............
# ...............
# x.......*....*.
# 6 18
# xx....
# ......
# ......
# *o....
# ......
# ...x..
# xxxxx.
# xx....
# ......
# .*....
# ..xx.*
# .....x
# ......
# *.....
# xx....
# xx....
# xx....
# xx....
# 13 17
# ............x
# ..........x.x
# ............x
# .......**....
# .............
# ....*.......x
# ............x
# o..........xx
# ...*.*......x
# ............x
# .......x.....
# ............x
# .....xx*.x.xx
# .....x.....xx
# ...xxx....xxx
# .*xxxx...xxxx
# .xxxxxx..xxxx
# 12 14
# ...........x
# .x......xx..
# .......xx...
# .....x.xx..x
# x.....*xx..*
# ...*.x.o....
# .x...x......
# ....xx......
# *..........*
# .........x..
# ...........x
# ............
# ............
# ............
# 7 10
# ......x
# *...*.x
# .......
# .......
# ....*.*
# .......
# .......
# .o.....
# **.....
# ..*....
# 8 10
# ........
# ........
# ........
# .......*
# ........
# *.......
# .....*xx
# *o.***xx
# .....xxx
# ....xxxx
# 6 14
# xxxx.x
# xxxx..
# xx...*
# xxxxx*
# *..xx.
# .*.*x.
# ..x*..
# xxxx..
# xxx...
# xx...x
# ...xx*
# ...xxx
# .o..xx
# x..xxx
# 17 7
# xxxxxxxxxx.....xx
# xxxxxxx.........x
# xxxxxxxx.x....*..
# xx.x.xxx*xx.x..*.
# .....xxx.xxxxx..o
# .......x.xxxxx.xx
# ........*xxxxx.xx
# 14 8
# xx...*..xxxxxx
# o.*xxx....x.xx
# x..*xx....x..x
# x...*........x
# ..............
# .*.......*....
# .x............
# xx*........x..
# 6 8
# xx...*
# x.....
# *...x*
# ......
# .o.*.*
# xx.xxx
# xx.xxx
# xx.xxx
# 12 20
# ..xxxxxxxxxx
# ..*xxxxxxxxx
# ..xx..xxxxxx
# ..x..*..xxxx
# ........xxxx
# .xx.xxx*xxxx
# xxx.*xxxxxxx
# xxxx.xxxxxxx
# xxxx.xxxxxxx
# xxxx.x.....x
# xx....o.x...
# xx........xx
# xxxx....xxxx
# xxxxx..xxxxx
# xxxxx..xxxxx
# xxxxx.xxx.xx
# xxxxx..x...x
# xxxxx.......
# xxx..*.x..xx
# xxx..xxxxxxx
# 8 10
# ...*...x
# .......x
# ..*.....
# ........
# .......o
# ........
# ........
# x.......
# ......*.
# ........
# 20 18
# x........xxxxxxxxxxx
# ..........xxxxxxxxxx
# .........xxxxxxxxxxx
# ...........x.xxx.xxx
# .....xx......x....xx
# ....*xxx............
# xxx..xxx...........x
# xx...xx..........o*x
# xx..xxx.............
# xx.xxx..............
# x..xxx..............
# ....x..x....*.......
# ..xxxxxxxx..*.......
# x.......x.........x.
# xx....xxxx..xx....x.
# ......xxxx.......xxx
# xxxx.*xxxx......xxxx
# xxxx.xxxxx......xxxx
# 8 8
# x.xxx*.x
# o......x
# xx.*.*.x
# xx....*x
# xxx...xx
# xxxx.*..
# xxxx....
# xxxx..**
# 14 13
# ........xxxxxx
# ........x*.xxx
# x..........xxx
# ..x.........xx
# ..x........xxx
# ..*..xxxxx*.xx
# .....xxxxx.*.x
# ..xx...*xxx...
# x...........xx
# ...........xxx
# .........x.xxx
# ......o..x.xxx
# .......xxx.*..
# 10 19
# xxx..xxxxx
# xxxx...xxx
# xxxx...x.x
# xxx......x
# xo......xx
# ........xx
# ........xx
# x.......xx
# .......xxx
# ...xx..xxx
# xx**....xx
# xx.xxx..xx
# x..xxxx.xx
# ..xx..x..x
# .xxx.....x
# .xxx..x.xx
# .xxx....xx
# *.....x...
# ..xxx.....
# 6 11
# .xx.*x
# .xx*.x
# ...x..
# *.xo.*
# .....x
# xxx..x
# xxxx*.
# xx..*.
# x...**
# xxx...
# xxx...
# 9 12
# xxxxxxxox
# xxxxxxx.*
# xxxxxxx..
# *xxxxxx..
# xxxxxx...
# xxxxxx.xx
# .......xx
# xxxxx**xx
# xxx...*xx
# xxx*.x.xx
# xxxx*.xxx
# xxxxx.xxx
# 19 16
# xxxxxxx...xxxxxxxxx
# xxxxxxx.........xxx
# xxxxxxx.....x...xxx
# xxxxxxxxxxx.....oxx
# xxxxx.xxxxx..xxx.xx
# xxxxx............xx
# xxxxx......xxx.....
# xxxxx...x..xxxx...x
# xxx...xxx.xxxxxxxxx
# ....xxxxx.xxxxxxxxx
# x......xx.xxxxxxxxx
# xxxx.*.....xxxxxxxx
# xxxx...x....x...*xx
# xxxxx.xx.xx...x..xx
# xxxxxxxx.x.........
# xxxxxxxxxxxx*x.....
# 7 12
# ..xxxxx
# ..xxxxx
# ..xxxxx
# *..xxxx
# xx.xxxx
# xx..x..
# xxx**.*
# xxx.o*.
# ..x*.xx
# .*...xx
# ..*.xxx
# .xxxxxx
# 14 13
# ....*..*.....x
# ..............
# ..x...*x......
# x.xxx.........
# xxxxxxxx......
# xxxxx......xx.
# xxxxx.........
# xx............
# .......*......
# ...o..........
# .........*...*
# ......*.......
# *.......*.....
# 11 12
# xxxx.......
# xxxx.......
# xxxx*......
# xxxx.......
# xxx.....*..
# .........*.
# ..........*
# ...........
# ..........x
# xx......x..
# xxxx..ox...
# xxxxx.x....
# 9 9
# xx....*xx
# xxx..xxx.
# xx..x....
# xx.x..xx.
# x.....xx.
# x...x.o*.
# x...xxxxx
# x*..xxxxx
# ..x.xxxxx
# 10 14
# xxxxxx..xx
# xx.xxx....
# ....x...*.
# ...*......
# ..........
# ...o......
# ..........
# .......x..
# x*.....xxx
# .x.xxx.xxx
# ......*xxx
# xx.xx...xx
# xxxxx...xx
# xxxxxx.xxx
# 12 10
# xx...x.....x
# xx...x.....x
# xx...x...*.x
# ....*...x..x
# ....*..xx.xx
# x.xx...xx..x
# x.xxxxxxxx..
# x...xx.o...*
# xxx.........
# xxxx..xxx...
# 20 14
# xxx.xxxxxxxxxxxxxxxx
# ......xxxxxxxxxxxxxx
# .xx....xxxxxxxxxxxxx
# .xx....xxxxxxxxxxx*x
# ....x.......xxxxxxxx
# xxxxxx....x..xxxxxxx
# xxxxxxx.xxxx..x..xxx
# xxx*.......xx.....xx
# xx.........xxxxx....
# xx...xo..x.xxxxxx...
# xxxxxx......xxxxx..*
# xxxxxxx....xx**.....
# xxxxxxx.x*.xxx.....x
# xxxxxxxxxx.xxxx...xx
# 13 20
# ..xxxxxxxxxxx
# ..xxxxxxxxxxx
# ..xxxxxxxxxxx
# ..*.xxxxxxxxx
# .....xxxxxxxx
# .....xxxxxxxx
# ...*.xxxxxxxx
# ....xxx..xxxx
# xx.x.xxx.xxxx
# xx*..xx......
# xxxx.x..*....
# xx...x*......
# .........o*xx
# .......xxx.xx
# x.....xxxxxxx
# xxxxx.xxxxxxx
# *.xxx...xxxxx
# *......xxxxxx
# ......*xxxxxx
# .....xxxxxxxx
# 14 18
# xxxxxxx*......
# xxxxxxx.......
# xxxxxxxx......
# xxxxxxxxxx....
# x.xxxx.....xxx
# x*xxx..x..xxxx
# ......xxxxxxxx
# ....x.xxxxxxxx
# ....xoxxxxxxxx
# *.xxx.xxxxxxxx
# x.xxx.xxxxxxxx
# xxxxx.xxxxxxxx
# xx.xx*xxxxxxxx
# x.....xxxxxxxx
# xx......xxxxxx
# xxx.x..xxxxxxx
# xx..*..xxxxxxx
# xx....xxxxxxxx
# 19 13
# xxxxxxxxxxx.......*
# xxxxxxxxxx..xx.....
# xxxxxxxxxx.xx..x...
# xxxxxxxxxx.x.....x.
# xxxxxxxxxx.x.....x.
# .xx.x.xxx..x.......
# .o....xx.....xxx...
# ....*.....xx.......
# ......xxxxxx......x
# x.x...xxxxxxx......
# xxxx..xxxxxxx......
# xxxxxxxxxxxx.*....x
# xxxxxxxxxxxxxxxx...
# 6 15
# ......
# .....o
# .x....
# *.....
# ..*.x.
# ....x.
# ......
# ......
# .....*
# ......
# ....x.
# ......
# ......
# x.....
# x.x...
# 13 8
# xxxxxxx...*..
# xxx..........
# xx.*.........
# xxx....*.....
# .xxx...*.....
# *.*...*....xx
# ....x.....xxx
# ......o..xxxx
# 19 15
# xxxxxx.x..xxxxxxxxx
# xxxxx...x...xxxxx.x
# xxxxxo....x.xxxx...
# xxxxx.......x.xx...
# xxxxx.x*.....*....x
# x..........x..xxx..
# x.x...*x........x*.
# x....xx...xx..x....
# x...xxxx.xxxxxxx.xx
# *..xxxxxxxxxxxxx.xx
# x......xxxxxxxxxxxx
# .....x.xxxxxxxxxxxx
# .*.x...xxxxxxxxxxxx
# ...xx*...*xxxxxxxxx
# *x.xxxx.xxxxxxxxxxx
# 7 12
# ....x.x
# ....x..
# o....*.
# .......
# .......
# .......
# .......
# .......
# x.....*
# x.....*
# .....*.
# ....*..
# 16 7
# .....*x.........
# ..........*....x
# *........*......
# .*......*......o
# ................
# ....*.........xx
# ...x*.....*x...x
# 8 10
# xx.xxxxx
# xx.o.xx.
# xxx*..x.
# x..*....
# .......x
# ..xx.xxx
# xxx...xx
# xxx...xx
# xxx.*.xx
# xxx..xxx
# 15 12
# ........xxxxxxx
# ...........xxxx
# ........o..xxxx
# ........x...xxx
# ..*...........x
# *............xx
# ..............x
# .........*.....
# ...............
# ...............
# ...............
# ...............
# 9 10
# x......*.
# .........
# ...o.....
# .........
# xx.......
# xx.......
# x........
# x........
# ...*.*...
# xxx......
# 7 20
# .o..xxx
# ....xxx
# ...xxxx
# x.xxxxx
# x.xxxxx
# ..xxxxx
# .xxxxxx
# ..x.xxx
# *...*xx
# ....xxx
# .......
# .......
# ..*....
# xxxx...
# xxx....
# xxxx...
# xxxxx..
# xx.x.*.
# xx.....
# xx.*...
# 6 6
# *.*x..
# ......
# ..*..*
# x.o...
# xx....
# xx.xxx
# 16 10
# xxxxxxxxxxxxx..x
# xx.xxxxxxxxxx...
# xx..xxxxxxxx..*.
# ..*..xxxxx......
# x....x.xxx...x..
# x........x.x.x.x
# x.x........x...x
# *....*..xxoxx..x
# ........xxxxxxxx
# .......xxxxxxxxx
# 11 6
# ........x.x
# *xxxx.o...x
# xxxxx.....x
# xxxxx....*.
# xxxx*.*..*.
# xxxx..xxxx.
# 7 8
# xxx....
# xo*....
# .......
# xxx....
# xxxx...
# xxx....
# xx..*x.
# xxxxxx*
# 15 8
# xxx......xxx...
# xxx........x...
# x......*......*
# x......o.......
# ...*....xx.xx..
# ........xx.....
# ....x...xx.....
# ..x*.xxxxxxxx.x
# 11 20
# ..xx..xxxxx
# ...x..xxxxx
# .......xxxx
# .....x...o.
# .....xxx...
# ......xx...
# .....xxxx..
# .....xxxxx.
# ......xxx..
# .x..x.xxxx.
# ......xxxx.
# .*..x.xxxx.
# .......xxxx
# ........xxx
# ....*.....x
# ......x...x
# ..........x
# ......*....
# ...........
# ...........
# 12 8
# .....**....*
# .x*o...*..xx
# xx....xxxxxx
# x**...xxxxxx
# .....xxxxxxx
# ...x.xxxxxxx
# *.....xxxxxx
# x*....xxxxxx
# 11 17
# x...*..xx..
# x......xx..
# ...........
# .*.........
# o........x.
# ..........*
# ...........
# .......*...
# ...........
# ...........
# ...........
# ..*..*.....
# ...........
# ...........
# ...........
# .......*...
# ...........
# 14 6
# .......*...xxx
# xxx....*.*.xxx
# xxxxx.x.o....x
# xxxxx........x
# xxxxx.......x.
# xxxxx*....*...
# 8 7
# x......x
# ...*..xx
# xx....x.
# x.o.....
# x.x..*..
# x.x....*
# xxx.....
# 16 19
# xxxxxxxxx.....xx
# xxxxxxxx.......x
# xxxxxxxx........
# xxxxxxxx....x..x
# xxxxxxxx.......x
# xxxxxxxxx......x
# xxxxxxxx........
# xxxxxx.x........
# xxxxx.....x.....
# xxxxx.x.**......
# xxxx....*.......
# xxxx..x.........
# x..x.....x..xxxx
# .............xxx
# .........xxxxxxx
# ..........xxxxxx
# .......x..xxxxxx
# xx..x....oxxxxxx
# xxx*.....xxxxxxx
# 14 14
# xxxxxxxxxx..*.
# xxxxxxxxx....*
# xxxxxxxx......
# xxxxxx....*..x
# xx.........o.x
# x.........*xxx
# x..........xxx
# xxx.x......xxx
# xx..x....*...x
# ....xx.......x
# ....xxx...x..x
# ....x.....xxxx
# x........xxxxx
# xxxx.....xxxxx
# 8 20
# xxx..xxx
# xxxx.xxx
# xx...xxx
# xx...xxx
# xxx..xxx
# xxxx.xx.
# xxxx.x..
# xxxx....
# xxxxx...
# xxxxx...
# .x......
# ..o.....
# ........
# ........
# ........
# ..*..*..
# ........
# ....xx..
# *....xx.
# .....xxx
# 6 12
# xxxx*o
# xxxx..
# xxxx..
# ...**.
# *.....
# .*.x..
# x.*x..
# x.....
# xx..x.
# xx..x*
# xxx*xx
# xx..xx
# 7 10
# ..x....
# ..xx**.
# ..o....
# .......
# *......
# ......*
# .*...*.
# *.*....
# ....x*.
# ...xxxx
# 12 13
# ........xx..
# ...*........
# .......xx...
# .....*.x....
# ...........x
# .........x..
# ..........*.
# ...x.*.xx...
# ..x........o
# ...*.....x..
# ............
# ............
# .*..........
# 12 13
# *.xxxxxxx.xx
# *xxxxx......
# .xxxxx..x.xx
# .*.x..oxxxxx
# .xx.....xxxx
# *..*x.x.xxxx
# xx*x....xxxx
# xxxx.xxxxxxx
# xxxx..xxxxxx
# ..xx.xxxxxxx
# .....xxxxxxx
# x....*xxxxxx
# x.*xxxxxxxxx
# 18 19
# xxxxxxxxx....xxxx.
# xxxxxxxx......xxx.
# xxx.xxx...........
# xxx.xx...*....x...
# xxx.xx............
# xxx..x...x.....xxx
# xxxx.x........xxxx
# xxxx.......xxxxxxx
# xxxxx..xx*..xxxxxx
# xxxx...xx..xxxxxx*
# xxxx*.......xxxxxx
# x........xx.xxxxxx
# x.x....xx.x.xxxxxx
# ..x....xx....xxxxx
# .......xxx......xx
# .......xxx......xx
# ....xx.xx.......xx
# ....xx.xxx..o....x
# ....xx..xx.......x
# 15 13
# .xxxxxxxxxxxxxx
# ..x....xxxxxxxx
# .....*xxxxxxxxx
# ..*xx.xxxxxxxxx
# x.oxx*xxx....*x
# xxxx...........
# xxxxxx*.x....xx
# xxxxxx.xxxxxxxx
# xxxxx..xxxxxxxx
# xxxxx..xxxxxxxx
# xxxxx...xxxxxxx
# xxxxx......xxxx
# xxxxxxxxx.*xxxx
# 15 12
# xxxxxxxxx..*...
# xxxxx...x..**.x
# xx.xxxx.x......
# xx.xxxx.x..xx.x
# xx.x....xo.xxxx
# xx.*......xxxxx
# ..........xxxxx
# ...*....xxxxxxx
# ...........xxxx
# xx.........xxxx
# xxxxxx.xx*.xxxx
# xxxxxxxxx..xxxx
# 10 16
# ....xx.xxx
# .xx.x....x
# .xx.xx....
# .xx.xx.x.x
# ..........
# ..x..*....
# ..xx..xx.x
# .xx*.xxx..
# xx........
# xx.......x
# xx..o.x..x
# x**...xx.x
# xx..x..x.x
# xx.*xx..*x
# ....xxx.xx
# x...xxxxxx
# 13 14
# x.....xxxxxxx
# .......xxxxxx
# .......xxxx..
# xxxxx....o...
# xxxx*x*xx....
# xxxxxx.xxx*..
# xxxxxx.xxx*.x
# xxxxxx.xxx.xx
# xxxxx..xxxxxx
# xxxxx.xxxxxxx
# xxxx..xxxxxxx
# xxxx...xxxxxx
# xxxxxx.xxxxxx
# xxxx....xxxxx
# 9 15
# xxxxx*.x.
# xxxxxx...
# xxxx...xx
# xxxx.xxxx
# .xxx..xxx
# ..xx...x.
# ...x.*...
# ***x.xxx*
# ...*.xxxx
# .....xxxx
# .x.*o.xxx
# xxxx....x
# xxxx*....
# xxxxx...x
# xxxx..xxx
# 7 15
# xxxxx.x
# .xxx.o.
# .......
# .......
# ...*...
# .......
# .....x.
# xxx*...
# xxxxx..
# xxxxxx.
# xxxxx..
# xxxx.*.
# xxx..xx
# xx...xx
# x....xx
# 15 6
# xxxx.......*.*.
# .x........x...x
# ..o.x*x*....*.x
# x..............
# x*.*...........
# x...........*..
# 16 10
# .xxxxxxxx.xxxxxx
# ...xxxx....xxxxx
# ...xxx.....xxxxx
# ...**x......xxxx
# .....xx.....xxxx
# *...............
# x.xxxxxxx....o..
# x..xxx...*.....x
# x.xxxx.xx.xxxxxx
# xxxxxx...xxxxxxx
# 6 9
# xx.xxx
# x....x
# ....**
# .x****
# ....*.
# ......
# ......
# *..*x.
# xx.o..
# 19 18
# ............*....x.
# ....*...........*..
# ...................
# ...................
# ...................
# xx...........x*....
# xx..o........xx....
# xxx..........xx..*x
# ............xxxx.xx
# .................xx
# ...................
# ..x................
# ..x.....x.........x
# ..xxx...x..........
# ..x................
# xxx..x......x*...*.
# xxxxx..........xxx.
# xxxxx......xxxxxxxx
# 14 20
# xxxx....xxxxxx
# xxx.....xxxxxx
# xxx.x....xxxxx
# xx........xxxx
# x......x..xxxx
# .......x..xxxx
# x.........xxxx
# x....x....xx.x
# x....x...*..*.
# x....xx.....xx
# xxxxxxx....*..
# xxxxxxx.x.....
# xxxxxxx.......
# xx..xxx.......
# x...xxx.......
# .....x..xxx...
# .......xxx...x
# .o*...xxxx...x
# ....x.xxxx..xx
# xx.xx.xxxxxxxx
# 18 10
# xxxx...........*..
# x...............xx
# xx...............x
# xx............o..*
# xx.*..............
# x*................
# ..................
# .*......*.........
# ...............*..
# ..xxxx............
# 14 14
# .........xxxxx
# .....x.......x
# .............x
# ............*.
# ..............
# .....*.o.....x
# x............x
# xx............
# xx............
# xx.*.........*
# ....*.x.......
# .....x........
# ............*.
# .....x..x.....
# 6 14
# ....xx
# *....x
# x...xx
# ......
# ......
# x.....
# ..x.*x
# ...xx*
# .x.xxx
# xx..xx
# xxxo*x
# xxx..*
# xxx...
# xx....
# 19 10
# ...xxxxxxxxxx...xxx
# *....xxx.xxxx....xx
# ..*.......xxx....x.
# .*...xxxx...x......
# ...xxxxxxxx........
# x*xxxxxxxxxx..*...*
# xxxxxxxxxxxx.......
# xxxxxxxxx..*.....xx
# xxxxxxxxx...o.*...x
# xxxxxxxxx.........x
# 8 8
# *...xx..
# ....x...
# x.....x.
# x..*..x.
# .....xx.
# x....*.*
# x...xx.o
# xxxxxxx.
# 12 6
# ....xxx.....
# *....xx...*.
# .x..*....*xx
# ...o....x*xx
# ..x.......*x
# *xx.xx.x...x
# 7 8
# xxxxxx.
# xxxxxx.
# x..xxx.
# x..xx..
# o..x.*x
# .*.....
# .....x*
# x..x.xx
# 16 17
# xxxxxxxxx.....xx
# xxxxxxxxx...*.xx
# xxxxxxxx.....xxx
# xxxxxx...x...xxx
# xxxx....x...xxxx
# xxx....xx...xxxx
# xx......xx..xxxx
# xx..x...x.....xx
# xx.............x
# xx.............x
# ................
# .xx.............
# .........o.x..xx
# .x....*...*...xx
# xx.........xxxxx
# xx.....xxxxxxxxx
# xx....xxxxxxxxxx
# 19 14
# .........x.........
# *..................
# ...................
# x.................*
# ...................
# ...................
# ....x.....*..*.....
# .*.*x......x.......
# xx.....o...x..xx...
# xxxx......x........
# xxxxx.....x........
# xxxxxxx............
# xxxxxxxx...x......x
# xxxxxxxxx*.........
# 14 7
# xxxxx.........
# ..x.x.....x*..
# ..............
# x.*..*......o.
# xxxxx.....*..x
# xxxxx....*..xx
# xxxxxxxx...xxx
# 19 13
# xxxxxx...xx...xxxxx
# xxxxx....xxx..xx.xx
# xxxx..x..xx...xx...
# xxxx..............x
# xxx...x....x......x
# xxx...x...xxxxo..xx
# x.x...*...xxxx..xxx
# ......x...xxx.xxxxx
# x...x.....xx..xxxxx
# xx*.xxx.x.x...xxxxx
# xx.xxxxxx...xxxxxxx
# xxxxxxxxx...*xxxxxx
# xxxxxxxx.....xxxxxx
# 13 6
# xxx..o.*.xxxx
# xx*......*.xx
# xx*...x*...xx
# .*.xxxx.....x
# .x*xxxx...*.x
# xxxxxxxx.....
# 12 12
# xxxxxx*.xo.x
# xxxx.*......
# xxxx.xxxxxxx
# xxxx.xxxxxxx
# x.....xxxxxx
# ..x..xxxxxxx
# *....xxxxxxx
# x*.x..xxxxxx
# xxxxx.xxxxxx
# xxxxx.xxxxxx
# xxxxx.*xxxxx
# xxxxxx.x*xxx
# 14 6
# xxx*.........x
# ..........*..x
# xxxx........xx
# xxx....x.*.*..
# xxx....x......
# xxxx...x...xxo
# 17 20
# xx*o...xx.....xxx
# xx.....*....xxxxx
# xxxx....x...xxxxx
# xx..........xxxxx
# xx..........xxxxx
# xx..x.........xxx
# xxx........xx.xxx
# xxxx......xxx.xxx
# xxxx.x.....xx...x
# x.xx.xx....xxxx.x
# ........xxxx....x
# ...xxxxxxxx..xx..
# ...xxxxxx*x.xxx..
# ...xxxxxxx...xxxx
# ...xxxxxxxxx..xxx
# ...xxxxxxxxxx*...
# xxxxxxxxxxx......
# xxxxxxxxxxx......
# xxxxxxxxx..*.....
# xxxxxxx*xxxx.....
# 14 11
# xxxxxxxxxx.xxx
# xxxxx..xxx..xx
# xxxxxx......*x
# xxxxxx*......x
# x*xxx......*xx
# x............x
# x*.........x..
# x........*...x
# ......x...*xxx
# .o.*x.xx.xxxxx
# ..xxxxxxxxxxxx
# 10 11
# .xxxxxx.xx
# .xxxxx..xx
# ..*xxxx..x
# ...**x...x
# ...*.x...x
# x*x..o..*x
# xxx....x..
# xxxxx**...
# xxxxx*x...
# xxxxxxxx..
# xxxxxxxx..
# 10 17
# ..........
# xx.....*..
# ..........
# xx*.......
# ..........
# ..........
# ..........
# ..........
# ........*.
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ...o......
# 13 7
# xxxx.........
# xx...........
# ..*..........
# ...........xx
# ............x
# x............
# xx..*...*.o..
# 6 19
# xxxx..
# ..xxo.
# ......
# .xxx.x
# .xx..x
# .xx.xx
# .xx.**
# .*xx..
# ..xx..
# .xx..x
# x..*.x
# ...*.x
# ......
# ......
# .xx...
# x.....
# xx...x
# xx..xx
# xx..xx
# 9 15
# xxxxxx...
# xxxxxx...
# xxx.o....
# xx.......
# xx.x....x
# .x.x.....
# ...*....*
# .........
# ......*..
# x........
# xxx......
# xx.....*.
# x........
# xxxxx.x..
# xxxxxxxx.
# 16 15
# xxxxx.....xxxxxx
# xxxxx.x...xxxxxx
# x......*...xxxxx
# xxx........xxxxx
# xx.*....x..x.xxx
# xxx..*.........x
# xxx...xxxx.x..xx
# xx....xxxxx...xx
# xx...xxxxx....xx
# ...........*.xxx
# ....xxxxxx.....x
# ..x..xxxx.......
# ....*xxxx.x.o...
# x...x.x..*....x.
# xx..x.*.xx......
# 13 6
# xxxxxxx..xxxx
# xxxxx....*.*x
# xxxxx.x...xxx
# x..xx....o.xx
# x.....x.*..xx
# .**xxxx..x*..
# 10 15
# .....x....
# ..........
# .......xx.
# ......xxxx
# x....*xxxx
# .*.o..xxxx
# ......xx*.
# ..........
# .....xx...
# ...xxxx..*
# ..xxxxx...
# ..xxxxx...
# ....xx....
# ....xxx...
# ..*.xxx...
# 13 11
# xxxxxxxxx.*.x
# xxxxxxxx...xx
# xxxxxxxx.xxxx
# *xxxxxxx.xxxx
# x*x*x....xxxx
# xxxxx*xx.xxxx
# xo..x..xx.*.x
# *......xx....
# xxxxxx.....*x
# xxxxxx*.xxxxx
# xxxxxxx.xxxxx
# 17 13
# xxx.*.....xx....x
# ......*x...x.....
# ............x...x
# *................
# o......*......x..
# x....*.....x....x
# ...........*....x
# ......*x.........
# xx.......*.......
# xxx.....xxxx.x..x
# xxx...x.xx......x
# xxx..............
# xxxx.............
# 13 19
# xx.xxxxxxxxxx
# .x*.xxxxxxxxx
# ....xxxxxxxxx
# .....xx.xxxxx
# .........xxxx
# ........*xxxx
# .........xxxx
# ............x
# .............
# ............x
# ........*....
# .............
# ........xx.x.
# .......x...x.
# *....x....*..
# .............
# ..........x..
# o......xx.x.x
# .......x....x
# 15 19
# xxxxxxx..xxxxxx
# xxxxxxx...xxxxx
# xxxxxx....xxxxx
# xxxxxx......xxx
# xxxxx....x..xxx
# xxxxx.x..*.xxxx
# xxx....*...xxxx
# xxx........xxxx
# xxx.x.......xxx
# xx...o......xxx
# x......x....xxx
# ............xxx
# x..........*.xx
# xx.x...*......x
# xx......x.....x
# x.............x
# x...x..xx.....x
# xxxxxxxxx......
# xxxxxxxxx..xxxx
# 19 18
# x.x...xx.......xxxx
# ......xx........xxx
# .......xx..x.xx.xxx
# .....x.x......x.xxx
# .....x..xx......xxx
# ...x....xx......xxx
# .........xxx....xxx
# ..x......xx.*....xx
# .........x......xxx
# xx...............xx
# xx.....xx........xx
# xxx....xxxx..*...xx
# xxx.xx.xxxx.......x
# xxx....xx.x.......x
# xxx............x..x
# xx.x....o....*.x.xx
# xx.................
# xxxx...............
# 11 10
# ....x......
# ....*.o....
# ..*.*......
# x*.......*.
# x.....xx..x
# x..x.*xx..*
# xxxxxxxx...
# xxxxx*.....
# xxxxx......
# xxxxx.xx...
# 9 19
# xxxxx...x
# xxxx.....
# xxxx.....
# xx..x....
# xx.......
# xxxxxx*.*
# ...xxx.xx
# .....x..x
# .....*...
# ........x
# .ox...xxx
# *...*..xx
# .*.......
# xx.......
# xx..*....
# xxx......
# x........
# x*.*..xxx
# ......xxx
# 9 8
# ......*.x
# *........
# ....o.*.*
# .........
# ........*
# ........x
# .........
# x.....*..
# 12 17
# xxx......x.x
# xx...x...x.x
# xx...*......
# xx..........
# xx..........
# ...........x
# ..*ox.......
# ............
# x...........
# ...x........
# .......x....
# ..x.x.......
# .xx..xx.....
# .xx*........
# xx......*...
# xx....xxx.xx
# xx....xxxxxx
# 0 0
# 
# 
# 정답 :
# 29
# 23
# 37
# 27
# 22
# 16
# -1
# 16
# 31
# 14
# 43
# 18
# 49
# 19
# 38
# 18
# 27
# -1
# 37
# 24
# 46
# 18
# 23
# 25
# 18
# -1
# 50
# 52
# 35
# 17
# 28
# 61
# 17
# 37
# 8
# 19
# 18
# 31
# 11
# 34
# 22
# 13
# 24
# 29
# 28
# 41
# 16
# 11
# 22
# 18
# 15
# 25
# 24
# 32
# 41
# -1
# 36
# 32
# 29
# -1
# 37
# 16
# 27
# 20
# 17
# 44
# 23
# 36
# 31
# -1
# 40
# 13
# 26
# 10
# 22
# 53
# 18
# 36
# 25
# -1
# 17
# -1
# 34
# 24
# 28
# 12
# 35
# 18
# 47
# 24
# 36
# -1
# 29
# 36
# 22
# 14
# 29
# 32
# 23
# 27