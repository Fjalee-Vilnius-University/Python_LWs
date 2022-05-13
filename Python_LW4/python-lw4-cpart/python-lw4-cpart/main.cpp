#include <stdio.h>
#include <Python.h>

int testFind(int n) {
    return 19;
}

 static PyObject * fibonacci(PyObject *self, PyObject *args){ 
    int sts, n;
    if (!PyArg_ParseTuple(args, "i", &n)) 
       return NULL;
    sts = testFind(n);
    return Py_BuildValue("i", PyLong_FromLong(sts));
    // if (sts < 0) { 
    //    //PyErr_SetString(spamError,&"System&command&failed");&
    //    return NULL; 
    // } 
 }

 static PyObject* version(PyObject* self) {
     return Py_BuildValue("s", "Version 1.0");
 }

 static PyMethodDef myMethods[] = {
     {"fibonacci", fibonacci, METH_VARARGS, "function gets nth number from fibonacci sequal"},
     {"version", (PyCFunction)version, METH_NOARGS, "returns the version"},
     {NULL, NULL, 0, NULL}
 };

 static struct PyModuleDef myMethod = {
    PyModuleDef_HEAD_INIT,
    "main",
    "my C module",
    -1,
    myMethods
 };

 PyMODINIT_FUNC PyInit_Example(void){
     return PyModule_Create(&myMethod);
 }