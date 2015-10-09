#include <iostream>
#include "python2.7/Python.h"

using namespace std;

int main(int argc, char *argv[])
{
	PyObject *pname , *pmodule , *pdict, *pfunc, *pvalue;

	Py_Initialize();
	
	// pname = PyString_FromString("bin_classifier");

	// pmodule = PyImport_Import(pname);

	// // pdict = PyModule_GetDict(pmodule);

	// // pfunc = PyDict_GetItemString(pdict, "gg");

	// cout<<"Hello world!"<<endl;
	

	PyRun_SimpleString("from bin_sentiment import bin_classifier");

	PyRun_SimpleString("bin_classifier.classify('no')");


	string str;



	while(1){

		getline(cin , str);

		if(str == "END"){
			break;
		}

		string to_python = "print bin_classifier.classify('"+str+"')";

		char str_c_py[200];
		strcpy(str_c_py , to_python.c_str());

		printf("%s\n", str_c_py);

		// cout<<to_python<<endl;

		PyRun_SimpleString(str_c_py);

	}

	Py_Finalize();
	return 0;
}