#include <iostream>
using namespace std;

//cuenta la cantidad de numeros positivos solamente, si se presiona cero se detiene
int main (){
    int num;
    int contador = 0;

    cin>>num;

    while(num != 0){
        if (num > 0){
            contador++;
        }
        cin>>num;
    }
    cout<<"contador: "<<contador<<endl;


    return 0;
}