def dfs(v):
  if v>7:
    return
  else:
    dfs(v*2)
    dfs(v*2+1)
    print(v)

if __name__=="__main__":
  dfs(1)