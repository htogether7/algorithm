from collections import defaultdict
def solution(edges):
    answer = []
    node = -1
    node_set = set()
    out_dict = defaultdict(list)
    in_dict = defaultdict(list)
    
    # 0 => 생성 노드 | 1 => 도넛 | 2 => 막대 | 3 => 8자
    for a,b in edges:
        out_dict[a].append(b)
        in_dict[b].append(a)
        node_set.add(a)
        node_set.add(b)
    
    # 추가 노드 확정
    for n in node_set:
        if n not in in_dict and len(out_dict[n]) >= 2:
            node = n
    
    node8s = []
    # 8자 노드 추출
    for n in node_set:
        if n not in in_dict:
            continue
        if n not in out_dict:
            continue
        if len(in_dict[n]) >= 2 and len(out_dict[n]) >= 2:
            node8s.append(n)
            
    sticks = []
    # 막대 노드 추출
    for n in node_set:
        if n not in out_dict:
            sticks.append(n)
    
    total = len(out_dict[node])

    
    return [node, total-len(sticks)-len(node8s) ,len(sticks), len(node8s)]