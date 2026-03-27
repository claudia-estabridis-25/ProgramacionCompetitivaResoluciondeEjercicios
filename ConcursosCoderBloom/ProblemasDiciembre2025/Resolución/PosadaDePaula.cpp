#include <bits/stdc++.h>
using namespace std;

int main() {
	int n; cin>>n;
    int a;
    int suma = 0;
    
    for(int i=1; i<=n; i++)
    {
        cin>>a;
        suma += a;
    }
	
    cout<<suma;
    
    return 0;
}
