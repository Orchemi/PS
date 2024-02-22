function solution(n)
{
    return Array.from(String(n)).map((n) => +n).reduce((a, c) => a+c);
}