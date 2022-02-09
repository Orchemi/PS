#include <stdio.h>
int main(){
    int x,y,w,h;
    int mini(int a, int b);
    scanf("%d %d %d %d", &x, &y, &w, &h);
    printf("%d", mini(mini(x,w-x),mini(y,h-y)));
    return 0;
}

int mini(int a, int b){
    if(a>b)
        return b;
    else
        return a;
}