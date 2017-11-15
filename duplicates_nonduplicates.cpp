#include<iostream>

using namespace std;
void duplicateornot(int arr[], int n)
{
int* count = new int[n];
    cout<<"Duplicates are : \n";
    for(int i=0;i<n;i++)
    {
        if(count[arr[i]] == 0)
            {
                count[arr[i]]++;
            }     
         else if (count[arr[i]] == 1)
         {  count[arr[i]]++;
            cout<<arr[i]<<endl;
         }
         
         
    }
    cout<<"Non-duplicates are : \n";
    for(int j=0;j<n;j++)
    {
        if(count[arr[j]] == 1)
        {
            cout<<arr[j]<<endl;
        }
    }
}    
    
int main()
{
    int n;
    cout<<"Enter the number of elements\n";
    cin>>n;
    int *arr = new int(n);
    cout<<"Enter the elements\n";
    for (int i=0;i<n;i++)
    {
        cin>>arr[i];
        
    }
    
    duplicateornot(arr,n);
return 0;
}


