def solution(T):
    B = []
    B = [w for w in T]
    return ''.join(sorted(B, reverse = True))
