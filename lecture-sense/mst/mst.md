# 최소 스패닝 트리 (Minimum Spanning Tree)

## 프림

- 프림 -> 다익스트라 -> 트리
- 다익스트라를 이용해서, 방문한 곳인지 확인한다.

1. 방문하면서 링크 정보를 저장한다.
2. 방문 한 곳은 다시 연결하지 않는다.

## 크루스칼

- 크루스칼 -> 유니온 파인드 -> 트리
- 유니온 파인드를 이용해서, 같은 집합인지 확인한다.

1. 모든 링크를 한번에 가져온다.
2. 링크를 연결하면서 같은 집합으로 만들어 준다.
3. 만약에 이미 같은 집합이라면 연결하지 않는다.
