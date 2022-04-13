#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
bool cmp(string a,string b){
    return a < b; //按字典序从小到大排列 
} 

int main(){
    string s[3];
    s[0] = "wu";s[1]="jia";s[2]="jun";
    sort(s,s+3,cmp);
    for(int i = 0;i < 3;i++){
        cout << s[i]<<" ";
    }
}