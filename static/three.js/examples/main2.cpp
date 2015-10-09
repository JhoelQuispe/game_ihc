#include <iostream>
#include "python2.7/Python.h"

using namespace std;

int main(int argc, char *argv[])
{
	PyObject *pname , *pModule , *pdict, *pFunc, *pvalue, *pargs;

	Py_Initialize();
	
	pname = PyString_FromString("bin_sentiment.microphone_recognition");

	pModule = PyImport_Import(pname);

	Py_DECREF(pname);

	if (pModule != NULL) {
		cout<<"ok import"<<endl;
        pFunc = PyObject_GetAttrString(pModule , "reconocer");


        if (pFunc && PyCallable_Check(pFunc)) {
        	cout<<"ok function"<<endl;
        	pvalue = PyObject_CallObject(pFunc , NULL);
        	if(pvalue != NULL){
        		cout<<"In C++ " << PyInt_AsLong(pvalue)<<endl;
        	}
        }



    }
    else{
    	cout<<"wtf"<<endl;
        /* pFunc is a new reference */
    }


	// pdict = PyModule_GetDict(pmodule);

	// // pfunc = PyDict_GetItemString(pdict, "gg");

	// cout<<"Hello world!"<<endl;
	



	// while(1){

	// 	getline(cin , str);

	// 	if(str == "END"){
	// 		break;
	// 	}

	// 	string to_python = "print bin_classifier.classify('"+str+"')";

	// 	char str_c_py[200];
	// 	strcpy(str_c_py , to_python.c_str());

	// 	printf("%s\n", str_c_py);

	// 	// cout<<to_python<<endl;

	// 	PyRun_SimpleString(str_c_py);

	// }

	Py_Finalize();
	return 0;
}