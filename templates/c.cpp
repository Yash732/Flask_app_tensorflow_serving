#include<iostream> 	
#include<bitset>
using namespace std; 	
int main(){ 	
     
    int n;
    cin >> n;
    string binary = bitset<4>(n).to_string();
    cout << binary << endl;
    
return 0; 	
}