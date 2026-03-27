#include <bits/stdc++.h>
using namespace std;

int main() {
	int n; cin>>n;
    int max = 0;
    int dia;

    for(int i = 1; i <= n; i++){
        int a; cin>>a;

// Debe ser (>) y no (>=), porque si fuera (>=) consideraría otros máximos repetidos y, por lo tanto, imprimiría el último día,
// y nosotros queremos el primer día que se dé el máximo.
        if (a > max){
            max =  a;
            dia = i;
        }
    }

    cout<<dia<<" "<<max<<endl;
}
