"""""
番号 11 〜 NN の足場がある。足場 i（1≦i≦N）i（1≦i≦N）の高さは h[i]h[i] 
である。足場 ii から 足場 jj への移動では|h[i]−h[j]||h[i]−h[j]| のコスト
がかかる。足場 ii へ移動できるのは、足場 i−1i−1 と i−2i−2 のみである。足場
11 から足場 NN への移動に必要な最小コストを求めよ。
"""""
'動的計画法'
print('Q1')
# 入力読み込み
N = int(input())
h = list(map(int, input().split()))

# DP 配列を用意
# dp[i] には i 番目の足場にたどり着くために必要な最低コストを入れる
dp = [0]*N

# 初期条件を入力
dp[0] = 0
dp[1] = abs(h[1]-h[0])

# 漸化式にしたがって DP を実装する
for i in range(2, N):
# i を現在いる足場と考える。
# i 番目の足場へ行く方法として i-i 番目からのジャンプと i-2 番目からのジャンプがある
# 2 通りの行き方のうちコストの少ない方を dp[i] とする
  dp[i] = min(dp[i-2]+abs(h[i]-h[i-2]), dp[i-1]+abs(h[i]-h[i-1]))

# dp 配列の末尾が N 番目の足場にたどり着くために必要なコストとなる
print(dp[-1])



#1番の問題の通り数が2通り以上
print('Q2')
# 入力読み込み
N, k = map(int, input().split())
h = list(map(int, input().split()))

# DP 配列を用意
# dp[i] には i 番目の足場にたどり着くために必要な最低コストを入れる
dp = [0] * N

# 初期条件を入力
dp[0] = 0

# 漸化式にしたがってループを回す
for i in range(1, N):
    # i を現在いる足場と考える。
    # i 番目の足場へ行く方法は max(k,i-k) 通り ある。
    # それぞれの行き方にかかるコストを tmp （tmporary） にまとめる。
    tmp = []
    for m in range(max(0, i-k), i):
        tmp.append(abs(h[m]-h[i])+dp[m])
    # tmp のうち最小コストを dp[i] とする
    dp[i] = min(tmp)

# dp 配列の末尾が N 番目の足場にたどり着くために必要なコストとなる
print(dp[-1])

"""""
太郎くんは NN 日間の夏休みを過ごす。i　(1≦i≦N)i　(1≦i≦N) 日目の太郎くんは
行動 AA、BB、CC のどれかひとつをとることで、幸福度 aiai、bibi、cici をそれ
ぞれ得る。太郎くんが夏休みで得られる最大幸福度を求めよ。ただし太郎くんは二日連
続で同じ行動は取らない。
"""

print('Q3')

# DP 配列を用意する
# 本問では i 日目の動作として「Aをやる」「Bをやる」「Cをやる」の3通りが考えられる
# それぞれの行動をするための最大幸福度をそれぞれの漸化式で求める
# i 日目に A、B、C をやるための最大幸福度は dp[i][0]、dp[i][1][1]、dp[i][2] とする
N = int(input())
dp = [[0]*3 for _ in range(n+1)]

# 初期条件を入力
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

# 漸化式にしたがって DP を実行する
for i in range(1,N+1):
  a,b,c = map(int,input().split())
  dp[i][0] = max(dp[i-1][1]+a,dp[i-1][2]+a)
  dp[i][1] = max(dp[i-1][0]+b,dp[i-1][2]+b)
  dp[i][2] = max(dp[i-1][0]+c,dp[i-1][1]+c)

# 最終日までに得られる幸福度の最大値を求める
print(max(dp[-1]))