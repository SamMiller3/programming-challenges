//5th febuary 2021
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

{
    class Program
    { 
    static public int i;
	static public int s;
	static public int c;
	static public int n;
        static void Main(string[] args)
        {
        string inpt;
inpt=Console.ReadLine();
if ((inpt).Length >= 7){
 s=0;
 n=0;
 c=0;
 i=0;
 }
 while (i<=(inpt).Length-1){
  if (inpt[i].ToString() == "@".ToString() || inpt[i].ToString() == "!".ToString() || inpt[i].ToString() == "#".ToString() || inpt[i].ToString() == "$".ToString() || inpt[i].ToString() == "%".ToString() || inpt[i].ToString() == "&".ToString() || inpt[i].ToString() == "*".ToString()) {
   c=c+1;
   }
  if (inpt[i].ToString() == "1" || inpt[i].ToString() == "2" || inpt[i].ToString() == "3" || inpt[i].ToString() == "4" || inpt[i].ToString() == "5" || inpt[i].ToString().ToString() == "6" || inpt[i].ToString() == "0" || inpt[i].ToString() == "7" || inpt[i].ToString() == "8" || inpt[i].ToString() == "9") {
   n=n+1;
   }
  i=i+1;
 if (c>=2 && n>=2){
  Console.WriteLine("Strong");
  }
 else{
  Console.WriteLine("Weak");
  }
        }
    }
}
}
#PYTHON VERSION
inpt=input("")
if len(inpt) >= 7:
 i=0
 s=0
 n=0
 c=0
 while i<=len(inpt)-1:
  if inpt[i] == "@" or inpt[i] == "!" or inpt[i] == "#" or inpt[i] == "$" or inpt[i] == "%" or inpt[i] == "&" or inpt[i] == "*":
   c=c+1
  if inpt[i] == "1" or inpt[i] == "2" or inpt[i] == "3" or inpt[i] == "4" or inpt[i] == "5" or inpt[i] == "6" or inpt[i] == "0" or inpt[i] == "7" or inpt[i] == "8" or inpt[i] == "9":
   n=n+1
  i=i+1
 if c>=2 and n>=2:
  print("Strong")
 else:
  print("Weak")
else:
 print ("Weak")
