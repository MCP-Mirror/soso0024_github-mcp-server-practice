def fibonacci_recursive(n):
    """再帰的アプローチでフィボナッチ数列のn番目の値を計算
    Args:
        n (int): 計算したい数列の位置（0から開始）
    Returns:
        int: フィボナッチ数列のn番目の値
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    """反復的アプローチでフィボナッチ数列のn番目の値を計算
    Args:
        n (int): 計算したい数列の位置（0から開始）
    Returns:
        int: フィボナッチ数列のn番目の値
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(n):
    """フィボナッチ数列の最初のn項を生成
    Args:
        n (int): 生成したい数列の長さ
    Returns:
        list: フィボナッチ数列の最初のn項
    """
    sequence = []
    for i in range(n):
        sequence.append(fibonacci_iterative(i))
    return sequence

# テスト用のコード
if __name__ == "__main__":
    # 最初の10項を表示
    n = 10
    print(f"最初の{n}項のフィボナッチ数列:")
    print(fibonacci_sequence(n))
    
    # 特定の位置の値を計算（例：第10項）
    position = 10
    print(f"\n第{position}項の値:")
    print(f"再帰的アプローチ: {fibonacci_recursive(position)}")
    print(f"反復的アプローチ: {fibonacci_iterative(position)}")
