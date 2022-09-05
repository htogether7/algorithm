def solution(p):
    answer = ''
    
    if not p:
        return answer;
    
    if check_right_string(p):
        return p;
    
    left_count = 0;
    right_count = 0;
    u = ''
    v = ''
    for ind,char in enumerate(p):
        if char == "(":
            left_count += 1;
        elif char == ')':
            right_count += 1;
        
        if left_count == right_count:
            u = p[:ind+1];
            v = p[ind+1:];
            break;
    
    if check_right_string(u):
        return u + solution(v);
    else:
        tmp = "(";
        tmp += solution(v);
        tmp += ")";
        
        tmp_u = u[1:len(u)-1];
        for i in tmp_u:
            if i == '(':
                tmp += ')';
            else:
                tmp += '(';
        return tmp;
        

def check_right_string(s):
    stack = [];
    for i in s:
        if not stack:
            stack.append(i);
        else:
            if i == "(":
                stack.append(i);
            else:
                if i == ")":
                    if stack[-1] == "(":
                        stack.pop();
                    else:
                        stack.append(i);
    if stack:
        return False;
    else:
        return True;